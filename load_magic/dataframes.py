
rows_list = []
# Group by join and then sort by date per Denny
student_list = acla_events_df['Join'].unique()

for student in student_list:
    student_df = acla_events_df.loc[acla_events_df['Join'] == student]
    
    # Get input row in dictionary format; key = col_name
    row_dict = {}
    row_dict['Join'] = student
    row_dict['student_name'] = student_df['student_name'].tolist()[int(student_df['student_name'].shape[0]/2)]
    row_dict['Course'] = student_df['Course'].tolist()[int(student_df['Course'].shape[0]/2)]
    row_dict['Class'] = student_df['Class'].tolist()[int(student_df['Class'].shape[0]/2)]
    row_dict['Position'] = student_df['Position'].tolist()[int(student_df['Position'].shape[0]/2)]
    for row_index, row_series in student_df.iterrows():
        #print(row_index)
        column_prefix = row_series.loc['derived_event']
        for column_suffix, value in row_series.iteritems():
            #print(column_suffix, value)
            if column_suffix in event_columns_list:
                column_name = str(column_prefix) + '_' + str(column_suffix)
                row_dict[column_name] = value
    
    rows_list.append(row_dict)

event_grouping_df = pd.DataFrame(rows_list, columns=total_column_list)
event_grouping_df.sample(n=15).T.sample(n=5).T