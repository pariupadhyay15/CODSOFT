rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''
import random
print("1=ROCK \n2=PAPER \n3"
      "=SCISSORS")
game=[rock,paper,scissors]
computer=random.randint(1,3)
human=int(input("Choose "))

# print(f"computer chose {computer}")
if computer==1 and human==1:
    print("computer chose ROCK")
    print("you chose ROCK")
    print("Its a DRAW")
elif computer==1 and human ==2:
    print("computer chose ROCK")
    print("you chose PAPER")
    print("You WIN")
elif computer==1 and human ==3:
    print("computer chose ROCK")
    print("you chose SCISSORS")
    print("You LOSE")
elif computer==2 and human ==1:
    print("computer chose PAPER")
    print("you chose ROCK")
    print("You LOSE")
elif computer==2 and human ==2:
    print("computer chose PAPER")
    print("you chose PAPER")
    print("Its a DRAW")
elif computer==2 and human ==3:
    print("computer chose PAPER")
    print("you chose SCISSORS")
    print("You WIN")
elif computer==3 and human ==1:
    print("computer chose SCISSORS")
    print("you chose ROCK")
    print("You WIN")
elif computer==3 and human ==2:
    print("computer chose SCISSORS")
    print("you chose PAPER")
    print("You LOOSE")
elif computer==3 and human ==3:
    print("computer chose SCISSORS")
    print("you chose SCISSORS")
    print("Its a DRAW")
else:
    print("WRONG CHOICE")
