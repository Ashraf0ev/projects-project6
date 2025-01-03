# Функция для шифрования text
def encrypt_function(text, shift):
    if not isinstance(shift,int):
        shift=int(shift)
    encrypted_text = ""  # Начинаем пустую строку для зашифрованного текста
    for char in text: 
        if char.isalpha():  # Если символ буква то тогда свигаем букву по алфавиту
            new_char = chr(ord(char)+shift)
            encrypted_text += new_char  # Добавляем новый символ в зашифрованный текст
        else:
            encrypted_text += char  
    return encrypted_text  # Возвращаем зашифрованный текст

# Функция для дешифрования текста
def descrypt_function(text, shift):
    if not isinstance(shift, int):
        shift = int(shift)
    decrypted_text = ""  # Начинаем пустую строку для расшифрованного текста
    for char in text:  # Проходим по каждому символу в тексте
        if char.isalpha():  # Если символ буква то тогда свигаем букву по алфавиту
            new_char = chr(ord(char)-shift) 
            decrypted_text += new_char  # Добавляем новый символ в расшифрованный текст
        else:
            decrypted_text += char  
    return decrypted_text  # Возвращаем расшифрованный текст

#  результат
text = input("Введите текст для шифровки: ")
shift = (input("Введите шаг сдвига: "))

encrypted =encrypt_function(text, shift)
print("Зашифрованный текст:", encrypted)
decrypted =descrypt_function(encrypted, shift)
print("Дешифрованный текст:", decrypted)