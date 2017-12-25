
file.name <- format(as.Date(Sys.time())-1, 'FBOFeed%Y%m%d')
# ftp://ftp.fbo.gov/FBOFeed20140806
# file.url <- paste('ftp://ftp.fbo.gov/', file.name, sep='')
# file.download <- download.file(url=file.url,
#               destfile=paste(file.name, '.txt', sep=''), quiet=FALSE)
# file.download <- url(file.url, open='r')

# install.packages('rjson')
require('rjson')
fbo.data <- fromJSON(file=paste(file.name, '.json', sep=''))


# AMDCSS
# ARCHIVE
# AWARD - Award Notice
# COMBINE - Combined Synopsis/Solicitation
# FAIROPP - Fair Opportunity / Limited Sources Justification
# JA - Justification and Approval (J&A)
# MOD - Modification/Amendment/Cancel
# PRESOL - Presolicitation
# SNOTE - Special Notice
# SRCSGT - Sources Sought
# SSALE - Sale of Surplus Property
# UNARCHIVE



names(head(fbo.data[[1]][[1]]))
fbo.types <- unlist(lapply(fbo.data, function(x) {
  names(x[[1]])
}))

fbo.list <- sapply(1:length(fbo.types), function(row.number) {
  eval(parse(text=paste('fbo.data[[', row.number,
                        ']][[1]]$', fbo.types[row.number], sep='')))
})
fbo.list[sample.int(length(fbo.list), size=3)]

fbo.list[[1]]$SUBJECT
fbo.title <- sapply(1:length(fbo.list), function(row.number) {
  title <- eval(parse(text=paste('fbo.list[[', row.number,
                                 ']]$SUBJECT', sep='')))
  if(is.null(title)) {title <- ''}
  return(title)
})
fbo.title[sample.int(length(fbo.title), size=3)]

fbo.list[[1]]$CLASSCOD
fbo.ccode <- sapply(1:length(fbo.list), function(row.number) {
  ccode <- eval(parse(text=paste('fbo.list[[', row.number,
                                 ']]$CLASSCOD', sep='')))
  if(is.null(ccode)) {ccode <- ''}
  return(ccode)
})
fbo.ccode[sample.int(length(fbo.ccode), size=3)]

fbo.list[[1]]$NAICS
fbo.naics <- sapply(1:length(fbo.list), function(row.number) {
  naics <- eval(parse(text=paste('fbo.list[[', row.number,
                                 ']]$NAICS', sep='')))
  if(is.null(naics)) {naics <- ''}
  return(naics)
})
fbo.naics[sample.int(length(fbo.naics), size=3)]

fbo.list[[1]]$SOLNBR
fbo.solnumber <- sapply(1:length(fbo.list), function(row.number) {
  solnumber <- eval(parse(text=paste('fbo.list[[', row.number,
                                     ']]$SOLNBR', sep='')))
  if(is.null(solnumber)) {solnumber <- ''}
  return(solnumber)
})
fbo.solnumber[sample.int(length(fbo.solnumber), size=3)]

fbo.list[[1]]$SETASIDE
fbo.setaside <- sapply(1:length(fbo.list), function(row.number) {
  setaside <- eval(parse(text=paste('fbo.list[[', row.number,
                                    ']]$SETASIDE', sep='')))
  if(is.null(setaside)) {setaside <- ''}
  return(setaside)
})
fbo.setaside[sample.int(length(fbo.setaside), size=3)]

fbo.list[[1]]$DATE
fbo.createddate <- sapply(1:length(fbo.list), function(row.number) {
  MMDD <- eval(parse(text=paste('fbo.list[[', row.number,
                                ']]$DATE', sep='')))
  if(is.null(MMDD)) {MMDD <- '0101'}
  YY <- eval(parse(text=paste('fbo.list[[', row.number,
                              ']]$YEAR', sep='')))
  if(is.null(YY)) {YY <- '00'}
  createddate <- paste(MMDD, YY, sep='')
  
  return(createddate)
})
fbo.createddate[sample.int(length(fbo.createddate), size=3)]

fbo.list[[12]]$DESC
fbo.synopsis <- sapply(1:length(fbo.list), function(row.number) {
  synopsis <- eval(parse(text=paste('fbo.list[[', row.number,
                                    ']]$DESC', sep='')))
  if(is.null(synopsis)) {synopsis <- ''}
  return(synopsis)
})
fbo.synopsis[sample.int(length(fbo.synopsis), size=3)]

fbo.list[[1]]$RESPDATE
fbo.responsedate <- sapply(1:length(fbo.list), function(row.number) {
  responsedate <- eval(parse(text=paste('fbo.list[[', row.number,
                                        ']]$RESPDATE', sep='')))
  if(is.null(responsedate)) {responsedate <- '010100'}
  
  return(responsedate)
})
fbo.responsedate[sample.int(length(fbo.responsedate), size=3)]

fbo.df <- data.frame(type=as.factor(fbo.types), title=fbo.title,
                     ccode=as.factor(fbo.ccode), naics=as.factor(fbo.naics),
                     solnumber=fbo.solnumber, setaside=as.factor(fbo.setaside),
                     createddate=as.Date(fbo.createddate, '%m%d%y'),
                     synopsis=fbo.synopsis, stringsAsFactors=FALSE)
fbo.df$filename <- format(as.Date(Sys.time())-1, 'FBOFeed%Y%m%d')
fbo.df$recommended <- 'NO'
fbo.df[sample.int(nrow(fbo.df), size=5), sample.int(ncol(fbo.df), size=3)]
unique(fbo.df$type)
fbo.df[fbo.df$type=='SSALE', ]$recommended <- 'NO'
fbo.df$title

save(fbo.df, file='fbo-df.RData')

require(tm)
fbo.dc <- PlainTextDocument(x=fbo.df$synopsis, author='fbo.gov',
                            description="Nightly file-based notice
                            information from the Federal Business Opportunities (https://www.fbo.gov/)
                            application / database. The FBO feed files include new and updated
                            opportunities, information about awarded contracts, and other details
                            concerning the offer and disposition of federal government contracts and
                            tenders.",
                            id=fbo.df$solnumber, 
                            heading=fbo.df$title,
                            origin='ftp.fbo.gov', language='en_US', 
                            localmetadata=list(type=fbo.df$type,
                                               ccode=fbo.df$ccode,
                                               naics=fbo.df$naics,
                                               setaside=fbo.df$setaside,
                                               createddate=fbo.df$createddate,
                                               responsedate=fbo.df$responsedate))

fbo.vs <- VectorSource(fbo.dc)
fbo.vc <- Corpus(fbo.vs)


# strip whitspace from the documents in the collection
fbo.vc <- tm_map(fbo.vc, stripWhitespace)

# convert uppercase to lowercase in the document collection
fbo.vc <- tm_map(fbo.vc, tolower)

# remove numbers from the document collection
fbo.vc <- tm_map(fbo.vc, removeNumbers)

# remove punctuation from the document collection
fbo.vc <- tm_map(fbo.vc, removePunctuation)

# using a standard list, remove English stopwords from the document collection
fbo.vc <- tm_map(fbo.vc, removeWords, stopwords('english'))

# there is more we could do in terms of data preparation 
# stemming... looking for contractions... pronoun possessives... 

# we take what is clearly a 'bag of words' approach here
# the workhorse technique will be TermDocumentMatrix()
# for creating a terms-by-documents matrix across the document collection
fbo.tdm <- TermDocumentMatrix(fbo.vc)

require(tm)
inspect(fbo.tdm[sample.int(nrow(fbo.tdm), size=3),
                sample.int(ncol(fbo.tdm), size=5)])
search.words <- c('defense', 'cbrn', 'intelligence', 'ied', 'biometrics', 'analysis',
                  'counter', 'leadership', 'training', 'search', 'risk', 'threat',
                  'policy', 'explosive', 'terrorism', 'doctrine', 'forensics')
fruitful.words <- unlist(sapply(search.words, function(term) {
  if(length(findAssocs(fbo.tdm, term, 0.5)) > 1) {return(term)}
}))
sapply(fruitful.words, function(term) {
  inspect(fbo.tdm[term, sample.int(ncol(fbo.tdm), size=5)])
})
# 
# inspect(removeSparseTerms(fbo.tdm, 0.4))

# remove sparse terms from the matrix and report the most common terms
# looking for additional stop words and stop word contractions to drop
examine.fbo.tdm <- removeSparseTerms(fbo.tdm, sparse=0.7265898)
top.words <- Terms(examine.fbo.tdm)
print(top.words)

fbo.mx <- as.matrix(examine.fbo.tdm)

fbo.tf <- fbo.mx
fbo.idf <- log(ncol(fbo.mx)/rowSums(fbo.mx))
fbo.tfidf <- fbo.mx

for(word in rownames(examine.fbo.tdm)){
  fbo.tfidf[word, ] <- fbo.tf[word, ] * fbo.idf[word]
}

findFreqTerms(examine.fbo.tdm, 1)

for(word in colnames(examine.fbo.tdm)){
  show(word)
  show(sort(fbo.tfidf[, word], decreasing=TRUE)[1:10])
}

# an analysis of this initial list of top terms shows a number of words 
# which we might like to drop from further analysis, 
# recognizing them as stop words to be dropped from the document collection
more.stop.words <- c('accordance', 'additional', 'available', 'commercial',
                     'considered', 'date', 'days', 'description', 'electronically',
                     'email', 'far', 'following', 'government', 'information',
                     'issued', 'items', 'may', 'must', 'number', 'price',
                     'procurement', 'provided', 'quote', 'received', 'request',
                     'required', 'requirement', 'responsible', 'shall', 'size',
                     'sources', 'standard', 'submit', 'submitted', 'system',
                     'time', 'via', 'will', 'within') 
fbo.vc <- tm_map(fbo.vc, removeWords, more.stop.words)
fbo.tdm <- TermDocumentMatrix(fbo.vc)
inspect(fbo.tdm[sample.int(nrow(fbo.tdm), size=10), sample.int(ncol(fbo.tdm), size=10)])
findFreqTerms(fbo.tdm, 2000)
findAssocs(fbo.tdm, 'CBRN', 0.5)

# save fbo documents and document collection (corpus)
save('fbo.df', 'fbo.dc', 'fbo.tdm', file='fbo-data.Rdata')

# remove sparse terms from the matrix and report the most common terms
examine.fbo.tdm <- removeSparseTerms(fbo.tdm, sparse=0.8685)
dim(fbo.tdm)
dim(examine.fbo.tdm)
inspect(examine.fbo.tdm[sample.int(nrow(examine.fbo.tdm), size=10),
                        sample.int(ncol(examine.fbo.tdm), size=10)])



# install.packages('slam')
require(slam)
dense.fbo.tdm <- as.matrix(examine.fbo.tdm)
object.size(examine.fbo.tdm)
object.size(dense.fbo.tdm)
require(reshape2)
dense.fbo.tdm=melt(dense.fbo.tdm, value.name='count')
head(dense.fbo.tdm)

require(ggplot2)
ggplot(dense.fbo.tdm, aes(x=Docs, y=Terms, fill=log10(count)))
geom_tile(colour='white')
scale_fill_gradient(high='#FF0000' , low='#FFFFFF')
ylab('')
theme(panel.background=element_blank())
theme(axis.text.x=element_blank(), axis.ticks.x=element_blank())

top.words <- Terms(examine.fbo.tdm)
length(top.words)  # the result of this is a bag of 81 words

# create a dictionary of the top words from the corpus
top.words.dictionary <- c(top.words)

# create terms-by-documents matrix using the mtpa.Dictionary
top.words.fbo.tdm <- TermDocumentMatrix(fbo.vc, list(dictionary=top.words.dictionary))

# classification of words into groups for further analysis
# use transpose of the terms-by-document matrix and cluster analysis
words.distance.object <- dist(x=as.matrix(top.words.fbo.tdm), method='euclidean')
top.words.hierarchical.clustering <- agnes(words.distance.object,diss=TRUE,
                                           metric='euclidean', stand=FALSE,
                                           method='ward') 
plot(top.words.hierarchical.clustering, cex.lab=0.05)

# hierarchical solution suggests that four or five clusters may work
# examine possible clustering soltions with partitioning
number.of.clusters.test <- NULL
for(number.of.clusters in 2:20) {
  try.words.clustering <- pam(words.distance.object,diss=TRUE,
                              metric='euclidean', stand=FALSE, k=number.of.clusters) 
  number.of.clusters.test <- 
    rbind(number.of.clusters.test,
          data.frame(number.of.clusters, 
                     ave.sil.width=try.words.clustering$silinfo$avg.width)) 
  cat('\n\n','Number of clusters: ',number.of.clusters,
      ' Average silhouette width: ',try.words.clustering$silinfo$avg.width,
      '\nKey identified concepts: ',try.words.clustering$medoids,
      '\nCluster average silhouette widths: ')
  print(try.words.clustering$silinfo$clus.avg.widths)
}  # end of for-loop for number-of-clusters test 
print(number.of.clusters.test)


# remove sparse terms from the matrix and report the most common terms
require(tm)
examine.fbo.tdm <- removeSparseTerms(fbo.tdm, sparse=0.93)
top.words <- Terms(examine.fbo.tdm)
length(top.words)  # the result of this is a bag of 200 words
common.english.words <- scan('4000-most-common-english-words-csv.csv',
                             what='char', sep='\n')
common.english.words <- tolower(common.english.words)
# head (common.english.words,10)
uncommon.fbo.words <- setdiff(top.words, common.english.words)

# save fbo documents and document collection (corpus)
save('common.english.words', 'uncommon.fbo.words', file='uncommon-fbo-words.Rdata')


rm(list=c('discussion.freq.list', 'discussion.sorted.freq.list',
          'discussion.text', 'discussion.words.list', 'discussion.words.vector',
          'dissimilarity.matrix', 'examine.fbo.tdm', 'mds.solution', 'more.stop.words',
          'number.of.clusters', 'try.words.clustering',
          'uncommon.discussion.words', 'words.distance.object', 'x', 'y'))


# subset(fbo.df, solnumber %in% sample(fbo.df$solnumber, size=length(fbo.dict)))
fbo.test.df <- fbo.df[1:length(fbo.dict), ]
fbo.test.df$title <- fbo.dict
fbo.test.df$synopsis <- fbo.dict
fbo.test.df[sample.int(nrow(fbo.test.df), size=5),
            sample.int(ncol(fbo.test.df), size=1)]

require(tm)
fbo.test.dc <- PlainTextDocument(x=fbo.test.df$synopsis, author=fbo.test.df$author,
                                 datetimestamp = as.POSIXlt(fbo.test.df$createddate, tz = 'GMT'),
                                 description=fbo.test.df$description, heading=fbo.test.df$title,
                                 id=fbo.test.df$solnumber, language=fbo.test.df$language,
                                 origin=fbo.test.df$origin, localmetadata=list(type=fbo.test.df$type,
                                                                               ccode=fbo.test.df$ccode,
                                                                               naics=fbo.test.df$naics,
                                                                               setaside=fbo.test.df$setaside,
                                                                               responsedate=fbo.test.df$responsedate))

fbo.test.vs <- VectorSource(fbo.test.dc)
fbo.test.vc <- Corpus(fbo.test.vs)
fbo.test.vc <- tm_map(fbo.test.vc, stripWhitespace)
fbo.test.vc <- tm_map(fbo.test.vc, tolower)
fbo.test.vc <- tm_map(fbo.test.vc, removeNumbers)
fbo.test.vc <- tm_map(fbo.test.vc, removePunctuation)
fbo.test.vc <- tm_map(fbo.test.vc, removeWords, stopwords('english'))

fbo.test.tdm <- TermDocumentMatrix(fbo.test.vc, list(dictionary=fbo.dict))
fbo.test.tdm.df <- as.data.frame(inspect(fbo.test.tdm))
fbo.test.terms <- names(which(rowSums(fbo.test.tdm.df)>0))
fbo.test.doc.nums <- as.numeric(names(which(colSums(fbo.test.tdm.df)>0)))
fbo.test.tdm.df$sum <- rowSums(fbo.test.tdm.df)

fbo.test.tdm.df <- subset(fbo.test.tdm.df, sum>0, select=fbo.test.doc.nums)

meta(fbo.test.dc, tag='Heading')[fbo.test.doc.nums]
meta(fbo.test.dc, tag='ID')[fbo.test.doc.nums]
names(meta(fbo.test.dc, tag='LocalMetaData'))
meta(fbo.test.dc, tag='LocalMetaData')[['responsedate']][fbo.test.doc.nums]

if(length(fbo.test.terms)>20) sample.rows <- sample(fbo.test.terms, size=20) else sample.rows <- fbo.test.terms
inspect(fbo.test.tdm[sample.rows, sample(fbo.test.doc.nums, size=10)])
fbo.test.africa.doc.number <- which(inspect(fbo.test.tdm['africa', ])>0)
meta(fbo.test.dc, tag='Heading')[fbo.test.africa.doc.number]

fbo.tdm.df <- as.data.frame(inspect(fbo.tdm))
fbo.terms <- names(which(rowSums(fbo.tdm.df)>0))
fbo.doc.nums <- as.numeric(names(which(colSums(fbo.tdm.df)>0)))
fbo.tdm.df$sum <- rowSums(fbo.tdm.df)

fbo.tdm.df <- subset(fbo.tdm.df, sum>0, select=fbo.doc.nums)

meta(fbo.dc, tag='Heading')[fbo.doc.nums]
meta(fbo.dc, tag='ID')[fbo.doc.nums]
names(meta(fbo.dc, tag='LocalMetaData'))
meta(fbo.dc, tag='LocalMetaData')[['responsedate']][fbo.doc.nums]

if(length(fbo.terms)>20) sample.rows <- sample(fbo.terms, size=20) else sample.rows <- fbo.terms
inspect(fbo.tdm[sample.rows, sample(fbo.doc.nums, size=10)])
# [2,] 'Call for Interest in Industry Involvement during NATO EXERCISE TRIDENT JUNCTURE 2015'
meta(fbo.dc, tag='Heading')[which(inspect(fbo.tdm['nato', ])>0)][2]
meta(fbo.dc, tag='ID')[which(inspect(fbo.tdm['nato', ])>0)][2]
rm(fbo.terms)

# save.image(file='attic.RData')
save('fbo.tdm.df', 'fbo.tdm', 'fbo.cols', 'fbo.tdm.df.rows', 'fbo.dc', 'fbo.vc', file='fbo.tdm.stuff.RData')
# save(list=ls(), file='everything.in.the.working.environment.RData')
rm(list=ls())
load('fbo.tdm.stuff.RData')
load('everything.in.the.working.environment.RData')



# there is more we could do in terms of data preparation 
# stemming... looking for contractions... pronoun possessives... 

# we take what is clearly a 'bag of words' approach here
# the workhorse technique will be TermDocumentMatrix()
# for creating a terms-by-documents matrix across the document collection
# fbo.tdm <- TermDocumentMatrix(fbo.vc)

#Tokenizer for n-grams and passed on to the term-document matrix constructor
MygramTokenizer <- function(x) NGramTokenizer(x, Weka_control(min=1, max=3))

# install.packages('RWeka')
require(RWeka)
require(tm)
terms.tdm <- TermDocumentMatrix(fbo.vc, control=list(tokenize=MygramTokenizer))
inspect(terms.tdm[sample.int(nrow(terms.tdm), size=5),
                  sample.int(ncol(terms.tdm), size=1)])

terms.inspect <- as.data.frame(inspect(terms.tdm['price alone', ]))
colnames(terms.inspect)

fbo.edges <- setdiff(findFreqTerms(fbo.tdm, 2), findFreqTerms(fbo.tdm, 3))



# remove sparse terms from the matrix and report the most common terms
# looking for additional stop words and stop word contractions to drop
examine.fbo.tdm <- removeSparseTerms(fbo.tdm, sparse=0.8354531)
top.words <- Terms(examine.fbo.tdm)

# an analysis of this initial list of top terms shows a number of words 
# which we might like to drop from further analysis, 
# recognizing them as stop words to be dropped from the document collection
more.stop.words <- c('accordance', 'additional', 'available', 'commercial',
                     'considered', 'date', 'days', 'description', 'electronically',
                     'email', 'far', 'following', 'government', 'information',
                     'issued', 'items', 'may', 'must', 'number', 'price',
                     'procurement', 'provided', 'quote', 'received', 'request',
                     'required', 'requirement', 'responsible', 'shall', 'size',
                     'sources', 'standard', 'submit', 'submitted', 'system',
                     'time', 'via', 'will', 'within') 
fbo.vc <- tm_map(fbo.vc, removeWords, more.stop.words)
fbo.tdm <- TermDocumentMatrix(fbo.vc)

# save fbo documents and document collection (corpus)
save('fbo.df', 'fbo.dc', 'fbo.tdm', file='fbo-data.Rdata')


# remove sparse terms from the matrix and report the most common terms
require(tm)
examine.fbo.tdm <- removeSparseTerms(fbo.tdm, sparse=0.93)
top.words <- Terms(examine.fbo.tdm)
length(top.words)  # the result of this is a bag of 200 words
common.english.words <- scan('4000-most-common-english-words-csv.csv',
                             what='char', sep='\n')
common.english.words <- tolower(common.english.words)
uncommon.fbo.words <- setdiff(top.words, common.english.words)

# save fbo documents and document collection (corpus)
save('common.english.words', 'uncommon.fbo.words', file='uncommon-fbo-words.Rdata')