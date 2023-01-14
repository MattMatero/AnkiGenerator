import pandas as pd
from os import path
import uuid

def validate_default_csv():

    files = {"cards":["uuid","word_id","front","back","deck_id"],
            "decks":["uuid","name"],
            "queried_words":["uuid","word","english_def","pos","other forms"]}

    for file in files.keys():
        if not path.exists(f"./data/{file}.csv"):
            df = pd.DataFrame([], columns=files[file])
            save_df(df, f"./data/{file}.csv")
        else:
            df = open_file(f"./data/{file}.csv")
            print(df.columns)
            print(files[file])
            if len(df.columns) != len(files[file]) or not (df.columns == files[file]).all():
                raise Exception(f"Columns mismatch for {file}.csv")
        
            

def generate_uuid(df):

    iters = 10

    while iters > 0:

        new_uuid = uuid.uuid4()

        if len(df.index) == 0 or new_uuid not in df["uuid"]:
            return new_uuid
        
        iters -= 1

    return None

def open_template_file(file_path):
    with open(file_path) as f:
        return f.read()

def open_file(file_loc, columns=None):
    if path.exists(file_loc):
        df = pd.read_csv(file_loc)
    else:
        df = pd.DataFrame([], columns=columns)

    return df

def insert(df, list_data):
    
    new_uuid = generate_uuid(df)

    if new_uuid is None:
        raise Exception("Failed to generate unique UUID")

    list_data.insert(0,new_uuid)

    df.loc[len(df)] = list_data

    return df


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

    qw = open_file("./data/qw_test.csv")

    #print(generate_uuid(qw))

    new_row = ["預かる","あずかる",['to look after', 'to take care of', 'to keep', 'to hold on to', 'to keep in custody'],
    ['Godan verb with ru ending', 'Transitive verb'],[]]

    print(insert(qw, new_row))

def test2():
    validate_default_csv()


if __name__ == "__main__":
    test2()