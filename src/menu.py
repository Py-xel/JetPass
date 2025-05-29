import questionary
from actions import view_flights, reserve_flight


def main_menu(flights):
    while True:
        choice = questionary.select(
            "What would you like to do?",
            choices=["View all available flights", "Reserve a flight", "Exit"],
        ).ask()

        if choice == "View all available flights":
            view_flights(flights)
        elif choice == "Reserve a flight":
            reserve_flight(flights)
        elif choice == "Exit":
            print("Thank you for using the flight reservation system.")
            break
