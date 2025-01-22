 # -*- coding: utf-8 -*-
"""
Created on Mon Dec  9 19:58:17 2024

@author: dande
"""

annual_salary = int(input("What is your annual salary" ))
semi_annual_raise = float(input("What is your semi-anual raise, as a decimal" ))
portion_saved = float(input("What percentage of your salary do you want to save: "))
total_cost = int(input("How much is your dream home: "))
portion_downpayment= .25
annual_return=.04
required_deposit = total_cost * portion_downpayment


current_savings=0.0
monthly_salary = annual_salary/12
months=0.0

while current_savings < required_deposit:
    current_savings += current_savings*(annual_return/12)
    current_savings += monthly_salary * portion_saved
 

    months += 1
    
    if months % 6 == 0:
        monthly_salary += monthly_salary * semi_annual_raise




print(f"It will take you {months} months to save enough for a down payment.")