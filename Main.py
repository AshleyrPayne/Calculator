from basiccalc import Calculator
from multitable import Multable


# Function for user input
def userinput():
    num1 = int (input("Enter a number:"))
    num2 = int (input("Enter another number:")) 
    i=0   
    while (i!=1):
        print("Please select the calculation you require by entering associated number -\n"
        "1. Addition\n"
        "2. Subtraction\n"
        "3. Multiplication\n"
        "4. Division\n"
        "5. Multiplication table")
        operation = int(input("Selection: "))
        if (operation == 1):
            i+=1
            break
        elif (operation == 2):
            i+=1
            break
        elif (operation == 3):
            i+=1
            break
        elif (operation == 4):
            i+=1
            break
        elif (operation == 5):
            i+1
            break

    return num1, num2, operation


num1, num2, operation = userinput()

calc = Calculator(num1, num2)
calc2 = Multable(num1,num2)
i = 0

while(i!=1):

    if (operation == 1):
        print(calc.add_numbers())
        i+=1
        break
    elif(operation == 2):
        print(calc.subtract_numbers())
        i+=1
        break
    elif(operation == 3):
        print(calc.multiplication_numbers())
        i+=1
        break
    elif(operation == 4):
        print(calc.division_numbers())
        i+=1
        break
    elif(operation == 5):
        print(calc2.table())
        i+=1
        break
else:
    userinput()