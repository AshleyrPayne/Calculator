from basiccalc import Calculator
'''

multiplication table

'''
class Multable(Calculator):
    def __init__(self, num1, num2):
        super().__init__(num1, num2)

    def table(self):
        total = self.num1 + self.num2
        print(f"sum of {self.num1} * {self.num2} = {self.multiplication_numbers()}")
        for i in range(1,50+1):
            print(f"{total} * {i} = {total * i}")

#x = Multable(num1,num2)

#print (x.table())