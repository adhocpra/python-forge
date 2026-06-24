# {key_change, value_change for key, value in dict_name.items()}

ages= {
    1:25,
    2:34,
    3:45
}
new_ages= {key+3: val+10 for key, val in ages.items()}
print(new_ages)

student= {
    "name" : "A",
    "gpa" : 9,
    "major" : "cs"
}

for key,value in student.items():
    print(key, "" ,value)

for key in student.keys():
    print(key)

for value in student.values():
    print(value)


#list comprehension
nums= [1,2,3,4,5,6]
squares= [x**2 for x in nums]
print(squares) #basic transform

#filetrs
evens= [x for x in nums if x%2==0]
print(evens)

#combined
even_squares=[x**2 for x in nums if x%2==0]
print(even_squares)

pairs=[(x,y)for x in [1,2,3] for y in ["a","b"]]
print(pairs)