import pandas as pd
import uuid
from os import path
from data_handler import open_file
import argparse
import sys


def add_deck(df, name):
    if name not in df['deck name'].unique():
        new_record = pd.DataFrame.from_dict({'deck name': [name], 'uuid': [str(uuid.uuid4())]})
        df = pd.concat([df, new_record])
        return df
    else:
        print("Deck already exists")
        sys.exit(0)

def save_updated_df(df,file_loc):
    print(df.head())
    df.to_csv(file_loc, index=False)

if __name__ == '__main__':
    
    parser = argparse.ArgumentParser(prog='deck generator', description='given a name of an anki deck generates a unique uuid pair')
    parser.add_argument('--name', type=str)
    parser.add_argument('--file_loc', type=str, default='./decks/decks.csv')

    args = parser.parse_args()

    df = open_file(args.file_loc, columns=['deck name', 'uuid'])
    
    if args.name is not None:
        print(f"Adding deck: {args.name}")
        df = add_deck(df,args.name)
        save_updated_df(df,args.file_loc)
        print(f"Saved to {args.file_loc}")
    else:
        print("Please enter a deck name")
        sys.exit(0)
