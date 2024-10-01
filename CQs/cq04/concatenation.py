"""concatenation"""

__author__ = "730753141"


def concat(str1: str, str2: str) -> str:
    """returns the concatenation of 2 strings"""
    return str1 + str2


word1: str = "happy"
word2: str = "tuesday"

if __name__ == "__main__":
    print(concat(word1, word2))
