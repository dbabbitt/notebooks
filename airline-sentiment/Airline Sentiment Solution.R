
# /Users/davebabbitt/Documents/Data Science Projects/Airline Sentiment/Airline Sentiment Solution.R
#Install libraries
if(!require('caret')) install.packages('caret', repos = 'http://cran.us.r-project.org'); require('caret')
if(!require('tm')) install.packages('tm', repos = 'http://cran.us.r-project.org'); require('tm')
if(!require('SnowballC')) install.packages('SnowballC', repos = 'http://cran.us.r-project.org'); require('SnowballC')
if(!require('Hmisc')) install.packages('Hmisc', repos = 'http://cran.us.r-project.org'); require('Hmisc')
if(!require('plyr')) install.packages('plyr', repos = 'http://cran.us.r-project.org'); require('plyr')

# Read in raw data. Split data set into a training dataset (train) to train the model and a testing dataset (test) to test the model.
getwd()
raw <- read.csv("./hackathon_data/train.csv")
inTrain <- createDataPartition(y=raw$airline_sentiment, p=0.7, list=FALSE)
test <- raw[-inTrain,]
train <- raw[inTrain,]

# Remove the @airline bit of the text of the tweet
train$text = gsub("^@\\w+ *", "", train$text)
test$text = gsub("^@\\w+ *", "", test$text)
head(train)

# Generate a function to preprocess tweets and create a term frequency matrix
processText = function(text_to_analyze){
  CorpusTranscript = Corpus(VectorSource(text_to_analyze))
  #CorpusTranscript = tm_map(CorpusTranscript, content_transformer(function(x) iconv(x, to='UTF-8-MAC', sub='byte')),
                            #mc.cores=1)
  CorpusTranscript = tm_map(CorpusTranscript, content_transformer(tolower), lazy=T) # Convert string to lower case
  CorpusTranscript = tm_map(CorpusTranscript, PlainTextDocument, lazy = T)
  CorpusTranscript = tm_map(CorpusTranscript, removePunctuation, lazy = T) # Remove punctuation
  CorpusTranscript = tm_map(CorpusTranscript, removeNumbers, lazy = T) # Remove numbers
  CorpusTranscript = tm_map(CorpusTranscript, removeWords, stopwords("english"), lazy = T) # Remove english stop words
  CorpusTranscript = tm_map(CorpusTranscript, stemDocument, lazy = T)  # Remove endings such as -ing and -ed from words
  docTM = DocumentTermMatrix(CorpusTranscript)
  docTM = removeSparseTerms(docTM, 0.99)
  docTM = as.data.frame(as.matrix(docTM))
  colnames(docTM) = make.names(colnames(docTM))
  return(docTM)
}

# Process text on training set
docTM_pos <- processText(train$text[train$airline_sentiment=='positive'])
  docTM_neg <- processText(train$text[train$airline_sentiment=='negative'])

# Calculate word frequency vector for tweets with positive and negative sentiment
freq_pos <- colSums(docTM_pos)
freq_pos <- data.frame(word=names(freq_pos), freq=freq_pos)
rownames(freq_pos) <- NULL
freq_neg <- colSums(docTM_neg)
freq_neg <- data.frame(word=names(freq_neg), freq=freq_neg)
rownames(freq_neg) <- NULL

# merge by word
freq <- merge(freq_neg, freq_pos, by.x="word", by.y="word", all=TRUE, suffixes=c("_neg","_pos"))
head(freq)

# clean up
freq$freq_neg[is.na(freq$freq_neg)] <- 0
freq$freq_pos[is.na(freq$freq_pos)] <- 0

# compute difference
freq$diff <- abs(freq$freq_neg - freq$freq_pos)
head(freq[order(-freq$diff), ])

# smoothing term will reduce the importance of words commonly used in BOTH negative and positive tweets
alpha <- 2**7

# ndsi
freq$diff2 <- abs(freq$freq_neg - freq$freq_pos)/(freq$freq_neg + freq$freq_pos + 2*alpha)
freq <- freq[order(-freq$diff2), ]
head(freq)

# number of words to consider in tf-idf matrix
num.features <- 125

# cast word to string
freq$word <- as.character(freq$word)
terms = freq$word[1:125]


#Define new function to create tf-idf matrix that takes a dictionary of terms for the tf-idf as a second argument.
analyzeText = function(text_to_analyze, terms){  
  CorpusTranscript = Corpus(VectorSource(text_to_analyze))
  #CorpusTranscript = tm_map(CorpusTranscript, content_transformer(function(x) iconv(x, to='UTF-8-MAC', sub='byte')),
                            #mc.cores=1)
  CorpusTranscript = tm_map(CorpusTranscript, content_transformer(tolower), mc.cores=1) # Convert string to lower case
  CorpusTranscript = tm_map(CorpusTranscript, PlainTextDocument, lazy = T)
  CorpusTranscript = tm_map(CorpusTranscript, removePunctuation, lazy = T) # Remove punctuation
  CorpusTranscript = tm_map(CorpusTranscript, removeNumbers, lazy = T) # Remove numbers
  CorpusTranscript = tm_map(CorpusTranscript, removeWords, stopwords("english"), lazy = T) # Remove english stop words
  CorpusTranscript = tm_map(CorpusTranscript, stemDocument, lazy = T)  # Remove endings such as -ing and -ed from words
  docTM = DocumentTermMatrix(CorpusTranscript, list(dictionary = terms))
  docTM = as.data.frame(as.matrix(docTM))
  colnames(docTM) = make.names(colnames(docTM))
  return(docTM)
}

# Calculate a tf-idf matrix from the training set using the top 100 terms from the 'terms' list
train_tfIdf = analyzeText(train$text, terms)

# Train random forest model
training = cbind(train, train_tfIdf)
n = length(training)
training <- training[,c(9:n)]
modelFit_rf = train(airline_sentiment ~ ., data=training, method="rf", preProcess = c("center", "scale"), prox=TRUE)
modelFit_rf
# Random Forest 
# 
# 3174 samples
# 125 predictor
# 3 classes: 'negative', 'neutral', 'positive' 
# 
# Pre-processing: centered (125), scaled (125) 
# Resampling: Bootstrapped (25 reps) 
# Summary of sample sizes: 3174, 3174, 3174, 3174, 3174, 3174, ... 
# Resampling results across tuning parameters:
#   
#   mtry  Accuracy   Kappa     
# 2   0.5971924  0.02809775
# 63   0.6488444  0.38487489
# 125   0.6376996  0.37206484
# 
# Accuracy was used to select the optimal model using  the largest value.
# The final value used for the model was mtry = 63.

# Process the test data set
test_tfIdf = analyzeText(test$text, terms)
testing = cbind(test, test_tfIdf)
n = length(testing)
testing <- testing[,c(9:n)]

# Apply model to predict sentiment on the test set
confusionMatrix(testing$airline_sentiment, predict(modelFit_rf,testing))
confusionMatrix
# Confusion Matrix and Statistics
# 
# Reference
# Prediction negative neutral positive
# negative      633     132       41
# neutral       138     159       24
# positive       66      43      123
# 
# Overall Statistics
# 
# Accuracy : 0.6733          
# 95% CI : (0.6476, 0.6982)
# No Information Rate : 0.6159          
# P-Value [Acc > NIR] : 6.317e-06       
# 
# Kappa : 0.4093          
# Mcnemar's Test P-Value : 0.009919        
# 
# Statistics by Class:
# 
# Class: negative Class: neutral Class: positive
# Sensitivity                   0.7563         0.4760         0.65426
# Specificity                   0.6686         0.8420         0.90692
# Pos Pred Value                0.7854         0.4953         0.53017
# Neg Pred Value                0.6311         0.8314         0.94232
# Prevalence                    0.6159         0.2458         0.13834
# Detection Rate                0.4658         0.1170         0.09051
# Detection Prevalence          0.5931         0.2362         0.17071
# Balanced Accuracy             0.7124         0.6590         0.78059

