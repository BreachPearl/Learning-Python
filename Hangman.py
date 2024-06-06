import random
print(''' 
  ___ ___                                              
 /   |   \_____    ____    ____   _____ _____    ____  
/    ~    \__  \  /    \  / ___\ /    / \__  \  /    \ 
\    Y    // __ \|   |  \/ /_/  >  Y Y  \/ __ \|   |  |
 \___|_  /(____  /___|  /\___  /|__|_|  (____  /___|  /
       \/      \/     \//_____/       \/     \/     \/ 
                                                       ''')
print("Welcome to hangman game")
Target_Words=["Celcius","Edition","hangman"]
stages = ['''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
      |
      |
      |
=========
''', '''
  +---+
  |   |
      |
      |
      |
      |
=========
''']
print("can you guess the 7 letter word before the stick man dies?")
word=(random.choice(Target_Words)).lower()
print(word)
emptylist=[]
for i in range(len(word)):
    emptylist.append('_') 
print(str(emptylist))
end_of_game=False
lives=6
while not end_of_game:                               #the way we used while loop is decalre a keyword called end of the game and making it false and once the condition is met we create a switch
    user_input=input("guess the word: ")             #and make it true so we can get out of the while loop 
    for i in range(len(word)):   #we are checking whether letter in present in the random word that got selected
        letter=word[i]
        if letter==user_input:           
            emptylist[i]=user_input    #if its equal we are replacing the blank
    if user_input not in emptylist:    #if it is not equal we reduce the lives
        lives=lives-1                  #once we lose all 6 lives we lose
        if lives==0:
            end_of_game=True
            print("You Lose")
    print(f"{''.join(emptylist)}")
    if "_" not in emptylist:           #kill switch for the while loop is to check if there are no more "_"
        end_of_game= True
        print("you win")
    print(stages[lives])



