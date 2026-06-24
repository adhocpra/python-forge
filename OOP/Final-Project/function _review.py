
# # Exercises

# - Create a function greet() that prints “Hello, World!” and call it.
# - Create a function add() that takes two numbers as parameters and prints their sum.
# - Create a function multiply(a, b) that returns the product of two numbers and print the result.
# - Write a function square(n) that returns the square of a number and call it for 5.
# - Create a function is_even(n) that returns True if a number is even, otherwise False.
# - Write a function greet_name(name) that prints “Hello, name” using the given parameter.
# - Create a function calculate_area(length, width) that returns area of a rectangle.
# - Write a function largest(a, b, c) that returns the largest of three numbers.
# - Write a function reverse_string(s) that returns the reverse of the string.
# - Create a function is_prime(n) that returns True if a number is prime, otherwise False.
# - Write a function sum_list(lst) that returns the sum of all numbers in a list.
    
#     ```java
#     def sum_numbers(*args):
#         total = 0
#         for num in args:
#             total += num
#         return total
    
#     nums = [1,2,3,4,5]
#     print(sum_numbers(*nums))  # 10
#     ```
    
# - Create a function count_vowels(s) that returns the number of vowels in a string.
# - Write a function greet_users(*names) that takes multiple names and prints a greeting for each.
# - Create a function check_password(password) that prints “Strong” if length ≥ 8 otherwise “Weak”.

def add (a,b):
    return a+b

print(add(3,4))

#default agrument
def greet(name= "guest"):
    print(f"Hello, {name}")
greet()
greet("Ram")


#variable-length arguments- when input no is unknown
def sum_num(*args):
    total =0
    for num in args:
        total += num
    return total
print(sum_num(1,2,3,4)) #this is a sum list

#**kwargs = multiple keyword arguments

def show_info(**kwargs):
    for key,value in kwargs.items():
        print(f"{key} : {value}")

show_info(name= "Ram", age=20)

#Docstring- Function Documentation
def add(a,b):
    """
    This function takes two numbers and return their sum.
    """
    return a+b
print(add.__doc__)