# if __author__  = "__slysch__":
    # 2-3. Personal Message: Store a person’s name in a variable, and print a message
    # to that person. Your message should be simple, such as, “Hello Eric, would you like
    # to learn some Python today?”
"""
We start talking about a string and this is anything inside either double or single quotes.

Here we are  to store as a value of a variable, someone's name and later concantenate
it with another string. (Remember you can only add two items together if they of the same data type)
"""

name = "Enter_your_name_here" #Enter your name here inside the quotes to make it a string
print("Hello " + name + "\nWelcome to the Python World!")
# \n used to enter a new line and \t for a new tab




# TAKE AWAY
# In case you run into integers, in order to concatenate them with a string, we shall
# have to first convert them into a string using "str()" or reverse with int() methods.
age = 18
print("I'm " + str(age) + " years old.")
