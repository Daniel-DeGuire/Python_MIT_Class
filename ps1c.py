# -*- coding: utf-8 -*-
"""
Created on Mon Dec 16 19:26:56 2024

@author: dande
"""

def calculate_savings_rate(starting_salary, target_savings, annual_return=0.04, semi_annual_raise=0.07, months=36, epsilon=100):
    """
    Calculate the savings rate required to reach the target savings within the given time frame.
    """
    # Initialize the bounds for bisection search
    low, high = 0, 10000  # Represent savings rate as an integer percentage (0% to 100%)
    steps = 0

    def savings_after_months(savings_rate):
        """
        Simulates the total savings after `months` given a specific `savings_rate`.
        """
        monthly_salary = starting_salary / 12
        current_savings = 0

        for month in range(1, months + 1):
            # Add monthly investment returns
            current_savings += current_savings * (annual_return / 12)

            # Add monthly savings contribution
            current_savings += monthly_salary * (savings_rate / 10000)

            # Adjust salary after semi-annual raises
            if month % 6 == 0:
                monthly_salary *= (1 + semi_annual_raise)

        return current_savings

    # Bisection search loop
    while high - low > 1:
        steps += 1
        mid = (low + high) // 2
        current_savings = savings_after_months(mid)

        if abs(current_savings - target_savings) <= epsilon:
            # Found an acceptable savings rate
            return mid / 10000, steps
        elif current_savings < target_savings:
            # Savings too low, increase the savings rate
            low = mid
        else:
            # Savings too high, decrease the savings rate
            high = mid

    # If no suitable rate is found, return None
    return None, steps


# Example usage
if __name__ == "__main__":
    starting_salary = int(input("What is your starting salary" ))
    target_savings = 250000

    result, steps_taken = calculate_savings_rate(starting_salary, target_savings)

    if result is not None:
        print(f"You need to save {result:.4f} of your income. Found in {steps_taken} steps.")
    else:
        print("It is not possible to save the required amount in the given time.")