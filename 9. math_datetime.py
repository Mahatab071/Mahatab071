# Python Math and Datetime Modules: In-Depth Guide

"""
Author: Kalim Amzad Chy
Email: kalim.amzad.chy@gmail.com

This Python script provides an in-depth guide to the math and datetime modules in Python.
We will explore:
1. Common mathematical functions and constants in the math module.
2. Handling dates and times using the datetime module.
3. Practical examples and real-world applications of both modules.

Each section includes detailed explanations, examples, and assignments.
"""

# Section 1: Math Module
# ----------------------
# The math module provides access to mathematical functions and constants.

import math

# Example 1: Using math functions
print("The square root of 16 is:", math.sqrt(16))
print("Pi is:", math.pi)
print("Euler's number is:", math.e)
print("Cosine of pi is:", math.cos(math.pi))

# Example 2: Using math to solve real-world problems
# Calculate the area of a circle with a given radius
radius = 5
area = math.pi * math.pow(radius, 2)
print(f"The area of the circle is: {area:.2f}")

# Section 2: Datetime Module
# --------------------------
# The datetime module allows you to manipulate dates and times.

import datetime

# Example 3: Working with datetime
now = datetime.datetime.now()
print("Current date and time:", now)
print("Year:", now.year)
print("Month:", now.month)
print("Day:", now.day)


# Example 4: Calculating differences in time
new_year = datetime.datetime(2024, 1, 1)
time_left_for_new_year = new_year - now
print("Days until new year:", time_left_for_new_year.days)

# Example 5: Formatting dates and times
formatted_date = now.strftime("%Y/%m/%d %H:%M:%S")
print("Formatted date and time:", formatted_date)

# Section 3: Practical Applications
# ---------------------------------
# Combining math and datetime for advanced calculations and data handling.

# Example 6: Calculating age in years
def calculate_age(birthdate):
    today = datetime.date.today()
    age = today.year - birthdate.year - ((today.month, today.day) < (birthdate.month, birthdate.day))
    return age

birthdate = datetime.date(1999, 6, 15)
age = calculate_age(birthdate)
print(f"Age is: {age} years")

# Assignments
# -----------
# Assignment 1: Write a function that calculates compound interest using the formula A = P(1 + r/n)^(nt).
def calculate_compound_interest(principal, rate, times_compounded, time):

    try:
        # Validate inputs
        if principal < 0 or rate < 0 or times_compounded <= 0 or time < 0:
            raise ValueError("All inputs must be non-negative, and times_compounded must be positive.")
        
        # Calculate compound interest
        amount = principal * (1 + rate / times_compounded) ** (times_compounded * time)
        return round(amount, 2)
    
    except Exception as e:
        print(f"Error: {e}")
        return None

# Example usage
principal_amount = 1000  # Principal (P)
annual_rate = 0.05       # Annual interest rate (5% → 0.05)
compounded = 4           # Quarterly compounding (n=4)
years = 5                # Time in years (t)

future_value = calculate_compound_interest(principal_amount, annual_rate, compounded, years)
print(f"The future value of the investment: ${future_value}")











# Assignment 2: Create a script that prints the current time and updates every second.
import time
from datetime import datetime

def display_current_time():
    """
    Displays the current time and updates every second.
    """
    try:
        while True:
            # Clear the previous output (optional for cleaner display)
            print("\033[H\033[J", end="")  # ANSI escape sequence to clear screen
            
            # Get the current time
            current_time = datetime.now().strftime("%H:%M:%S")
            
            # Print the current time
            print(f"Current Time: {current_time}")
            
            # Wait for one second
            time.sleep(1)
    except KeyboardInterrupt:
        print("\nProgram stopped by user.")

# Run the script
display_current_time()


# Congratulations on completing the in-depth section on Python's math and datetime modules!
# Review the assignments, try to solve them, and check your understanding of these powerful tools.
