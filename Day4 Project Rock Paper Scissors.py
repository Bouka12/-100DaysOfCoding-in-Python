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

#Write your code below this line 👇
import random
art=[rock, paper, scissors]
user=int( input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors \n"))

computer_choice=random.randint(0,3)
if user>3 or user<0:
  print(" You typed an invalid number. Try again!")
elif user==0 :
  print(rock)
  if computer_choice==1:
    print(f"Computer choice \n {art[computer_choice]}")
    print("You loose")
  elif computer_choice == 2:
    print(f"Computer choice \n {art[computer_choice]}")
    print("You win!")
  else: 
    print('replay')
  
elif user==1:
  print(paper)
  if computer_choice==2:
    print(f"Computer choice \n {art[computer_choice]}")
    print("You loose")
  elif computer_choice==0:
    print(f"Computer choice \n {art[computer_choice]}")
    print("You win!")
  else: 
    print('replay')
else:
  print(scissors)
  if computer_choice==0:
    print(f"Computer choice \n {art[computer_choice]}")
    print("You loose")
  elif computer_choice==1:
    print(f"Computer choice \n {art[computer_choice]}")
    print("You win!")
  else: 
    print('It \'s a draw')
