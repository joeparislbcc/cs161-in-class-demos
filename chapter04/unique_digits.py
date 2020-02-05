#! /usr/bin/env python3.7


def validate_input(prompt, input_len=4):
    """Validate user input.

    Validate the user's input to ensure it contains exactly four unique
    digit characters.

    Arguments:
        prompt {str} -- The prompt to display to the user.

    Returns:
        str -- The validated input.

    """
    while True:
        num = input(f"{prompt}")

        if not num.isdigit():
            print("Non-digit characters found.")
            continue

        digits = set(num)
        if len(digits) != len(num):
            print("You had repeated digits.")
            continue

        if len(num) != input_len:
            print("Your input must be exactly 4 digits long.")
            continue

        break

    return num


# for digit in num:  # 1234
#     if num.count(digit) > 1:
#         print("You cannot have repeated digits.")
#         break


def main():
    # get the key
    key = validate_input("Please enter a 4-digit key: ")

    # get the user's guess
    guess = validate_input("Please enter your guess: ")


if __name__ == "__main__":  ## if you run this module directly
    main()
