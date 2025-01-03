import time 

def watch(): 
    print("Секундомер запускается: ") 
    input("нажмите старт")
    start_time = time.time()           
    input("остановить секундомер: ")
    end_time = time.time() 
    final = float(end_time - start_time)
    minutes = final// 60 # it is a time
    seconds = final% 60   # it is a seconds
    print(f"прошло времени: {int(minutes)}  minutes and {seconds} seconds")
     
if __name__ == "__main__": 
    while True: 
        watch()
        repeat = input("Хочешь ли запустить еще раз? (да/нет) : ") 
        if repeat == "да": 
            print("Повтор") 
        else:
            print("стоп") 
            break