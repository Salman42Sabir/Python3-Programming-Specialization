# 1. Write a function called int_return that takes an integer as input and returns the same integer.

user_input = input("Enter a number")
def int_return(val):
    return int(val)
int_return(user_input)

# 2. Write a function called add that takes any number as its input and returns that sum with 2 added. 

user_input = input("Enter a number:")
def add(val):
    sum_val = int(val) + 2
    return sum_val
add(user_input)

# 3. Write a function called change that takes any string, adds “Nice to meet you!” to the end of the argument given, and returns that new string.

user_input = input("Enter a Sentence:")
def change(val):
    nice = "Nice to meet you!"
    final = val + nice
    return final
change(user_input)
