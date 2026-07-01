students= {
    "std1" : {"name": "Ram", "age": 21},
    "std2" : {"name" : "Sita", "age":31}
}
print(students["std1"]["name"])

#Excercises
# #- Create a dictionary student = {"name": "Ram", "age": 18, "grade": "A"} and print it.
# - Access the value of "name" from the student dictionary and print it.
# - Add a new key "city" with value "Kathmandu" to the student dictionary and print it.
# - Update the age of the student to 20 and print the dictionary.
# - Remove the key "grade" from the student dictionary and print it.
# - Create a dictionary fruits = {"apple": 10, "banana": 5, "mango": 7} and print the value of "banana".
# - Check if "orange" exists in the fruits dictionary.
# - Print all the keys of the fruits dictionary.
# - Print all the values of the fruits dictionary.
# - Print all key-value pairs of the fruits dictionary using items().
# - Create two dictionaries a = {"x": 10, "y": 20} b = {"z": 30} and merge them.
# - Use get() method to safely access key "name" from student dictionary.
# - Clear all items from a dictionary and print it.
# - Create a dictionary nums = {1: "one", 2: "two", 3: "three"} and print keys and values separately using a loop.
# - Create a nested dictionary student = {"name": "Ram", "marks": {"math": 80, "science": 90}} and print the math marks.
# 
student={
    "name": "Ram",
    "age" :18,
    "grade": "A"

}
print(student)
print(student["name"])
student["city"]="Kathmandu"
print(student)
student["age"]=20
print(student)
#get method:
print(student.get("name"))



fruits= {
    "apple":10,
    "banana" :5,
    "mango":7
}
print(fruits["banana"])

if "orange" in fruits:
    print("exists")
else:
    print("not found")


#printing keys
print(fruits.keys())
#printing values
print(fruits.values())

#key value pairs
print(fruits.items())

a= {
    "x":10,
     "y":20
}

b= {
    "z" :30
}

merged = a | b
print(merged) #or

merged1= {**a, **b}
print(merged1)

merged.clear()
print(merged)

nums = {
    1: "one",
    2: "two",
    3:"three"
}
for key, val in nums.items():
    print(key,val)


for key in nums:
    print(key)

for val in nums.values():
    print(val)


student= {
    "name": "Ram",
    "marks" :
    {
        "math" : 80,
        "science" :90
    }
}
print(student ["marks"] ["math"])