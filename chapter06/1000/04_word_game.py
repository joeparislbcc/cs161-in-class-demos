#! /usr/bin/env python3.7
"""Search the dictionary for a word containg 'aeiou' in order."""


def sanitize_text(text):
    """Sanitize the input.

    Remove all leading and training whitespace and conver to lower case.
    """
    return text.strip().lower()


def get_vowels_in_word(word):
    """Return a string containing all the vowels in word."""
    VOWELS = "aeiou"
    found_vowels = ""
    for char in word:
        if char in VOWELS:
            found_vowels += char
    return found_vowels


def play():
    """Play the vowel game."""
    # open a file for reading
    with open("dictionary.txt", "r") as in_file, open("all_vowels.txt", "w") as out_file:
        count = 1
        for word in in_file:
            # clean the input (strip all leading and trailing whitespace and convert to lowercase)
            sanitized_word = sanitize_text(word)

            # check for vowels in each word
            vowels = get_vowels_in_word(sanitized_word)

            # check if word contained all the vowels and they are in order
            if vowels == "aeiou":
                print(f"{count:>2}. {sanitized_word}", file=out_file)
                count += 1


if __name__ == "__main__":
    play()
