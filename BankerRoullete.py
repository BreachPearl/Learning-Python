# Instructions
# You are going to write a program that will select a random name from a list of names. The person selected will have to pay for everybody's food bill.

# Important: You are not allowed to use the choice() function.

# NOTE: In this exercise, you are working collaboratively with another programmer. They already dealt with input() and writing the code needed to get hold of the names in the input area, so you don't need to worry about that.

# The other programmer has written the code to separate the names in the input area into individual names and puts them inside a List called names. For their code to work correctly, you must enter all the names in the input area followed by comma then space. e.g. name, name, name

# You can try printing names to see what it looks like (but remember to remove that code when you submit the assignment).

# Assume that names works like this:

# input area: x, y, z, 
# names = ["x", "y", "z"]
# Example Input
# Angela, Ben, Jenny, Michael, Chloe
# Note: notice that there is a space between the comma and the next name.

# Example Output
# Michael is going to buy the meal today!

# Solution:
import random
names=["Angela", "Ben", "Jenny", "Michael", "Chloe"]
length_names=len(names)
x=random.randint(0,length_names-1)
print(names[x]+" is going to buy the meal today!")