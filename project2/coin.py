# The game (Орел и решка) 
import random
while True:
    coin = random.randint(0,1) 
# 0 - Орел, 1 - Решка.
    if coin == 0: 
        print("Выпадит Орел!") 
    else: 
        print("Выпадет Решка!")
    input()
      