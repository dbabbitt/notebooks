

# Get the file names
tweets.files <- list.files(path=paste(sep="/", getwd(), "data"),
                           pattern="^tweets_wordfiltered_\\d+_\\d+\\.csv$", ignore.case=TRUE)

# First apply read.csv, then rbind
tweets.csv <- do.call("rbind", lapply(tweets.files, function(x) {
  read.csv(paste(sep="/", getwd(), "data", x), stringsAsFactors=FALSE)}))
tweets.csv$tweetTime <- as.POSIXct(tweets.csv$tweetTime, format="%a %b %d %H:%M:%S %Y")
tweets.csv <- tweets.csv[complete.cases(tweets.csv[, 3]), ]
tweets.csv <- unique(tweets.csv)

# Save a copy to manipulate in Excel
write.csv(tweets.csv, file="tweets.csv", row.names=FALSE)


x.min <- min(strftime(tweets.csv$tweetTime, format="%H:%M"))
x.min <- as.numeric(strftime(as.POSIXct(x.min, format="%H:%M"), format="%H"))*60 +
  as.numeric(strftime(as.POSIXct(x.min, format="%H:%M"), format="%M"))
x.max <- max(strftime(tweets.csv$tweetTime, format="%H:%M"))
x.max <- as.numeric(strftime(as.POSIXct(x.max, format="%H:%M"), format="%H"))*60 +
  as.numeric(strftime(as.POSIXct(x.max, format="%H:%M"), format="%M"))
seq(x.min, x.max)
y.min <- as.numeric(min(strftime(tweets.csv$tweetTime, format="%u")))
y.max <- as.numeric(max(strftime(tweets.csv$tweetTime, format="%u")))
seq(y.min, y.max)

data <- data.frame(x=seq(x.min, x.max),
                   y=rep(y.min:y.max, each=x.max-x.min+1),
                   z=0,
                   stringsAsFactors=FALSE)

# Loop through all the tweets and tally the minutes
for(i in 1:nrow(tweets.csv)) {
  x <- as.numeric(strftime(tweets.csv[i, "tweetTime"], format="%H"))*60 +
    as.numeric(strftime(tweets.csv[i, "tweetTime"], format="%M"))
  y <- as.numeric(strftime(tweets.csv[i, "tweetTime"], format="%u"))
  row <- which(data$x==x & data$y==y)
  data[row, "z"] <- data[row, "z"] + 1
}

resolution <- 0.1 # you can increase the resolution by decreasing this number
# install.packages("akima")
require(akima)
a <- interp(x=data$x, y=data$y, z=data$z, 
            xo=seq(min(data$x), max(data$x), by=resolution), 
            yo=seq(min(data$y), max(data$y), by=resolution), duplicate="mean")
image(a) #you can of course modify the color palette and the color categories. See ?image for more explanation

filled.contour(a, color.palette=heat.colors, plot.axes={ axis(1, seq(x.min, x.max, by=60))
                                                         axis(2, y.min:y.max)})

# install.packages("twitteR")
require(twitteR)

# install.packages("stringr")
require(stringr)

# install.packages("igraph")
require(igraph)

as.hexavigesimal <- function(number) {
  converted <- ""
  # Repeatedly divide the number by 26 and convert the
  # remainder into the appropriate letter.
  while(number > 0) {
    remainder <- (number - 1) %% 26
    converted <- paste(letters[remainder+1], converted, sep="")
    number <- (number - remainder) %/% 26
  }
  
  class(converted) <- "hexavigesimal"
  return(converted)
}

get.tweeters.top <- function(tweeters.list, threshold=0) {
  tweeters.table <- table(unlist(tweeters.list))
  
  # Get the more active tweeters
  tweeters.top <- names(sort(tweeters.table[tweeters.table>threshold], decreasing=TRUE))
  #   tweeters.top <- names(sort(tweeters.table, decreasing=TRUE))
  
  return(tweeters.top)
}

# Get hexavigesimal abbreviations
tweeter.abbrv <- function(tweeter) {
  abbrv <- sapply(row(big.tweeters.top), as.hexavigesimal)[which(big.tweeters.top %in% tweeter, arr.ind=TRUE)]
  
  return(abbrv)
}
# tweeter.abbrv("@Hibachi11")

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
      g <- delete.vertices(g, which(degree(g, mode="out")<1))
      g <- delete.vertices(g, which(degree(g, mode="in")<1))
      g <- delete.vertices(g, which(degree(g, mode="out")<1))
      g <- delete.vertices(g, which(degree(g, mode="in")<1))
      g <- delete.vertices(g, which(degree(g, mode="out")<1))
      g <- delete.vertices(g, which(degree(g, mode="in")<1))
      g <- delete.vertices(g, which(degree(g, mode="out")<1))
      g <- delete.vertices(g, which(degree(g, mode="in")<1))
    } else {
      g <- delete.vertices(g, which(degree(g)<2))
      g <- delete.vertices(g, which(degree(g)<2))
      g <- delete.vertices(g, which(degree(g)<2))
      g <- delete.vertices(g, which(degree(g)<2))
    }
  }
  
  return(g)
}

random.conversations <- function() {
  g <- build.graph(big.list, sample(tweeters.top, 80), is.directed=TRUE)
  l <- layout.auto(g)
  plot(g, main="Big Talkers", vertex.shape="rectangle", vertex.size=10, vertex.size2=10, rescale=TRUE, layout=l)
  sort(V(g)$name)
}

# Prepend the tweeter to the front of the tweet
tweets.csv$text <- as.factor(paste("@", tweets.csv$userName, " ", tweets.csv$text, sep=""))

# Extact all the @names (tweeter will be in the front)
team.clean <- str_extract_all(tweets.csv$text, "@\\w+")

# Show tweeters who are mentioning someone else
big.list <- as.matrix(team.clean)
big.list <- big.list[sapply(big.list, function(x) {length(x)>1})]

# Show tweeters who are mentioned the most
big.tweeters.top <- as.matrix(get.tweeters.top(big.list, 1))

# Big List
g <- build.graph(big.list, big.tweeters.top, is.directed=TRUE)
l <- layout.auto(g)
plot(g, main="Everybody", vertex.shape="rectangle", vertex.size=10, vertex.size2=10, rescale=TRUE, layout=l)
tweeters.top <- V(g)$name
