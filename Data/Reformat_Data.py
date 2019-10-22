import getpass
class Encryption:
        def __init__(self):
            with open('Key.txt', 'r') as file:
                self.encrypt_key = file.read()

        def encrypt(self, data=''):
            key = self.encrypt_key*(len(str(data))//64+1)
            encrypted = ''
            for i in range(len(data)):
                char_id = str(ord(data[i])+ord(key[i]))
                char_val = '0'*(3-len(str(char_id)))+char_id
                encrypted += char_val
            return encrypted

        def decrypt(self, data=''):
            key = self.encrypt_key*(len(data)//64+1)
            decrypted = ''
            ctr = 0
            for i in range(0, len(data)//3):
                char_id = int(data[ctr:ctr+3])
                decrypted += chr(char_id-ord(key[i]))
                ctr += 3
            return decrypted

username = input("Enter username: ")
password = input("Enter password: ")
with open("Admins.txt",'r') as file:
    admins = Encryption().decrypt(file.read())
    admins = eval(admins)
if username in admins.keys():
    if password==admins[username]:
        data = {'Head_Boy': {'A1': 0, 'A2': 0, 'A3': 0}, 'Head_Girl': {'B1': 0, 'B2': 0, 'B3': 0}, 'Vice_Head_Boy': {'C1': 0, 'C2': 0, 'C3': 0}, 'Vice_Head_Girl': {'D1': 0, 'D2': 0, 'D3': 0}}
        enc_data = Encryption().encrypt(str(data))
        with open("Votes_encrypted.txt",'w') as file:
            file.write(enc_data)
        with open("Votes.txt",'w') as file:
            file.write(Encryption().encrypt('0'))
        print("Succesfully Reformated Data")
    else:
        print("Access Denied")
else:
    print("Access Denied")
        
    


    
