"""EX02 - Chardle - A cute step towards Wordle. """

__author__ = "730753141"


def input_word() -> str:
    """ask the user to input a word"""

    word: str = input("Enter a 5-character word: ")

    if len(word) < 5 or len(word) > 5:
        print("Error: word must contain 5 characters.")
        exit()  # function exits the program when encountered
    else:
        return word


def input_letter() -> str:
    """ask the user to input a single character"""

    char: str = input("Enter a single character: ")

    if len(char) < 1 or len(char) > 1:
        print("Error: Character must be a single character.")
        exit()
    else:
        return "'" + char + "'"


def contains_char(word: str, letter: str) -> None:
    print("Searching for " + letter + " in " + word)
    letter_count: int = 0

    # letter[1] because of the automatic '' that come with a single character.

    if word[0] == letter[1]:
        print(letter + " found at index 0")
        letter_count += 1

    if word[1] == letter[1]:
        print(letter + " found at index 1")
        letter_count += 1

    if word[2] == letter[1]:
        print(letter + " found at index 2")
        letter_count += 1

    if word[3] == letter[1]:
        print(letter + " found at index 3")
        letter_count += 1

    if word[4] == letter[1]:
        print(letter + " found at index 4")
        letter_count += 1

    if letter_count > 0:
        print(str(letter_count) + " instances of " + letter + " found in " + word)
    else:
        print("No instances of " + letter + " found in " + word)


def main() -> None:
    contains_char(word=input_word(), letter=input_letter())
    # calling all functions at once in main


if __name__ == "__main__":
    main()
