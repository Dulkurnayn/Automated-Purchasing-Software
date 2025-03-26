import random
from cryptography.fernet import Fernet
import os

class encryption():

    def hash(self,string):
        #string=string
        bytstring=string.encode(encoding = 'UTF-8')
        print(bytstring)
        offset = random.randint(100, 999) #this will be added to each byte
        hash=("")
        for bytes in bytstring:
            #print(bytes+offset, end = ' ') #end seprates the bytes to check appropraite fromat
            hash = (hash +" " + str(bytes))
        hash = (hash +" " + str(offset))
        offset= 0 #overwite the value so it cant bea accessed even if garbage collection doesn't occur
        print(hash)


    # will generate the key or load if exists
    def generate_key(self): 
        key_file = "fernet_key.key"
        if os.path.exists(key_file):
            with open(key_file, "rb") as f:
                key = f.read()
        else:
            key = Fernet.generate_key()
            with open(key_file, "wb") as f:
                f.write(key)
        return key

    # Encrypt the data using Fernet
    def encrypt_data(self,data, key):
        f = Fernet(key)
        encrypted_data = f.encrypt(data.encode())
        return encrypted_data
     # Decrypt the encrypted data using Fernet
    def decrypt_data(self,encrypted_data, key):
        f = Fernet(key)
        decrypted_data = f.decrypt(encrypted_data).decode()
        return decrypted_data


    # Store the encrypted data in an environment file
    def store_crypt_env(encrypted_data,key):
        with open(".env", "w") as env_file:
            env_file.write(f"ENCRYPTED_DATA={encrypted_data}")


class EnvManager:
    @staticmethod #use the devorator so it not necessary to have to instantiate the class 
    def load_encrypted_data_from_env():
        if os.path.exists(".env"):
            with open(".env", "r") as env_file:
                for line in env_file:
                    if line.startswith("ENCRYPTED_DATA="):
                        return line.split("ENCRYPTED_DATA=")[1].strip()
        return None

    # Example usage
    #encrypted_data = DataManager.load_encrypted_data_from_env()
    #print("Encrypted data:", encrypted_data)
    

   #decided the only way to safely store a master key is not to store it the users password will be the master key
#example use
a = encryption()  # Instantiate the encryption class
key=a.generate_key() #generate the key
print(key)
data=("helleoeoeoeoeoeo")
encrypted= a.encrypt_data(data,key) #encrypt passing in key and data

print("Encrypted data:",encrypted) #test output
    # Example usage
a.store_crypt_env(encrypted)
decrypted_data = a.decrypt_data(encrypted,key) #decrypt
print("Decrypted data:", decrypted_data)
password ="car"
username="apple"
a.hash(password)  # Call the hash method on the instance
a.hash(username)