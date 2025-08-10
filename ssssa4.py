def caesar_cipher(text, shift):
    result = ""
    for char in text:
        if char.isalpha():
            ascii_offset = 65 if char.isupper() else 97
            result += chr((ord(char) + shift - ascii_offset) % 26 + ascii_offset)
        else:
            result += char
    return result

text = input("Enter text to encrypt: ")
shift = int(input("Enter shift value (1-25): "))
encrypted = caesar_cipher(text, shift)
print(f"Encrypted text: {encrypted}")
decrypted = caesar_cipher(encrypted, -shift)
print(f"Decrypted text: {decrypted}")