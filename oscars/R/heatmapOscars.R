
if (!require('akima')) install.packages('akima', repos = 'http://cran.us.r-project.org'); require('akima')
data <- data.frame(x=c(1,1,2,2,3,4,5,6,7,7,8,9),
                   y=c(2,4,5,1,3,8,4,8,1,1,6,9),
                   distance=c(66,84,93,76,104,29,70,19,60,50,46,36))
resolution <- 0.1 # you can increase the resolution by decreasing this number (warning: the resulting dataframe size increase very quickly)
a <- interp(x=data$x, y=data$y, z=data$distance, 
            xo=seq(min(data$x),max(data$x),by=resolution), 
            yo=seq(min(data$y),max(data$y),by=resolution), duplicate="mean")
image(a) #you can of course modify the color palette and the color categories. See ?image for more explanation

filled.contour(a, color.palette=heat.colors)

tweets.csv <- tweets.df
tweets.csv$tweetTime <- as.POSIXct(tweets.csv$tweetTime, format="%a %b %d %H:%M:%S %Y")

# Save a copy to manipulate in Excel
write.csv(tweets.csv, file="tweets.csv", row.names=FALSE)

# aggregate POSIXct seconds data every 10 minutes
# install.packages("zoo")
require("zoo")
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
a <- interp(x=data$x, y=data$y, z=data$z, 
            xo=seq(min(data$x), max(data$x), by=resolution), 
            yo=seq(min(data$y), max(data$y), by=resolution), duplicate="mean")
a <- interp(x=data$x, y=data$y, z=data$z)
image(a) #you can of course modify the color palette and the color categories. See ?image for more explanation

filled.contour(a, color.palette=heat.colors, plot.axes={ axis(1, seq(x.min, x.max, by=60))
                                                         axis(2, y.min:y.max)})