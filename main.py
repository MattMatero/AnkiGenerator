from genanki.genanki import Model,Deck,Card,Note,Package
from deck_builder import make_deck
import argparse

if __name__ == "__main__":

    parser = argparse.ArgumentParser(prog="anki generator", description="test")

    parser.add_argument("--name", type=str) #Deck name
    parser.add_argument("--input", type=str) #words.csv

    args = parser.parse_args()

    make_deck(args.name, args.input)


    