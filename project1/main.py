num1 = float(input("Введите первое значения"))
num2 = float(input("Введите второе значения")) 
 
operator = input("Введите операцию (+, -, *, /):") 

if operator == '+':
     print(f"результат: {num1 + num2}")
elif operator == '-':
     print(f"результат: {num1 - num2}")
elif operator == '*':
     print(f"результат: {num1 * num2}")
elif operator == '/':
     print(f"результат: {num1 / num2}") 