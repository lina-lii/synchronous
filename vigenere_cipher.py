def vigenere_encrypt(key, message):
    """Шифрование текста с использованием шифра Вижинера."""
    key = (key * (len(message) // len(key) + 1))[:len(message)]
    encrypted = ''.join(chr((ord(m) + ord(k)) % 65536) for m, k in zip(message, key))
    return encrypted

def vigenere_decrypt(key, ciphertext):
    """Дешифрование текста, зашифрованного шифром Вижинера."""
    key = (key * (len(ciphertext) // len(key) + 1))[:len(ciphertext)]
    decrypted = ''.join(chr((ord(c) - ord(k)) % 65536) for c, k in zip(ciphertext, key))
    return decrypted

# Пример использования
key = "ключ"
message = "Привет, мир!"
ciphertext = vigenere_encrypt(key, message)
print("Зашифрованный текст:", ciphertext)
print("Расшифрованный текст:", vigenere_decrypt(key, ciphertext))
