
# install.packages('twitteR')
require(twitteR)

# install.packages('stringr')
require(stringr)

# Get the files names
tweets.files = list.files(path=paste(sep='/', getwd(), 'tweets'), pattern='\\.csv$', ignore.case=TRUE)

# First apply read.csv, then rbind
tweets.df = do.call('rbind', lapply(tweets.files, function(x) {
  read.csv(paste(sep='/', getwd(), 'tweets', x), stringsAsFactors = FALSE)}))

# Remove the tab at the end of some user ids and tweet ids
tweets.df$userID <- gsub('\t', '', tweets.df$userID)
tweets.df$tweetID <- gsub('\t', '', tweets.df$tweetID)
tweets.df$text <- gsub('&amp;', 'and', tweets.df$text)
# tweets.df$text <- gsub('\\s+@\\s+', ' at ', tweets.df$text)
tweets.df <- unique(tweets.df)

# Save a copy to manipulate in Java
write.csv(tweets.df, file='tweets.csv', row.names=FALSE)

sort(table(tweets.df$userID), decreasing=TRUE)[1:10]
tweets.df[which(tweets.df$userID==118934371), 'text']
tweets.df[which(tweets.df$userID==70744212), 'text']
tweets.df[which(tweets.df$userID==304627207), 'text']
tweets.df[which(tweets.df$userID==35112263), 'text']
