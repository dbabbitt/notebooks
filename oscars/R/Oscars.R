

# Get the file names
tweets.files <- list.files(path=paste(sep="/", getwd(), "tweets_preOscars"),
                           pattern="^extractedsentimentdata_tweets_preOscars_.+_key\\.csv$", ignore.case=TRUE)

# First apply read.csv, then rbind
tweets.csv <- do.call("rbind", lapply(tweets.files, function(x) {
  read.csv(paste(sep="/", getwd(), "tweets_preOscars", x), stringsAsFactors=FALSE)}))
tweets.csv <- unique(tweets.csv)


#============================================================
# Plot a Histogram

# install.packages("ggplot2")
require(ggplot2)

h<-hist(tweets.csv$Sentiment, breaks=6, col="blue", xlab="Sentiment", main="Sentiment") 
xfit<-seq(min(tweets.csv$Sentiment),max(tweets.csv$Sentiment),length=40) 
yfit<-dnorm(xfit,mean=mean(tweets.csv$Sentiment),sd=sd(tweets.csv$Sentiment)) 
yfit <- yfit*diff(h$mids[1:2])*length(tweets.csv$Sentiment) 
lines(xfit, yfit, col="black", lwd=2)

# install.packages("reshape2")
require(reshape2)
mdat <- melt(tweets.csv$Sentiment)
ph <- ggplot(mdat, aes(value)) +
  geom_histogram(aes(y=..density..), binwidth=5, colour='black', fill='skyblue') + 
  geom_density() + 
  facet_wrap(~variable, scales="free")
print(ph)

hist(tweets.csv$Sentiment, prob=TRUE, col="grey", breaks=6)# prob=TRUE for probabilities not counts
curve(dnorm(x, mean=mean(tweets.csv$Sentiment), sd=sd(tweets.csv$Sentiment)), add=TRUE)
lines(density(tweets.csv$Sentiment), col="blue", lwd=2) # add a density estimate with defaults
lines(density(tweets.csv$Sentiment, adjust=2), lty="dotted", col="darkgreen", lwd=2)

# Generate just the data for a histogram of the variable 'Sentiment'.
ds <- rbind(data.frame(dat=tweets.csv[, ][, "Sentiment"], grp="All"))

# Plot the data.
hs <- hist(ds[ds$grp=="All", 1], main="", xlab="Sentiment", ylab="Frequency",
           col="grey90", ylim=c(0, 84), breaks="fd", border=TRUE)
dens <- density(ds[ds$grp=="All", 1], na.rm=TRUE)
rs <- max(hs$counts)/max(dens$y)
# install.packages("colorspace")
require(colorspace)
lines(dens$x, dens$y*rs, type="l", col=rainbow_hcl(1)[1])

# Add a rug to the plot to highlight density distribution.
rug(ds[ds$grp=="All", 1])

# Add a title to the plot.
title(main="Distribution of Sentiment")

#============================================================

# Get the file names
tweets.files <- list.files(path=paste(sep="/", getwd(), "tweets_preOscars"),
                           pattern="^tweets_preOscars_.+_key\\.csv$", ignore.case=TRUE)

# First apply read.csv, then rbind
tweets.csv <- do.call("rbind", lapply(tweets.files, function(x) {
  read.csv(paste(sep="/", getwd(), "tweets_preOscars", x), stringsAsFactors=FALSE)}))
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


