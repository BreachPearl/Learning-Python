import random
print('''
  __ _  __ _ _ __ ___   ___  ___ 
 / _` |/ _` | '_ ` _ \ / _ \/ __|
| (_| | (_| | | | | | |  __/\__ \
 \__, |\__,_|_| |_| |_|\___||___/
  __/ |                          
 |___/  
''')
print("Welcome to the Rock Paper Scissors game!")
print("What do you choose? Type 0 for ROCK,1 for PAPER or 2 for SCISSORS")
Choice=int(input())
x=random.randint(0,2)
if Choice==0:
    print("your choice is Rock")
    print('''
            _______
        ---'   ____)
            (_____)
            (_____)
            (____)
        ---.__(___)
          ''')
    if x==0:
        print("computer choose rock")
        print('''
            _______
        ---'   ____)
            (_____)
            (_____)
            (____)
        ---.__(___)
                ''')
        print("Draw")
    if x==1:
        print("computer choose paper")
        print("""
            _______
        ---'    ____)
                ______)
                _______)
                _______)
        ---.__________)
            """)
        print("you lose")
    if x==2:
        print("computer choose Scissors")
        print("""
            _______
        ---'   ____)____
                    ______)
                __________)
            (____)
        ---.__(___)
            """)
        print("you win")
if Choice==1:
    print("your choice is paper")
    print("""
            _______
        ---'    ____)
                ______)
                _______)
                _______)
        ---.__________)
            """)
    if x==0:
        print("computer choose rock")
        print('''
            _______
        ---'   ____)
            (_____)
            (_____)
            (____)
        ---.__(___)
                ''')
        print("you win")
    if x==1:
        print("computer choose paper")
        print("""
            _______
        ---'    ____)
                ______)
                _______)
                _______)
        ---.__________)
            """)
        print("Draw")
    if x==2:
        print("computer choose Scissors")
        print("""
            _______
        ---'   ____)____
                    ______)
                __________)
            (____)
        ---.__(___)
            """)
        print("Computer wins")
if Choice==2:
    print("your choice is scissors")
    print("""
            _______
        ---'   ____)____
                  ______)
                __________)
            (____)
        ---.__(___)
            """)
    if x==0:
        print("computer choose rock")
        print('''
            _______
        ---'   ____)
            (_____)
            (_____)
            (____)
        ---.__(___)
                ''')
        print("Computer Wins")
    if x==1:
        print("computer choose paper")
        print("""
            _______
        ---'    ____)
                ______)
                _______)
                _______)
        ---.__________)
            """)
        print("You win")
    if x==2:
        print("computer choose Scissors")
        print("""
            _______
        ---'   ____)____
                    ______)
                __________)
            (____)
        ---.__(___)
            """)
        print("Draw")
if Choice<0 or Choice>2:
    print("invalid") 