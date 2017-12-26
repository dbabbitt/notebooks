
if (!require('tm')) install.packages('tm'); require('tm')

# Get the file names
tweets.files <- list.files(path=paste(sep="/", getwd(), "tweets_wordfiltered"))

# First apply read.csv, then rbind
tweets.csv <- do.call("rbind", lapply(tweets.files, function(x) {
  read.csv(paste(sep="/", getwd(), "tweets_wordfiltered", x), stringsAsFactors=FALSE)}))
tweets.csv <- unique(tweets.csv)

tweets.corpus <- VCorpus(VectorSource(tweets.csv$text))
tweets.corpus <- tm_map(tweets.corpus, removePunctuation)
tweets.corpus <- tm_map(tweets.corpus, content_transformer(tolower))
tweets.corpus <- tm_map(tweets.corpus, removeNumbers)
strip.nonlatins <- function(x) {gsub("[^A-Za-z\\s]+", " ", x)}
tweets.corpus <- tm_map(tweets.corpus, strip.nonlatins)
tweets.corpus <- tm_map(tweets.corpus, PlainTextDocument)
tweets.corpus <- tm_map(tweets.corpus, function(x) {removeWords(x, stopwords())})
tweets.corpus <- tm_map(tweets.corpus, removeWords, c("amp", "theâ€"))

# Prepare data for word cloud and market basket analysis
tweets.tdm <- TermDocumentMatrix(tweets.corpus)
tweets.mx <- as.matrix(tweets.tdm)

# Add up the counts on each row to create a frequency table
if (!require('wordcloud')) install.packages('wordcloud'); require('wordcloud')
tweets.sorted <- sort(rowSums(tweets.mx), decreasing=TRUE)
tweets.sorted[1:50]
tweets.sorted.df <- as.data.frame(tweets.sorted)
tweets.sorted.df$Terms <- names(tweets.sorted)
colnames(tweets.sorted.df) <- c("Count", "Terms")
wordcloud(tweets.sorted.df$Terms[1:50], tweets.sorted.df$Count[1:50])

# Remove stop words
if (!require('arules')) install.packages('arules'); require('arules')
english.stop.words <- c(
  "a", "able", "about", "above", "abst", "accordance", "according", "accordingly", "across", "act", "actually", "added", "adj",
  "affected", "affecting", "affects", "after", "afterwards", "again", "against", "ah", "all", "almost", "alone", "along",
  "already", "also", "although", "always", "am", "among", "amongst", "an", "and", "announce", "another", "any", "anybody",
  "anyhow", "anymore", "anyone", "anything", "anyway", "anyways", "anywhere", "apparently", "approximately", "are", "aren",
  "arent", "arise", "around", "as", "aside", "ask", "asking", "at", "auth", "available", "away", "awfully", "b", "back", "be",
  "became", "because", "become", "becomes", "becoming", "been", "before", "beforehand", "begin", "beginning", "beginnings",
  "begins", "behind", "being", "believe", "below", "beside", "besides", "between", "beyond", "biol", "both", "brief", "briefly",
  "but", "by", "c", "ca", "came", "can", "cannot", "can't", "cause", "causes", "certain", "certainly", "co", "com", "come",
  "comes", "contain", "containing", "contains", "could", "couldnt", "d", "date", "did", "didn't", "different", "do", "does",
  "doesn't", "doing", "done", "don't", "down", "downwards", "due", "during", "e", "each", "ed", "edu", "effect", "eg", "eight",
  "eighty", "either", "else", "elsewhere", "end", "ending", "enough", "especially", "et", "et-al", "etc", "even", "ever",
  "every", "everybody", "everyone", "everything", "everywhere", "ex", "except", "f", "far", "few", "ff", "fifth", "first",
  "five", "fix", "followed", "following", "follows", "for", "former", "formerly", "forth", "found", "four", "from", "further",
  "furthermore", "g", "gave", "get", "gets", "getting", "give", "given", "gives", "giving", "go", "goes", "gone", "got",
  "gotten", "h", "had", "happens", "hardly", "has", "hasn't", "have", "haven't", "having", "he", "hed", "hence", "her", "here",
  "hereafter", "hereby", "herein", "heres", "hereupon", "hers", "herself", "hes", "hi", "hid", "him", "himself", "his",
  "hither", "home", "how", "howbeit", "however", "hundred", "i", "id", "ie", "if", "i'll", "im", "immediate", "immediately",
  "importance", "important", "in", "inc", "indeed", "index", "information", "instead", "into", "invention", "inward", "is",
  "isn't", "it", "itd", "it'll", "its", "itself", "i've", "j", "just", "k", "keep", "keeps", "kept", "kg", "km", "know",
  "known", "knows", "l", "largely", "last", "lately", "later", "latter", "latterly", "least", "less", "lest", "let", "lets",
  "like", "liked", "likely", "line", "little", "'ll", "look", "looking", "looks", "ltd", "m", "made", "mainly", "make", "makes",
  "many", "may", "maybe", "me", "mean", "means", "meantime", "meanwhile", "merely", "mg", "might", "million", "miss", "ml",
  "more", "moreover", "most", "mostly", "mr", "mrs", "much", "mug", "must", "my", "myself", "n", "na", "name", "namely", "nay",
  "nd", "near", "nearly", "necessarily", "necessary", "need", "needs", "neither", "never", "nevertheless", "new", "next",
  "nine", "ninety", "no", "nobody", "non", "none", "nonetheless", "noone", "nor", "normally", "nos", "not", "noted", "nothing",
  "now", "nowhere", "o", "obtain", "obtained", "obviously", "of", "off", "often", "oh", "ok", "okay", "old", "omitted", "on",
  "once", "one", "ones", "only", "onto", "or", "ord", "other", "others", "otherwise", "ought", "our", "ours", "ourselves",
  "out", "outside", "over", "overall", "owing", "own", "p", "page", "pages", "part", "particular", "particularly", "past",
  "per", "perhaps", "placed", "please", "plus", "poorly", "possible", "possibly", "potentially", "pp", "predominantly",
  "present", "previously", "primarily", "probably", "promptly", "proud", "provides", "put", "q", "que", "quickly", "quite",
  "qv", "r", "ran", "rather", "rd", "re", "readily", "really", "recent", "recently", "ref", "refs", "regarding", "regardless",
  "regards", "related", "relatively", "research", "respectively", "resulted", "resulting", "results", "right", "run", "s",
  "said", "same", "saw", "say", "saying", "says", "sec", "section", "see", "seeing", "seem", "seemed", "seeming", "seems",
  "seen", "self", "selves", "sent", "seven", "several", "shall", "she", "shed", "she'll", "shes", "should", "shouldn't",
  "show", "showed", "shown", "showns", "shows", "significant", "significantly", "similar", "similarly", "since", "six",
  "slightly", "so", "some", "somebody", "somehow", "someone", "somethan", "something", "sometime", "sometimes", "somewhat",
  "somewhere", "soon", "sorry", "specifically", "specified", "specify", "specifying", "still", "stop", "strongly", "sub",
  "substantially", "successfully", "such", "sufficiently", "suggest", "sup", "sure", "t", "take", "taken", "taking", "tell",
  "tends", "th", "than", "thank", "thanks", "thanx", "that", "that'll", "thats", "that've", "the", "their", "theirs", "them",
  "themselves", "then", "thence", "there", "thereafter", "thereby", "thered", "therefore", "therein", "there'll", "thereof",
  "therere", "theres", "thereto", "thereupon", "there've", "these", "they", "theyd", "they'll", "theyre", "they've", "think",
  "this", "those", "thou", "though", "thoughh", "thousand", "throug", "through", "throughout", "thru", "thus", "til", "tip",
  "to", "together", "too", "took", "toward", "towards", "tried", "tries", "truly", "try", "trying", "ts", "twice", "two", "u",
  "un", "under", "unfortunately", "unless", "unlike", "unlikely", "until", "unto", "up", "upon", "ups", "us", "use", "used",
  "useful", "usefully", "usefulness", "uses", "using", "usually", "v", "value", "various", "'ve", "very", "via", "viz", "vol",
  "vols", "vs", "w", "want", "wants", "was", "wasnt", "way", "we", "wed", "welcome", "we'll", "went", "were", "werent",
  "we've", "what", "whatever", "what'll", "whats", "when", "whence", "whenever", "where", "whereafter", "whereas", "whereby",
  "wherein", "wheres", "whereupon", "wherever", "whether", "which", "while", "whim", "whither", "who", "whod", "whoever",
  "whole", "who'll", "whom", "whomever", "whos", "whose", "why", "widely", "willing", "wish", "with", "within", "without",
  "wont", "words", "world", "would", "wouldn't", "www", "x", "y", "yes", "yet", "you", "youd", "you'll", "your", "you're",
  "yours", "yourself", "yourselves", "you've", "z", "zero")
tweets.clean <- tweets.csv$text
tweets.clean <- tolower(tweets.clean)
for(i in 1:length(english.stop.words)) {
  tweets.clean <- gsub(paste("\\b", english.stop.words[i], "\\b\\s*", sep=""), "", tweets.clean)
}
tweets.clean <- gsub("[^A-Za-z ]+", "", tweets.clean)
tweets.clean <- gsub("\\s+", " ", tweets.clean)

# Show tweet words broken up into vectors
tweets.list <- sapply(tweets.clean, function(x) {names(table(unlist(strsplit(x, "\\s+"))))})

# Set transaction names
names(tweets.list) <- paste("Tr", c(1:length(tweets.list)), sep="")

# Coerce into transactions
tweets.xact <- as(tweets.list, "transactions")

# Analyze transactions
inspect(tweets.xact)
summary(tweets.xact)
image(tweets.xact)

# Generate the association rules
tweets.apriori <- apriori(tweets.xact,
                        parameter=list(support=0.015, confidence=0.800, minlen=3))

# Analyze association rules
sink(file="tweets.apriori.txt")
inspect(tweets.apriori)
sink()

if (!require('zoo')) install.packages('zoo'); require('zoo')
tweets.csv$tweetTime <- as.POSIXct(tweets.csv$tweetTime, format="%a %b %d %H:%M:%S %Y")
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

if (!require('akima')) install.packages('akima'); require('akima')
resolution <- 0.1 # you can increase the resolution by decreasing this number
a <- interp(x=data$x, y=data$y, z=data$z, 
            xo=seq(min(data$x), max(data$x), by=resolution), 
            yo=seq(min(data$y), max(data$y), by=resolution), duplicate="mean")
a <- interp(x=data$x, y=data$y, z=data$z)
image(a) #you can of course modify the color palette and the color categories. See ?image for more explanation

filled.contour(a, color.palette=heat.colors, plot.axes={ axis(1, seq(x.min, x.max, by=60))
                                                         axis(2, y.min:y.max)})

if (!require('qdap')) install.packages('qdap'); require('qdap')
tweets.wfm <- as.wfm(tweets.corpus)
summary(tweets.wfm)
