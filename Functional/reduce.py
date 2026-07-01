#gives a single value
from functools import reduce


def add(a,b):
    return a+b

nums= [1,2,3,4,5,6]

result= reduce(add,nums)
print(result)

def multiply(a,b):
    return a*b

nums= [1,2,3,4,5,6]
result= reduce(multiply, nums)
print(result)

def join_words(a,b):
    return a+ " " + b

words= ["hello", "world", "from", "python"]
result= reduce(join_words, words)
print(result)

#max number

def get_max(a,b):
    if a>b:
        return a
    return b

numbers= [25,8,35,90,25,3,-2]

result= reduce(get_max, numbers)
print(result)

def get_longest(a,b):
    if len(a)>len(b):
        return a
    return b

words= ["hi", "yo", "man", "ok"]

result= reduce(get_longest, words)
print(result)