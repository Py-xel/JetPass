import pandas as pd
from classes import DomesticFlight, InternationalFlight
from data_import import import_flight_data


def create_flights_from_dataframe(filepath):
    try:
        df = import_flight_data(filepath)
        df.columns = (
            df.columns.str.strip().str.lower()
        )  # get raw value without any leftover spaces etc.
    except Exception as e:
        print(f"Error loading CSV: {e}")
        return []

    flights = []

    for _, row in df.iterrows():
        flight_type = row["flight_type"].strip().lower()
        departure_date = row.get("departure_date", None)

        if flight_type == "domestic":
            flight = DomesticFlight(
                flight_num=row["flight_num"],
                origin=row["origin"],
                destination=row["destination"],
                ticket_price=row["ticket_price"],
                reserve_from=row["reserve_from"],
                reserve_till=row["reserve_till"],
                departure_date=row["departure_date"],
            )
        elif flight_type == "international":
            flight = InternationalFlight(
                flight_num=row["flight_num"],
                origin=row["origin"],
                destination=row["destination"],
                ticket_price=row["ticket_price"],
                reserve_from=row["reserve_from"],
                reserve_till=row["reserve_till"],
                departure_date=row["departure_date"],
            )
        else:
            print(f"Unknown flight type: {flight_type}")
            continue

        flights.append(flight)

    return flights
