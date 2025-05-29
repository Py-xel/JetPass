import json
import os
from classes import TicketReserve
from rich.console import Console

console = Console()  # Required for rich library

RESERVATION_FILE = "reservations.json"


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
            console.print(
                f"Reservation for ticket {new_reservation.ticket_number} already exists.",
                style="bold red",
            )
            return
    reservations.append(new_reservation)
    print("\033[H\033[3J", end="")  # ANSI escape code to clear console
    console.clear()  # clear rich console
    console.print(
        f"Reservation saved for flight {new_reservation.flight_number}!",
        style="bold green",
    )

    with open(RESERVATION_FILE, "w") as file:
        json.dump([r.to_dict() for r in reservations], file, indent=4)


def clear_reservations():
    with open(RESERVATION_FILE, "w") as file:
        json.dump([], file, indent=4)
