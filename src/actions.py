from rich.table import Table
from rich.console import Console
from rich.prompt import Prompt
from classes import TicketReserve
from reservations import save_reservation, load_reservations

console = Console()  # Required for rich library


def view_flights(flights):  # Lists all flights from the flight_data.csv table
    if not flights:
        console.print("No flights available.\n", style="bold red")
        return

    table = Table(show_header=True, header_style="bold white")

    table.add_column("Airline", style="cyan", justify="left")
    table.add_column("Flight Number", style="bold", justify="center")
    table.add_column("Origin", justify="center")
    table.add_column("Destination", justify="center")
    table.add_column("Price", style="green", justify="center")
    table.add_column("Reserve From", justify="center")
    table.add_column("Reserve Till", justify="center")
    table.add_column("Departure Date", style="yellow", justify="center")

    for flight in flights:
        table.add_row(
            flight.airline,
            flight.flight_num,
            flight.origin,
            flight.destination,
            f"{flight.ticket_price} Ft",
            flight.reserve_from,
            flight.reserve_till,
            flight.departure_date,
        )
    console.clear()
    console.print(table)


def reserve_flight(
    flights,
):  # Lists all flights then saves a selected one to a JSON file
    if not flights:
        console.print("No flights available for reservation.\n", style="bold red")
        return None

    table = Table(show_header=True, header_style="bold white")
    table.add_column("#", justify="center")
    table.add_column("Airline", style="cyan", justify="left")
    table.add_column("Flight Number", style="bold", justify="center")
    table.add_column("Origin", justify="center")
    table.add_column("Destination", justify="center")
    table.add_column("Price", style="green", justify="center")
    table.add_column("Reserve From", justify="center")
    table.add_column("Reserve Till", justify="center")
    table.add_column("Departure Date", style="yellow", justify="center")

    for i, flight in enumerate(flights, start=1):
        table.add_row(
            str(i),
            flight.airline,
            flight.flight_num,
            flight.origin,
            flight.destination,
            f"{flight.ticket_price} Ft",
            flight.reserve_from,
            flight.reserve_till,
            flight.departure_date,
        )

    console.clear()
    console.print(table)

    while True:
        try:
            choice = int(Prompt.ask("Enter the number of the flight to reserve"))
            if 1 <= choice <= len(flights):
                selected_flight = flights[choice - 1]

                reservation = TicketReserve(
                    flight_number=selected_flight.flight_num,
                    airline=selected_flight.airline,
                    origin=selected_flight.origin,
                    destination=selected_flight.destination,
                    departure_date=selected_flight.departure_date,
                    price=selected_flight.ticket_price,
                )

                save_reservation(reservation)

                return selected_flight
            else:
                console.print("Invalid number. Try again.", style="bold red")
        except ValueError:
            console.print("Please enter a valid number.", style="bold red")


def view_reservations():
    reservations = load_reservations()
    if not reservations:
        console.print("No reservations found.", style="bold red")
        return

    table = Table(show_header=True, header_style="bold white")
    table.add_column("Ticket Number", style="cyan", justify="center")
    table.add_column("Flight Number", style="bold", justify="center")
    table.add_column("Airline", justify="center")
    table.add_column("Origin", justify="center")
    table.add_column("Destination", justify="center")
    table.add_column("Departure Date", justify="center")
    table.add_column("Price", style="green", justify="center")

    for r in reservations:
        table.add_row(
            r.ticket_number,
            r.flight_number,
            r.airline,
            r.origin,
            r.destination,
            r.departure_date,
            f"{r.price} Ft",
        )

    console.print(table)
