class Flight:
    id: int
    flight_number: str
    take_off_point: str
    take_off_time: str
    destination: str
    price: float
    aircraft_id: int

    def __init__(self, flight_number: str, take_off_point: str, take_off_time: str, destination: str, price: float,
                 aircraft_id: int):
        self.flight_number = flight_number
        self.take_off_point = take_off_point
        self.take_off_time = take_off_time
        self.destination = destination
        self.price = price
        self.aircraft_id = aircraft_id

    def __str__(self):
        return f"{self.id}:\t{self.flight_number}\t{self.take_off_point}\t{self.take_off_time}\t{self.destination}\t{self.price}\t{self.aircraft_id}"
