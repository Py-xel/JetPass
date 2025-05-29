from flight_factory import create_flights_from_dataframe
from reservations import load_default_reservations
from menu import main_menu


def main():
    load_default_reservations()  # Load default reservations
    filepath = "./flight_data.csv"
    flights = create_flights_from_dataframe(filepath)

    if flights:
        main_menu(flights)
    else:
        print("No flights loaded.")


if __name__ == "__main__":
    main()
