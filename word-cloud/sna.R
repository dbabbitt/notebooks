
pairings <- read.csv("pairings.csv", na.strings=c(".", "NA", "", "?"),
                     strip.white=TRUE, encoding="UTF-8")
pairings$Departure.Arrival.Time <- strptime(pairings$Departure.Arrival.Time, format="%I:%M:%S %p")
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
# > as.hexavigesimal(4878821185187)
# [1] "wikipedia"
# attr(, "class")
# [1] "hexavigesimal"

pairings$vertice <- apply(row(pairings), 1, as.hexavigesimal)[1, ]
write.table(pairings, file ="vertices.csv", row.names=FALSE, sep=", ")
input <- c("Crew", "Pairing", "Flight.no", "Origin.Destination",
           "Departure.Arrival.Time")
numeric <- c("Crew", "Pairing", "Flight.no")
categoric <- c("Origin.Destination")
temporal <- c("Departure.Arrival.Time")
save(pairings, input, numeric, categoric, file="pairings.RData", ascii=FALSE)
load("pairings.RData")

# install.packages("sna")
require(sna)
# install.packages("RColorBrewer")
require("RColorBrewer")

graph.airports <- levels(pairings$Origin.Destination)
p <- subset(pairings, Crew<=5)
position.matrix <- cbind(as.numeric(as.POSIXct(p$Departure.Arrival.Time)),
                   as.numeric(p$Origin.Destination))
gplot(fc.layout)

#Open a plot window, and place some vertices
plot(0, 0, type="n", xlim=c(-1.5, 1.5), ylim=c(-1.5, 1.5), asp=1)
gplot.vertex(cos((1:10)/10*2*pi), sin((1:10)/10*2*pi), col=1:10,
             sides=3:12, radius=0.1)

# The graph for these examples has nine nodes and twelve directed edges

# Adjacency matrix with edge values:
data_vector <- c(0, 0, 0, 0, 0, 0, 0, 0, 0, 0.7, 0, 0, 0, 0, 0, 0, 0, 0, 
                 0, 0.1, 0, 0, 0, 0, 0, 0, 0, 0.9, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0.1, 0, 0.8, 0, 0, 0, 0, 0, 
                 0, 0, 0.2, 0, 0.9, 0, 0, 0, 0, 0, 0, 0, 0.4, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0.3, 0, 0.3, 0, 0, 
                 0, 0, 0, 0, 0, 0.5, 0, 0.6, 0)
data_matrix <- matrix(data_vector, nrow=9)

# Vector of edge values:
edge_data_vector <- c(0.7, 0.1, 0.9, 0.1, 0.8, 0.2, 0.9, 0.4, 0.3, 
                      0.3 , 0.5 , 0.6)

# Matrix for the node positions:
position_vector <- c(0, 0, 0, 1, 1, 1, 2, 2, 2, 2, 1, 0, 2, 1, 0, 2, 1, 0)
position_matrix <- matrix(position_vector, nrow=9)

# Vector for the node values:
node_vector <- c(3, 3, 4, 5, 6, 4, 3, 6, 5)

# Setting size of each node
gplot(data_matrix, coord=position_matrix, gmode="graph", jitter=FALSE, 
      displaylabels=TRUE, boxed.labels=FALSE, label.pos=1, vertex.cex=node_vector,
      adj=c(0, -.1))

options(warn = -1)  # drop vertice warnings about object length multiples
graph.pairings <- function(p) {
  pals <- c(brewer.pal(9, "Greens")[1:9], brewer.pal(9, "Blues")[1:9], 
            brewer.pal(9, "Oranges")[1:9], brewer.pal(9, "Purples")[1:9], 
            brewer.pal(9, "Reds")[1:9], brewer.pal(9, "Greys")[1:9])
  fc <- graph.empty()
  for(c in unique(p$Crew)) {
    tmp <- subset(p, Crew==c)
    count <- nrow(tmp)
    fc <- fc + vertices(tmp$vertice, color=pals[(c%%6)*9 + c%%9 + 1])
    x <- tmp$vertice[1:(count-1)]
    y <- tmp$vertice[2:count]
    for(i in 1:length(x)) {
      fc <- fc + edge(x[i], y[i], color="black", label=subset(tmp, vertice==x)$Flight.no[i])
    }
  }
  fc.layout <- cbind(as.numeric(as.POSIXct(p$Departure.Arrival.Time)),
                     as.numeric(p$Origin.Destination))
  plot(0, type="n", ann=FALSE, axes=FALSE, xlim=extendrange(fc.layout[, 1]), 
       ylim=extendrange(fc.layout[, 2]))
  sapply(unique(p$Origin.Destination), function(n) {
    abline(h=n)
    text(x=0, y=n, labels=graph.airports[n], col="gray60", adj=c(0, -.1))})
  plot(fc, layout=fc.layout, rescale=FALSE, add=TRUE,
       vertex.shape="rectangle",
       vertex.size=(strwidth(V(fc)$label) + strwidth("oo")) * 100,
       vertex.size2=strheight("kk") * 2 * 100, edge.arrow.size=0.4)
}
graph.pairings(subset(pairings, Crew<=5))
