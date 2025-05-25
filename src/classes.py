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
    ):
        self.flight_num = flight_num
        self.origin = origin
        self.destination = destination
        self.ticket_price = ticket_price
        self.reserve_from = reserve_from
        self.reserve_till = reserve_till
        self.departure_date = departure_date


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
    ):
        self.flight_num = flight_num
        self.origin = origin
        self.destination = destination
        self.ticket_price = ticket_price
        self.reserve_from = reserve_from
        self.reserve_till = reserve_till
        self.departure_date = departure_date


class Airline:  # Légi társaság osztály

    def __init__(self, name):
        self.name = name


class TicketReserve:  # Jegy foglalás osztály

    def __init__(self, ticket_number, flight_number):
        self.ticket_number = ticket_number
        self.flight_number = flight_number
