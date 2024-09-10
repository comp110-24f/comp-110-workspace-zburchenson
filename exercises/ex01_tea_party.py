"""EX01 Tea Party Planning Functions"""

__author__: str = "730753141"


def main_planner(guests: int) -> None:
    """big picture of the program"""
    print("A Cozy Tea Party for " + str(guests) + " People!")
    print("Tea Bags: " + str(tea_bags(people=guests)))
    print("Treats: " + str(treats(people=guests)))
    print(
        "Cost: $"
        + str(
            cost(tea_count=tea_bags(people=guests), treat_count=treats(people=guests))
            #  assign values to tea_count and trea_count
        )
    )
    # calls all the functions, concatenates the functions and string headings


def tea_bags(people: int) -> int:
    """compute the number of teabags through number of guests"""
    return 2 * people
    # number of people in attendance multiplied by expected number of teas (2)


def treats(people: int) -> int:
    """compute the number of treats needed based on number of teas had"""
    return int(tea_bags(people=people) * 1.5)


def cost(tea_count: int, treat_count: int) -> float:
    """compute the cost of tea bags & treats combined"""
    return (tea_count * 0.5) + (treat_count * 0.75)


if __name__ == "__main__":
    main_planner(guests=int(input("How many guests are attending your tea party?")))
