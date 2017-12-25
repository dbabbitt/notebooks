
pairings <- read.csv('pairings.csv', na.strings=c('.', 'NA', '', '?'),
                     strip.white=TRUE, encoding='UTF-8')
pairings$Departure.Arrival.Time <- strptime(pairings$Departure.Arrival.Time, format='%I:%M:%S %p')
as.hexavigesimal <- function(number) {
        converted <- ''
        # Repeatedly divide the number by 26 and convert the
        # remainder into the appropriate letter.
        while(number > 0) {
          remainder <- (number - 1) %% 26
          converted <- paste(letters[remainder+1], converted, sep='')
          number <- (number - remainder) %/% 26
        }
 
  class(converted) <- 'hexavigesimal'
        return(converted)
    }
# > as.hexavigesimal(4878821185187)
# [1] 'wikipedia'
# attr(,'class')
# [1] 'hexavigesimal'

pairings$vertice <- apply(row(pairings),1,as.hexavigesimal)[1,]
write.table(pairings, file ='vertices.csv', row.names=FALSE, sep=',')
input <- c('Crew', 'Pairing', 'Flight.no', 'Origin.Destination',
           'Departure.Arrival.Time')
numeric <- c('Crew', 'Pairing', 'Flight.no')
categoric <- c('Origin.Destination')
temporal <- c('Departure.Arrival.Time')
save(pairings, input, numeric, categoric, file='pairings.RData', ascii=FALSE)
load('pairings.RData')

# install.packages('igraph')
require(igraph)
# install.packages('RColorBrewer')
require('RColorBrewer')

graph.airports <- levels(pairings$Origin.Destination)
options(warn = -1)  # drop vertice warnings about object length multiples
graph.pairings <- function(p) {
  pals <- c(brewer.pal(9, 'Greens')[1:9], brewer.pal(9, 'Blues')[1:9], 
            brewer.pal(9, 'Oranges')[1:9], brewer.pal(9, 'Purples')[1:9], 
            brewer.pal(9, 'Reds')[1:9], brewer.pal(9, 'Greys')[1:9])
  fc <- graph.empty()
  for(c in unique(p$Crew)) {
    tmp <- subset(p, Crew==c)
    count <- nrow(tmp)
    fc <- fc + vertices(tmp$vertice, color=pals[(c%%6)*9 + c%%9 + 1])
    x <- tmp$vertice[1:(count-1)]
    y <- tmp$vertice[2:count]
    for(i in 1:length(x)) {
      fc <- fc + edge(x[i], y[i], color='black',
                      label=subset(tmp, vertice==x)$Flight.no[i])
    }
  }
  fc.layout <- cbind(as.numeric(as.POSIXct(p$Departure.Arrival.Time)),
                     as.numeric(p$Origin.Destination))
  plot(0, type='n', ann=FALSE, axes=FALSE, xlim=extendrange(fc.layout[,1]), 
       ylim=extendrange(fc.layout[,2]))
  sapply(unique(p$Origin.Destination), function(n) {
    abline(h=n)
    text(x=0, y=n, labels=graph.airports[n], col='gray60', adj=c(0, -.1))})
  plot(fc, layout=fc.layout, rescale=FALSE, add=TRUE,
       vertex.shape='rectangle', vertex.size=83916.62/4, vertex.size2=31.48945/4,
       edge.arrow.size=0.4, vertex.label=NA)
}
# png(filename='pairings.png', width=480*8, height=480,
#     res=72*2, pointsize=12/2)
graph.pairings(subset(pairings, Crew==1))
# dev.off()
