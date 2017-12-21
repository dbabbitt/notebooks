
# temp <- tempfile()
# download.file("https://www.kaggle.com/c/word2vec-nlp-tutorial/download/labeledTrainData.tsv.zip", temp)
# train.labeled <- read.delim(unz(temp, "labeledTrainData.tsv"), header=TRUE, quote='', stringsAsFactors=FALSE)
# unlink(temp)
train.labeled <- read.delim("labeledTrainData.tsv", header=TRUE, quote='', stringsAsFactors=FALSE)

# temp <- tempfile()
# download.file("https://www.kaggle.com/c/word2vec-nlp-tutorial/download/unlabeledTrainData.tsv.zip", temp)
# train.unlabeled <- read.delim(unz(temp, "unlabeledTrainData.tsv"), header=TRUE, quote='', stringsAsFactors=FALSE)
# unlink(temp)
train.unlabeled <- read.delim("unlabeledTrainData.tsv", header=TRUE, quote='', stringsAsFactors=FALSE)

# temp <- tempfile()
# download.file("https://www.kaggle.com/c/word2vec-nlp-tutorial/download/testData.tsv.zip", temp)
# test <- read.delim(unz(temp, "testData.tsv"), header=TRUE, quote='', stringsAsFactors=FALSE)
# unlink(temp)
test <- read.delim("testData.tsv", header=TRUE, quote='', stringsAsFactors=FALSE)

# combine the data
all.data <- rbind(train.labeled[, -2], train.unlabeled, test)
all.data$sentiment <- c(train.labeled$sentiment, rep(NA, nrow(train.unlabeled) + nrow(test)))

# index
train.labeled.ind <- 1:nrow(train.labeled)
train.ind <- 1:(nrow(train.labeled) + nrow(train.unlabeled))
test.ind <- (nrow(train.labeled) + nrow(train.unlabeled) + 1):nrow(all.data)

# clean up

# remove HTML tags
all.data$review.clean <- gsub('<.*?>', ' ', all.data$review)

# remove grammar/punctuation
all.data$review.clean <- tolower(gsub('[[:punct:]]', '', all.data$review.clean))

# read in the AFINN list
afinn <- read.delim("https://raw.githubusercontent.com/uwescience/datasci_course_materials/master/assignment1/AFINN-111.txt",
                    header=TRUE, quote='', stringsAsFactors=FALSE)
names(afinn) <- c('word', 'score')

# spaces are denoted by "-", so we need to clean it up a bit
afinn$word.clean <- gsub('-', ' ', afinn$word)

# one phrase in the list includes an apostrophe.
afinn$word.clean <- gsub("[[:punct:]]", '', afinn$word.clean)

# find the text frequency matrix

# this may take a while ...
if (!require('stringr')) install.packages('stringr'); require('stringr')
tf <- t(apply(t(all.data$review.clean), 2, function(x) str_count(x, afinn$word.clean)))

# sentiment rating for each row
all.data$afinn.rating <- as.vector(tf %*% afinn$score)

if (!require('ggplot2')) install.packages('ggplot2'); require('ggplot2')
ggplot(all.data[train.labeled.ind, ], aes(afinn.rating, fill=as.factor(sentiment))) + geom_density(alpha=.2)

if (!require('e1071')) install.packages('e1071'); require('e1071')

# fit a naive bayes classifier
nb.model <- naiveBayes(sentiment ~ afinn.rating, data=all.data[train.labeled.ind, ])

# predicted values
nb.pred <- predict(nb.model, newdata=all.data[test.ind, ], type='raw')

# format results for submission
results <- data.frame(id=all.data$id[test.ind], sentiment=nb.pred[, 2])
results$id <- gsub('"', '', results$id) #"
write.table(results, file='afinn_rating.csv', sep=',', row.names=FALSE, quote=FALSE)

# bag of scores

# scores range from -5 to 5
score.vectorizer <- function(sentence, words, word.scores)
{
  score.vector <- rep(0, length(table(word.scores)))
  k <- 0
  for (i in as.numeric(names(table(word.scores))))
  {
    k <- k + 1
    tempwords <- words[word.scores==i]
    score.vector[k] <- sum(str_count(sentence, tempwords))
  }
  
  return(score.vector)
}

score.data <- as.data.frame(t(apply(t(all.data$review.clean), 2,
                                    function(x) score.vectorizer(x, afinn$word.clean, afinn$score))))

# name columns
names(score.data) <- c('n5', 'n4', 'n3', 'n2', 'n1', 'zero', 'p1', 'p2', 'p3', 'p4', 'p5')

if (!require('randomForest')) install.packages('randomForest'); require('randomForest')

bag.of.scores.forest <- randomForest(score.data[train.labeled.ind, ], as.factor(train.labeled$sentiment))
bag.of.scores.forest.pred <- predict(bag.of.scores.forest, newdata=score.data[test.ind, ], type='prob')
results <- data.frame(id=all.data$id[test.ind], sentiment=bag.of.scores.forest.pred[, 2])
results$id <- gsub('"', '', results$id) # "
write.table(results, file='bag_of_scores.csv', sep=',', row.names=FALSE, quote=FALSE)

tf <- as.data.frame(tf)
idf <- log(length(train.ind)/colSums(sign(tf[train.ind, ])))
tf.idf <- as.data.frame(t(apply(tf, 1, function(x) x * idf)))

# remove infinite idf values since they go to zero when computing tf-idf
idf[is.infinite(idf)] <- 0

# compute tf-idf
tf.idf <- as.data.frame(t(apply(tf, 1, function(x) x * idf)))

# fit a classifier
tfidf.forest <- randomForest(tf.idf[train.labeled.ind, ], as.factor(all.data$sentiment[train.labeled.ind]), ntree=100)

# compute predictions and write as csv
tfidf.forest.pred <- predict(tfidf.forest, newdata=tf.idf[test.ind, ], type='prob')
results <- data.frame(id=all.data$id[test.ind], sentiment=tfidf.forest.pred[, 2])
results$id <- gsub('"', '', results$id)
write.table(results, file='tfidf_afinn.csv', sep=',', row.names=FALSE, quote=FALSE)

if (!require('tm')) install.packages('tm'); require('tm')

# construct corpus (using only training data)
corpus <- Corpus(VectorSource(all.data$review.clean[train.ind]))

# tf matrix using all words (minus stop words)
# list of stop words can be found at
# http://jmlr.csail.mit.edu/papers/volume5/lewis04a/a11-smart-stop-list/english.stop
tf <- DocumentTermMatrix(corpus, control=list(stopwords=stopwords('english'), removeNumbers=T))

# only include words that occur in at least .1% of reviews
tf <- removeSparseTerms(tf, .999)

# convert to dense matrix for easier analysis
tf <- as.matrix(tf)

head(colnames(tf))

# sum up the columns to find the occurrences of each word in the corpus
word.freq <- colSums(tf)

# put in nicer format
word.freq <- data.frame(word=names(word.freq), freq=word.freq)
rownames(word.freq) <- NULL

head(word.freq)

head(word.freq[order(-word.freq$freq), ])

word.freq <- function(document.vector, sparsity=.999)
{
  # construct corpus
  temp.corpus <- Corpus(VectorSource(document.vector))
  
  # construct tf matrix and remove sparse terms
  temp.tf <- DocumentTermMatrix(temp.corpus, control=list(stopwords=stopwords('english'), removeNumbers=T))
  temp.tf <- removeSparseTerms(temp.tf, sparsity)
  temp.tf <- as.matrix(temp.tf)
  
  # construct word frequency df
  freq.df <- colSums(temp.tf)
  freq.df <- data.frame(word=names(freq.df), freq=freq.df)
  rownames(freq.df) <- NULL
  
  return(freq.df)
}
word.freq.pos <- word.freq(all.data$review.clean[all.data$sentiment==1])
word.freq.neg <- word.freq(all.data$review.clean[all.data$sentiment==0])

head(word.freq.pos)
head(word.freq.pos[order(-word.freq.pos$freq), ])

head(word.freq.neg)
head(word.freq.neg[order(-word.freq.neg$freq), ])

# merge by word
freq.all <- merge(word.freq.neg, word.freq.pos, by='word', all=TRUE, suffixes=c(".neg",".pos"))
head(freq.all)

# clean up
freq.all$freq.neg[is.na(freq.all$freq.neg)] <- 0
freq.all$freq.pos[is.na(freq.all$freq.pos)] <- 0

# compute difference
freq.all$diff <- abs(freq.all$freq.neg -freq.all$freq.pos)

head(freq.all[order(-freq.all$diff), ])

# smoothing term
alpha <- 2**7

# ndsi
freq.all$ndsi <- abs(freq.all$freq.neg - freq.all$freq.pos)/(freq.all$freq.neg + freq.all$freq.pos + 2*alpha)

head(freq.all[order(-freq.all$ndsi), ])

# number of words to consider in tf-idf matrix
num.features <- 2**10

# sort the frequency data
freq.all <- freq.all[order(-freq.all$ndsi), ]

# cast word to string
freq.all$word <- as.character(freq.all$word)

# build the tf matrix
tf <- t(apply(t(all.data$review.clean), 2, function(x) str_count(x, freq.all$word[1:num.features])))

# idf vector
idf <- log(length(train.ind)/colSums(sign(tf[train.ind, ])))
idf[is.infinite(idf)] <- 0

# tf-idf matrix
tf.idf <- as.data.frame(t(apply(tf, 1, function(x) x * idf)))
colnames(tf.idf) <- freq.all$word[1:num.features]

# train random forest classifier
ndsi.forest <- randomForest(tf.idf[train.labeled.ind, ], as.factor(all.data$sentiment[train.labeled.ind]), ntree=100)

# predict and write output
ndsi.pred <- predict(ndsi.forest, newdata=tf.idf[test.ind, ], type='prob')
results <- data.frame(id=all.data$id[test.ind], sentiment=bag.of.scores.forest.pred[, 2])
results$id <- gsub('"', '', results$id) # "
write.table(results, file='ndsi_tfidf.csv', sep=',', row.names=FALSE, quote=FALSE)





