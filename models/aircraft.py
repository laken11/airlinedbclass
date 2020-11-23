class Aircraft:
    id: int
    aircraft_number: str
    capacity: int
    name: str
    type: str

    def __init__(self, aircraft_number: str, capacity: int, name: str, type: str):
        self.aircraft_number = aircraft_number
        self.capacity = capacity
        self.name = name
        self.type = type

    def __str__(self):
        return f"{self.id}:\t{self.aircraft_number}\t{self.name}\t{self.type}\t{self.capacity}"
