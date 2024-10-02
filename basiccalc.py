'''

Calc class

'''
class Calculator:
    
    def __init__(self, num1, num2) -> None:
        self.num1 = num1
        self.num2 = num2


#Addition
    def add_numbers(self):
        return f"The result of the sum of the numbers is {self.num1 + self.num2}"

#Subtraction   
    def subtract_numbers(self):
        return F"The result of the subtraction of the numbers is {self.num1 - self.num2}"

#Multiplcation
    def multiplication_numbers(self):
        return f"The result of the multiplication of the numbers is {self.num1 * self.num2}"

#Division
    def division_numbers(self):
        return f"The result of the division of the numbers is {self.num1 / self.num2}"





