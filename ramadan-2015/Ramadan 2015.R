
if (!require('igraph')) install.packages('igraph', repos = 'http://cran.us.r-project.org'); require('igraph')
if (!require('stringr')) install.packages('stringr', repos = 'http://cran.us.r-project.org'); require('stringr')
if (!require('Unicode')) install.packages('Unicode', repos = 'http://cran.us.r-project.org'); require('Unicode')


get.tweeters.top <- function(tweeters.list, threshold=0) {
  tweeters.table <- table(unlist(tweeters.list))
  
  # Get the more active tweeters
  tweeters.top <- names(sort(tweeters.table[tweeters.table>threshold], decreasing=TRUE))
  #   tweeters.top <- names(sort(tweeters.table, decreasing=TRUE))
  
  return(tweeters.top)
}

# Build a graph with the @names for vertices
build.graph <- function(tweeters.list, tweeters.top, is.directed=FALSE, is.isolates.deleted=TRUE) {
  g <- graph.empty(directed=is.directed)
  g <- g + vertices(tweeters.top)
  # plot(g)
  
  # Get list of tweets worth making edges for
  tweets.list <- tweeters.list[sapply(tweeters.list, function(x) {x[1] %in% tweeters.top})]
  for(x in tweets.list) {
    for(y in x[2:length(x)]) {
      if(y %in% tweeters.top) {
        g <- g + edge(x[1], y)
      }
    }
  }
  g <- simplify(g)
  # plot(g)
  if(is.isolates.deleted) {
    if(is.directed) {
      g <- delete.vertices(g, which(degree(g, mode='out')<1))
      g <- delete.vertices(g, which(degree(g, mode='in')<1))
      g <- delete.vertices(g, which(degree(g, mode='out')<1))
      g <- delete.vertices(g, which(degree(g, mode='in')<1))
      g <- delete.vertices(g, which(degree(g, mode='out')<1))
      g <- delete.vertices(g, which(degree(g, mode='in')<1))
      g <- delete.vertices(g, which(degree(g, mode='out')<1))
      g <- delete.vertices(g, which(degree(g, mode='in')<1))
    } else {
      g <- delete.vertices(g, which(degree(g)<2))
      g <- delete.vertices(g, which(degree(g)<2))
      g <- delete.vertices(g, which(degree(g)<2))
      g <- delete.vertices(g, which(degree(g)<2))
    }
  }
  
  return(g)
}


ramadan.df <- read.csv('Ramadan2015.csv', fileEncoding='',
                       numerals='no.loss', as.is=TRUE, stringsAsFactors=FALSE)

# Prepend the tweeter to the front of the tweet
ramadan.df$text <- as.factor(paste('@', ramadan.df$userName, ' ',
                                 ramadan.df$text, sep=''))

# Extact all the @names (tweeter will be in the front)
userName.list <- str_extract_all(ramadan.df$text, '@\\w+')
userName.mx <- as.matrix(userName.list)

# Show tweeters who are mentioning someone else
userName.list <- userName.mx[sapply(userName.mx, function(x) {length(x)>1})]
top.tweeters.mx <- as.matrix(get.tweeters.top(userName.list, 0))

# Big List
g <- build.graph(userName.list, top.tweeters.mx, is.directed=TRUE)
l <- layout.auto(g)
plot(g, main='Top Tweeters', vertex.shape='rectangle', vertex.size=10,
     vertex.size2=10, rescale=TRUE, layout=l)


# Heat Map
ramadan.df$tweetTime <- as.POSIXct(ramadan.df$tweetTime, format='%a %b %d %H:%M:%S +0000 %Y')

#Adjust time minus 5 hours
ramadan.df$tweetTime <- ramadan.df$tweetTime - 18000

#Adjust time again just so we focus in on important days minus 2 days
ramadan.df$tweetTime <- ramadan.df$tweetTime - 172800

# aggregate POSIXct seconds data every 10 minutes
if (!require('zoo')) install.packages('zoo', repos = 'http://cran.us.r-project.org'); require('zoo')
x <- zoo(ramadan.df$tweetTime)
x.agg <- aggregate(x, time(x) - as.numeric(time(x)) %% 600, mean)

x.min <- min(strftime(ramadan.df$tweetTime, format='%H:%M'))
x.min <- as.numeric(strftime(as.POSIXct(x.min, format='%H:%M'), format='%H'))*60 +
  as.numeric(strftime(as.POSIXct(x.min, format='%H:%M'), format='%M'))
x.max <- max(strftime(ramadan.df$tweetTime, format='%H:%M'))
x.max <- as.numeric(strftime(as.POSIXct(x.max, format='%H:%M'), format='%H'))*60 +
  as.numeric(strftime(as.POSIXct(x.max, format='%H:%M'), format='%M'))

y.min <- as.numeric(min(strftime(ramadan.df$tweetTime, format='%u')))
y.max <- as.numeric(max(strftime(ramadan.df$tweetTime, format='%u')))

data <- data.frame(x=seq(x.min, x.max),
                   y=rep(y.min:y.max, each=x.max-x.min+1),
                   z=0,
                   stringsAsFactors=FALSE)

# Loop through all the tweets and tally the minutes
for(i in 1:nrow(ramadan.df)) {
  x <- as.numeric(strftime(ramadan.df[i, 'tweetTime'], format='%H'))*60 +
    as.numeric(strftime(ramadan.df[i, 'tweetTime'], format='%M'))
  y <- as.numeric(strftime(ramadan.df[i, 'tweetTime'], format='%u'))
  row <- which(data$x==x & data$y==y)
  data[row, 'z'] <- data[row, 'z'] + 1
}

if (!require('akima')) install.packages('akima', repos = 'http://cran.us.r-project.org'); require('akima')
a <- interp(x=data$x, y=data$y, z=data$z)
filled.contour(a, color.palette=rainbow, plot.axes={axis(1, seq(x.min, x.max, by=60))
                                                    axis(2, y.min:y.max)})
