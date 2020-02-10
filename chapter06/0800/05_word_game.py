#! /usr/bin/env python3.7

"""Search the dictionary for the first word that conains 'aeiou' in order."""


def sanitize_word(word):
    """Remove all leading and trailing whitespace and fixing the case of a word."""
    return word.strip().lower()


def get_vowels_in_word(word):
    """Return a string containing all the vowels in a word."""
    VOWELS = "aeiou"
    found_vowels = ""
    for char in word:
        if char in VOWELS:
            found_vowels += char
    return found_vowels


def play():
    """Play the game."""

    # print instructions for the user
    print("Find words containing vowels in order.")

    count = 1
    with open("dictionary.txt", "r") as in_file:
        for word in in_file:
            # sanitize the word
            word = sanitize_word(word)

            # check if all the vowels are present and in order
            vowels = get_vowels_in_word(word)
            if vowels == "aeiou":
                print(f"{count:>2}. {word}")
                # break

                count += 1


if __name__ == "__main__":
    play()
