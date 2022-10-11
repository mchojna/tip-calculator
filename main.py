"""
Title: Tip Calculator
Author: Michał Chojna
Date: 02.06.2022
Description: Calculates total cost of the bill and splits the bill by a given number of people
"""

# Prints welcome message
print("Welcome to the Tip Calculator.")

# Takes the amount of the bill from the user
bill = float(input("What was the total bill? $"))

# Takes the percentage of bill which the user wants to use as a tip
percentage_tip = int(input("What percentage tip would you like to give? "))

# Takes the total number of people to split bill between
people = int(input("How many people to split the bill? "))

# Calculates the amount of the tip
tip = bill * (percentage_tip / 100)

# Calculates the amount of the total bill
total_bill = bill + tip

# Calculates the amount of the bill after split between total number of people
per_person = round(total_bill / people, 2)

# Prints the amount of the total bill
print(f"Total bill: {round(total_bill, 2):.2f}$")

# Prints the amount of the total bill each person should pay
print(f"Each person should pay: ${round(per_person, 2):.2f}")
