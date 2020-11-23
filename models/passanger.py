class Passenger:
    id: str
    name: str
    age: int
    phone_number: str
    email: str
    address: str
    gender: str

    def __init__(self, name: str, age: int, phone_number: str, email: str, address: str, gender: str):
        self.name = name
        self.age = age
        self.phone_number = phone_number
        self.email = email
        self.address = address
        self.gender = gender

    def __str__(self):
        return f"{self.id}:\t{self.name}\t{self.age}\t{self.phone_number}\t{self.email}\t{self.address}\t{self.gender}"