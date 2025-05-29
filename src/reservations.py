import json
import os
from classes import TicketReserve

RESERVATION_FILE = "reservations.json"


def load_reservations():
    if not os.path.exists(RESERVATION_FILE):
        return []

    with open(RESERVATION_FILE, "r") as file:
        data = json.load(file)
        return [TicketReserve.from_dict(item) for item in data]


def save_reservation(new_reservation):
    reservations = load_reservations()
    reservations.append(new_reservation)

    with open(RESERVATION_FILE, "w") as file:
        json.dump([r.to_dict() for r in reservations], file, indent=4)

    print("\033[H\033[3J", end="")  # ANSI escape code to clear console
    print(f"Reservation saved for flight {new_reservation.flight_number}!")


def clear_reservations():
    with open(RESERVATION_FILE, "w") as file:
        json.dump([], file, indent=4)
