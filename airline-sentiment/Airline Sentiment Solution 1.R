#Install libraries
library(caret)
library(tm)
library(SnowballC)
library(Hmisc)
library(plyr)

# Read in raw data. Split data set into a training dataset (train) to train the model and a testing dataset (test) to test the model.
raw <- read.csv("/Users/melissahedberg/airline-twitter-sentiment/hackathon_data/train.csv")
inTrain <- createDataPartition(y=raw$airline_sentiment, p=0.7, list=FALSE)
test <- raw[-inTrain,]
train <- raw[inTrain,]

# Remove the @airline bit of the text of the tweet
train$text = gsub("^@\\w+ *", "", train$text)
test$text = gsub("^@\\w+ *", "", test$text)
head(train)

# Generate a function to preprocess tweets and create a tf-idf matrix
processText = function(text_to_analyze){
  CorpusTranscript = Corpus(VectorSource(text_to_analyze))
  CorpusTranscript = tm_map(CorpusTranscript, content_transformer(function(x) iconv(x, to='UTF-8-MAC', sub='byte')),
                            mc.cores=1)
  CorpusTranscript = tm_map(CorpusTranscript, content_transformer(tolower), mc.cores=1) # Convert string to lower case
  CorpusTranscript = tm_map(CorpusTranscript, PlainTextDocument, lazy = T)
  CorpusTranscript = tm_map(CorpusTranscript, removePunctuation, lazy = T) # Remove punctuation
  CorpusTranscript = tm_map(CorpusTranscript, removeNumbers, lazy = T) # Remove numbers
  CorpusTranscript = tm_map(CorpusTranscript, removeWords, stopwords("english"), lazy = T) # Remove english stop words
  CorpusTranscript = tm_map(CorpusTranscript, stemDocument, lazy = T)  # Remove endings such as -ing and -ed from words
  docTM = DocumentTermMatrix(CorpusTranscript, control = list(weighting = function(x) weightTfIdf(x, normalize = FALSE)))
  docTM = removeSparseTerms(docTM, 0.98)
  docTM = as.data.frame(as.matrix(docTM))
  colnames(docTM) = make.names(colnames(docTM))
  return(docTM)
}

# Generate tf-idf matrix with the training set
train_tfIdf = processText(train$text)

# Train random forest model
training = cbind(train, train_tfIdf)
n = length(training)
training <- training[,c(9:n)]
modelFit_rf = train(airline_sentiment ~ ., data=training, method="rf", preProcess = c("center", "scale"), prox=TRUE)
modelFit_rf
# Random Forest 
# 
# 3174 samples
# 64 predictor
# 3 classes: 'negative', 'neutral', 'positive' 
# 
# Pre-processing: centered (64), scaled (64) 
# Resampling: Bootstrapped (25 reps) 
# Summary of sample sizes: 3174, 3174, 3174, 3174, 3174, 3174, ... 
# Resampling results across tuning parameters:
#   
#   mtry  Accuracy   Kappa    
# 2    0.6243946  0.1122228
# 33    0.6348979  0.3195645
# 64    0.6231826  0.3062585
# 
# Accuracy was used to select the optimal model using  the largest value.
# The final value used for the model was mtry = 33.

# Extract terms used to train the model
terms = names(train_tfIdf)

#Define new function to create tf-idf matrix that takes a dictionary of terms for the tf-idf as a second argument.
analyzeText = function(text_to_analyze, terms){  
  CorpusTranscript = Corpus(VectorSource(text_to_analyze))
  CorpusTranscript = tm_map(CorpusTranscript, content_transformer(function(x) iconv(x, to='UTF-8-MAC', sub='byte')),
                            mc.cores=1)
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

# Apply preprocessing to test dataset
testDocTM = analyzeText(test$text, terms)
testing = cbind(test, testDocTM)
n = length(testing)
testing <- testing[,c(9:n)]

# Apply model to the test set to predict sentiment
# confusionMatrix(testing$airline_sentiment, predict(modelFit_rf,testing[-1]))
# Confusion Matrix and Statistics
# 
# Reference
# Prediction negative neutral positive
# negative      758      48        0
# neutral       312       9        0
# positive      224       6        2
# 
# Overall Statistics
# 
# Accuracy : 0.5659         
# 95% CI : (0.539, 0.5924)
# No Information Rate : 0.9522         
# P-Value [Acc > NIR] : 1              
# 
# Kappa : -0.0237        
# Mcnemar's Test P-Value : <2e-16         
# 
# Statistics by Class:
# 
# Class: negative Class: neutral Class: positive
# Sensitivity                  0.58578       0.142857        1.000000
# Specificity                  0.26154       0.759259        0.830508
# Pos Pred Value               0.94045       0.028037        0.008621
# Neg Pred Value               0.03074       0.947977        1.000000
# Prevalence                   0.95217       0.046358        0.001472
# Detection Rate               0.55776       0.006623        0.001472
# Detection Prevalence         0.59308       0.236203        0.170714
# Balanced Accuracy            0.42366       0.451058        0.915254