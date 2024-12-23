#!/usr/bin/env python
# coding: utf-8







# Soli Deo gloria







from sklearn.feature_extraction.text import CountVectorizer, TfidfTransformer
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import classification_report
from sklearn.model_selection import GridSearchCV, train_test_split
from storage import Storage
import numpy as np
import os
import pandas as pd
import re

import warnings
warnings.filterwarnings('ignore')

s = Storage()



scanner_regex = re.compile(r'\b[1-9a-zA-Z][0-9a-zA-Z]*( *[#\+]{1,2}|\b)')
def regex_tokenizer(corpus):
    
    return [match.group() for match in re.finditer(scanner_regex, corpus)]



# Rebuild the datframe from the dictionary
basic_quals_dict = s.load_object('basic_quals_dict')
rows_list = [{'qualification_str': qualification_str,
              'is_fit': is_fit} for qualification_str, is_fit in basic_quals_dict.items()]
basic_quals_df = pd.DataFrame(rows_list)

# Re-transform the bag-of-words and tf-idf from the new manual scores
sents_list = basic_quals_df.qualification_str.tolist()

# Bag-of-words
cv = CountVectorizer(lowercase=True, tokenizer=regex_tokenizer,
                     token_pattern=r'\b[1-9a-zA-Z][0-9a-zA-Z]*[#\+]{0,2}', ngram_range=(1, 3))
bow_matrix = cv.fit_transform(sents_list)

# Tf-idf, must get from BOW first
tt = TfidfTransformer()
tfidf_matrix = tt.fit_transform(bow_matrix)


# # Parameter estimation using grid search with cross-validation
# 
# The Logistic Regression classifier is optimized by cross-validation,
# which is done using the :class:`sklearn.model_selection.GridSearchCV` object
# on a development set that comprises only half of the available labeled quals data.
# 
# The performance of the selected hyper-parameters and trained model is
# then measured on a dedicated evaluation set that was not used during
# the model selection step.

# To apply an classifier on this data, we need to
# turn the data in a (samples, feature) matrix:
X = tfidf_matrix.toarray()
y = basic_quals_df.is_fit.to_numpy()

# Split the dataset in two equal parts
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.5)

# Set the parameters by cross-validation
tuned_parameters = [
                    
                    # 'saga' also supports 'elasticnet' penalty
                    {'penalty': ['elasticnet'],
                     'solver': ['saga'],
                     'tol': [1e-5, 1e-4, 1e-3],
                     'C': [0.1, 1.0, 10.0],
                     'class_weight': [None, 'balanced'],
                     'max_iter': [250, 500, 1000],
                     'warm_start': [True],
                     'l1_ratio': [0, 0.5, 1]}
                    
                    ]

# When a search engine returns 30 pages (only 20 of which were relevant)
# while failing to return 40 additional relevant pages, its precision
# is 20/30 = 2/3 while its recall is 20/60 = 1/3. So, in this case,
# precision is "how useful the search results are", and recall is
# "how complete the results are".
scores_list = ['precision', 'recall']

# Dump the results to a file
file_name = 'penalty_elasticnet_tuning_results.txt'
txt_dir = os.path.join(s.saves_folder, 'txt')
file_path = os.path.join(txt_dir, file_name)

with open(file_path, 'w') as f:
    print('Tuning Logit hyper-parameters', file=f)
    print('', file=f)
for score in scores_list:
    with open(file_path, 'a') as f:
        print('Tuning hyper-parameters for {}'.format(score), file=f)
        print('', file=f)

    clf = GridSearchCV(LogisticRegression(), tuned_parameters,
                       scoring='{}_macro'.format(score))
    clf.fit(X_train, y_train)
    
    with open(file_path, 'a') as f:
        print('Best parameters set found on development set:', file=f)
        print('', file=f)
        print(clf.best_params_, file=f)
        print('', file=f)
        print('Grid scores on development set:', file=f)
        print('', file=f)
    means = clf.cv_results_['mean_test_score']
    stds = clf.cv_results_['std_test_score']
    for mean, std, params in zip(means, stds, clf.cv_results_['params']):
        with open(file_path, 'a') as f:
            print('%0.3f (+/-%0.03f) for %r' % (mean, std * 2, params), file=f)
    with open(file_path, 'a') as f:
        print('', file=f)

        print('Detailed classification report:', file=f)
        print('', file=f)
        print('The model is trained on the full development set.', file=f)
        print('The scores are computed on the full evaluation set.', file=f)
        print('', file=f)
    y_true, y_pred = y_test, clf.predict(X_test)
    print(score, set(y_test) - set(y_pred))
    with open(file_path, 'a') as f:
        print(classification_report(y_true, y_pred), file=f)
        print('', file=f)