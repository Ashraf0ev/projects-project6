from peewee import *
from datetime import datetime 

# база данные 
db = SqliteDatabase('people.db')  

class BaseModel(Model):
    """Создание базового класса"""
    class Meta:
        database = db  

class Person(BaseModel):
    name = CharField()  # имя человека
    birthday = DateField()  # дата рождения

class Friend(BaseModel):
    # связи с друзьями
    surname = CharField()
    friend = ForeignKeyField(Person, backref="friends")  # обратная связь 

def people():
    # Создание записей в таблице Person
    ashraf = Person.create(name='Ashraf', birthday='2004-10-14')
    aleksandr = Person.create(name='Aleksandr', birthday='2005-08-25')
    alibek = Person.create(name='Alibek', birthday='2006-04-19')
    xusan = Person.create(name='Xusan', birthday='2005-08-11')
    otabek = Person.create(name='Otabek', birthday='2006-04-06')

    # Создание записи в таблице Friends
    ashraf_friends = [
        Friend.create(surname='Mukhtorjonov', friend=ashraf),
        Friend.create(surname='Donich', friend=aleksandr),
        Friend.create(surname='Mahkmudov', friend=alibek),
        Friend.create(surname='Yusupov', friend=xusan),
        Friend.create(surname='Itpu', friend=otabek),
    ] 
    return ashraf_friends

def calculator_age(ashraf_friends):
   # Сохранение данных в базе (целиком)
    today = datetime.today().date()
    friend_dict = {} 

    for friend in ashraf_friends:
        person = friend.friend  # друг
        birthday_date = person.birthday  # дата рождения друга
        
        if isinstance(birthday_date, str):  
            birthday_date = datetime.strptime(birthday_date, '%Y-%m-%d').date()  # преобразуем в datetime.date

        age = today.year - birthday_date.year - ((today.month, today.day) < (birthday_date.month, birthday_date.day))
        
        friend_dict[person.name] = {
            "birthday": birthday_date,
            "age": age
        }
   
    print(f"Friend of Ashraf:")
    for name, details in friend_dict.items():
        print(f"name: {name}, birthday: {details['birthday']}, age: {details['age']}") 

def main():
    # Подключение к базе данных и создание таблиц
    with db:
        db.create_tables([Person, Friend]) 
        ashraf_friends = people()
        calculator_age(ashraf_friends)

if __name__ == "__main__":
    main()