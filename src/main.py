from data_import import import_flight_data
from flight_factory import create_flights_from_dataframe
from menu import main_menu


def main():
    filepath = "./flight_data.csv"
    flights = create_flights_from_dataframe(filepath)

    if flights:
        main_menu(flights)
    else:
        print("No flights loaded.")


if __name__ == "__main__":
    main()
