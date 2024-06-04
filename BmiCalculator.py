# 1st input: enter height in meters e.g: 1.65
height = input()
# 2nd input: enter weight in kilograms e.g: 72
weight = input()

float_height=float(height)
int_weight=int(weight)
BMI=(int_weight/(float_height*float_height))
print(round(BMI))

#another way to round number is 8//3  using 2 slahes which will round it to the whole number 

#example for fstring in python
#what f string does is it can add values in between the string
print(f"your BMI is {round(BMI)}")