def xor_encrypt(key, message):
    """Шифрование текста с использованием XOR."""
    key = (key * (len(message) // len(key) + 1))[:len(message)]
    encrypted = ''.join(chr(ord(m) ^ ord(k)) for m, k in zip(message, key))
    return encrypted

def xor_decrypt(key, ciphertext):
    """Дешифрование текста, зашифрованного XOR."""
    return xor_encrypt(key, ciphertext)  # Обратная операция та же самая

# Пример использования
key = "ключ"
message = "Привет, мир!"
ciphertext = xor_encrypt(key, message)
print("Зашифрованный текст:", ciphertext)
print("Расшифрованный текст:", xor_decrypt(key, ciphertext))
