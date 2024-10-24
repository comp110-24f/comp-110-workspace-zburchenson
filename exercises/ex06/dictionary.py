"""Dictionary Utils in Python"""

__author__ = "730753141"


def invert(input: dict[str, str]) -> dict[str, str]:
    """invert the keys and values of a dict"""

    inverted_input: dict[str, str] = {}

    for key in input:
        if key in inverted_input or input[key] in inverted_input:
            raise KeyError("Duplicate key found.")
        else:
            inverted_input[input[key]] = key

    return inverted_input


def favorite_color(input: dict[str, str]) -> str:
    """returns the color appearing most freq"""

    color_counts: dict[str, int] = {}

    for name in input:
        color: str = input[name]
        if color in color_counts:
            color_counts[color] += 1
        else:
            color_counts[color] = 1

    max: int = 0
    fave_color: str = ""

    for color in color_counts:

        if color_counts[color] > max:
            max = color_counts[color]
            fave_color = color

    return fave_color


def count(input: list[str]) -> dict[str, int]:
    """produce a dict where each key is unique"""

    # each key is a unique val in the given list;
    # each val associated is the count of the number of times
    # it appears in the input list

    num_count: dict[int, int] = {}

    for num in input:
        if num in num_count:
            num_count[num] += 1
        else:
            num_count[num] = 1

    return num_count


def alphabetizer(input: list[str]) -> dict[str, list[str]]:
    """produce a dict where each key is unique letter"""
    # produce a dict where each key is a unique letter in the alphabet
    # each val is a list of the words that begin with that letter

    # final - letter - str ; words - list[str]
    # f_letter ; words
    # alphabet ; letter + words

    alphabet: dict[str, list[str]] = {}
    f_letter: str = ""

    for word in input:
        f_letter = word[0].lower()
        if f_letter not in alphabet:
            alphabet[f_letter] = []
        alphabet[f_letter].append(word)

    return alphabet


def update_attendance(
    input: dict[str, list[str]], day: str, student: str
) -> dict[str, list[str]]:
    """update dict with attendance info"""

    if day not in input:
        input[day] = []

    if student not in input[day]:
        input[day].append(student)

    return input


attendance_log: dict = {"Monday": ["Vrinda", "Kaleb"], "Tuesday": ["Alyssa"]}
print(update_attendance(attendance_log, "Tuesday", "Vrinda"))
