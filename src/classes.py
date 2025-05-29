class Flight:  # Járat osztály

    def __init__(
        self,
        flight_num,
        destination,
        ticket_price,
        reserve_from,
        reserve_till,
        departure_date,
    ):
        self.flight_num = flight_num
        self.destination = destination
        self.ticket_price = ticket_price
        self.reserve_from = reserve_from
        self.reserve_till = reserve_till
        self.departure_date = departure_date


class DomesticFlight:  # Belföldi járat osztály

    def __init__(
        self,
        flight_num,
        origin,
        destination,
        ticket_price,
        reserve_from,
        reserve_till,
        departure_date,
        airline,
    ):
        self.flight_num = flight_num
        self.origin = origin
        self.destination = destination
        self.ticket_price = ticket_price
        self.reserve_from = reserve_from
        self.reserve_till = reserve_till
        self.departure_date = departure_date
        self.airline = airline


class InternationalFlight:  # Nemzetközi járat osztály

    def __init__(
        self,
        flight_num,
        origin,
        destination,
        ticket_price,
        reserve_from,
        reserve_till,
        departure_date,
        airline,
    ):
        self.flight_num = flight_num
        self.origin = origin
        self.destination = destination
        self.ticket_price = ticket_price
        self.reserve_from = reserve_from
        self.reserve_till = reserve_till
        self.departure_date = departure_date
        self.airline = airline


import uuid


class TicketReserve:
    def __init__(
        self,
        flight_number,
        airline,
        origin,
        destination,
        departure_date,
        price,
        ticket_number=None,
    ):
        self.ticket_number = ticket_number or str(
            uuid.uuid4()
        )  # Generate a random uuid
        self.flight_number = flight_number
        self.airline = airline
        self.origin = origin
        self.destination = destination
        self.departure_date = departure_date
        self.price = price

    def to_dict(self):
        return {
            "ticket_number": self.ticket_number,
            "flight_number": self.flight_number,
            "airline": self.airline,
            "origin": self.origin,
            "destination": self.destination,
            "departure_date": self.departure_date,
            "price": self.price,
        }

    @staticmethod  # Fallback values "Unknow" will prevent the program from crashing, if there is missing data (hopefully)...
    def from_dict(data):
        return TicketReserve(
            flight_number=data.get("flight_number"),
            airline=data.get("airline", "Unknown"),
            origin=data.get("origin", "Unknown"),
            destination=data.get("destination", "Unknown"),
            departure_date=data.get("departure_date", "Unknown"),
            price=data.get("price", 0),
            ticket_number=data.get("ticket_number"),
        )
