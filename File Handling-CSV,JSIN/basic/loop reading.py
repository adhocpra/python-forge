file= open("tasks.txt","r")

line= file.readline()
while line:
    print(line, end="")
    line= file.readline()

file.close()