from peewee import *

db = SqliteDatabase('people.db')

class BaseModel(Model):
    """Создание базового класса"""
    class Meta:
        database = db

class Person(BaseModel):
    name = CharField()
    birthday = DateField()

class Family(BaseModel):
    surname = CharField()
    family = ForeignKeyField(Person, backref='families')  # Связь с таблицей Person

def people():
    # Создание записей в таблице Person
    ashraf = Person.create(name='Ashraf', birthday='2004-10-14')
    gulnara = Person.create(name='Gulnara', birthday='1981-03-20')
    
    # Создание записи в таблице Family
    yodgarova = Family.create(surname='Yodgarova', family=ashraf)
    
    # Сохранение данных в базе
    ashraf.save()
    gulnara.save()
    yodgarova.save()

def main():
    # Подключение к базе данных и создание таблиц
    with db:
        db.create_tables([Person, Family])
    people()

if __name__ == "__main__":
    main()
