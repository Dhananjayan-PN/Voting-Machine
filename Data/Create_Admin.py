class Encryption:
    def __init__(self):
        with open('Data/Key.txt', 'r') as file:
            self.encrypt_key = file.read()

    def encrypt(self, data=''):
        key = self.encrypt_key*(len(str(data))//64 + 1)
        encrypted = ''
        for i in range(len(data)):
            char_id = str(ord(data[i]) + ord(key[i]))
            char_val = '0'*(3-len(str(char_id))) + char_id
            encrypted += char_val
        return encrypted

    def decrypt(self, data=''):
        key = self.encrypt_key*(len(data)//64 + 1)
        decrypted = ''
        ctr = 0
        for i in range(0, len(data)//3):
            char_id = int(data[ctr:ctr+3])
            decrypted += chr(char_id - ord(key[i]))
            ctr += 3
        return decrypted

users = {'Sam': 'Password123', 'Djay': 'Password456'}
file = open('Admins.txt', 'r+')
raw_data = str(users)
encrypted_data = Encryption().encrypt(raw_data)
file.write(encrypted_data)
file.close()
