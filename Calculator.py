def add(n1,n2):
    return n1+n2
def sub(n1,n2):
    return n1-n2
def mul(n1,n2):
    return n1*n2
def div(n1,n2):
    return n1/n2
operation={
    "+":add,
    "-":sub,
    "*":mul,
    "/":div
}
def Calculator():
    num1 = int(input("what is the first number?:"))
    for i in operation:
        print(i)
    should_con=True
    while should_con:
        operation_symbol=input("what operation do you wanna choose?")
        num2 = int(input("what is the next number?:"))
        calculation_function=operation[operation_symbol]
        answer=calculation_function(num1,num2) 
        print(f"{num1} {operation_symbol} {num2} = {answer}")

        if input(f"type 'y' for cointinuing calculating with {answer}:")=="y":
            num1=answer
            operation_symbol=input("what operation do you wanna choose?")
            num2 = int(input("what is the next number?:"))
            calculation_function=operation[operation_symbol]
            answer=calculation_function(num1,num2) 
            print(f"{num1} {operation_symbol} {num2} = {answer}")
        else:
            should_con=False
            Calculator()
Calculator()