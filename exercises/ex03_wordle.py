""" Worldle created in python."""

__author__ = "730753141"


def input_guess(secret_word_len: int) -> None:

    guess: str = input(f"Enter a {secret_word_len} character word: ")

    while len(guess) != secret_word_len:
        guess = input(f"That wasn't {secret_word_len} chars! Try again: ")
    return guess


def contains_char(secret_word: str, char_guess: str) -> bool:
    """searches for a char in the word and returns true or false"""

    assert len(char_guess) == 1

    idx: int = 0
    occurence: int = 0

    while idx < len(secret_word):
        if secret_word[idx] == char_guess:
            occurence += 1
        idx += 1

    if occurence > 0:
        return True
    else:
        return False


def emojified(guess: str, secret_word: str) -> str:
    """compare 2 strings of equal length and return emoji combo"""
    # if statement class contains char and uses the emoji codes
    assert len(guess) == len(secret_word)

    idx: int = 0
    white_box: str = "\U00002B1C"
    green_box: str = "\U0001F7E9"
    yellow_box: str = "\U0001F7E8"
    emoji_combo: str = ""

    while idx < len(guess):
        if guess[idx] == secret_word[idx]:
            emoji_combo += green_box
        elif contains_char(secret_word, guess[idx]):
            emoji_combo += yellow_box
        else:
            emoji_combo += white_box
        idx += 1

    return emoji_combo


def main(secret: str) -> None:
    """The entrypoint of the program and main game loop!"""
    turns: int = 1
    # while turns is less than 6, print turn # and secret status
    while turns <= 6:
        print(f"=== Turn {turns}/6 ===")
        guess: str = input_guess(len(secret))

        print(emojified(guess, secret))

        if secret == guess:
            print(f"You won in {turns}/6 turns!")
            exit()

        elif turns == 6 and secret != guess:
            print("X/6 - Sorry, try again tomorrow!")

        turns += 1


if __name__ == "__main__":
    main(secret="codes")
