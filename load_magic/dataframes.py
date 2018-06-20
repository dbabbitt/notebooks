
import pandas as pd
import math

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
                row_dict['dtype'] = dtype
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

                rows_list.append(row_dict)

    ranking_columns = ['column_name', 'dtype', 'count_blanks', 'count_uniques', 'count_zeroes', 'has_dates']
    blank_ranking_df = pd.DataFrame(rows_list, columns=ranking_columns)
    
    return(blank_ranking_df)

def example_iterrows():
    '''
    rows_list = []
    for row_index, row_series in student_df.iterrows():
        #print(row_index)
        
        # Get input row in dictionary format; key = col_name
        row_dict = {}
        
        for column_index, column_value in row_series.iteritems():
            #print(column_index, value)
            row_dict[column_index] = column_value
    
    rows_list.append(row_dict)

    event_grouping_df = pd.DataFrame(rows_list, columns=total_column_list)
    event_grouping_df.sample(n=15).T.sample(n=5).T
    '''

    return "Don't run this, just look at the code using example_iterrows?"

