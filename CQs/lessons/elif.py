def get_weather_report() -> str:
    """displays the weather instructions"""

    weather: str = input("What is the weather?")

    if (weather == "rainy") or (weather == "cold"):
        print("Bring a jacket!")
    elif weather == "hot":
        print("Keep cool out there!")
    else:
        print("I don't recognize this weather.")


get_weather_report()
