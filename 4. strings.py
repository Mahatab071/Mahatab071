# Advanced Python: Strings

"""
Author: Kalim Amzad Chy
Email: kalim.amzad.chy@gmail.com

This Python script is designed to provide a comprehensive understanding of Python strings.
We will explore:
1. String basics - Creation, accessing, and updating.
2. All string methods and their uses.
3. Practical applications of strings in data manipulation.

Each section includes detailed explanations, examples, and challenging assignments.
"""

# Section 1: String Basics
# ------------------------
# Strings in Python are sequences of characters.

# Example 1: Creating and Using Strings
simple_string = "Hello, Python learners!"
# print(simple_string[0])  # Accessing the first character

# Strings are immutable
# Trying to change a character directly will raise a TypeError
# simple_string[0] = "h"  # Uncommenting this line will cause an error

# String Methods
# Finding substrings
# print(simple_string.find('python'))  # Returns the start index of 'Python'

# Replacing substrings
modified_string = simple_string.replace('learners', 'developers')
print("Modified String:", modified_string)

# Splitting strings
# print(simple_string)

marks = "80: 83: 70: 48: 47"
marks_list = marks.split(': ')  # Splits the string into a list of marks
print("Array of marks:", marks_list)

words = simple_string.split(', ')  # Splits the string into a list of words
print("Array of words:", words)

# Joining strings
joined_string = '-'.join(marks_list)  # Joins the list back into a single string
print("Joined string:", joined_string)

# Case conversion
# print(simple_string.upper())  # Converts to uppercase
# print(simple_string.lower())  # Converts to lowercase

# Stripping whitespace
user_input = "   some user input   "
# print(user_input)
# print(user_input.strip())  # Removes leading and trailing whitespace
# print(user_input.rstrip())  # Removes trailing whitespace
# print(user_input.lstrip())  # Removes leading whitespace

# Assignment 1: Create a string that contains a simple bio data like name, age, and country. Extract each piece of information and print them separately.
# Write your code below:
student="name:Syed, age:20, country:BANGLADESH"
sl=student.split(',')
print(sl[0])
print(sl[1])
print(sl[2])

# Section 2: Advanced String Operations
# -------------------------------------
# Strings can be used in more complex operations like formatting.

# Example 2: String Formatting
name = "Alice"
age = 30
greeting = f"Hello, my name is {name} and I am {age} years old."
print(greeting)

# Old-style formatting
old_greeting = "Hello, my name is %s and I am %d years old." % (name, age)
print(old_greeting)


# Assignment 2: Create a formatted string that includes data from a list or dictionary. For example, use a dictionary to store a person's information and format a string to include it.
# Write your code below:

person_info = ["John Doe", 30, "USA", "Software Engineer"]


formatted_string = f"Name: {person_info[0]}, Age: {person_info[1]}, Country: {person_info[2]}, Profession: {person_info[3]}"

# Printing the formatted string
print(formatted_string)



# Section 3: Advanced Slicing and Multiline Strings
# -------------------------------------
# Python strings are immutable, which means that every string operation creates a new string.

# Example 1: Advanced Slicing
complex_string = "Hello, Python enthusiasts!"
reverse_string = complex_string[::-1]  # Reverses the string using slicing
# print(reverse_string)

# Multiline strings
multiline_string = """This is a string that spans
multiple lines within triple quotes."""
# print(multiline_string)

# Raw strings
path = r"C:\new_folder\test.txt"  # Raw string ignores escape characters
print(path)

# String Methods
# Counting substrings
# print("The count of 'n' is:", complex_string.count('n'))

# Formatting strings with str.format() and f-strings
pi = 3.14159
formatted_string = "The value of pi is {:.2f}".format(pi)  # Formatting to two decimal places
# print(formatted_string)

# Assignment 3: Write a function that takes a string and returns a dictionary with the counts of each character in the string.
# Write your code below:
def count_characters(input_string):
    ltr = {}
    for char in input_string:
        if char in ltr:
            ltr[char] += 1
        else:
            ltr[char] = 1
    return ltr

# Example usage
input1 = "hello world"
r = count_characters(input1)
print(r)



# Section 4: Regular Expressions
# ------------------------------
# Regular expressions are used for pattern matching in strings.


import re

# Basic Regex: Matching Literal Strings
pattern = 'earth'
text = 'Hello, world!'
match = re.search(pattern, text)
if match:
    print("Match found:", match.group())
else:
    print("No match found.")


# Character Classes
pattern = r'\d+'  # Matches one or more digits
text = 'There are 123 apples, 45 oranges, and 78 bananas.'
matches = re.findall(pattern, text)
print("Numbers found:", matches)

# Alternation and Grouping
pattern = r'apple|banana'  # Matches 'apple' or 'banana'
text = 'I like apples, oranges.'
matches = re.findall(pattern, text)
print("Fruits found:", matches)


# Positive Lookahead
pattern = r'\d{3}(?=px)'  # Matches a number only if it's followed by 'px'
text = 'The 487 image is 106px by 209px.'
matches = re.findall(pattern, text)
print("Numbers followed by 'px':", matches)

# Non-capturing Group
pattern = r'(?:\d{3}-)?\d{3}-\d{4}'  # Matches phone numbers with optional area code
text = 'Call 415-555-1234 or 555-4321 or 008-718-6897'
matches = re.findall(pattern, text)
print("Phone numbers found:", matches)


# Example: Email Validation
# A more detailed regex for validating an email address.
email_regex = r"^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$"
email = "example@domain.com"
email = "example@domain"
if re.match(email_regex, email):
    print("Valid email!")
else:
    print("Invalid email!")


# Example: Extracting Phone Numbers
# Regex to match US phone number formats
phone_regex = r"\b\d{3}[-.]?\d{3}[-.]?\d{4}\b"
text = "Call me at 415-555-1011 tomorrow, or 564-9712 or at 415.555.9999 for office line."
phones = re.findall(phone_regex, text)
print("Phone numbers found:", phones)

# Example: Replacing Text
# Replacing all occurrences of digits with a placeholder
replaced_text = re.sub(r'\d', 'X', 'My number: 12345, office: 98765')
print("Censored text:", replaced_text)

# Assignment: Write a regex to find all the hashtags in a string.
text_with_hashtags = "This is a #great day to learn #regex in #Python!"


# Assignments: Write a regex to find the Bangladesh phone number with all variations.
# 01454565767
# +880196345634
# 0088785674657
# 01845-567567
import re

# Regex pattern to match Bangladesh phone numbers

pattern =r'(\+?88)?01[1-9]\d{8}(-\d{2,4})?'
#Test cases
phone_numbers = [
    '01454565767',
    '+8801963456341',
    '008878567465700',
    
]

# Applying regex to find matches
for number in phone_numbers:
    if re.match(pattern, number):
        print(f"{number} matches the pattern.")
 


# Congratulations on completing the advanced section on Python strings!
# Review the assignments, try to solve them, and check your understanding of string manipulation techniques.
