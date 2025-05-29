import questionary
from reservations import save_reservation
from classes import TicketReserve
import random


def view_flights(flights):
    print("\nAvailable Flights:")
    for flight in flights:
        print(
            f"{type(flight).__name__} | Flight: {flight.flight_num}, "
            f"{flight.origin} → {flight.destination}, "
            f"Departure: {flight.departure_date}, "
            f"Price: {flight.ticket_price} Ft"
        )
    print()


def reserve_flight(flights):
    flight_nums = [flight.flight_num for flight in flights]

    selected = questionary.select(
        "Select a flight to reserve:", choices=flight_nums
    ).ask()

    if selected:
        # Generate a random ticket number
        ticket_number = f"TKT{random.randint(1000, 9999)}"

        # Create and save reservation
        reservation = TicketReserve(ticket_number, selected)
        save_reservation(reservation)
