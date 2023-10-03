"""Employee pay calculator."""
"""ENTER YOUR SOLUTION HERE!"""

class Employee:
    def __init__(self, name, isSalary, hours, pay, contracts, bonus):
        self.name = name
        self.isSalary = isSalary
        self.hours = hours
        self.pay = pay
        self.contracts = contracts
        self.bonus = bonus

    def get_pay(self):
        total = 0
        if self.isSalary:
            total = total + self.pay
        else:
            total = total + self.pay * self.hours
        if self.contracts != 0:
            total = total + self.contracts * self.bonus
        elif self.bonus != 0 and self.contracts == 0:
            total = total + self.bonus

        return total

    def __str__(self):
        if self.isSalary:
            if self.contracts == 0 and self.bonus == 0:
                return f"{self.name} works on a monthly salary of {self.pay}. Their total pay is {self.get_pay()}."
            else:
                if self.contracts > 0:
                    return f"{self.name} works on a monthly salary of {self.pay} and receives a commission for {self.contracts} contract(s) at {self.bonus}/contract. Their total pay is {self.get_pay()}."
                else:
                    return f"{self.name} works on a monthly salary of {self.pay} and receives a bonus commission of {self.bonus}. Their total pay is {self.get_pay()}."
            
            
        
        elif self.isSalary == False:
            if self.contracts == 0 and self.bonus == 0:
                return f"{self.name} works on a contract of {self.hours} hours at {self.pay}/hour. Their total pay is {self.get_pay()}."
            else:
                if self.contracts > 0:
                    return f"{self.name} works on a contract of {self.hours} hours at {self.pay}/hour and receives a commission for {self.contracts} contract(s) at {self.bonus}/contract. Their total pay is {self.get_pay()}."
                else:
                    return f"{self.name} works on a contract of {self.hours} hours at {self.pay}/hour and receives a bonus commission of {self.bonus}. Their total pay is {self.get_pay()}."

                    


                
            
        


# Billie works on a monthly salary of 4000.  Their total pay is 4000.
billie = Employee('Billie', True, 0, 4000, 0, 0)

# Charlie works on a contract of 100 hours at 25/hour.  Their total pay is 2500.
charlie = Employee('Charlie', False, 100, 25, 0, 0)

# Renee works on a monthly salary of 3000 and receives a commission for 4 contract(s) at 200/contract.  Their total pay is 3800.
renee = Employee('Renee', True, 0, 3000, 4, 200)

# Jan works on a contract of 150 hours at 25/hour and receives a commission for 3 contract(s) at 220/contract.  Their total pay is 4410.
jan = Employee('Jan', False, 150, 25, 3, 220)

# Robbie works on a monthly salary of 2000 and receives a bonus commission of 1500.  Their total pay is 3500.
robbie = Employee('Robbie', True, 0, 2000, 0, 1500)

# Ariel works on a contract of 120 hours at 30/hour and receives a bonus commission of 600.  Their total pay is 4200.
ariel = Employee('Ariel', False, 120, 30, 0, 600)

print(str(billie))
print(str(charlie))
print(str(renee))
print(str(jan))
print(str(robbie))
print(str(ariel))