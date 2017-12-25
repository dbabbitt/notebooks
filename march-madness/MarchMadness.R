
if (!require('akima')) install.packages('akima', repos = 'http://cran.us.r-project.org'); require('akima')
if (!require('rjson')) install.packages('rjson', repos = 'http://cran.us.r-project.org'); require('rjson')

tweets.csv <- read.csv(file="tweets.csv", numerals="no.loss", stringsAsFactors=FALSE)
tweets.csv$tweetTime <- as.POSIXct(tweets.csv$tweetTime, format="%Y-%m-%d %H:%M:%S")
# tweets.csv$dstOffset <- 0
# tweets.csv$rawOffset <- 0
load("API.key.RData")
API.URL <- "https://maps.googleapis.com/maps/api/timezone/json?"
for(i in 1:nrow(tweets.csv)) {
  if(tweets.csv[i, "rawOffset"]==0) {
    lat <- tweets.csv[i, "lat"]
    lon <- tweets.csv[i, "lon"]
    tz.json <- fromJSON(file=paste0(API.URL, "location=", lat, ",", lon,
                                    "&timestamp=", as.numeric(tweets.csv[i, "tweetTime"]), "&key=", API.key))
    if(tz.json[["status"]] == "OVER_QUERY_LIMIT") break
    else Sys.sleep(1)
    dstOffset <- tz.json[["dstOffset"]]
    if(!is.null(dstOffset)) tweets.csv[i, "dstOffset"] <- dstOffset
    rawOffset <- tz.json[["rawOffset"]]
    if(!is.null(rawOffset)) tweets.csv[i, "rawOffset"] <- rawOffset
  }
}

tweets.csv$totOffset <- tweets.csv$dstOffset + tweets.csv$rawOffset
tweets.csv$tweetOffset <- tweets.csv$tweetTime + tweets.csv$totOffset

build.heatmap <- function(sample.df) {
  x.min <- min(strftime(sample.df$tweetOffset, format="%H:%M"))
  x.min <- as.numeric(strftime(as.POSIXct(x.min, format="%H:%M"), format="%H"))*60 +
    as.numeric(strftime(as.POSIXct(x.min, format="%H:%M"), format="%M"))
  x.max <- max(strftime(sample.df$tweetOffset, format="%H:%M"))
  x.max <- as.numeric(strftime(as.POSIXct(x.max, format="%H:%M"), format="%H"))*60 +
    as.numeric(strftime(as.POSIXct(x.max, format="%H:%M"), format="%M"))
  
  y.min <- as.numeric(min(strftime(sample.df$tweetOffset, format="%u")))
  y.max <- as.numeric(max(strftime(sample.df$tweetOffset, format="%u")))
  
  data <- data.frame(x=seq(x.min, x.max),
                     y=rep(y.min:y.max, each=x.max-x.min+1),
                     z=0,
                     stringsAsFactors=FALSE)
  
  # Loop through all the tweets and tally the minutes
  for(i in 1:nrow(sample.df)) {
    x <- as.numeric(strftime(sample.df[i, "tweetOffset"], format="%H"))*60 +
      as.numeric(strftime(sample.df[i, "tweetOffset"], format="%M"))
    y <- as.numeric(strftime(sample.df[i, "tweetOffset"], format="%u"))
    row <- which(data$x==x & data$y==y)
    data[row, "z"] <- data[row, "z"] + 1
  }
  
  if (!require('akima')) install.packages('akima', repos = 'http://cran.us.r-project.org'); require('akima')
  a <- interp(x=data$x, y=data$y, z=data$z)
  filled.contour(a, color.palette=rainbow, plot.axes={axis(1, seq(x.min, x.max, by=60))
                                                      axis(2, y.min:y.max)})
}

build.heatmap(tweets.csv[tweets.csv$totOffset==-25200, ])
build.heatmap(tweets.csv[tweets.csv$totOffset==-21600, ])
build.heatmap(tweets.csv[tweets.csv$totOffset==-18000, ])
build.heatmap(tweets.csv[tweets.csv$totOffset==-14400, ])

# Save a copy to manipulate in Excel
write.csv(tweets.csv, file="Data/tweets.csv", row.names=FALSE)
