from menu.menu import Menu
from menu.menu_item import MenuItem
from models.aircraft import Aircraft
from repositories.aircraftrepository import AircraftRepository
from utils import prompt_for_valid_integer_input, prompt_for_non_empty_string_input


class AircraftManagementService:
    menu: Menu
    aircraft_repository: AircraftRepository

    def __init__(self, aircraft_repository: AircraftRepository, menu: Menu):
        self.menu = Menu([
            MenuItem("List aircraft", lambda: self.__list_aircrafts()),
            MenuItem("Find aircraft", lambda: self.__find_aircraft()),
            MenuItem("Create aircraft", lambda: self.__create_aircraft()),
            MenuItem("Update aircraft", lambda: self.__update_aircraft()),
            MenuItem("Delete aircraft", lambda: self.__delete_aircraft()),
        ], parent=menu)
        self.aircraft_repository = aircraft_repository

    def display_menu(self):
        self.menu.display()

    def __list_aircrafts(self):
        aircrafts = self.aircraft_repository.list()
        for aircraft in aircrafts:
            print(aircraft)
        self.display_menu()

    def __find_aircraft(self):
        # get id from user
        id = prompt_for_valid_integer_input("Please enter the id: ")
        aircraft = self.aircraft_repository.find(id)
        if aircraft is None:
            return self.__find_aircraft()
        print(aircraft)
        self.display_menu()

    def __create_aircraft(self):
        capacity = prompt_for_valid_integer_input("Please enter the capacity: ")
        name = prompt_for_non_empty_string_input("Please enter the name: ")
        aircraft_number = prompt_for_non_empty_string_input("Please enter the aircraft number: ")
        aircraft_type = prompt_for_non_empty_string_input("Please enter the type: ")
        aircraft = Aircraft(aircraft_number, capacity, name, aircraft_type)
        self.aircraft_repository.create(aircraft)
        self.display_menu()

    def __update_aircraft(self):
        id = prompt_for_valid_integer_input("Please enter the id: ")
        capacity = prompt_for_valid_integer_input("Please enter the capacity: ")
        name = prompt_for_non_empty_string_input("Please enter the name: ")
        aircraft_number = prompt_for_non_empty_string_input("Please enter the aircraft number: ")
        aircraft_type = prompt_for_non_empty_string_input("Please enter the type: ")
        aircraft = Aircraft(aircraft_number, capacity, name, aircraft_type)
        self.aircraft_repository.update(id, aircraft)
        self.display_menu()

    def __delete_aircraft(self):
        id = prompt_for_valid_integer_input("Please enter the id: ")
        self.aircraft_repository.delete(id)
        self.display_menu()

