from jisho_api.word import Word
from data_handler import open_file

def query_word(word):
    r = Word.request(word)
    data = r.data[0]

    if len(data.japanese) == 1:
        reading = data.japanese[0].reading
    else:
        other_forms = []
        for j in data.japanese:
            if j == word:
                reading = j.reading
            else:
                other_forms.append(j.word)


    if len(data.senses) == 1:
        english_def = data.senses[0].english_definitions
        pos = data.senses[0].parts_of_speech
    else:
        ## TODO
        pass

    return [word, reading, english_def, pos]

def process_word_list(df):
    
    word_list = []
    for word in df['words'].to_numpy():
        word_list.append(query_word(word))

    return word_list

def save_word_csv(words, columns):

    df = pd.DataFrame(words, columns=columns)
    df.to_csv('./outputs/queried_words.csv')
    return df

if __name__ == '__main__':

    print("Processing word list")

    df = open_file('./data/words.csv')
    word_lookups = process_word_list(df)
    save_word_csv(word_lookups, ['word', 'reading', 'english_def', 'pos'])
