import os

def iv_encrypt(key, message):
    """Шифрование текста с использованием вектора инициализации (IV)."""
    iv = os.urandom(len(key))  # Генерация случайного IV
    key = (key * (len(message) // len(key) + 1))[:len(message)]
    encrypted = []
    
    prev = iv
    for m, k in zip(message.encode('utf-8'), key.encode('utf-8')):
        enc = m ^ k ^ prev[0]
        encrypted.append(enc)
        prev = bytes([enc])
    
    return iv + bytes(encrypted)

def iv_decrypt(key, ciphertext):
    """Дешифрование текста, зашифрованного с использованием IV."""
    iv, encrypted = ciphertext[:len(key)], ciphertext[len(key):]
    key = (key * (len(encrypted) // len(key) + 1))[:len(encrypted)]
    decrypted = []
    
    prev = iv
    for c, k in zip(encrypted, key.encode('utf-8')):
        dec = c ^ k ^ prev[0]
        decrypted.append(dec)
        prev = bytes([c])
    
    return bytes(decrypted).decode('utf-8')

# Пример использования
key = "ключ"
message = "Привет, мир!"
ciphertext = iv_encrypt(key, message)
print("Зашифрованный текст (с IV):", ciphertext)
print("Расшифрованный текст:", iv_decrypt(key, ciphertext))
