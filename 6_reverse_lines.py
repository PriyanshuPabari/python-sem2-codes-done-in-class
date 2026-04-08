# Reverse each line
# #PRIYANSHU 590022242

with open("file.txt") as f:
    data = f.read()

lines = data.split('\n')
for line in lines:
    print(line[::-1])