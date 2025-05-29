import questionary
from prompt_toolkit.styles import Style
from actions import view_flights, reserve_flight, view_reservations, delete_reservation
from reservations import clear_reservations
from prompt_toolkit.output.win32 import NoConsoleScreenBufferError


def main_menu(flights):

    custom_style = Style(
        [
            ("qmark", "fg:#673ab7 bold"),  # purple question mark
            ("question", "bold"),
            ("answer", "fg:#4caf50 bold"),  # green answer text
            ("pointer", "fg:#673ab7 bold"),
            ("highlighted", "fg:#673ab7 bold"),
            ("selected", "fg:#cc5454"),  # selected item (can customize too)
            ("separator", "fg:#cc5454"),
            ("instruction", ""),
            ("text", ""),
            ("disabled", "fg:#858585 italic"),
        ]
    )  # Customized style for questionary

    while True:
        try:
            choice = questionary.select(
                "What would you like to do?",
                choices=[
                    "View Flights",
                    "Reserve Flight",
                    "My Reservations",
                    "Delete Reservation",
                    "Exit",
                ],
                style=custom_style,
            ).ask()
        except NoConsoleScreenBufferError:
            print(
                "ERROR: No Windows console found.\n"
                "Please run this program in a terminal like cmd.exe, PowerShell, or Windows Terminal."
            )
            break  # Exit the menu loop

        if choice == "View Flights":
            view_flights(flights)
        elif choice == "Reserve Flight":
            reserve_flight(flights)
        elif choice == "My Reservations":
            view_reservations()
        elif choice == "Delete Reservation":
            delete_reservation()
        elif choice == "Exit":
            clear_reservations()
            print("Thank you for using JetPass! ✈️")
            break
