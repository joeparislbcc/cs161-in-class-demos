#! /usr/bin/env python3.7


def is_all_digits(value):
    """Check is input consists of only digit characters.

    Arguments:
        value {str} -- The value to check.

    Returns:
        bool -- True if value contains only digit characters, False
        otherwise.

    """
    if value.isdigit():
        return True
    return False


def is_correct_length(value, length):
    """Check if input is length characters long.

    Arguments:
        value {str} -- The value to check.
        length {int} -- The length we are checking against.

    Returns:
        bool -- True if len(value) == length, False otherwise.

    """
    return len(value) == length


def has_duplicates(value):
    """Check if values has any duplicate characters.

    Arguments:
        value {str} -- The value to check.

    Returns:
        bool -- True if there are duplicate characters in value, False
        otherwise.

    """
    s = set(value)
    return len(s) != len(value)


def is_valid_input(value, length):
    """Validate input.

    Valid input will contain exactly {length} unique digit characters.

    Arguments:
        value {str} -- The value to be validated.
        length {int} -- The required number of characters.

    Returns:
        bool -- True if value contains exactly {length} unique
        characters, False otherwise.

    """
    all_digits = is_all_digits(value)
    correct_length = is_correct_length(value, length)
    duplicates = has_duplicates(value)

    # input is valid if all_digits is true, it correct_length is true,
    # but duplicates is false
    return all_digits and correct_length and not duplicates


def main():
    while True:
        key = input("Please enter a 4-digit key: ")
        if is_valid_input(key, 4):
            break
        else:
            print("The key must be 4 unique digits")

    while True:
        guess = input("Please enter a 4-digit guess: ")
        if is_valid_input(guess, 4):
            break
        else:
            print("The key must be 4 unique digits")


if __name__ == "__main__":
    main()

# # get the key
# while True:
#     key = input("Please enter a 4-digit key: ")

#     # check that every character is a digit
#     if not key.isdigit():
#         print("Your input contains non-digit characters.")
#         continue

#     # check that the key is 4 characters long
#     if len(key) != 4:
#         print("Your input must be exactly 4 digits.")
#         continue

#     # check that every digit is unique
#     character_set = set(key)
#     if len(character_set) != len(key):
#         print("Your input had duplicate digits.")
#         continue

#     break

# # get the user's guess
# while True:
#     guess = input("{lease enter your 4-digit guess: }")

#     if not guess.isdigit():
#         print("Your input contains non-digit characters.")
#         continue

#     # check that the key is 4 characters long
#     if len(key) != 4:
#         print("Your input must be exactly 4 digits.")
#         continue

#     # check that every digit is unique
#     character_set = set(key)
#     if len(character_set) != len(key):
#         print("Your input had duplicate digits.")
#         continue

#     break
