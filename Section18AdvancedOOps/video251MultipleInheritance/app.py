from admin import admin_class
from databasefile import database
admin_obj=admin_class("Parag","1234567",3)

admin_obj.add_to_database()

print(database.find_user(lambda x: x['username']=='Parag'))