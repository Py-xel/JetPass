import questionary
from actions import view_flights, reserve_flight, view_reservations
from reservations import clear_reservations


def main_menu(flights):
    while True:
        choice = questionary.select(
            "What would you like to do?",
            choices=[
                "View all available flights",
                "Reserve a flight",
                "View current reservations",
                "Exit",
            ],
        ).ask()

        if choice == "View all available flights":
            view_flights(flights)
        elif choice == "Reserve a flight":
            reserve_flight(flights)
        elif choice == "View current reservations":
            view_reservations()
        elif choice == "Exit":
            clear_reservations()
            print("Thank you for using JetPass!")
            break
