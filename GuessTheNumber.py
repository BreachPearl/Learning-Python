import random
print(''' 
    ___                       _____ _                __                 _               
  / _ \_   _  ___  ___ ___  /__   \ |__   ___    /\ \ \_   _ _ __ ___ | |__   ___ _ __ 
 / /_\/ | | |/ _ \/ __/ __|   / /\/ '_ \ / _ \  /  \/ / | | | '_ ` _ \| '_ \ / _ \ '__|
/ /_\\| |_| |  __/\__ \__ \  / /  | | | |  __/ / /\  /| |_| | | | | | | |_) |  __/ |   
\____/ \__,_|\___||___/___/  \/   |_| |_|\___| \_\ \/  \__,_|_| |_| |_|_.__/ \___|_|   
                                                                                       ''')
print("welcome to guess the number game:")
print("you got to guess a number between 1 and 100")
difficulty=input("choose the difficulty: HARD or EASY: ").lower()
number=random.randint(1,100)
def guess_num(no_of_lives):
    user_input=int(input("Guess the number: "))
    while no_of_lives>1:
        if user_input>number:
            no_of_lives=no_of_lives-1
            print(f"too high \n guess again \n you have {no_of_lives} lives left")
            user_input=int(input("Guess the number: "))
        elif user_input<number:
            no_of_lives=no_of_lives-1
            print(f"too low \n guess again \n you have {no_of_lives} lives left")
            user_input=int(input("Guess the number: "))
        else:
           print(f"You have won! Congrats! The number is {number}")
           break
    print("You lose. The number was", number)
    
if difficulty=="hard":
    print("you have 5 attempts to guess the number")
    lives=5
    guess_num(lives)
elif difficulty=="easy":
    print("you have 5 attempts to guess the number")
    lives=10
    guess_num(lives)
else:
    print("Invalid difficulty choice. Please choose HARD or EASY.")