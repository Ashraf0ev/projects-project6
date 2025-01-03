from project5.cryptographer import encrypt_function, descrypt_function

def main():
    text = input("Введите текст для шифровки: ")
    shift = int(input("Введите шаг сдвига: ")) 

    encrypted = encrypt_function(text, shift)
    print("Зашифрованный текст:", encrypted)

    decrypted = descrypt_function(encrypted, shift)
    print("Дешифрованный текст:", decrypted)

if __name__ == '__main__':
    main()