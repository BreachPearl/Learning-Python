# 1st input: enter height in meters e.g: 1.65
height = input()
# 2nd input: enter weight in kilograms e.g: 72
weight = input()

float_height=float(height)
int_weight=int(weight)
BMI=(int_weight/(float_height*float_height))
print(int(BMI))