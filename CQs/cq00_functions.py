"""First challenge question in COMP 110 (CQ00)"""

__author__ = "730753141"


def mimic(message: str) -> str:
    """Take input and repeat it back"""
    return message


def main() -> None:
    """print the result of mimic"""
    print(mimic(message=input("what is your message?")))


if __name__ == "__main__":
    main()
