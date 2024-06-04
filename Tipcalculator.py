print("Welcome to the tip Calculator")
bill=float(input("what was the total bill?"))
tip_percentage=float(input("what percentage do you wanna tip? 10, 12, or 15?"))
tip=(bill*tip_percentage)/100
split=float(input("how many people are spliting the bill?"))
splited_bill=round((bill+tip)/split,2)
print(f"each person should pay: {splited_bill}")