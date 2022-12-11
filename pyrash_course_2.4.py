# 2-4. Name Cases: Store a person’s name in a variable, and then
# print that person’s name in lowercase, uppercase, and titlecase


# Solution
name = input("Enter your name please: ")  # Variable with a query for a user to enter their names.
print(f"Lower case: {name.lower()}, Upper case: {name.upper()}, Titlecase: {name.title()}")


# I have used a formatted string to include all three required variables in one line of code.
# instead of printing three lines of code.
# Note that the functions called like .lower() are python built-in functions available for reuse at any time in the code
# You simply have to write a variable, followed by a dot, and you will see a
# number of other applicable built-in functions.
