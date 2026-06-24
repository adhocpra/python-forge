import json
#normal data:
student= {
    "name" : "A",
    "courses": ["A", "B"],
    "attendance":{
        "A": 3,
         "B" :1
        }
}
print("before saving:")
print(student)
print(type(student))

#save to a file - dict-json-file
with open("student_data.json", "w") as f: # f is the object of the file
    json.dump(student,f, indent=4)
print("\nSaved to student_data.json")

#load back

with open("student_data.json", "r") as f:
    loaded= json.load(f)
print("\nAfter loaded:")
print(loaded)