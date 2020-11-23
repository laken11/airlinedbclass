class Booking:
    id: int
    flight_id: int
    booking_reference: str
    class_of_flight: str
    seat_number: int
    destination: str
    price: float
    passenger_id: int

    def __init__(self, flight_id: int, booking_reference: str, class_of_flight: str, seat_number: int, destination: str, price: float, passenegr_id: int):
        self.flight_id = flight_id
        self.booking_reference = booking_reference
        self.class_of_flight = class_of_flight
        self.seat_number = seat_number
        self.destination = destination
        self.price = price
        self.passenger_id = passenegr_id

    def __str__(self):
        return f"{self.id}:\t{self.flight_id}\t{self.booking_reference}\t{self.class_of_flight}\t{self.seat_number}\t{self.destination}\t{self.price}\t{self.passenger_id}"
