import random

Upper_Alphabets=['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
#upperAlpha=[chr(i) for i in range(ord('A'),ord('Z')+1)]
Lower_Alphabets=['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
#lowerAlpha=[chr(i) for i in range(ord('a'),ord('z')+1)]

'''
    CPU times: total: 0 ns
    Wall time: 0 ns

    CPU times: total: 0 ns
    Wall time: 2.17 ms
'''
numbers=[0,1,2,3,4,5,6,7,8,9]
#num=list(range(0,10))

'''
    CPU times: total: 0 ns
    Wall time: 0 ms

    CPU times: total: 0 ns
    Wall time: 0 ns
'''

#SpecialChar=['!', '"', '#', '$', '%', '&', "'", '(', ')', '*', '+', ',', '-', '.', '/', ':', ';', '<', '=', '>', '?', '@', '[', '\\', ']', '^', '_', '{', '|', '}']
SpecialChar=[chr(i) for i in range(33,48)]+[chr(i) for i in range(58,65)]+[chr(i) for i in range(91,96)]+[chr(i) for i in range(123,126)]

'''
    CPU times: total: 0 ns
    Wall time: 3.51 ms

    CPU times: total: 0 ns
    Wall time: 0 ns
'''
def defaultpassword():
    #This password will return any random password
    passwordlist=[Upper_Alphabets,Lower_Alphabets,SpecialChar,numbers]
    password=[]
    for j in passwordlist:
        x=random.randint(1,5)
        for k in range(x):
            password.append(str(random.choice(j)))

    random.shuffle(password)
    finalpassword="".join(password)
    return finalpassword

def customizedpassword():
    password=[]
    num=int(input("Enter the number of Numbers you want in your passord :"))
    sp_char=int(input("Enter the number of special characters you want in your password :"))
    up_alpha=int(input("Enter the number of capital letters you want in your password :"))
    low_alpha=int(input("Enter the number of small letter alphabets you want in your password :"))
    for i in range(num):
        temp=random.randint(0,9)
        password.append(str(temp))
    for i in range(sp_char):
        temp=random.choice(SpecialChar)
        password.append(temp)
    for i in range(up_alpha):
        temp=random.choice(Upper_Alphabets)
        password.append(temp)
    for i in range(low_alpha):
        temp=random.choice(Lower_Alphabets)
        password.append(temp)
    
    random.shuffle(password)
    finalpassword="".join(password)
    return finalpassword
def user():
    print("""
        1. Default
        2. Customize
        """)
    try:    
        a=int(input("Enter your choice :"))
        if a==1:
            b=defaultpassword()
            print(b)
        elif a==2:
            b=customizedpassword()
            print(b)
        else:
            print("Invalid Input","\n","``Kindly choose valid Input``")
            user()
    except ValueError:
        print("Invalid Input","\n","``Kindly choose valid Input``")
        user()
user()