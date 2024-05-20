import tkinter as tk
from tkinter import messagebox

class tax_calculate:
    def __init__(self):
        pass

    def calculation_income_tax(self, income):
        if income <= 300000:
            return 0
        elif 300001 <= income <= 400000:
            return (income *.1)
        elif 400001 <= income <= 650000:
            return (income *.15)
        elif 650001 <= income <= 1000000:
            return (income *.2)
        elif 1000001 <= income <= 1500000:
            return (income *.25)
        else:
            return (income *.30)

class PIT_calculator(tax_calculate):  # Inherits from tax_calculate class
    """
    Class to calculate Personal Income Tax (PIT) based on various factors such as income,
    employment status, organization type, and number of children.
    """
    
    def __init__(self, name, income, regular, organisation_type, children):  # Constructor method
        """
        Initializes the PIT_calculator object with personal details and financial information.
        
        Parameters:
        - name (str): The name of the individual.
        - income (float): Annual income of the individual.
        - regular (bool): Indicates if the individual is a regular employee.
        - organisation_type (str): Type of the organization ('govt', 'private', 'corporate').
        - children (int): Number of children for deduction purposes.
        """
        self.name = name  # Instance variable for name
        self.income = income  # Instance variable for income
        self.regular = regular  # Instance variable indicating if the individual is a regular employee
        self.organisation_type = organisation_type  # Instance variable for organization type
        self.children = children  # Instance variable for number of children


    def calculate_deduction(self):
        deduction = 0
        if self.regular:
            if self.organisation_type == 'govt':
                deduction += self.income * 0.05 + 2400
            elif self.organisation_type == 'private':
                deduction += self.income * 0.05
            elif self.organisation_type == 'corporate':
                deduction += self.income * 0.05
        else:
            if self.organisation_type == 'private':
                deduction += self.income * 0.05
            elif self.organisation_type == 'corporate':
                deduction += self.income * 0.05
        if isinstance(self.children, int) and self.children > 0:
            deduction += self.children * 350000
        return deduction

    class TaxCalculator:
        def __init__(self, income):
          self.income = income

    def calculate_deduction(self):
        # Example calculation
        return self.income * 0.2

    def calculate_tax(self):
        # Encapsulate deduction calculation in a new method
        deduction_amount = self.get_deduction_amount()
        
        taxable_income = self.income - deduction_amount
        tax = self.calculation_income_tax(taxable_income)
        
        if tax >= 1000000:
            tax += tax * 0.1
        
        return tax
    
def main():
    root = tk.Tk()
    root.withdraw()  # Hide the main window

def get_deduction_amount(self):
        # Directly return the result of calculate_deduction
        return self.calculate_deduction()


def main():
    # Define name variable
    name = None
    
    # Prompt the user to enter their name
name = input('Enter your name: ')

    # Convert the employee's monthly income to annual income
income = int(input("Enter employee monthly income: ")) * 12

    # Ask if the employee is a regular employee and store the boolean result
regular = input("Is employee a regular employee? (y/n): ").lower() == 'y'

    # Get the organization type from the user
organisation_type = input("Enter organization type (govt/private/corporate): ").lower()

    # Count the number of children
children = int(input("Enter number of children: "))

# Call the main function to execute the program
if __name__ == "__main__":
    main()


employee = PIT_calculator(name, income, regular, organisation_type, children)

tax_payable = employee.calculate_tax()

print(f"Tax payable for employee {name} is Nu. {tax_payable}")

messagebox.showinfo("Tax Calculation", f"Tax payable for employee {name} is Nu. {tax_payable}")

if __name__ == "__main__":
    main()

