"""Challenge question w conditionals!"""

__author__ = "730753141"


def guess_a_number() -> None:
    """function to guess a number"""

    secret: int = 7
    x: int = int(input("Guess a number:"))
    print("Your guess was " + str(x))

    if int(x) < secret:
        print("Your guess was too low! The secret number is " + str(secret))
    elif int(x) > secret:
        print("Your guess was too high! The secret number is " + str(secret))
    else:
        print("You got it!")
    return None


if __name__ == "__main__":
    guess_a_number()
