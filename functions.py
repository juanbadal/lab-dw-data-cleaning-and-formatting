
# Writing functions in functions.py file

import pandas as pd
def clean_column_names(df: pd.DataFrame) -> pd.DataFrame:
    '''
    Modifies column names of a dataframe, changing them to lowercase and switching the spaces with underscores.
    '''
    for c in range(len(df.columns)):
        df.columns.values[c] = df.columns.values[c].lower().replace(' ', '_')
    return df



def st_to_state(df: pd.DataFrame) -> pd.DataFrame:
    '''
    Modifies a column name from 'st' to 'state'.
    '''
    if 'st' in df.columns:
        df.rename(columns={'st': 'state'}, inplace=True)
        return df
    else:
        'st column not found in the dataframe'
 


def standardize_gender_col(df: pd.DataFrame) -> pd.DataFrame:
    '''
    If the dataframe has a 'gender' column, replaces all values in it with their first letter in uppercase.
    '''
    if 'gender' in df.columns:
        df['gender'] = df['gender'].apply(lambda x: x[0].upper() if isinstance(x, str) else x)
        return df
    else:
        print('gender column not found in the dataframe')

        
        
def standardize_state_col(df: pd.DataFrame, options={'AZ': 'Arizona', 'Cali': 'California', 'WA': 'Washington'}) -> pd.DataFrame:
    '''
    If the dataframe has a 'state' column, replaces values in the column using dict mapping.
    '''
    if 'state' in df.columns:
        df['state'] = df['state'].replace(options)
        return df
    else:
        print('state column not found in the dataframe')

        
        
def bachelors_to_bachelor(df: pd.DataFrame, options={'Bachelors': 'Bachelor'}) -> pd.DataFrame:
    '''
    If the dataframe has a 'education' column, replaces 'Bachelors' with 'Bachelor'.
    '''
    if 'education' in df.columns:
        df['education'] = df['education'].replace(options)
        return df
    else:
        print('education column not found in the dataframe')

        
        
def fix_percentages(df: pd.DataFrame, colname='customer_lifetime_value') -> pd.DataFrame:
    '''
    Takes a dataframe column (default='customer_lifetime_value'), removes percentage symbol, converts to float and divides by 100.
    '''
    df[colname] = df[colname].replace('%', '', regex=True).astype(float) / 100
    return df



def standardize_vehicle_class(df: pd.DataFrame, options={'Sports Car': 'Luxury', 'Luxury SUV': 'Luxury', 'Luxury Car': 'Luxury'}) -> pd.DataFrame:
    '''
    If the dataframe has a 'vehicle_class' column, replaces values in the column using dict mapping.
    '''
    if 'vehicle_class' in df.columns:
        df['vehicle_class'] = df['vehicle_class'].replace(options)
        return df
    else:
        print('vehicle_class column not found in the dataframe')
        
        
        
def fix_complaints_column(df: pd.DataFrame, colname='number_of_open_complaints') -> pd.DataFrame:
    '''
    Takes a dataframe column (default='number_of_open_complaints'), splits it by forwardslash, takes the middle value and converts to float.
    '''
    df[colname] = df[colname].str.split(pat='/').str[1].astype(float)
    return df



def remove_null_rows(df: pd.DataFrame) -> pd.DataFrame:
    '''
    Drops all rows from a dataframe in which all columns have null values.
    '''
    df.dropna(how='all', inplace=True)
    df.reset_index(drop=True, inplace=True)
    return df



def remove_nulls_col(df: pd.DataFrame, colname='gender') -> pd.DataFrame:
    '''
    Drops all rows from a dataframe where the value of a specific column (default='gender') is null.
    '''
    df.dropna(subset=colname, inplace=True)
    return df



def impute_nulls(df: pd.DataFrame, colname='customer_lifetime_value', method='median') -> pd.DataFrame:
    '''
    Imputes statistic value (default=median) for nulls values in a column (default='customer_lifetime_value').
    '''
    if colname not in df.columns:
        print(f"Column '{colname}' not found in the DataFrame.")
        return df

    if method == 'mean':
        fill_value = df[colname].mean()
    elif method == 'median':
        fill_value = df[colname].median()
    elif method == 'mode':
        fill_value = df[colname].mode().iloc[0]
    else:
        print("Invalid method. Defaulting to median.")
        fill_value = df[colname].median()

    df[colname].fillna(fill_value, inplace=True)
    return df


def remove_duplicates(df: pd.DataFrame) -> pd.DataFrame:
    '''
    Removes fully duplicated rows from a dataframe and resets index.
    '''
    df.drop_duplicates(inplace=True)
    df.reset_index(drop=True, inplace=True)
    return df



def clean_dataframe(df: pd.DataFrame) -> pd.DataFrame:
    '''
    Applies all previous cleaning and preprocessing functions to a dataframe.
    '''
    clean_column_names(df)
    st_to_state(df)
    standardize_gender_col(df)
    standardize_state_col(df)
    bachelors_to_bachelor(df)
    fix_percentages(df)
    standardize_vehicle_class(df)
    fix_complaints_column(df)
    remove_null_rows(df)
    remove_nulls_col(df)
    impute_nulls(df)
    remove_duplicates(df)
    return df
