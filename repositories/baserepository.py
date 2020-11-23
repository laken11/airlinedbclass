import mysql.connector


class BaseRepository:
    db = None

    def __init__(self):
        if BaseRepository.db is None:
            BaseRepository.db = mysql.connector.connect(host="localhost",
                                                        user="root",
                                                        password="OlaniteAbdulrazaq1999",
                                                        database="airlineManagement")
