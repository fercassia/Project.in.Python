def add (x,y):
    return x+y
def sub (x,y):
    return x-y
def div (x,y):
    return x/y
def mult (x,y):
    return x*y

print("Choose a command: 1.Add\n 2.Subtraction\n 3.Division\n 4.Multiplication\n 9.Exit\n  ")

while True:
    oper = int (input("Command input (1/2/3/4/9): \n"))
    if oper in [1 , 2 , 3, 4]:
        num1 = float(input("Type a number: "))
        num2 = float(input("Type a number: "))
        if oper == 1:
            print (str(num1)+" + "+ str(num2)+" = " + str(add(num1,num2)))
        elif oper == 2:
            print (str(num1)+" - "+ str(num2)+" = " + str(sub(num1,num2)))
        elif oper == 3:
            print (str(num1)+" / "+ str(num2)+" = " + str(div(num1,num2)))
        elif oper == 4:
            print (str(num1)+" * "+ str(num2)+" = " + str(mult(num1,num2)))
    else:
        print("Invalid Number")
    if oper == 9:
        print("Confirm for exit")
        print("1. Yes")
        exit = int(input("Command for confirmation: \n"))
        if exit == 1:
            print("To the next!")
            break