tweets.csv <- read.csv(file="tweets_MarchMadness_March26to29_Test.csv", numerals="no.loss", stringsAsFactors=FALSE)
tweets.csv$tweetTime <- as.POSIXct(tweets.csv$tweetTime, format="%a %b %d %H:%M:%S %Y")

#Adjust time minus 5 hours
tweets.csv$tweetTime <- tweets.csv$tweetTime - 18000

#Adjust time again just so we focus in on important days minus 2 days
tweets.csv$tweetTime <- tweets.csv$tweetTime - 172800

# Save a copy to manipulate in Excel
write.csv(tweets.csv, file="a.csv", row.names=FALSE)

# aggregate POSIXct seconds data every 10 minutes
if (!require('zoo')) install.packages('zoo', repos = 'http://cran.us.r-project.org'); require('zoo')
x <- zoo(tweets.csv$tweetTime)
x.agg <- aggregate(x, time(x) - as.numeric(time(x)) %% 600, mean)
max(strftime(tweets.csv$tweetTime, format="%H:%M"))

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

if (!require('akima')) install.packages('akima', repos = 'http://cran.us.r-project.org'); require('akima')
a <- interp(x=data$x, y=data$y, z=data$z, 
            xo=seq(min(data$x), max(data$x), by=resolution), 
            yo=seq(min(data$y), max(data$y), by=resolution), duplicate="mean")
a <- interp(x=data$x, y=data$y, z=data$z)
image(a) #you can of course modify the color palette and the color categories. See ?image for more explanation

filled.contour(a, color.palette=rainbow, plot.axes={ axis(1, seq(x.min, x.max, by=60))
                                                         axis(2, y.min:y.max)})
#title("March Madness Termporal Heatmap", xlab ="Time", ylab = "Dates")


#filled.contour(a, color.palette=rainbow, plot.axes={ axis(1, seq(x.min, x.max, by=60))
#axis(2, y.min:y.max)})
