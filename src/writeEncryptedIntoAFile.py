from cryptography.fernet import Fernet

# Schlüssel generieren
key = Fernet.generate_key()

cipher_suite = Fernet(key)

data = b"Hello World"

encrypted_data = cipher_suite.encrypt(data)

with open("loggin_data.txt", "wb") as file:
    file.write(encrypted_data)