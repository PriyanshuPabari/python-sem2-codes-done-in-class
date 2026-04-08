# Count lines
# #PRIYANSHU 590022242

with open("file.txt") as f:
    data = f.read()

print(data.count("\n") + 1)