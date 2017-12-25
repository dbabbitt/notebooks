
file.name <- format(as.Date(Sys.time())-1, 'FBOFeed%Y%m%d')
# ftp://ftp.fbo.gov/FBOFeed20140806
# file.url <- paste('ftp://ftp.fbo.gov/', file.name, sep='')
# file.download <- download.file(url=file.url,
#               destfile=paste(file.name, '.txt', sep=''), quiet=FALSE)
# file.download <- url(file.url, open='r')

# install.packages('rjson')
require('rjson')
fbo.data <- fromJSON(file=paste(file.name, '.json', sep=''))

fbo.types <- unlist(lapply(fbo.data, function(x) {
  names(x[[1]])
}))

fbo.list <- sapply(1:length(fbo.types), function(row.number) {
  eval(parse(text=paste('fbo.data[[', row.number,
                               ']][[1]]$', fbo.types[row.number], sep='')))
})

fbo.title <- sapply(1:length(fbo.list), function(row.number) {
  title <- eval(parse(text=paste('fbo.list[[', row.number,
                        ']]$SUBJECT', sep='')))
  if(is.null(title)) {title <- ''}
  return(title)
})

fbo.ccode <- sapply(1:length(fbo.list), function(row.number) {
  ccode <- eval(parse(text=paste('fbo.list[[', row.number,
                                 ']]$CLASSCOD', sep='')))
  if(is.null(ccode)) {ccode <- ''}
  return(ccode)
})

fbo.naics <- sapply(1:length(fbo.list), function(row.number) {
  naics <- eval(parse(text=paste('fbo.list[[', row.number,
                                 ']]$NAICS', sep='')))
  if(is.null(naics)) {naics <- ''}
  return(naics)
})

fbo.solnumber <- sapply(1:length(fbo.list), function(row.number) {
  solnumber <- eval(parse(text=paste('fbo.list[[', row.number,
                                     ']]$SOLNBR', sep='')))
  if(is.null(solnumber)) {solnumber <- ''}
  return(solnumber)
})

fbo.setaside <- sapply(1:length(fbo.list), function(row.number) {
  setaside <- eval(parse(text=paste('fbo.list[[', row.number,
                                    ']]$SETASIDE', sep='')))
  if(is.null(setaside)) {setaside <- ''}
  return(setaside)
})

fbo.createddate <- sapply(1:length(fbo.list), function(row.number) {
  MMDD <- eval(parse(text=paste('fbo.list[[', row.number,
                                ']]$DATE', sep='')))
  if(is.null(MMDD)) {MMDD <- '0101'}
  YY <- eval(parse(text=paste('fbo.list[[', row.number,
                                ']]$YEAR', sep='')))
  if(is.null(YY)) {YY <- '00'}
  createddate <- paste(MMDD, YY, sep='')
  
  return(createddate)
})

fbo.synopsis <- sapply(1:length(fbo.list), function(row.number) {
  synopsis <- eval(parse(text=paste('fbo.list[[', row.number,
                                    ']]$DESC', sep='')))
  if(is.null(synopsis)) {synopsis <- ''}
  return(synopsis)
})

fbo.responsedate <- sapply(1:length(fbo.list), function(row.number) {
  responsedate <- eval(parse(text=paste('fbo.list[[', row.number,
                                        ']]$RESPDATE', sep='')))
  if(is.null(responsedate)) {responsedate <- '010100'}
  
  return(responsedate)
})

fbo.df <- data.frame(type=as.factor(fbo.types), title=fbo.title,
                     ccode=as.factor(fbo.ccode), naics=as.factor(fbo.naics),
                     solnumber=fbo.solnumber, setaside=as.factor(fbo.setaside),
                     createddate=as.Date(fbo.createddate, '%m%d%y'),
                     responsedate=as.Date(fbo.responsedate, '%m%d%y'),
                     synopsis=fbo.synopsis, recommended='NO', author='fbo.gov',
                     filename=format(as.Date(Sys.time())-1, 'FBOFeed%Y%m%d'),
                     language='en_US', origin='ftp.fbo.gov', stringsAsFactors=FALSE)
# fbo.df[fbo.df$type=='SSALE', ]$recommended <- 'NO'
fbo.df$description <- "Nightly file-based notice 
information from the Federal Business Opportunities (https://www.fbo.gov/) 
application / database. The FBO feed files include new and updated 
opportunities, information about awarded contracts, and other details 
concerning the offer and disposition of federal government contracts and 
tenders."

save(fbo.df, file='fbo-df.RData')

fbo.dict <- c('defense', 'intelligence', 'CBRN', 'training', 'analysis', 'threat', 'counter',
              'leadership', 'terrorism', 'biometrics', 'IED', 'NATO', 'forensics', 'explosive',
              'bomb disposal', 'crisis management', 'improvised explosive device', 'risk',
              'capability development', 'counter-threat', 'doctrine', 'policy', 'risk management',
              'search', 'special operations', 'cyber')

# install.packages('tm')
require(tm)
fbo.dc <- PlainTextDocument(x=fbo.df$synopsis, author=fbo.df$author,
                            datetimestamp = as.POSIXlt(fbo.df$createddate, tz = 'GMT'),
                            description=fbo.df$description, heading=fbo.df$title,
                            id=fbo.df$solnumber, language=fbo.df$language,
                            origin=fbo.df$origin, localmetadata=list(type=fbo.df$type,
                                                                     ccode=fbo.df$ccode,
                                                                     naics=fbo.df$naics,
                                                                     setaside=fbo.df$setaside,
                                                                     responsedate=fbo.df$responsedate))

fbo.vs <- VectorSource(fbo.dc)
fbo.vc <- Corpus(fbo.vs)


# strip whitspace from the documents in the collection
fbo.vc <- tm_map(fbo.vc, stripWhitespace)

# convert uppercase to lowercase in the document collection
fbo.vc <- tm_map(fbo.vc, tolower)

# remove numbers from the document collection
fbo.vc <- tm_map(fbo.vc, removeNumbers)

# remove punctuation from the document collection
fbo.vc <- tm_map(fbo.vc, removePunctuation)

# using a standard list, remove English stopwords from the document collection
fbo.vc <- tm_map(fbo.vc, removeWords, stopwords('english'))

fbo.tdm <- TermDocumentMatrix(fbo.vc, list(dictionary=fbo.dict))

# inspect.id <- function(searchterm, number) {
#   sink('NUL')
#   i <- inspect(fbo.tdm[searchterm, ])
#   sink()
#   paste(meta(fbo.dc, tag='ID')[which(i>0)][number],
#         meta(fbo.dc, tag='LocalMetaData')[['naics']][which(i>0)][number],
#         meta(fbo.dc, tag='Heading')[which(i>0)][number],
#         sep='\t')
# }
# 
# inspect.all <- function(searchterm) {
#   sink('NUL')
#   i <- inspect(fbo.tdm[searchterm, ])
#   sink()
#   cbind(searchterm,
#         meta(fbo.dc, tag='ID')[which(i>0)],
#         meta(fbo.dc, tag='LocalMetaData')[['naics']][which(i>0)],
#         meta(fbo.dc, tag='Heading')[which(i>0)])
# }

todays.listings.df <- data.frame(term=NULL, id=NULL, naics=NULL, title=NULL, stringsAsFactors=FALSE)
# searchterm <- 'defense'
for(searchterm in fbo.dict) {
  sink('NUL')
  i <- inspect(fbo.tdm[searchterm, ])
  sink()
  
  id <- meta(fbo.dc, tag='ID')[which(i>0)]
  if(length(id)>1) {
    newRow <- data.frame(term=searchterm,
                         id=id,
                         title=meta(fbo.dc, tag='Heading')[which(i>0)],
                         ccode=meta(fbo.dc, tag='LocalMetaData')[['ccode']][which(i>0)],
                         naics=meta(fbo.dc, tag='LocalMetaData')[['naics']][which(i>0)],
                         stringsAsFactors=FALSE)
    todays.listings.df <- rbind(todays.listings.df, newRow)
  }
#   colnames(todays.listings.df) <- c('term', 'id', 'naics', 'title')
}
write.csv(todays.listings.df, file='todays.listings.csv', row.names=FALSE)

# sink('NUL')
# i <- inspect(fbo.tdm['defense', ])
# sink()
