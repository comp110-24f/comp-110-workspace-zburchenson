def check_first_letter(word: str, letter: str) -> str:
    """check 1st letter of word"""
    if word[0] == letter:
        return "match!"
    else:
        return "no match!"

check_first_letter(word="hello", letter="l")
