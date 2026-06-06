# Caesar Cipher Encryption & Decryption

def encrypt(text, shift):
    encrypted = ""

    for char in text:
        if char.isalpha():
            if char.isupper():
                encrypted += chr((ord(char) - ord('A') + shift) % 26 + ord('A'))
            else:
                encrypted += chr((ord(char) - ord('a') + shift) % 26 + ord('a'))
        else:
            encrypted += char

    return encrypted


def decrypt(text, shift):
    decrypted = ""

    for char in text:
        if char.isalpha():
            if char.isupper():
                decrypted += chr((ord(char) - ord('A') - shift) % 26 + ord('A'))
            else:
                decrypted += chr((ord(char) - ord('a') - shift) % 26 + ord('a'))
        else:
            decrypted += char

    return decrypted


message = input("Enter Message: ")
shift = int(input("Enter Shift Key: "))

encrypted_text = encrypt(message, shift)
decrypted_text = decrypt(encrypted_text, shift)

print("\nEncrypted Text:", encrypted_text)
print("Decrypted Text:", decrypted_text)
