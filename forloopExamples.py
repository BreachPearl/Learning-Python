#calucalting the average height in the given list of heights 
student_heights=[180, 124, 165, 173, 189, 169, 146]
totalheight=0
for i in student_heights:
  totalheight=totalheight+i
numstu=len(student_heights)
average_height=round(totalheight/numstu)
print(f"total height = {totalheight}\nnumber of students = {numstu}\naverage height = {average_height}")

# --------------------------------------------------------------------------------------------------------

#highest number in the given set of list
student_scores=[78, 65, 89, 86, 55, 91, 64, 89]
greatest_number=student_scores[0]
for i in range(0,len(student_scores)-1):
  if greatest_number<student_scores[i+1]:
    greatest_number=student_scores[i+1]
print(f"The highest score in the class is: {greatest_number}")

# ---------------------------------------------------------------------------------------------------------

#Sum of Even Numbers
target = int(input("Enter a number between 0 and 1000\n")) # 

sum=0;
for i in range(0,target+1,2):     # here 2 is the no.of skips you wanna take while running through the loop
  sum+=i;
print(sum)
#-----------------------------------------------------------------------------------------------------------

# You are going to write a program that automatically prints the solution to the FizzBuzz game. These are the rules of the FizzBuzz game:

# Your program should print each number from 1 to 100 in turn and include number 100.

# When the number is divisible by 3 then instead of printing the number it should print "Fizz".

# When the number is divisible by 5, then instead of printing the number it should print "Buzz".`

# And if the number is divisible by both 3 and 5 e.g. 15 then instead of the number it should print "FizzBuzz"

for i in range(1,101):
  if i%3==0 and i%5==0:
    print("FizzBuzz")
  elif i%3==0:
    print("Fizz")
  elif i%5==0:
    print("Buzz")
  else:
    print(i)