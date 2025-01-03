from peewee import *
from datetime import datetime  
 # база данные 
db = SqliteDatabase('passwords.db') 
"""Создание модель пользователя"""

class User(Model): 
    username = CharField()
    password = CharField()
    last_update=DateTimeField(default=datetime.now)

    class Meta:
        database=db  
#основная функция где пользователь создает свой пароль    
def create_password():
    username=input("Введите имя пользователя: ")
    password=input("Введите ваш пароль: ")

    if User.select().where(User.username == username).exists():
        print("Пользователь уже существует.")
    else:
        User.create(username=username, password=password)
        print("Пароль успешно создан!")

def change_password():
    username = input("Введите имя пользователя: ") 
    new_password=input("Введите новый пароль: ")
#обновления или изменение пароля 
    if User.update(password=new_password,last_update=datetime.now()).where(User.username==username).execute(): 
        print('Пароль изменен успешно!')
    else:
        print('Пароль не найден') 

def show_password():
     username= input('Введите имя пользователя: ')
     user=User.get_or_none(User.username==username)

     if user:
          print('пароль:',user.password)
          print('обновлен:',user.last_update)
     else:
          print('пользователь не найдено')

def main():
     # Подключение к базе данных и создание таблиц
    with db:
        db.create_tables([User]) 

    while True:
        print("Меню:")
        print("1. Создать пароль")
        print("2. Изменить пароль")
        print("3. Показать пароль")
        print("4. Выйти")
        choice = input('Выберите номер:')
        
        if choice == "1":
            create_password()
        elif choice == "2":
            change_password()
        elif choice == "3":
            show_password()
        elif choice == "4":
            print("Выход")
            break
        else:
            print("ошибка,пробуйте заново ")

if __name__=="__main__":
    main()