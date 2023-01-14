import pandas as pd
from os import path

def open_file(file_loc, columns=None):
    if path.exists(file_loc):
        df = pd.read_csv(file_loc)
    else:
        df = pd.DataFrame([], columns=columns)

    return df

def save_df(df, output_path):
    df.to_csv(output_path)
    return df
