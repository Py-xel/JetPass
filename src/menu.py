import questionary
from actions import view_flights, reserve_flight
from reservations import clear_reservations


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
            clear_reservations()
            print("Thank you for JetPass!")
            break
