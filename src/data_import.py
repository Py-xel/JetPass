import pandas as pd


def import_flight_data(filepath):
    import pandas as pd

    try:
        df = pd.read_csv(filepath, encoding="latin1", delimiter=";")  # <--- here
        print("Columns found in CSV:", df.columns.tolist())
        return df
    except FileNotFoundError:
        print(f"Error: File not found at {filepath}!")
    except pd.errors.EmptyDataError:
        print(f"Error: Empty CSV file at {filepath}!")
    except pd.errors.ParserError:
        print(f"Error: Could not parse file at {filepath}")
    return None
