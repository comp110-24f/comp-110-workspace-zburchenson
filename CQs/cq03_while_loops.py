"""While Loops Practice Question"""

__author__ = "730753141"


def num_instances(phrase: str, search_char: str) -> int:
    """return the count of occurences of search_char"""

    count: int = 0
    index: int = 0

    while index < len(phrase):
        if phrase[index] == search_char:
            count += 1
        index += 1

    return count


num_instances(phrase="Hello!", search_char="e")
