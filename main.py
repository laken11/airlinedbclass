from menu.menu_item import MenuItem
from menu.menu import Menu
from repositories.aircraftrepository import AircraftRepository
from services.aircraft_management import AircraftManagementService


# services
aircraft_management_service: AircraftManagementService = None


# repositories
aircraft_repository: AircraftRepository = None


def main():
    main_menu = Menu([])
    main_menu.items.extend([
        MenuItem("Aircraft management", lambda: go_to_aircraft_management(main_menu)),
    ])
    main_menu.display()


def go_to_aircraft_management(main_menu):
    global aircraft_management_service
    global aircraft_repository
    __set_aircraft_management_service_if_none(main_menu)
    aircraft_management_service.display_menu()


def __set_aircraft_management_service_if_none(main_menu):
    global aircraft_repository, aircraft_management_service
    if aircraft_management_service is None:
        __set_aircraft_repository_if_none()
        aircraft_management_service = AircraftManagementService(aircraft_repository, main_menu)


def __set_aircraft_repository_if_none():
    global aircraft_repository
    if aircraft_repository is None:
        aircraft_repository = __create_aircraft_repository()


def __create_aircraft_repository() -> AircraftRepository:
    repo = AircraftRepository()
    return repo


main()
