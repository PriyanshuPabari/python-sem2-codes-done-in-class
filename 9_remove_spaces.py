# Remove spaces from file
# #PRIYANSHU 590022242

with open("file.txt") as f:
    data = f.read()

print(data.strip())
