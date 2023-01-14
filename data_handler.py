import pandas as pd
from os import path
import uuid


def generate_uuid(df):

    iters = 10

    while iters > 0:

        new_uuid = uuid.uuid4()

        if len(df.index) == 0 or new_uuid not in df["uuid"]:
            return new_uuid
        
        iters -= 1

    return None


def open_file(file_loc, columns=None):
    if path.exists(file_loc):
        df = pd.read_csv(file_loc)
    else:
        df = pd.DataFrame([], columns=columns)

    return df

def insert(df, list_data):
    
    pd.DataFrame.from_dict({'words'})

def save_df(df, output_path):
    df.to_csv(output_path, index=False)
    return df


def test():
    words = open_file("./data/words.csv")

    print(words)

    print(words.columns)

    name = "TEST_WORD"

    df = pd.DataFrame.from_dict({'words': [name]})
    #df = pd.DataFrame(d)

    #print(df)

    words = pd.concat([words, df], ignore_index=True)

    print(words.head(10))
    print(words.columns)

def test1():

    cards = open_file("./data/cards.csv")


    print(generate_uuid(cards))

if __name__ == "__main__":
    test1()