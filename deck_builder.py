from genanki.genanki import Model,Deck,Card,Note,Package
from data_handler import open_file


def build_template():
    card_template = Model(
      1607392319,
      'Simple Model',
      fields=[
        {'name': 'Question'},
        {'name': 'Answer'},
        {'name': 'def'},
        {'name': 'pos'},
        {'name': 'other forms'},
      ],
      templates=[
        {
          'name': 'Card 1',
          'qfmt': open_template_file('./templates/front.html'),
          'afmt': open_template_file('./templates/back.html'),
        },
      ])

    return card_template

def open_template_file(file_path):
    with open(file_path) as f:
        return f.read()

def make_card(template, card_details):
    my_card = Note(model=template,fields=card_details)
    return my_card


def make_deck(deck_name):
    my_deck = Deck(2059400110, deck_name)
    return my_deck

def add_cards_to_deck(deck, cards):
    pass

template = build_template()

my_deck = make_deck('testing')
my_deck.add_note(make_card(template, ['奪う','うばう',"['to snatch away', 'to dispossess', 'to steal']","['Godan verb with u ending', 'Transitive verb']","[]"]))
Package(my_deck).write_to_file('./output/test_deck.apkg')
