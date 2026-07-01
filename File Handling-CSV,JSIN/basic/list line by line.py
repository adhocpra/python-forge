file=open("tasks.txt", "r")

lines= file.readlines() #use list comprehension to remove '\'
new_lines= [line.strip()for line in lines]
print(lines) #*
print(new_lines)