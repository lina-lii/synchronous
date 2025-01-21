from collections import Counter

def caesar_break(ciphertext):
    """Взлом шифра Цезаря методом частотного анализа."""
    # Находим наиболее частый символ в тексте
    most_common_char = Counter(ciphertext).most_common(1)[0][0]
    # Предполагаем, что это пробел (в Unicode пробел = 32)
    key = (ord(most_common_char) - ord(' ')) % 65536
    return caesar_decrypt(key, ciphertext), key

# Пример использования
hacked_message, hacked_key = caesar_break(ciphertext)
print("Взломанный текст:", hacked_message)
print("Ключ:", hacked_key)
