
install.packages('twitteR')
library(twitteR)
install.packages('wordcloud')
library(wordcloud)
install.packages('tm')
library(tm)

# Clean the text for use
clean.text = function(x)
{
  x = tolower(x)
  x = gsub('\\brt\\b', '', x)
  x = gsub('\\bhttp\\w*', '', x)
  x = gsub('[^a-zA-Z0-9@#]', ' ', x)
  
  # Clean up white space
  x = gsub('\\s+', ' ', x)
  x = gsub('^\\s+', '', x)
  x = gsub('\\s+$', '', x)
  
  return(x)
}

# Import the files and clean them
txt1.csv <- read.csv('tweets_1_18_colts.csv')
txt1.csv$text <- as.factor(txt1.csv$text)
colts_clean = clean.text(txt1.csv$text)

txt2.csv <- read.csv('tweets_1_18_patriots.csv')
txt2.csv$text <- as.factor(txt2.csv$text)
patriots_clean = clean.text(txt2.csv$text)

# Finish work on files and combine them for use
colts = paste(colts_clean, collapse = ' ')
patriots = paste(patriots_clean, collapse = ' ')

all = c(colts, patriots)

# Remove common words
all = removeWords(all, c(stopwords('english'), 'a', 'able', 'about', 'actually', 'afan', 'afc', 'ago', 'aint', 'almost', 'alot', 'already', 'alright', 'also', 'always', 'am', 'amp', 'an', 'and', 'another', 'any', 'anybody', 'anymore', 'anyone', 'anything', 'anyway', 'anyways', 'are', 'arent', 'away', 'baby', 'back', 'bad', 'ball', 'ballgame', 'baltimore', 'bandwagon', 'bay', 'beat', 'beating', 'because', 'believe', 'believed', 'best', 'bestof', 'bet', 'better', 'bff', 'big', 'biggest', 'blew', 'blow', 'blows', 'blue', 'bound', 'bounds', 'bout', 'bowl', 'boy', 'boys', 'bring', 'bringing', 'bro', 'bros', 'brought', 'bruh', 'but', 'bye', 'came', 'can', 'cant', 'cannot', 'care', 'cause', 'championship', 'cheer', 'cheering', 'cheers', 'cheese', 'cheesehead', 'city', 'cmon', 'colorado', 'come', 'comes', 'comin', 'coming', 'could', 'couldnt', 'couldve', 'couple', 'cowgirl', 'cowgirls', 'crap', 'cuz', 'dallas', 'dang', 'darn', 'day', 'days', 'definitely', 'denver', 'denverbroncos', 'did', 'didnt', 'dislike', 'do', 'does', 'doesnt', 'dog', 'dogs', 'doing', 'done', 'dont', 'dub', 'dude', 'dudes', 'eah', 'early', 'easy', 'either', 'else', 'end', 'ending', 'england', 'enough', 'even', 'ever', 'every', 'everybody', 'everyone', 'fan', 'fans', 'far', 'fck', 'feel', 'feeling', 'feelings', 'feels', 'few', 'field', 'fgs', 'final', 'finally', 'fine', 'finna', 'foh', 'football', 'for', 'ftw', 'fukin', 'game', 'gameday', 'games', 'gave', 'get', 'gets', 'getting', 'girl', 'girls', 'give', 'gives', 'giving', 'go', 'goal', 'goals', 'god', 'goes', 'goin', 'going', 'gonna', 'good', 'got', 'gotta', 'great', 'green', 'greenbay', 'guess', 'gunna', 'guy', 'guys', 'ha', 'haha', 'half', 'happen', 'happened', 'happening', 'happens', 'hate', 'have', 'havent', 'hawks', 'he', 'hea', 'head', 'heard', 'heck', 'hell', 'hear', 'her', 'here', 'heres', 'hes', 'hey', 'him', 'hit', 'hitting', 'hold', 'holy', 'home', 'hope', 'hopefully', 'hoping', 'hour', 'hours', 'house', 'huh', 'i', 'idc', 'idk', 'if', 'ill', 'im', 'ima', 'in', 'indianapolis', 'init', 'ing', 'instead', 'int', 'is', 'isint', 'isnt', 'it', 'itll', 'its', 'ive', 'just', 'job', 'jobs', 'keep', 'kicked', 'kicking', 'kind', 'kinda', 'knew', 'know', 'knows', 'known', 'last', 'least', 'left', 'legit', 'less', 'let', 'lets', 'like', 'likes', 'line', 'lines', 'little', 'lmao', 'lol', 'look', 'looking', 'looks', 'los', 'losing', 'lose', 'loses', 'loss', 'lost', 'lot', 'love', 'made', 'make', 'makes', 'making', 'man', 'many', 'may', 'maybe', 'mean', 'means', 'meet', 'meeting', 'met', 'might', 'minutes', 'miss', 'more', 'move', 'moving', 'much', 'looked', 'must', 'nah', 'nation', 'need', 'needed', 'needs', 'never', 'new', 'next', 'nice', 'night', 'nfc', 'nfl', 'no', 'nobody', 'noh', 'not', 'nothing', 'now', 'oh', 'of', 'off', 'ok', 'okay', 'old', 'omg', 'one', 'ones', 'or', 'out', 'outta', 'pack', 'people', 'pick', 'place', 'places', 'play', 'played', 'player', 'players', 'playing', 'playoff', 'playoffs', 'plays', 'please', 'point', 'points', 'pre', 'probably', 'pull', 'put', 'rather', 'ready', 'real', 'really', 'red', 'repeat', 'return', 'returning', 'right', 'root', 'rooting', 'row', 'running', 'runs', 'said', 'saw', 'say', 'saying', 'says', 'score', 'scores', 'scoring', 'season', 'seattle', 'seattles', 'sea', 'see', 'seeing', 'seem', 'seems', 'seen', 'sees', 'serious', 'seriously', 'set', 'she', 'shes', 'should', 'shouldnt', 'shouldve', 'show', 'showed', 'showing', 'shows', 'side', 'sides', 'sigh', 'since', 'small', 'smh', 'so', 'some', 'somebody', 'something', 'sometime', 'sometimes', 'someone', 'spos', 'sposcenter', 'sta', 'stadium', 'stand', 'stands', 'stas', 'state', 'states', 'step', 'steps', 'still', 'stop', 'stupid', 'suck', 'sucked', 'sucking', 'sucks', 'super', 'superbowl', 'suppo', 'suppose', 'supposed', 'sure', 'swear', 'take', 'takes', 'taking', 'talk', 'talking', 'team', 'teams', 'tell', 'texan', 'texans', 'texas', 'thank', 'thanks', 'that', 'thats', 'the', 'thegame', 'their', 'theirs', 'there', 'theres', 'thewin', 'they', 'theyll', 'theyre', 'thing', 'things', 'think', 'thinking', 'thinks', 'this', 'thisgame', 'tho', 'though', 'thought', 'three', 'till', 'time', 'timeout', 'timeouts', 'to', 'today', 'todays', 'told', 'tonight', 'too', 'took', 'total', 'totally', 'touchdown', 'touchdowns', 'turn', 'try', 'trying', 'tweet', 'tweeting', 'tweets', 'twitter', 'two', 'ugh', 'versus', 'via', 'vs', 'wait', 'waitin', 'waiting', 'wanna', 'want', 'wanted', 'wants', 'was', 'wasnt', 'washington', 'watch', 'watched', 'watching', 'way', 'we', 'week', 'weekend', 'weeks', 'weekends', 'welcome', 'well', 'went', 'what', 'whatever', 'whats', 'who', 'whoever', 'whole', 'whos', 'whose', 'why', 'will', 'win', 'winning', 'wins', 'wisconsin', 'won', 'wont', 'word', 'words', 'worst', 'would', 'wouldnt', 'wouldve', 'wow', 'wtf', 'xiix', 'xlix', 'ya', 'yall', 'yard', 'yards', 'yea', 'yeah', 'year', 'years', 'yellow', 'yes', 'yet', 'yolo', 'york', 'you', 'youll', 'your', 'youre', 'yours', 'zone'))

# Create corpus
corpus = Corpus(VectorSource(all))

# Create term-document matrix
tdm = TermDocumentMatrix(corpus)

# Convert as matrix
tdm = as.matrix(tdm)

# Column names
colnames(tdm) = c('colts', 'patriots')

# Comparison Cloud
comparison.cloud(tdm, random.order = FALSE, colors = c('#00B2FF', 'red'), title.size = 1.5, max.words = 100)

# Commonality Cloud
commonality.cloud(tdm, random.order = FALSE, colors = brewer.pal(8, 'Dark2'), title.size = 1.5)

# Association Rules
require(arules, quietly = TRUE)

# Example 1: creating transactions from a list
a_list <- list(
  c('a', 'b', 'c'), c('a', 'b'), c('a', 'b', 'd'), c('c', 'e'), c('a', 'b', 'd', 'e')
)

# Set transaction names
names(a_list) <- paste('Tr', c(1:5), sep = '')
a_list

# Coerce into transactions
trans1 <- as(a_list, 'transactions')

# Analyze transactions
summary(trans1)
image(trans1)

# Example 2: creating transactions from a matrix
a_matrix <- matrix(c(
  1, 1, 1, 0, 0,
  1, 1, 0, 0, 0,
  1, 1, 0, 1, 0,
  0, 0, 1, 0, 1,
  1, 1, 0, 1, 1
), ncol = 5)

# Set dim names
dimnames(a_matrix) <- list(c('a', 'b', 'c', 'd', 'e'), paste('Tr', c(1:5), sep = ''))

a_matrix

# Coerce
trans2 <- as(a_matrix, 'transactions')
trans2
inspect(trans2)

# Example 3: creating transactions from data.frame
a_df <- data.frame(age = as.factor(c(6, 8, NA, 9, 16)),
                   grade = as.factor(c('A', 'C', 'F', NA, 'C')),
                   pass = c(TRUE, TRUE, FALSE, TRUE, TRUE))  

# Note: factors are translated differently to logicals and NAs are ignored
a_df

# Coerce
trans3 <- as(a_df, 'transactions') 
inspect(trans3)
as(trans3, 'data.frame')

# Example 4: creating transactions from a data.frame with 
# transaction IDs and items 
a_df3 <- data.frame(
  TID = c(1, 1, 2, 2, 2, 3), item = c('a', 'b', 'a', 'b', 'c', 'b')
)
a_df3
trans4 <- as(split(a_df3[, 'item'], a_df3[, 'TID']), 'transactions')
trans4
inspect(trans4)

# Show tweet words broken up into a vector
colts.list <- sapply(colts_clean, function(x) {names(table(unlist(strsplit(x, '\\s+'))))})

# Set transaction names
names(colts.list) <- paste('Tr', c(1:length(colts.list)), sep = '')

# Coerce into transactions
colts.xact <- as(colts.list, 'transactions')
colts.df <- as(colts.xact, 'data.frame')

# Analyze transactions
inspect(colts.xact)
summary(colts.xact)
image(colts.xact)

# Generate the association rules
colts.apriori <- apriori(colts.xact,
                         parameter = list(support = 0.100, confidence = 0.100, minlen = 2))

# Analyze association rules
inspect(colts.apriori)
summary(colts.apriori)

# Summarise the resulting rule set
generateAprioriSummary(colts.apriori)
