from cryptography.fernet import Fernet

with open("loggin_data.txt", "rb") as file:
    encrypted_data = file.read()
    decrypted_data = cipher_suite.decrypt(encrypted_data)
    print(decrypted_data.decode("utf-8"))