from jisho_api.word import Word
from data_handler import open_file, save_df
import pandas as pd
import sys

def query_word(word):
    r = Word.request(word)
    data = r.data[0]
    
    res = []
    other_forms = []

    if len(data.japanese) == 1:
        reading = data.japanese[0].reading
    else:
        for j in data.japanese:
            if j.word == word:
                reading = j.reading
            else:
                other_forms.append(j.word)
  
    if len(data.senses) == 1:
        english_def = data.senses[0].english_definitions
        pos = data.senses[0].parts_of_speech
        res.append([word, reading, english_def, pos, other_forms])
    else:
        for i in range(min([len(data.senses)//2, 3])):
            english_def = data.senses[i].english_definitions
            pos = data.senses[i].parts_of_speech
            
            if not pos[0] == 'Wikipedia definition':
                res.append([word,reading,english_def,pos, other_forms])
        

    return res

def process_word_list(df):
    
    word_list = []
    for word in df['words'].to_numpy():
        word_list.extend(query_word(word))

    return word_list


if __name__ == '__main__':

    print("Processing word list...")

    df = open_file('./data/words.csv')
    word_lookups = process_word_list(df)
    lookup_df = pd.DataFrame(word_lookups, columns=['word', 'reading', 'english_def', 'pos', 'other forms'])
    save_df(lookup_df, './data/queried_words.csv')
