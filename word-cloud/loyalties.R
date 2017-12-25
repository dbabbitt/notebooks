
# Read in the big data file
tweets.csv <- read.csv('tweets.csv')

# Make a data frame to hold the loyalty scores
loyalty.df <- data.frame(userName = unique(tweets.csv$userName),
                         patriots = 0, broncos = 0, steelers = 0, colts = 0, bengals = 0, ravens = 0,
                         seahawks = 0, packers = 0, cowboys = 0, panthers = 0, cardinals = 0, lions = 0)
teams <- names(loyalty.df)[2:length(names(loyalty.df))]

# Loop through all the tweets and inspect for and tally the team mentions
for(i in 1:nrow(tweets.csv)) {
  user.name <- tweets.csv[i, 'userName']
  user.row <- which(loyalty.df$userName == user.name)
  tweet.text <- tweets.csv[i, 'text']
  for(team.col in teams) {
    if(grepl(team.col, tweet.text, ignore.case = TRUE)) {
      loyalty.df[user.row, team.col] <- loyalty.df[user.row, team.col] + 1
    } 
  }
}

# Save a copy to manipulate in Java
write.csv(loyalty.df, file = 'loyalty.csv', row.names = FALSE)

loyalty.df$rownumber <- NULL
loyalty.df$loyalty <- ''
for(i in 1:nrow(loyalty.df)) {
  loyalty.df[i, 'loyalty'] <- names(which.max(loyalty.df[i, teams]))
}

loyalty.df[with(loyalty.df, order(-patriots)), ][1, ]
loyalty.df[with(loyalty.df, order(-broncos)), ][1, ]
loyalty.df[with(loyalty.df, order(-steelers)), ][1, ]
loyalty.df[with(loyalty.df, order(-colts)), ][1, ]
loyalty.df[with(loyalty.df, order(-bengals)), ][1, ]
loyalty.df[with(loyalty.df, order(-ravens)), ][1, ]
loyalty.df[with(loyalty.df, order(-seahawks)), ][1, ]
loyalty.df[with(loyalty.df, order(-packers)), ][1, ]
loyalty.df[with(loyalty.df, order(-cowboys)), ][1, ]
loyalty.df[with(loyalty.df, order(-panthers)), ][1, ]
loyalty.df[with(loyalty.df, order(-cardinals)), ][1, ]
loyalty.df[with(loyalty.df, order(-lions)), ][1, ]
