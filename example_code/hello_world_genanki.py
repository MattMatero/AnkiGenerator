from genanki.genanki import Model,Deck,Card,Note,Package


my_model = Model(
  1607392319,
  'Simple Model',
  fields=[
    {'name': 'Question'},
    {'name': 'Answer'},
  ],
  templates=[
    {
      'name': 'Card 1',
      'qfmt': '{{Question}}',
      'afmt': '{{FrontSide}}<hr id="answer">{{Answer}}',
    },
  ])

my_note = Note(
  model=my_model,
  fields=['Capital of America', 'Washington D.C.'])

print(my_note)

my_deck = Deck(2059400110, 'Game Vocab')
my_deck.add_note(my_note)
Package(my_deck).write_to_file('game_vocab.apkg')
