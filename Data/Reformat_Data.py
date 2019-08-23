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
        data = {'Head_Boy': {'BHAVVYA SARNA': 6, 'DHRUV K': 2, 'KEVIN CARVALHO': 0}, 'Head_Girl': {'SNEHA ROY': 7, 'YASHASWINI GAUR': 1, 'SAFREEN AFSAL': 0}, 'Vice_Head_Boy': {'SOYAM KUMAR S': 3, 'PRATHAM RAWAL': 4, 'NIKSHEEP GRAMPUROHIT': 1}, 'Vice_Head_Girl': {'PRAGYA MISHRA': 3, 'SMRITI PREM': 3, 'MAHIKA SURI': 2}}
        enc_data = Encryption().encrypt(str(data))
        with open("Votes_encrypted.txt",'w') as file:
            raw_data = file.write(enc_data)
        print("Succesfully Reformated ")
    else:
        print("Access Denied")
else:
    print("Access Denied")
        
    


    
