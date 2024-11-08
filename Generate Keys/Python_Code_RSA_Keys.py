import os
from Cryptodome.PublicKey import RSA
from Cryptodome.Cipher import PKCS1_OAEP

def generate_key_pair():
    key = RSA.generate(2048)
    private_key = key.export_key()
    public_key = key.publickey().export_key()

    with open('private_key.pem', 'wb') as f:
        f.write(private_key)

    with open('public_key.pem', 'wb') as f:
        f.write(public_key)

def read_private_key():
    with open('private_key.pem', 'rb') as f:
        private_key = RSA.import_key(f.read())
        print("reading private key.. in progress")
    return private_key

def encrypt_data(data):
    with open('public_key.pem', 'rb') as f:
        public_key = RSA.import_key(f.read())

    cipher = PKCS1_OAEP.new(public_key)
    ciphertext = cipher.encrypt(data)

    with open('encrypted_data.bin', 'wb') as f:
        f.write(ciphertext)
        print("data encryped")

def decrypt_data():
    with open('private_key.pem', 'rb') as f:
        private_key = RSA.import_key(f.read())

    cipher = PKCS1_OAEP.new(private_key)

    with open('encrypted_data.bin', 'rb') as f:
        ciphertext = f.read()

    plaintext = cipher.decrypt(ciphertext)

    with open('decrypted_data.txt', 'w') as f:
        f.write(plaintext.decode())
        print("Data decryption in progress")
        print("Files have been created in the folder")

if __name__ == "__main__":
    private_key = None

    if not os.path.exists("private_key.pem"):
        generate_key_pair()

    if os.path.exists("private_key.pem"):
        private_key = read_private_key()

    if private_key is not None:
        encrypt_data(b'This is a long text string that will be encrypted using RSA \nHello Professor')
        decrypt_data()
    else:
        print("Error with Keys... no key was generated or found!")
