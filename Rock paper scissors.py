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
#Taking player choice
choice = int(input('What do you chose? Type 0 for rock, Type 1 for paper, Type 2 for scissors: '))
print()
print('Your choice')
if choice == 0:
    print(rock)
elif choice == 1:
    print(paper)
else:
    print(scissors)

#selecting random choice for computer
print('The computer choose: ')
ai = random.randint(0,2)
if ai == 0:
    print(rock)
elif ai == 1:
    print(paper)
else:
    print(scissors)

#The game
if choice == ai:
    print('DRAW!!')
elif choice == 0 and ai == 1:
    print('YOU LOSE!!')
elif choice == 0 and ai == 2:
    print('YOU WIN!!')
elif choice == 1 and ai == 0:
    print('YOU WIN!!')
elif choice == 1 and ai == 2:
    print('YOU LOSE!!')
elif choice == 2 and ai == 0:
    print('YOU LOSE!!')
else:
    print('YOU WIN!!')

