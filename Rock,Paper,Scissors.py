import random

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

user_choice = int(input("Enter your choice:\n0-Rock\n1-Paper\n2-Scissors\n"))

computer_choice = random.randint(0,2)

#BRUTE FORCE APPROACH
'''
if user_choice == 0:
  print(rock)
  if computer_choice == 0:
    print(f"\n\n{rock}\n\n")
    print("Draw")
  elif computer_choice == 1:
    print(f"\n\n{paper}\n\n")
    print("Computer Wins")
  elif computer_choice == 2:
    print(f"\n\n{scissors}\n\n")
    print("You Win")
elif user_choice == 1:
  print(paper)
  if computer_choice == 0:
    print(f"\n\n{rock}\n\n")
    print("You Win")
  elif computer_choice == 1:
    print(f"\n\n{paper}\n\n")
    print("Draw")
  elif computer_choice == 2:
    print(f"\n\n{scissors}\n\n")
    print("Computer Wins")
elif user_choice == 2:
  print(scissors)
  if computer_choice == 0:
    print(f"\n\n{rock}\n\n")
    print("Computer Wins")
  elif computer_choice == 1:
    print(f"\n\n{paper}\n\n")
    print("You Win")
  elif computer_choice == 2:
    print(f"\n\n{scissors}\n\n")
    print("Draw")
'''

# We can also code this differently without so many if statements
Options = [rock, paper, scissors]
print(f"\n{Options[user_choice]}\n{Options[computer_choice]}\n")
if user_choice-computer_choice == 1:
    print("You win")
elif user_choice-computer_choice == -1:
    print("Computer wins")
elif computer_choice == user_choice:
    print("Draw")
elif computer_choice > user_choice:
    print("You win")
elif computer_choice < user_choice:
    print("Computer wins")
