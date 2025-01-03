import random 
# print(random.randint(0, 10))  
num = random.randint(0, 10)  
while True: 
    a = int(input("Введите число от 0 до 10: ") )
    if a < 0 or a > 10: 
        print("Введите число от 0 до 10 ") 
    if a < num : 
        print("число слишком маленькое")
    elif a > num :
        print("число слишком большое")
    else:
        print("Угадали число!") 
        break
# The game (Орел и решка) 
while True:
     coin = random.randint(0,1) 
# 0 - Орел, 1 - Решка.
int(input("Орел 0 или Решка 1: ")) 
if input == coin: 
    print("Вы угадали")
else:
     print('Вы не угадали')
      