def caesar_encrypt(key, message):
    """Шифрование текста с использованием обобщенного шифра Цезаря."""
    encrypted = ''.join(chr((ord(char) + key) % 65536) for char in message)
    return encrypted

def caesar_decrypt(key, ciphertext):
    """Дешифрование текста, зашифрованного шифром Цезаря."""
    decrypted = ''.join(chr((ord(char) - key) % 65536) for char in ciphertext)
    return decrypted

# Пример использования
message = "Привет, мир!"
key = 5
ciphertext = caesar_encrypt(key, message)
print("Зашифрованный текст:", ciphertext)
print("Расшифрованный текст:", caesar_decrypt(key, ciphertext))
