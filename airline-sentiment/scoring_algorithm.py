#!/usr/bin/env python

# note - if libs like numpy or scipy are not installed, python will throw an exception. 
# the scoreboard will detect this and long the error, but all scoring scripts should
# be tested on the production environment prior to use.

from __future__ import division
from numpy import genfromtxt 
import csv
import scipy
import sys
import argparse
import pandas

parser = argparse.ArgumentParser()
parser.add_argument("--verbose", help="increase output verbosity", action="store_true")
# answer_submission.csv + answer_key.csv + max_points
parser.add_argument("submission", help="/path/to/answer_submission.csv")
parser.add_argument("key", help="/path/to/answer_key.csv")
parser.add_argument("max", help="Maximum score")
args = parser.parse_args()
if args.verbose:
    from sklearn import metrics


def main():

#EXAMPLE COMMAND LINE USAGE: python ScoreClassifierModified.py </path/to/answer_submission.csv> </path/to/answer_key.csv> <max_points>

# The only print() statement should have the user's score.  Anything else will be treated as an error and logged.

    #GET COMMAND LINE ARGUMENTS
    submittedFile = args.submission
    answerFile = args.key
    totalScore = int(args.max)
    

    #READ IN THE ANSWER FILE -- FIRST COLUMN THE CLASSIFICATION; OTHERS IRRELEVANT
    if args.verbose:
        print('Inputting answer key.')
    data = pandas.read_csv(answerFile, header=None, names=['key'])

    #CREATE ARRAY WITH ONLY THE CLASSIFICATION KEY
    actuals = data['key']


    #READ IN SUBMITTED FILE -- THIS SHOULD ONLY HAVE A SINGLE COLUMN WITH THE CLASSIFICATION
    if args.verbose:
        print('Inputting submitted file.')
    data = pandas.read_csv(submittedFile, header=None, names=['key'])
    answers = data['key']


    
    #ACTUALLY CALCULATE THE SCORE
    if args.verbose:
        print('Accuracy score:')
        print(metrics.accuracy_score(actuals, answers))
    
    errors = 0
    for i in range(len(answers)):
        if answers[i] != actuals[i]:
            errors = errors + 1
    
    if args.verbose:
        print('Your score is: ' + str(totalScore * (len(answers) - errors) / len(answers)))
    else:
        print(str(totalScore * (len(answers) - errors) / len(answers)))
    if args.verbose:
        print('Confusion matrix:')
        print(metrics.confusion_matrix(actuals, answers))

if __name__=="__main__":
    main()
