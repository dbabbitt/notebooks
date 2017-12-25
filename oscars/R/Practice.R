
setwd('C:/Users/Dave/Documents/notebooks/oscars/R/')
tweets.csv <- read.csv('../data/csv/tweets.csv', na.strings = c('.', 'NA', '', '?'),
                       strip.white = TRUE, encoding = 'Latin1', stringsAsFactors = FALSE)
colnames(tweets.csv) <- c('tweetID', 'tweetTime', 'tweetAuthor', 'tweetText')

if (!require('chron')) install.packages('chron', repos = 'http://cran.us.r-project.org'); require('chron')
dtparts <- strsplit(tweets.csv$tweetTime[1],' ')
dtparts