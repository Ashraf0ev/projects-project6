num1 = float(input("Введите первое значения "))
num2 = float(input("Введите второе значения "))
operator = input("Введите операцию (+, -, *, /): ") 
def calculator(num1, num2, operator):
    if operator == '+':  
        return num1 + num2
    elif operator == '-': 
        return num1 - num2
    elif operator == '*':
        return num1 * num2 
    elif operator == '/': 
        return num1 / num2
    else:    
        return ("Uncorrect operator")

print(calculator(num1,num2,operator))  
print("hello")