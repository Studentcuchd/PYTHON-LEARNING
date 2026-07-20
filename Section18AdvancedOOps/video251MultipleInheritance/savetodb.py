from databasefile import database
class savtodatabase:
    def add_to_database(self):
        database.add_data(self.dict_convert())