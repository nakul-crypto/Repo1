

class AirlineTicket:
    # class variable
    airlines_name = "IndiGo"

    # initialiser
    def __init__(self, dep_city, arr_city, flight_no, seat_no):
        # instance variable
        self.departure_city = dep_city
        self.arrival_city = arr_city
        self.flight_number = flight_no
        self.seat_no = seat_no
        print(f"Enter your journey details here: 1.Departure city:{dep_city}, 2.Arrival City:{arr_city}")

    # instance method
    def get_departure_city(self):
        return self.departure_city

    def get_arrival_city(self):
        return self.arrival_city

    def get_flight_no(self):
        return self.flight_number

    def seat_details(self):
        return self.seat_no

    # class method
    @classmethod
    def get_airlines_name(cls):
        return cls.airlines_name

    # static method
    @staticmethod
    def disp_greeting_msg():
        print("Have a safe flight: IndiGo Airlines")


def main():

    passenger_1_ticket = AirlineTicket("Pune", "Bangalore", "6E7127", "12K")
    passenger_2_ticket = AirlineTicket("Delhi", "Kolkata", "6E8742", "10J")

    print(f"Ticket details for the {passenger_1_ticket} is Departure City: {passenger_1_ticket.departure_city}, Arrival City: {passenger_1_ticket.arrival_city},\n "
          f"FLight no:{passenger_1_ticket.flight_number}, Seat No: {passenger_1_ticket.seat_no}")

    print(
        f"Ticket details for the {passenger_2_ticket} is Departure City: {passenger_2_ticket.departure_city}, Arrival City: {passenger_2_ticket.arrival_city},\n "
        f"FLight no:{passenger_2_ticket.flight_number}, Seat No: {passenger_2_ticket.seat_no}")


main()