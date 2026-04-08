# Count digits in file
# #PRIYANSHU 590022242

with open("file.txt") as f:
    data = f.read()

digits = "0123456789"
count = 0
for char in data:
    if char in digits:
        count += 1

print(f"Number of digits in the file: {count}")