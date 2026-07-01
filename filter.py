#syntax=filter(function,iterable)
def is_even(x):
    return x%2==0
    #return-true or false

nums= [1,2,3,4,5,6]
result= list(filter(is_even,nums))
print(result)

result= [x for x in nums if x%2==0]
print(result)

def is_passed(mark):
    return mark >=40

marks= [40,50,60,70,30,20]
result= list(filter(is_passed,marks))
print(result)

result= [mark for mark in marks if mark>=40]
print(result)

def starts_with_r(name):
    return name.startswith("r")

names= ["ram", "radha", "rakesh", "kal", "sal"]

result= list(filter(starts_with_r,names))
print(result)

result= [name for name in names if name.startswith("r")]
print(result)

def is_long(w):
    return  len(w) >4

words= ["hi", "hello", "hey", "whatsup"]

result= list(filter(is_long,words))
print(result)

result= [w for w in words if len(w)>4]
print(result)

def is_positive(n):
    return n>0
nums= [-1,0,3,-5,0.99]
result= list(filter(is_positive,nums))
print(result)

result= [n for n in nums if n>0]
print(result)



items =["hello", "123", "word", "88", "py"]

result= list(filter(str.isalpha, items))
print(result)

result= [item for item in items if str.isalpha(item)]
#OR
result =[item for item in items if item.isalpha()]
print(result)


mixed= [0,1, "", "hi", None, 42, False, True]
result= list(filter(None, mixed))
print(result)

result= [m for m in mixed if m]
print(result)
