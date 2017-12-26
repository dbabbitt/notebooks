
# install.packages('twitteR')
require(twitteR)

# Clean the text for use
clean.text <- function(x)
{
  x <- tolower(x)
  x <- gsub('\\brt\\b', '', x)
  x <- gsub('\\ba\\b', '', x)
  x <- gsub('\\bto\\b', '', x)
  x <- gsub('\\bthe\\b', '', x)
  x <- gsub('\\bi\\b', '', x)
  x <- gsub('\\bin\\b', '', x)
  x <- gsub('\\band\\b', '', x)
  x <- gsub('\\bis\\b', '', x)
  x <- gsub('\\bthis\\b', '', x)
  x <- gsub('\\bbe\\b', '', x)
  x <- gsub('\\bit\\b', '', x)
  x <- gsub('\\bfor\\b', '', x)
  x <- gsub('\\bhttps?[^\\s]+', '', x)
  x <- gsub("['\'`]+', '', x)
  x <- gsub('[^a-zA-Z0-9@#_]+', ' ', x)
  
  # Clean up white space
  # x <- gsub('@\\s+', '@', x)
  # x <- gsub('#\\s+', '#', x)
  x <- gsub('\\s+', ' ', x)
  x <- gsub('^\\s+', '', x)
  x <- gsub('\\s+$', '', x)
  
  return(x)
}

# Import the files and clean them
team.csv <- read.csv('extractedlocationdata_20150111_cowboys_summary.csv')
team.clean <- clean.text(team.csv$Sentence)

# Association Rules
require(arules, quietly = TRUE)

# Show tweet words broken up into vectors
team.list <- sapply(team.clean, function(x) {names(table(unlist(strsplit(x, '\\s+'))))})

# Set transaction names
names(team.list) <- paste('Tr', c(1:length(team.list)), sep = '')

# Coerce into transactions
team.xact <- as(team.list, 'transactions')
# team.df <- as(team.xact, 'data.frame')

# Analyze transactions
# inspect(team.xact)
# summary(team.xact)
# image(team.xact)

# Generate the association rules
team.apriori <- apriori(team.xact,
                        parameter = list(support = 0.04, confidence = 0.100, minlen = 3))

# Analyze association rules
sink(file = 'apriori.txt')
inspect(team.apriori)
sink()
# summary(team.apriori)

gsub('\\bhttps?[^\\s]+', '',
     'I love my Cowboys  #finishthefight #cowboys @ Zapata Casa https://tco/cuujYzzsc3')
clean.text('I love my Cowboys  #finishthefight #cowboys @ Zapata Casa https://tco/cuujYzzsc3')
