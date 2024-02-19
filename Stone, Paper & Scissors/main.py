import random

paper='''
    _______
---'   ____)____
          ________)
          _________)
         _________)
---.__________)
'''

scissor='''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)

'''

stone='''
    _____
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)

'''
l1=[stone,paper,scissor]
p1,p2=0,0
print("Heyy! I am Pixxy")
name=input("What is your name? ")
def play(a,b):
    print("""1. Stone\n2. Paper\n3. Scissors\n4. Exit""")
    p1,p2=a,b
    try:
        player1=int(input("Enter your choice :"))
    except ValueError:
        print("Invalid Input, Try Again !")
        play(p1,p2)
    player2=random.choice(l1)
    #score
    if player1==1: #stone
        if player2==paper:
            p2+=1
        elif player2==scissor:
            p1+=1
    elif player1==2: #paper
        if player2==scissor:
            p2+=1
        elif player2==stone:
            p1+=1
    elif player1==3: #scissors
        if player2==stone:
            p2+=1
        elif player2==paper:
            p1+=1
    def display(p1,p2):
        if player1==1:
            print(stone, player2)
            print(name, " :", p1,"\n"+"pixxy :", p2)
            play(p1,p2)
        elif player1==2:
            print(paper, player2)
            print(name, " :", p1,"\n"+"pixxy :", p2)
            play(p1,p2)
        elif player1==3:
            print(scissor, player2)
            print(name, " :", p1,"\n"+"pixxy :", p2)
            play(p1,p2)
        else:
            print("Thank you for playing with me :)")
    display(p1,p2)
print("Nice to meet you {}!".format(name),'\n')
print("Let's Play Stone, Paper & Scissors !")
play(p1,p2)