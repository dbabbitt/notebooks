

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
  # 	tweeters.top <- names(sort(tweeters.table, decreasing=TRUE))
  
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

# Get the file names
tweets.files <- list.files(path=paste(sep="/", getwd(), "tweets_preOscars"),
                           pattern="^tweets_preOscars_.+_key\\.csv$", ignore.case=TRUE)

# First apply read.csv, then rbind
team.csv <- do.call("rbind", lapply(tweets.files, function(x) {
  read.csv(paste(sep="/", getwd(), "tweets_preOscars", x), stringsAsFactors=FALSE)}))
team.csv <- unique(team.csv)

# Prepend the tweeter to the front of the tweet
team.csv$text <- as.factor(paste("@", team.csv$userName, " ", team.csv$text, sep=""))

# Extact all the @names (tweeter will be in the front)
team.clean <- str_extract_all(team.csv$text, "@\\w+")

# Show tweeters who are mentioning someone else
big.list <- as.matrix(team.clean)
big.list <- big.list[sapply(big.list, function(x) {length(x)>1})]

# Show tweeters who are mentioning someone else
big.tweeters.top <- as.matrix(get.tweeters.top(big.list, 1000))

# Big List
g <- build.graph(big.list, big.tweeters.top, is.directed=TRUE)
l <- layout.auto(g)
plot(g, main="Everybody", vertex.shape="rectangle", vertex.size=10, vertex.size2=10, rescale=TRUE, layout=l)
plot(g, main="Everybody", vertex.shape="rectangle", vertex.size=10, vertex.size2=10, rescale=TRUE, layout=l,
     vertex.label=sapply(V(g)$name, tweeter.abbrv))
tweeters.top <- V(g)$name

# Cull out the triangles of conversation
triangle.tweeters <- c("@TheEllenShow", "@ActuallyNPH", "@ABC", "@neilmeron",
                       "@TheAcademy", "@craigzadan", "@ABCNetwork",
                       "@GMA", "@ladygaga")
random.conversations()

# Get all triangle tweeter tweets
triangle.tweets <- team.csv[which(paste(sep="", "@", team.csv$userName) %in% triangle.tweeters),
                            c("tweetID", "text", "tweetTime", "userID", "userName")]

# Extact all the @names (tweeter will be in the front)
triangle.tweets$tweeters <- str_extract_all(triangle.tweets$text, "@\\w+")
triangle.tweets$tweetTime <- strptime(triangle.tweets$tweetTime, format="%a %b %d %H:%M:%S %Y")
triangle.tweets$tweeters[1:2]
triangle.tweets[1:2, c("userName", "tweeters", "tweetTime")]
triangle.tweets <- triangle.tweets[order(triangle.tweets$tweetTime), ]

# Build a graph with the @names for vertices
g <- graph.empty(directed=TRUE)
g <- g + vertices(triangle.tweeters)

# Lay out in a circle to avoid edges going under vertices
l <- layout.circle(g)

plot(g, layout=l)

# Get list of tweets worth making edges for
edged <- FALSE
for(i in 1:length(triangle.tweets$tweeters)) {
  tweeters <- triangle.tweets[i, "tweeters"][[1]]
  originator <- tweeters[1]
  tweetTime <- triangle.tweets[i, "tweetTime"]
  for(tweeter in tweeters) {
    if(tweeter != originator) {
      if(tweeter %in% triangle.tweeters) {
        g <- g + edge(originator,  tweeter)
        edged <- TRUE
      }
    }
  }
  if(edged) {
    png(filename=strftime(tweetTime, format="%m_%d_%H_%M.png"))
    plot(g, main=strftime(tweetTime, format="%m/%d %H:%M"), layout=l)
    dev.off()
    edged <- FALSE
  }
}
# g <- simplify(g)
plot(optimal.community(g), g, main="Pre-Oscars", layout=l, vertex.label=" ")

lapply(triangle.tweets$tweeters, function(x) {
  if(length(x)>1 {
    
  }})

# Show tweeters who are mentioning someone else
triangle.tweeters.list <- as.matrix(team.clean)
triangle.tweeters.list <- triangle.tweeters.list[sapply(triangle.tweeters.list, function(x) {length(x)>1})]

# Triangle tweeters
g <- build.graph(triangle.tweeters.list, unique(triangle.tweets$userName), is.directed=TRUE, is.isolates.deleted=FALSE)
l <- layout.auto(g)
plot(g, main="Triangle tweeters", vertex.shape="rectangle", vertex.size=10, vertex.size2=10, rescale=TRUE, layout=l,
     vertex.label=sapply(V(g)$name, tweeter.abbrv))
plot(g, main="Triangle tweeters", vertex.shape="rectangle", vertex.size=10, vertex.size2=10, rescale=TRUE, layout=l)


# Colts vs Broncos
tweeters.top <- get.tweeters.top(colts.vs.broncos.tweeters.list)
g <- build.graph(colts.vs.broncos.tweeters.list, tweeters.top, is.directed=TRUE)
l <- layout.auto(g)
plot(g, main="Colts vs Broncos", vertex.shape="rectangle", vertex.size=10, vertex.size2=10, rescale=TRUE, layout=l,
     vertex.label=sapply(V(g)$name, tweeter.abbrv))
plot(g, main="Colts vs Broncos", vertex.shape="rectangle", vertex.size=10, vertex.size2=10, rescale=TRUE, layout=l)
# plot(g, layout=layout.random(g))
# plot(g, vertex.shape="rectangle", layout=layout.kamada.kawai(g),
#      vertex.label=sapply(row(layout.random(g))[, 1], as.hexavigesimal))

# Remove the colts and broncos @names and anaylze the communities
g <- delete.vertices(g, c("@Colts", "@Broncos"))
l <- layout.auto(g)
plot(g, main="Colts vs Broncos", vertex.shape="rectangle", vertex.size=10, vertex.size2=10, rescale=TRUE, layout=l,
     vertex.label=sapply(V(g)$name, tweeter.abbrv))
plot(g, main="Colts vs Broncos", vertex.shape="rectangle", vertex.size=10, vertex.size2=10, rescale=TRUE, layout=l)
plot(optimal.community(g), g, main="Colts vs Broncos Community Structure", vertex.shape="rectangle",
     vertex.size=10, vertex.size2=10, vertex.label=sapply(V(g)$name, tweeter.abbrv), layout=l)
# l <- layout.fruchterman.reingold(g)
# plot(g, vertex.shape="rectangle", layout=l, vertex.size=10, vertex.size2=10,
#      vertex.label=sapply(row(layout.random(g))[, 1], as.hexavigesimal))
# plot(g, layout=layout.spring(g))

# Colts vs Broncos: See how db, dc, cx, bt, and dd are doing
tweeters.top <- c("@DetFrankFrank", "@Dc5fanMary", "@4eyesJohnny", "@SoxOnTheBrain", "@FanForumsTV",
                  "@Colts", "@Broncos", "@Patriots", "@Ravens")
g <- build.graph(colts.vs.broncos.tweeters.list, tweeters.top, TRUE, FALSE)
l <- layout.auto(g)
plot(g, main="Colts vs Broncos", vertex.shape="rectangle", vertex.size=10, vertex.size2=10, rescale=TRUE, layout=l)

# Colts vs Patriots: See how db, dc, cx, bt, and dd are doing
tweeters.top <- c("@DetFrankFrank", "@Dc5fanMary", "@4eyesJohnny", "@SoxOnTheBrain", "@FanForumsTV",
                  "@Colts", "@Broncos", "@Patriots", "@Ravens")
g <- build.graph(colts.vs.pats.tweeters.list, tweeters.top, TRUE, FALSE)
l <- layout.auto(g)
plot(g, main="Colts vs Patriots", vertex.shape="rectangle", vertex.size=10, vertex.size2=10, rescale=TRUE, layout=l)

# Patriots vs Colts: See how db, dc, cx, bt, and dd are doing
tweeters.top <- c("@DetFrankFrank", "@Dc5fanMary", "@4eyesJohnny", "@SoxOnTheBrain", "@FanForumsTV",
                  "@Colts", "@Broncos", "@Patriots", "@Ravens")
g <- build.graph(pats.vs.colts.tweeters.list, tweeters.top, TRUE, FALSE)
l <- layout.auto(g)
plot(g, main="Patriots vs Colts", vertex.shape="rectangle", vertex.size=10, vertex.size2=10, rescale=TRUE, layout=l)


# Analyze the relationships between Patriots and Seahawks tweeters
hawks.vs.panthers <- "tweets/tweets_1_10_seahawks.csv" # playing the Panthers
hawks.vs.packers <- "tweets/tweets_1_18_packers.csv" # playing the Packers
hawks.vs.panthers.tweeters.list <- get.tweeters.list(hawks.vs.panthers)
hawks.vs.packers.tweeters.list <- get.tweeters.list(hawks.vs.packers)
big.list <- mapply(hawks.vs.panthers.tweeters.list, hawks.vs.packers.tweeters.list,
                   FUN=list, SIMPLIFY=FALSE)

# Show tweeters who are mentioning someone else
pats.vs.ravens.tweeters.list <- get.tweeters.list(pats.vs.ravens)
big.list <- mapply(big.list, pats.vs.ravens.tweeters.list,
                   FUN=list, SIMPLIFY=FALSE)
pats.vs.colts.tweeters.list <- get.tweeters.list(pats.vs.colts)
big.list <- mapply(big.list, pats.vs.colts.tweeters.list,
                   FUN=list, SIMPLIFY=FALSE)
big.tweeters.top <- as.matrix(get.tweeters.top(big.list))

# Seahawks vs Panthers
tweeters.top <- get.tweeters.top(hawks.vs.panthers.tweeters.list, 8)
g <- build.graph(hawks.vs.panthers.tweeters.list, tweeters.top)
l <- layout.auto(g)
plot(g, main="Seahawks vs Panthers", vertex.shape="rectangle", vertex.size=10, vertex.size2=10, rescale=TRUE, layout=l,
     vertex.label=sapply(V(g)$name, tweeter.abbrv))
plot(g, main="Seahawks vs Panthers", vertex.shape="rectangle", vertex.size=10, vertex.size2=10, rescale=TRUE, layout=l)
plot(optimal.community(g), g, main="Seahawks vs Panthers Community Structure", vertex.shape="rectangle",
     vertex.size=10, vertex.size2=10, vertex.label=sapply(V(g)$name, tweeter.abbrv), layout=l)

# Remove the seahawks and panthers @names and anaylze the communities
g <- delete.vertices(g, c("@Seahawks", "@Panthers"))
l <- layout.auto(g)
plot(g, main="Seahawks vs Panthers", vertex.shape="rectangle", vertex.size=10, vertex.size2=10, rescale=TRUE, layout=l,
     vertex.label=sapply(V(g)$name, tweeter.abbrv))
plot(g, main="Seahawks vs Panthers", vertex.shape="rectangle", vertex.size=10, vertex.size2=10, rescale=TRUE, layout=l)
plot(optimal.community(g), g, main="Seahawks vs Panthers Community Structure", vertex.shape="rectangle",
     vertex.size=10, vertex.size2=10, vertex.label=sapply(V(g)$name, tweeter.abbrv), layout=l)

####################################################################################################################

# Authenticate user
reqURL <- "https://api.twitter.com/oauth/request_token"
accessURL <- "http://api.twitter.com/oauth/access_token"
authURL <- "http://api.twitter.com/oauth/authorize"
load("consumerKey.RData")
load("consumerSecret.RData")
twitCred <- OAuthFactory$new(consumerKey=consumerKey,
                             consumerSecret=consumerSecret,
                             requestURL=reqURL,
                             accessURL=accessURL,
                             authURL=authURL)

# Complete the handshake
# Gets "SSL certificate problem: unable to get local issuer certificate"
twitCred$handshake()

registerTwitterOAuth(twitCred)

searchTwitter("patriots")

# Create a social network in gephi format
# Download the Zachary Karate Club network from Nexus
# paste(sep = "", getIgraphOpt("nexus.url"), "/api/dataset?id=karate&format=R-igraph")
# karate <- nexus.get("karate")
load("karate.Rdata")
karate

# Optimalize modularity
optcom <- optimal.community(karate)
print(modularity(optcom))
V(karate)$comm <- membership(optcom)
print(modularity(karate, membership(optcom)))
plot(optcom, karate)

# Compare to the greedy optimizer
fc <- fastgreedy.community(karate)
print(modularity(fc))

# Fit a HRG model to the network
hrg <- hrg.fit(karate)
hrg

# The fitted model, more details
print(hrg, level=5)

# Plot the full hierarchy, as an igraph graph
ihrg <- as.igraph(hrg)
ihrg$layout <- layout.reingold.tilford
plot(ihrg, vertex.size=10, edge.arrow.size=0.2)

# Customize the plot a bit, show probabilities and communities
vn <- sub("Actor ", "", V(ihrg)$name)
colbar <- rainbow(length(optcom))
vc <- ifelse(is.na(V(ihrg)$prob), colbar[V(karate)$comm], "darkblue")
V(ihrg)$label <- ifelse(is.na(V(ihrg)$prob), vn, round(V(ihrg)$prob, 2))
par(mar=c(0,0,3,0))
plot(ihrg, vertex.size=10, edge.arrow.size=0.2,
     vertex.shape="none", vertex.label.color=vc,
     main="Hierarchical network model of the Karate Club")

# Plot it as a dendrogram, looks better if the 'ape' package is installed
dendPlot(hrg)

# Make a very hierarchical graph
g1 <- graph.full(5)
g2 <- graph.ring(5)

g <- g1 + g2
g <- g + edge(1, vcount(g1)+1)

plot(g)

# Fit HRG
ghrg <- hrg.fit(g)
dendPlot(ghrg)

# Create a consensus dendrogram from multiple samples, takes longer...
hcons <- hrg.consensus(g)
hcons$consensus

# Predict missing edges
pred <- hrg.predict(g)
pred

# Add some the top 5 predicted edges to the graph, colored red
E(g)$color <- "grey"
lay <- layout.auto(g)
g2 <- add.edges(g, t(pred$edges[1:5,]), color="red")
plot(g2, layout=lay)

# Add four more predicted edges, colored orange
g3 <- add.edges(g2, t(pred$edges[6:9,]), color="orange")
plot(g3, layout=lay)

el <- matrix(data=c("foo", "bar", "bar", "foobar"), ncol=2, byrow=TRUE)
g13 <- graph.edgelist(el)
plot(g13)

# A complete graph of 12 vertices
set.seed(999);mydata=matrix(runif(24),ncol=2)
rownames(mydata)=LETTERS[1:12]
g=graph.adjacency(cov(t(mydata)),weighted=TRUE)
plot(g)

# A skinny graph with a few detached vertices
g=delete.edges(g, which(E(g)$weight <=.1))
plot(g)

# Here it is all cleaned up
g=delete.vertices(g,which(degree(g)<1))
plot(g)
