from data_import import import_flight_data
from flight_factory import create_flights_from_dataframe


def main():
    # region --- Reads and imports a csv file into a pandas dataframe.
    filepath = "./flight_data.csv"
    df = import_flight_data(filepath)
    # endregion

    # region --- Convert data to flight objects and display them
    flights = create_flights_from_dataframe(filepath)

    print(f"\nLoaded {len(flights)} flights:")
    for flight in flights:
        print(
            f"{type(flight).__name__} | Flight: {flight.flight_num}, "
            f"{flight.origin} → {flight.destination}, "
            f"Departure: {flight.departure_date}, "
            f"Price: {flight.ticket_price} Ft, "
            f"Reserve: {flight.reserve_from} to {flight.reserve_till}"
        )
    # endregion


if __name__ == "__main__":
    main()
