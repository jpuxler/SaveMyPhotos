from cryptography.fernet import Fernet

# Schlüssel generieren
key = Fernet.generate_key()

cipher_suite = Fernet(key)

with open("logging_data.txt", "rb") as file:
    encrypted_data = file.read()
    decrypted_data = cipher_suite.decrypt(encrypted_data)
    print(decrypted_data.decode("utf-8"))