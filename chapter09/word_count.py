#! /usr/bin/env python3.8
"""Word count example."""

from typing import Dict
from string import punctuation
from collections import namedtuple
import pathlib


def get_file_name():
    """Get user's selection of a file to open."""
    text_file = namedtuple("text_file", "title, file_name")
    files = {
        1: text_file("Peter Pan", "peter_pan.txt"),
        2: text_file("The Wonderful Wizard of Oz", "the_wonderful_wizard_of_oz.txt"),
    }

    while True:
        print("What file would you like to open?")

        for k, v in files.items():
            print(f"\t{k}) {v.title}")
        try:
            menu_selection = int(input("Enter your selection: "))
            file = files[menu_selection].file_name
        except (ValueError, KeyError):
            print("\nInvalid selection. Please choose an item from the menu.\n")
        else:
            return pathlib.Path(__file__).parent / file


def get_word_counts(text: str) -> Dict[str, int]:
    """Count the occurances of words in the text."""
    # remove all punctuation
    text = text.translate(str.maketrans("", "", punctuation))

    # naively tokenize text
    words = text.lower().split()

    word_counts: Dict[str, int] = {}

    for word in words:
        word_counts[word] = word_counts.get(word, 0) + 1

    x = word_counts

    new_dict = {k: v for k, v in sorted(x.items(), reverse=True, key=lambda item: item[1])}

    return new_dict


def pretty_print(words: Dict[str, int], count: int = 25, filtered=True):
    """Print 'count' most common words in the file."""
    out = f"\nThe {count} most common words in the file"
    if filtered:
        out += ", excepting the\n100 most common English words,"
    out += " are:\n"
    print(out)

    word_list = [word for word in words.keys()]

    if filtered:
        with open(pathlib.Path(__file__).parent / "most_common_english_words.txt", "r") as in_file:
            common_words = [line.strip() for line in in_file]

        word_list = [word for word in word_list if word not in common_words]

    for n in range(count):
        print(f"{word_list[n]:<15}", end="")

        if (n + 1) % 5 == 0:
            print()


def main():
    """Run the program."""
    file = get_file_name()
    with open(file, "r") as in_file:
        try:
            text = in_file.read()
        except IOError as err:
            print("*** Error reading file ***")
            print(err.__cause__)
        else:
            word_counts = get_word_counts(text)
            pretty_print(word_counts)


if __name__ == "__main__":
    main()
