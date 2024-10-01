def less_than_10(num: int) -> None:

    dub: int = num * 2
    dub = dub - 1
    print(dub)

    if num < 10:
        print("Small Number!")
    else:
        print("Big Number!")
    print("Have a good day!")


def get_ticket_price() -> int:
    age: int = int(input("What is your age?"))
    if (age <= 12) or (age > 60):
        price: int = 5
    else:
        price: int = 10
    return price


print(get_ticket_price())
