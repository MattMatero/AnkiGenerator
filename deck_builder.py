from genanki.genanki import Model,Deck,Card,Note,Package
from data_handler import get_cards, generate_uuid_type, add_deck 
from card_builder import generate_queried_words

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
    my_card = Note(model=template,fields=card_details,sort_field="Question")
    return my_card


def gen_deck(deck_name):

    deck_uuid = generate_uuid_type("Deck")

    add_deck(deck_name, deck_uuid)

    my_deck = Deck(deck_uuid, deck_name)
    return my_deck

def add_cards_to_deck(deck, cards_csv, template):
    
    cards = get_cards(cards_csv)

    for card in cards.to_numpy():
        deck.add_note(make_card(template, card))

def make_deck(deck_name, input_file):
    
    template = build_template()

    new_deck = gen_deck(deck_name)
    generate_queried_words(input_file, deck_name)
    add_cards_to_deck(new_deck, deck_name, template)

    Package(new_deck).write_to_file(f"./output/anki_deck_{deck_name}.apkg")


def test():

    template = build_template()

    my_deck = make_deck('testing')
    my_deck.add_note(make_card(template, ['奪う','うばう',"['to snatch away', 'to dispossess', 'to steal']","['Godan verb with u ending', 'Transitive verb']","[]"]))
    Package(my_deck).write_to_file('./output/test_deck.apkg')

def test2():

    template = build_template
    my_deck = make_deck('testing')
    my_deck.sort_field_index=0
    add_cards_to_deck(my_deck,"food_test", template)


if __name__ == "__main__":
    test2()
