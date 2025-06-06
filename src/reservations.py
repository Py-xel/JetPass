import json
import os
from classes import TicketReserve
from rich.console import Console

console = Console()  # Required for rich library

RESERVATION_FILE = "reservations.json"


def full_clear():
    os.system("cls" if os.name == "nt" else "clear")
    console.clear()


def load_reservations():
    if not os.path.exists(RESERVATION_FILE):
        return []

    with open(RESERVATION_FILE, "r") as file:
        data = json.load(file)
        return [TicketReserve.from_dict(item) for item in data]


def save_reservation(new_reservation):
    reservations = load_reservations()

    for r in reservations:
        if (
            r.flight_number == new_reservation.flight_number
        ):  # Check for duplicate flight numbers as they are unique
            full_clear()
            console.print(
                f"Reservation for flight {new_reservation.flight_number} already exists.",
                style="bold red",
            )
            return
    reservations.append(new_reservation)
    full_clear()
    console.print(
        f"Reservation saved for flight {new_reservation.flight_number}!",
        style="bold green",
    )

    with open(RESERVATION_FILE, "w") as file:
        json.dump([r.to_dict() for r in reservations], file, indent=4)


def load_default_reservations():  # Hardcoded reservation as required by task
    if os.path.exists(RESERVATION_FILE):
        with open(RESERVATION_FILE, "r") as file:
            data = json.load(file)
            if data:  # If file already has reservations, do nothing
                return

    default_reservations = [
        TicketReserve(
            flight_number="LH1234",
            airline="Lufthansa",
            origin="FRA",
            destination="JFK",
            departure_date="2025-06-15",
            price=120000,
        ),
        TicketReserve(
            flight_number="AF4323",
            airline="Air France",
            origin="CDG",
            destination="FRA",
            departure_date="2025-07-20",
            price=444869,
        ),
        TicketReserve(
            flight_number="BA9876",
            airline="British Airways",
            origin="LHR",
            destination="JFK",
            departure_date="2025-08-10",
            price=150000,
        ),
    ]

    with open(RESERVATION_FILE, "w") as file:
        json.dump([r.to_dict() for r in default_reservations], file, indent=4)


def clear_reservations():
    with open(RESERVATION_FILE, "w") as file:
        json.dump([], file, indent=4)
