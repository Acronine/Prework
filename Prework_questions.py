# Question 1
# Write a function to print "hello_USERNAME!" USERNAME is the input of the function.

def hello_name(user_name):
    """Display a greeting to the given username."""
    print("Hello " + user_name.title() + "!")


# Question 2
# Write a python function, first_odds that prints the odd numbers from 1-100 and returns nothing

def first_odds():
    """
    Counts from 1 to 100 2 at a time starting at 1. 
    Also returns nothing.
    """
    for number in range(1, 100, 2):
        print(number)
    return None

# Question 3
# Please write a Python function, max_num_in_list to return the max number of a given list.

def max_num_in_list(a_list):
    """
    Checks to make sure all the values are either integers or floats.
    If they aren't, they are removed from a copy list.
    Then it returns the max number from the remaining values in the list.
    """
    split_list = a_list[:]
    for number in split_list:
        if type(number) != int:
            if type(number) != float:
                split_list.remove(number)
    return max(split_list)
          

# Question 4
# Write a function to return if the given year is a leap year. A leap year is divisible by 4, but not divisible by 100,
#  unless it is also divisible by 400. The return should be boolean Type (true/false).

def is_leap_year(a_year):
    """
    Checks to see if what's given is an integer.
    Then checks to see if the number given is divisible by 4.
    Returns true if the year is a leap year, but false if it isn't.
    """
    if type(a_year) != int:
        return "Invalid Response"
    else:
        if (a_year % 4) == 0:
            leap_year = True
            return leap_year
        elif(a_year % 4) != 0:
            leap_year = False
            return leap_year
    

# Question 5
# Write a function to check to see if all numbers in list are consecutive numbers. 
# The return should be boolean Type.

def is_consecutive(a_list):
    """Checks each number in a list by index 
    to see if they follow each other consecutively"""
    true_len = (len(a_list) - 1)
    for number in range(0, true_len):
        if number == true_len:
            continue
        elif a_list[number + 1] - a_list[number] != 1:
            consecutiveness = False
            return consecutiveness
            break
    consecutiveness = True
    return consecutiveness