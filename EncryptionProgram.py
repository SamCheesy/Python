import base64

def encryptPass(passw):
    encodedBytes = base64.b64encode(passw.encode())
    print(encodedBytes)

user_pass = input("enter your password: ")
encryptPass(user_pass)