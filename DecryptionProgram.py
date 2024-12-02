import base64

def decrypt(passw):
    decrypted_bytes = base64.b64decode(passw)
    decrypted_data = decrypted_bytes.decode()
    print(decrypted_data)

user_password = input("Password to decrypt: ")
decrypt(user_password)