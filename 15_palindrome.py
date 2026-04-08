# Check palindrome lines
# #PRIYANSHU 590022242

with open("file.txt") as f:
    data = f.read()

print([line for line in data.split("\n") if line == line[::-1]])
