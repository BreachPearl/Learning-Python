name1 = input() # What is your name?
name2 = input() # What is their name?
Combined_name=name1+name2
name_lowercase=Combined_name.lower()
t=name_lowercase.count("t")      #string.count("the letter you want ")    what it does is it counts the specified letter occurances in that string
r=name_lowercase.count("r")
u=name_lowercase.count("u")
e=name_lowercase.count("e")
firstdigit=t+r+u+e
l=name_lowercase.count("l")      #string.count("the letter you want ")    what it does is it counts the specified letter occurances in that string
o=name_lowercase.count("o")
v=name_lowercase.count("v")
e=name_lowercase.count("e")
seconddigit=l+o+v+e
finalscore=str(firstdigit)+str(seconddigit)
score=int(finalscore)
if score<10 or score>90:
  print(f"Your score is {score}, you go together like coke and mentos.")
elif score>40 and score<50:
  print(f"Your score is {score}, you are alright together.")
else:
  print(f"Your score is {score}.")


