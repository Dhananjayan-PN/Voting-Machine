from tkinter import *
import time
import datetime

class Encryption:
    def __init__(self):
        with open('Data/Key.txt', 'r') as file:
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


class Voting:
    def __init__(self):
        self.ref_time = time.time()
        self.encryption_manager = Encryption()
        self.logo = ''
        self.window = None
        self.voteframe = None
        self.categories = [ 'Head_Boy', 'Head_Girl', 'Vice_Head_Boy', 'Vice_Head_Girl']
        self.Vice_Head_Boy = ['A1', 'A2', 'A3']
        self.Vice_Head_Girl = ['B1', 'B2', 'B3']
        self.Head_Boy = ['C1', 'C2', 'C3']
        self.Head_Girl = ['D1', 'D2', 'D3']
        self.votes = []

    def create_instance(self, Session):
        self.session = Session

    def start(self):
        self.image = {}
        self.window = Tk()
        self.window.title('DPSE 2019 Elections')
        icon = 'Data/Pics/DPSE.ico'
        self.window.iconbitmap(icon)
        self.window.configure(bg='white')
        self.window.bind('e', lambda event: self.settings())
        self.window.bind('n', lambda event: self.restart())
        self.voteframe = Frame(self.window, bg='light cyan')
        self.voteframe.pack(expand='yes', fill=BOTH)
        for cat in self.categories:
            self.image[cat] = {}
            for candidate in eval('self.' + cat):
                self.image[cat][candidate] = PhotoImage(file='Data/Pics/{}.png'.format(candidate))
        self.logo = PhotoImage(file='Data/Pics/Logo.png')
        self.thanks = PhotoImage(file='Data/Pics/Thanks.png')
        sub_ctr = 0
        self.switch_window(sub_ctr)
        self.window.geometry('1366x760+0+0')
        self.window.attributes("-fullscreen", True)
        self.window.mainloop()

    def restart(self):
        self.voteframe.destroy()
        self.voteframe = Frame(self.window, bg='light cyan')
        self.voteframe.pack(expand='yes', fill=BOTH)
        sub_ctr = 0
        self.switch_window(sub_ctr)
        

    def switch_window(self, sub_ctr):
        if sub_ctr == 0:
            self.votes=[]
        else:
            pass
        cat = self.categories[sub_ctr]
        can_list = eval('self.'+cat)
        hed = Label(self.voteframe, text = "DELHI PUBLIC SCHOOL BANGALORE - EAST", font = ('Helvetica', 40, 'bold'),width = 37, height=1, bg='light cyan', fg='SpringGreen4')
        hed.grid(row=0, column=1, padx=1, pady=1, columnspan=3)
        ttl = Label(self.voteframe, text = "SCHOOL COUNCIL ELECTIONS 2019-20", font = ('Helvetica', 35, 'bold'),width = 37, height=1, bg='light cyan', fg='SpringGreen4' )
        ttl.grid(row=1, column=1, padx=1, pady=1, columnspan=3)
        lbl = Label(self.voteframe, text=cat.replace('_', ' ').upper(), font=('Helvetica', 50, 'bold'), width=15, height=1, bg='light cyan', fg='SpringGreen4')
        lbl.grid(row=2, column=1, padx=1, pady=30, columnspan=3)
        lbl = Label(self.voteframe, image=self.logo, width=115, height=140, relief='flat', bd=0, bg='white')
        lbl.grid(row=0, column=0, padx=1, pady=1)
        fn = ('Helvetica', 18, 'bold')
        for i in range(len(can_list)):
            name = can_list[i]
            img = self.image[cat][name]
            lbl = Label(self.voteframe, image=img, bd=1, width=190, height=210)
            lbl.grid(row=3, column=i+1, padx=10, pady=5)
            btn = Button(self.voteframe, text=name, font=fn, width=21, height=1, bd=3, relief='raised')
            func = lambda event, category=cat, cand=name, _ctr=sub_ctr: self.vote(event, category, cand, _ctr)
            btn.bind('<Button-1>', func)
            btn.configure(bg='LightBlue2')
            btn.grid(row=4, column=i+1, pady=4, padx=40, columnspan=1)
        self.window.update()

    def settings(self):
        self.user = Admin(self.session)

    def vote(self, event, category, candidate, sub_ctr):
        self.votes.append((category,candidate))
        if sub_ctr < 3:
            sub_ctr += 1
            self.switch_window(sub_ctr)
        else:
            self.voteframe.destroy()
            self.voteframe = Frame(self.window, bg='light cyan')
            self.voteframe.pack(expand='yes', fill=BOTH)
            lbl = Label(self.voteframe,text="CONFIRM YOUR CHOICES", font=('Helvetica', 35, 'bold'),width = 25, height=1, bg='light cyan', fg='SpringGreen4')
            lbl.grid(row=0, column=1, padx=1, pady=10, columnspan=6)
            lbl = Label(self.voteframe, image=self.logo, width=115, height=140, relief='flat', bd=0, bg='white')
            lbl.grid(row=0, column=0, padx=1, pady=1)
            for i in range(4):
                if i<2:
                    category,candidate = self.votes[i]
                    lbl = Label(self.voteframe,text=candidate+" as "+category.replace("_"," ").upper(), font=('Helvetica', 15, 'bold'), width = 30, height=1, bg='light cyan', fg='SpringGreen4')
                    lbl.grid(row=i+1, column=1, padx=1,pady=1,columnspan=2)
                    img = self.image[category][candidate]
                    lbl = Label(self.voteframe, image=img, bd=1, width=190, height=210)
                    lbl.grid(row=i+1, column=3, padx=1, pady=10)
                elif i>=2:
                    category,candidate = self.votes[i]
                    lbl = Label(self.voteframe,text=candidate+" as "+category.replace("_"," ").upper(), font=('Helvetica', 15, 'bold'), width = 37, height=1, bg='light cyan', fg='SpringGreen4')
                    lbl.grid(row=i-1, column=4, padx=1,pady=1,columnspan=2)
                    img = self.image[category][candidate]
                    lbl = Label(self.voteframe, image=img, bd=1, width=190, height=210)
                    lbl.grid(row=i-1, column=6, padx=1, pady=10)
            btn = Button(self.voteframe, text="CONFIRM", font=('Helvetica', 10, 'bold'), width=12, height=1, bd=3, relief='raised')
            func = lambda event: self.confirm()
            btn.bind('<Button-1>', func)
            btn.configure(bg='LightBlue2')
            btn.grid(row=5, column=3, pady=20, padx=1, columnspan=1)            
            btn = Button(self.voteframe, text="REVOTE", font=('Helvetica', 10, 'bold'), width=12, height=1, bd=3, relief='raised')
            func = lambda event: self.revote()
            btn.bind('<Button-1>', func)
            btn.configure(bg='LightBlue2')
            btn.grid(row=5, column=4, pady=4, padx=4, columnspan=1)
            
    def confirm(self):
        file1 = open('Data/Votes.txt','r')
        votes = file1.read()
        file1.close()
        if votes=='':
            votes=0
        else:
            votes=int(self.encryption_manager.decrypt(votes))
        votes+=1
        file1=open('Data/Votes.txt','w')
        file1.write(str(self.encryption_manager.encrypt(str(votes))))
        file1.close()
        file2 = open('Data/Votes_encrypted.txt', 'r+')
        raw_data = file2.read()
        file2.close()
        decrypted_data = self.encryption_manager.decrypt(raw_data)
        data = eval(decrypted_data)
        for category,candidate in self.votes:
            data[category][candidate] += 1          
        self.voteframe.destroy()
        self.voteframe = Frame(self.window, bg='light cyan')
        self.voteframe.pack(expand='yes', fill=BOTH)
        lbl = Label(self.voteframe, image=self.thanks, bg='light cyan')
        lbl.pack(expand='yes', fill=BOTH)
        self.save(str(data))
        if time.time() > self.ref_time+420:
            self.ref_time = time.time()
            self.tmp()
        self.window.update()

    def tmp(self):
        print('_________')
        with open('Data\Votes_Encrypted.txt', 'r') as file:
            data = file.read()
        file_name = 'Data\Backup_{}.txt'.format((str(datetime.datetime.now().time()).split('.')[0]).replace(':', '_'))
        file = open(file_name, 'w')
        file.write(data)
        file.close()
        
    def revote(self):
        self.voteframe.destroy()
        self.voteframe = Frame(self.window, bg='light cyan')
        self.voteframe.pack(expand='yes', fill=BOTH)
        sub_ctr = 0
        self.switch_window(sub_ctr)
        
    def reset(self,frame):
        file1=open("Data/Votes.txt",'w')
        file1.write(self.encryption_manager.encrypt('0'))
        file1.close()
        file = open('Data/Votes_encrypted.txt', 'r+')
        raw_data = file.read()
        file.close()
        decrypted_data = self.encryption_manager.decrypt(raw_data)
        data = eval(decrypted_data)
        for category in self.categories:
            for candidate in eval('self.'+category):
                data[category][candidate]=0
        self.save(str(data))
        frame.quit()
        
    def save(self, raw_data=''):
        encrypted_data = self.encryption_manager.encrypt(raw_data)
        file = open('Data/Votes_encrypted.txt', 'w')
        file.write(encrypted_data)
        file.close()
        

class Admin:
    def __init__(self, session):
        self.logged_in = False
        self.session = session
        self.categories = ['Head_Boy', 'Head_Girl', 'Vice_Head_Boy', 'Vice_Head_Girl']
        self.raw_results = ''
        self.encryption_manager = Encryption()
        self.login_screen()
        
    def check(self):
        username = self.username.get().capitalize()
        password = self.password.get()
        self.login(username, password)
        if self.logged_in:
            self.enclosure.destroy()
            self.enclosure = Frame(self.popup, width=30)
            self.enclosure.grid(row=0, column=0)
            self.show_results()

    def login_screen(self):
        self.popup = Tk()
        self.popup.geometry('420x200+483+270')
        self.popup.title('Login')
        #icon = '{}/Data/Pics/DPSE.ico'.format(os.getcwd())
        self.popup.iconbitmap("Data/Pics/DPSE.ico")
        fn = ('Helvetica', 30, 'bold')
        self.enclosure = Frame(self.popup, width=600, bg='white')
        self.enclosure.pack(expand='yes', fill=BOTH)
        self.username = Entry(self.enclosure, font=fn, width=18, bd=3, bg='white', relief='ridge')
        self.username.grid(row=0, column=0, pady=5, padx=8)
        self.password = Entry(self.enclosure, font=fn, width=18, bd=3, bg='white', show='*', relief='ridge')
        self.password.grid(row=1, column=0, pady=5, padx=8)
        fn = ('Helvetica', 20, 'bold')
        btn = Button(self.enclosure, text='Login', command=self.check, font=fn, width=18, bg='white', bd=2)
        btn.grid(row=2, column=0, pady=4)
        self.popup.update()

    def login(self, username, password):
        with open('Data/Admins.txt') as file:
            raw_data = file.readlines()
            logins = {}
            for line in raw_data:
                login_ids = eval(Encryption().decrypt(line))
                logins.update(login_ids)
        if username in logins.keys():
            if password == logins[username]:
                self.get_results()
                self.logged_in = True

    def get_by_rank(self, data):
        data = list(data)
        scores = []
        for i in data:
            scores.append(i[1])
        ctr_final = 0
        resulted = []
        while ctr_final < len(data):
            mx = max(scores)
            ind = scores.index(mx)
            resulted.append(data[ind])
            scores[ind] = -1
            ctr_final += 1
        return resulted
 
    def show_results(self):
        self.popup.geometry('970x280+200+165')
        rw = 0
        cl = 0
        grid = 0
        if self.logged_in:
            self.popup.title('Election Results')
            self.enclosure.configure(bg='light cyan')
            self.session.window.destroy()
            self.page_no = 0
            self.popup.bind('<Left>', lambda event, act=-1: self.scroll(event, act))
            self.popup.bind('<Right>', lambda event, act=1: self.scroll(event, act))
            self.screen_scroll()

    def scroll(self, event, act):
        if act==-1 and self.page_no>0:
            self.page_no -= 1
        elif act==1 and self.page_no<3:
            self.page_no += 1
        else:
            pass
        self.screen_scroll()

    def screen_scroll(self):
        page_no = self.page_no
        heading = ('Helvetica', 35, 'bold')
        regular = ('Helvetica', 23)
        rw = 0
        cl = 0
        if self.logged_in:
            self.enclosure.destroy()
            self.enclosure = Frame(self.popup, width=600, bg='light cyan')
            self.enclosure.pack(expand='yes', fill=BOTH)
            raw_results = eval(self.encryption_manager.decrypt(self.raw_data))
            category = self.categories[page_no]
            btn = Button(self.enclosure, text="RESET VOTES", font=('Helvetica', 10, 'bold'), width=12, height=1, bd=4, relief='raised')
            func = lambda event: Voting().reset(self.enclosure)
            btn.bind('<Button-1>', func)
            btn.configure(bg='LightBlue2')
            btn.grid(row=0, column=0, pady=1, padx=1, columnspan=1)
            votes=self.get_votes()
            vote_num_txt = "Votes : " + str(votes)
            lbl1=Label(self.enclosure, text=vote_num_txt, font=('Helvetica', 17, 'bold'), width=10, bg='light cyan', fg='SpringGreen4')
            lbl1.grid(row=1, column=0, pady=1, padx=2,columnspan=1)
            txt = category.replace('_', ' ').upper()
            lbl = Label(self.enclosure, text=txt, font=heading, width=20, bg='light cyan', fg='SpringGreen4')
            lbl.grid(row=rw, column=cl+1, pady=1, padx=2,columnspan=2)
            rw += 1
            raw_data = list(raw_results[category].items())
            final_data = self.get_by_rank(raw_data)
            for each in final_data:
                txt = '{} got {} votes'.format(each[0], each[1])
                lbl = Label(self.enclosure, text=txt, font=regular, width=45, bg='light cyan', fg='SpringGreen4')
                lbl.grid(row=rw, column=cl+1, padx=2, pady=10,columnspan=2)
                rw += 1
            self.popup.update()
            
    def get_votes(self):
        file = open("Data/Votes.txt","r")
        votes=self.encryption_manager.decrypt(file.read())
        file.close()
        return votes

    def get_results(self):
        file = open('Data/Votes_encrypted.txt', 'r')
        self.raw_data = file.read()
        file.close()

    def logout(self):
        if self.logged_in:
            self.logged_in = False
            self.popup.title('Login')

Session = Voting()
Session.create_instance(Session)
Session.start()
