"""Practing application of lists"""

# creating an empty list
my_numbers: list[float] = []  # w/ a literal

# adding a value to a list name.append(value)
my_numbers.append(1.5)
my_numbers.append(2.3)

# creating a list w/ values already in it
game_points: list[int] = [102, 86, 94]
# game_points: list[int | float] = [102, 93, 4.5, 22.22](ints and floats in list)

# accessing an index in a list
# print(game_points[0])
last_game: int = game_points[2]
# print(last_game)

# modifying by index ; changes index list value
game_points[1] = 72
# print(game_points)

# length of an index
len(game_points)
# print(len(game_points))

# remove item from list
game_points.pop(1)
# print(game_points)

grocery_list: list[str] = ["bananas", "eggs", "apples"]

grocery_list.append("bananas")

# print(grocery_list)


# print(game_points)


def display(integers: list[int]) -> None:
    """print every element in the input list"""

    idx: int = 0

    while idx < len(integers):
        print(integers[idx])
        idx += 1


display(integers=game_points)
