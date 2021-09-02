import os
import random
import string
import time


linesep =  "\n"
symbols = ['!', '#', '$', '%', '&' ,'(', ')', '*', '+', ',', '-', '.', '/', ':', ';', '<', '=', '>', '?', '@', '[',]


file_name= 'datafile.txt'
def dencode():
    character_list = f';GFs+yP5kI/,A9Y&bVe8<hRnMzZ0=E.X!D$ 4lN(afWi6HK"r:)#pT%vCtogJq?SxL3*B>md-O1QU7jw[2cu@{linesep}'    
    with open(file_name, 'r+') as f:
        olddata = f.read()
        unencoded_data = ''
        for i in olddata:
            pos = character_list.find(i)
            unencoded_data += character_list[(pos -12) % len(character_list)]
        f.seek(0)
        f.write(unencoded_data)
        f.close()
        

def encode():
    character_list = f';GFs+yP5kI/,A9Y&bVe8<hRnMzZ0=E.X!D$ 4lN(afWi6HK"r:)#pT%vCtogJq?SxL3*B>md-O1QU7jw[2cu@{linesep}'    
    with open(file_name, 'r+') as f:
        data = f.read()
        encoded_data = ''
        for i in data:
            pos = character_list.find(i)
            encoded_data += character_list[(pos + 12) % len(character_list)]
        f.seek(0)
        f.write(encoded_data)
        f.close()
        time.sleep(1)
        print("bye, thank you for using my tool")
        time.sleep(3)
safeguard = input(f'please enter the program password {linesep}')
if safeguard != 'start':
    quit()
    
dencode()


while True:
    comm = input(f'write "new" to make a new password, "edit" to add your own password, "read" to list your passwords, or "quit" to close the program {linesep} (this also saves any passwords you have made) {linesep} DO NOT EXIT HITING THE X IN THE CORNER OF THE APP{linesep} {linesep}')
    commnew = "new"
    commread = "read"   
    commquit = 'quit'
    commedit = 'edit'
    if comm == commnew:
        num = random.randint(1000, 9999)
        lett1=random.choice(string.ascii_letters)
        lett2=random.choice(string.ascii_letters)
        lett3=random.choice(string.ascii_letters)
        lett4=random.choice(string.ascii_letters)
        lett5=random.choice(string.ascii_letters)
        lett6=random.choice(string.ascii_letters)
        caplett=random.choice(string.ascii_uppercase)
        unqlett=random.choice(symbols)
        lowlett=random.choice(string.ascii_lowercase)
        passw = lett1 + lett2 + lett3 + lett4 + lett5 + lett6 + str(num) + caplett + unqlett + lowlett
        f = open("datafile.txt", "a")
        passname= input("What is password for? " )
        f.write(linesep)
        f.write(passname + ": " + str(passw))
        print("password is: " + passw + linesep +linesep)
        f.close()
    elif comm == commread:
        f = open("datafile.txt", "r")
        print(linesep + f.read() + linesep +linesep +linesep)
        f.close()
    elif comm == commquit:
        encode()
        exit() 
    elif comm == commedit:
        f = open('datafile.txt', 'a')
        editname = input('What is the password for?')
        editword = input('What is the password?')
        f.write(linesep)
        f.write(editname + ": " + editword)
        f.close()
    else: 
        print("command not recognized")   
    

# In[ ]:
