from typing import List

from repositories.baserepository import BaseRepository
from models.aircraft import Aircraft


class AircraftRepository(BaseRepository):
    def __init__(self):
        super().__init__()
        self.db = BaseRepository.db

    def create(self, aircraft: Aircraft):
        cursor = self.db.cursor()
        sql = "INSERT INTO aircraft(aircraft_number, capacity, name, type) VALUES(%s, %s, %s, %s)"
        val = (aircraft.aircraft_number, aircraft.capacity, aircraft.name, aircraft.type)
        cursor.execute(sql, val)
        self.db.commit()
        aircraft.id = cursor.lastrowid

    def update(self, id: int, aircraft: Aircraft):
        cursor = self.db.cursor()
        sql = "UPDATE aircraft SET aircraft_number= %s, capacity = %s, name = %s, type = %s WHERE id = %s"
        val = (aircraft.aircraft_number, aircraft.capacity, aircraft.name, aircraft.type, id)
        cursor.execute(sql, val)
        self.db.commit()

    def list(self):
        cursor = self.db.cursor()
        sql = "SELECT id, aircraft_number, name, type, capacity FROM aircraft"
        cursor.execute(sql)
        result = cursor.fetchall()
        aircrafts: List[Aircraft] = []
        for record in result:
            aircraft = AircraftRepository.__map_selected_result_to_aircraft(record)
            aircrafts.append(aircraft)
        return aircrafts

    def find(self, id: int):
        cursor = self.db.cursor()
        sql = "SELECT id, aircraft_number, type, capacity, name FROM aircraft WHERE id = %s"
        adr = (id,)
        cursor.execute(sql, adr)
        record = cursor.fetchone()
        aircraft = AircraftRepository.__map_selected_result_to_aircraft(record)
        return aircraft
    
    def delete(self, id: int):
        cursor = self.db.cursor()
        sql = "DELETE FROM aircraft WHERE id = %s"
        adr = (id,)
        cursor.execute(sql, adr)
        self.db.commit()

    @staticmethod
    def __map_selected_result_to_aircraft(record) -> Aircraft:
        if record is None:
            return None
        else:
            id, aircraft_number, type, name, capacity = record
            aircraft = Aircraft(aircraft_number, type, name, capacity)
            aircraft.id = id
            return aircraft
