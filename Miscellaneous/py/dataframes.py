
import pandas as pd
import math
import statsmodels.api as sm

def get_page_tables(tables_url):
    tables_df_list = pd.read_html(tables_url)
    print(sorted([(i, df.shape) for (i, df) in enumerate(tables_df_list)], key=lambda x: x[1][0], reverse=True))
    
    return tables_df_list


def get_column_descriptions(df, column_list=None):
    
    if column_list is None:
        column_list = df.columns
    g = df.columns.to_series().groupby(df.dtypes).groups
    rows_list = []
    for dtype, dtype_column_list in g.items():
        for column_name in dtype_column_list:
            if column_name in column_list:
                
                # Get input row in dictionary format; key = col_name
                row_dict = {}
                row_dict['column_name'] = column_name
                row_dict['dtype'] = str(dtype)
                row_dict['count_blanks'] = df[column_name].isnull().sum()
                
                # Count how many unique numbers there are
                try:
                    row_dict['count_uniques'] = len(df[column_name].unique())
                except Exception:
                    row_dict['count_uniques'] = math.nan
                
                # Count how many zeroes the column has
                try:
                    row_dict['count_zeroes'] = int((df[column_name] == 0).sum())
                except Exception:
                    row_dict['count_zeroes'] = math.nan
                
                # Check to see if the column has any dates
                date_series = pd.to_datetime(df[column_name], errors='coerce')
                null_series = date_series[~date_series.notnull()]
                row_dict['has_dates'] = (null_series.shape[0] < date_series.shape[0])
                
                # Show the minimum value in the column
                try:
                    row_dict['min_value'] = df[column_name].min()
                except Exception:
                    row_dict['min_value'] = math.nan
                
                # Show the maximum value in the column
                try:
                    row_dict['max_value'] = df[column_name].max()
                except Exception:
                    row_dict['max_value'] = math.nan
                
                # Show whether the column contains only integers
                try:
                    row_dict['only_integers'] = (df[column_name].apply(lambda x: float(x).is_integer())).all()
                except Exception:
                    row_dict['only_integers'] = float('nan')

                rows_list.append(row_dict)

    columns_list = ['column_name', 'dtype', 'count_blanks', 'count_uniques', 'count_zeroes', 'has_dates',
                    'min_value', 'max_value', 'only_integers']
    blank_ranking_df = pd.DataFrame(rows_list, columns=columns_list)
    
    return(blank_ranking_df)

def example_iterrows():
    '''
    rows_list = []
    columns_list = ['distance_from_white', 'distance_from_black', 'distance_from_red', 'distance_from_green', 'distance_from_blue',
                    'distance_from_magenta', 'distance_from_yellow', 'distance_from_cyan']
    index_list = []
    for row_index, row_series in student_df.iterrows():
        #print(row_index)
        
        # Get input row in dictionary format; key = col_name
        row_dict = {}
        index_list.append(row_index)
        
        for column_index, column_value in row_series.iteritems():
            #print(column_index, value)
            row_dict[column_index] = column_value
    
        rows_list.append(row_dict)

    event_grouping_df = pd.DataFrame(rows_list, columns=columns_list, index=index_list)
    event_grouping_df.sample(n=15).T.sample(n=5).T
    '''

    return "Don't run this, just look at the code using example_iterrows?"

def get_max_rsquared_adj(df, columns_list, verbose=False):
    if verbose:
        t0 = time.time()
    rows_list = []
    n = len(columns_list)
    for i in range(n-1):
        first_column = columns_list[i]
        first_series = df[first_column]
        max_similarity = 0.0
        max_column = first_column
        for j in range(i+1, n):
            second_column = columns_list[j]
            second_series = df[second_column]
            
            # Assume the first column is never identical to the second column
            X, y = first_series.values.reshape(-1, 1), second_series.values.reshape(-1, 1)
            #this_similarity = abs(first_series.cov(second_series))
            
            # Compute with statsmodels, by adding intercept manually
            X1 = sm.add_constant(X)
            result = sm.OLS(y, X1).fit()
            this_similarity = abs(result.rsquared_adj)
            
            if this_similarity > max_similarity:
                max_similarity = this_similarity
                max_column = second_column

        # Get input row in dictionary format; key = col_name
        row_dict = {}
        row_dict['first_column'] = first_column
        row_dict['second_column'] = max_column
        row_dict['max_similarity'] = max_similarity

        rows_list.append(row_dict)

    column_list = ['first_column', 'second_column', 'max_similarity']
    column_similarities_df = pd.DataFrame(rows_list, columns=column_list)
    if verbose:
        t1 = time.time()
        print(t1-t0, time.ctime(t1))

    return column_similarities_df
