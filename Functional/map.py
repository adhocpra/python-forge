#Map, 
def square(x):
    return x*x

nums= [1,2,3,4,5]

result= list(map(square,nums))
print(result)

#vs list comprehension
result= [x*x for x in nums]
print(result)
# expression for item in iterable]
# With a condition (filter):


# [expression for item in iterable if condition]
# Examples:


# # squares
# [x*x for x in nums]

# # only even numbers
# [x for x in nums if x % 2 == 0]

# # squares of only even numbers
# [x*x for x in nums if x % 2 == 0]

def to_upper(x):
    return x.upper()
names= ["alice", "bob", "charlie"]
result= list(map(to_upper,names))
print(result)

result= [x.upper() for x in names]
print(result)


def add_ten(x):
    return x+10

nums = [10,20,30]
result= list(map(add_ten, nums))
print(result)

result=[x+10 for x in nums]
print(result)


fruits= ["apple", "banana", "cherry", "dragonfruits"]
print(len(fruits))
result= list(map(len,fruits))
print(result)

result=[len(fruit) for fruit in fruits]
print(result)

nums= [1,2,3,4,5]

result= list(map(str,nums))
print(result)

result= [str(num) for num in nums]
print(result)

nums= input("enter number : ").split()
print(nums)

result= list(map(int,nums))
print(result)

#or

result= list(map(int, input("enter number :").split()))
print(result)

result= [int(num) for num in input("enter number: ").split()]
print(result)