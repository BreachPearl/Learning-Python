# 1st input: enter height in meters e.g: 1.65
height = input()
# 2nd input: enter weight in kilograms e.g: 72
weight = input()

float_height=float(height)
int_weight=int(weight)
BMI=(int_weight/(float_height*float_height))

if BMI<18.5:
    print(f"Your BMI is {BMI}, you are underweight.")
elif BMI<25:
    print(f"Your BMI is {BMI}, you have a normal weight.")
elif BMI<30:
    print(f"Your BMI is {BMI}, you are slightly overweight.")
elif BMI<35:
    print(f"Your BMI is {BMI}, you are obese.")
else:
    print(f"Your BMI is {BMI}, you are clinically obese.")
