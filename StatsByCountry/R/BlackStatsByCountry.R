
if(!require('rattle')) install.packages('rattle', repos = 'http://cran.us.r-project.org'); require('rattle')
rattle()

# Rattle is Copyright (c) 2006-2013 Togaware Pty Ltd.

# ============================================================ 
# Rattle timestamp: 2015-07-04 06:50:31 x86_64-w64-mingw32 

# Rattle version 3.0.2 user 'Dave'

# Export this log textview to a file using the Export button or the Tools 
# menu to save a log of all activity. This facilitates repeatability. Exporting 
# to file 'myrf01.R', for example, allows us to the type in the R Console 
# the command source('myrf01.R') to repeat the process automatically. 
# Generally, we may want to edit the file to suit our needs. We can also directly 
# edit this current log textview to record additional information before exporting. 

# Saving and loading projects also retains this log.

library(rattle)

# This log generally records the process of building a model. However, with very 
# little effort the log can be used to score a new dataset. The logical variable 
# 'building' is used to toggle between generating transformations, as when building 
# a model, and simply using the transformations, as when scoring a dataset.

building <- TRUE
scoring  <- ! building

# The colorspace package is used to generate the colours used in plots, if available.

library(colorspace)

# A pre-defined value is used to reset the random seed so that results are repeatable.

seed <- 42 

# ============================================================ 
# Rattle timestamp: 2015-07-04 06:50:40 x86_64-w64-mingw32 

# Load the data.

dataset <- read.csv('file:///C:/Users/Dave/Google Drive/Other/Neoreaction/BlackStatsByCountry/blackstatsbycountry.csv', na.strings = c('.', 'NA', '', '?'), strip.white = TRUE, encoding = 'UTF-8')
dim(dataset)[1]
nrow(dataset)
levels(dataset$Racial_Region)
baw <- subset(dataset, Racial_Region == 'African' | Racial_Region == 'European',
              select = c(Country, Racial_Region, UNODC_murder_Rate, Lynn_Vanhanen_Avg_IQ))
if(!require('rpart')) install.packages('rpart', repos = 'http://cran.us.r-project.org'); require('rpart')
try.tree <- rpart(Racial_Region ~ UNODC_murder_Rate + Lynn_Vanhanen_Avg_IQ, data = baw)
print(try.tree)
try.tree <- rpart(Racial_Region ~ UNODC_murder_Rate, data = baw)
print(try.tree)
subset(baw, Racial_Region == 'European' & UNODC_murder_Rate > = 5,
       select = c(Country, Racial_Region, UNODC_murder_Rate, Lynn_Vanhanen_Avg_IQ))
plot(try.tree)
fancyRpartPlot(try.tree, main = 'Decision Tree Racial_Region')
mean(subset(baw, Racial_Region == 'European', select = c(UNODC_murder_Rate))$UNODC_murder_Rate)
mean(subset(baw, Racial_Region == 'African', select = c(UNODC_murder_Rate))$UNODC_murder_Rate)
sd(subset(baw, Racial_Region == 'European', select = c(UNODC_murder_Rate))$UNODC_murder_Rate)
sd(subset(baw, Racial_Region == 'African', select = c(UNODC_murder_Rate))$UNODC_murder_Rate)
t.test(subset(baw, Racial_Region == 'European', select = c(UNODC_murder_Rate))$UNODC_murder_Rate,
       subset(baw, Racial_Region == 'African', select = c(UNODC_murder_Rate))$UNODC_murder_Rate)

baw$Atlantic_Slave_Trade <- 'No'
baw[baw$Country %in% c('Senegal', 'Gambia', 'Guinea-Bissau', 'Guinea', 'Sierra Leone',
                       'Liberia', "Côte d'Ivoire', 'Ghana', 'Togo', 'Benin', 'Nigeria",
                       'Cameroon', 'Equatorial Guinea', 'Gabon', 'Congo', 'Angola', 'Mozambique',
                       'Madagascar'), ]$Atlantic_Slave_Trade <- 'Yes'
baw[baw$Country %in% c('Portugal', 'United Kingdom', 'United States - Black', 'United States - Total',
                       'United States - White', 'Spain', 'France', 'Netherlands',
                       'Denmark'), ]$Atlantic_Slave_Trade <- 'Yes'
t.test(subset(baw, Racial_Region == 'African' & Atlantic_Slave_Trade == 'Yes',
              select = c(UNODC_murder_Rate))$UNODC_murder_Rate,
       subset(baw, Racial_Region == 'African' & Atlantic_Slave_Trade == 'No',
              select = c(UNODC_murder_Rate))$UNODC_murder_Rate)
# ============================================================ 
# Rattle timestamp: 2015-07-04 06:50:40 x86_64-w64-mingw32 

# Note the user selections. 

# Build the training/validate/test datasets.

set.seed(seed) 
nobs <- nrow(dataset) # 81 observations 
sample <- train <- sample(nrow(dataset), 0.69*nobs) # 56 observations
validate <- sample(setdiff(seq_len(nrow(dataset)), train), 0.15*nobs) # 12 observations
test <- setdiff(setdiff(seq_len(nrow(dataset)), train), validate) # 13 observations

# The following variable selections have been noted.

input <- c('Country', 'Racial_Subregion', 'UNODC_murder_Rate', 'Lynn_Vanhanen_Avg_IQ',
               'Power_Index')

numeric <- c('UNODC_murder_Rate', 'Lynn_Vanhanen_Avg_IQ', 'Power_Index')

categoric <- c('Country', 'Racial_Subregion')

target  <- 'Racial_Region'
risk    <- NULL
ident   <- NULL
ignore  <- NULL
weights <- NULL
