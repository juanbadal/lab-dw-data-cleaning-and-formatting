
# Writing functions in functions.py file

import pandas as pd

def clean_column_names(df: pd.DataFrame):
    '''
    Modifies column names of a dataframe, changing them to lowercase and switching the spaces with underscores.
    '''
    for c in range(len(df.columns)):
        df.columns.values[c] = df.columns.values[c].lower().replace(' ', '_')
    return df

def remove_null_rows(df: pd.DataFrame):
    '''
    Drops all rows of a dataframe in which all columns have null values.
    '''
    df = df.dropna(how='all')
    return df

def remove_duplicates(df: pd.DataFrame):
    '''
    Drops all fully duplicated rows and resets df index.
    '''
    df = df.drop_duplicates().reset_index()
    return df
    
def generic_cleaning(df: pd.DataFrame) -> pd.DataFrame:
    '''
    Creates a copy of a dataframe.
    Modifies column names to be conventionally correct, drops all rows containing full missing values and removes duplicated rows.
    '''
    df = clean_column_names(df)
    df = remove_null_rows(df)
    df = remove_duplicates(df)
    return df
