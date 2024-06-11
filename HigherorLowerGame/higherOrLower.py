from asciitext import logo
from asciitext import vs
from gamedata import data
import random
print(logo)
score=0
def random_data():
    global A
    A=random.choice(data)
    global B
    B=random.choice(data)
    while A == B:  # to amke sure A and B are not the same
        B = random.choice(data)
    print(f"Compare A: {A['name']}, a {A['description']}, from {A['country']}")
    print(vs)
    print(f"Compare B: {B['name']}, a {B['description']}, from {B['country']}")
def Compare():
    global score
    random_data()
    user_choice=input("Who has more Followers? Type 'A' or 'B': ").upper()
    if A['follower_count']>B['follower_count'] and user_choice=="A":
        score+=1
        print(f"Correct Answer your score is {score} ! keep playing!")
        Compare()
    elif A['follower_count']>B['follower_count'] and user_choice=="B":
        print("Sorry thats wrong Final Score is" , score)
    elif A['follower_count']<B['follower_count'] and user_choice=="B":
        score+=1
        print(f"Correct Answer your score is {score} ! keep playing!")
        Compare()
    elif A['follower_count']<B['follower_count'] and user_choice=="A":
        print("Sorry thats wrong Final Score is" , score)
    else:
        print("wrong input either enter 'A' or 'B' ")
Compare()



