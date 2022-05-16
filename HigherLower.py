import random
import os
from game_data import data
from art import logo,vs
#Function clears the python console
def clearconsole():
    command = 'clear'
    if os.name in ('nt','dos'):
        command = 'cls'
    os.system(command)
def compare(a,b):
    if a > b:
        return 'A'
    elif a < b:
        return 'B'
    else: 
        return 'Equal'
#print logo
print(logo)
# Choose two data parts A and B and print them
Score = 0
A = random.choice(data)
game_on = True
while game_on:
    print(f"Compare A: {A['name']}, {A['description']}, {A['country']}.")
# print versus symbol
    print(vs)
    B = random.choice(data)
    print(f"Against B: {B['name']}, {B['description']}, {B['country']}.")
# Choose who has more followers
    Choice = input('Who has more followers: Type \'A\' or \'B\' ? ')
    Answer  = compare(A['follower_count'],B['follower_count'])
# Compare Choice and Answer to know if you won
    if Choice == Answer or Answer == 'Equal':
        Score = Score + 1
        A = B
        clearconsole()
        print(logo)
        print(f'You are right. Current Score is {Score}')
    else:
        clearconsole()
        print(logo)
        print(f'Sorry that\'s wrong.You scored: {Score}')
        game_on = False
    