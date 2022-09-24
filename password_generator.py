import string
from random import randint, shuffle
l1= list(string.ascii_lowercase)
l2=list(string.ascii_uppercase)
l3=list(string.digits)
l4=list(string.punctuation)
while True:
    password =[]
    def pass_len():
        while True:
            len_=int(input('Enter lenth of your password 6-12 : '))
            if len_ in range (6,13):
                return len_
            else : 
                print('INVALID LENTH try again !!')
    lent=pass_len()
    pl=round(lent*0.3)
    pu=round(lent*0.3)
    pn=round(lent*0.2)
    pp=round(lent*0.2)
    shuffle(l1)
    shuffle(l2)
    shuffle(l3)
    shuffle(l4)
    for i in range (pl):
        password.extend(l1[i])
    for i in range (pu):
        password.append(l2[i])
    for i in range (pn):
        password.append(l3[i])
    for i in range (pp):
        password.append(l4[i])
    shuffle(password)
    password = ''.join(password)
    print('SIR YOUR STRONG PASSWORD IS : ',password)
    n=input('YOU WANT TO TRY AGIN ? (y/n) : ')
    if n == 'n':
        print('THANKS FOR USING MY TOOL (: (by karim bdk)')
        break
