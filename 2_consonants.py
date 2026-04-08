# Count consonants in file
# #PRIYANSHU 590022242

with open("file.txt") as f:
    data = f.read()

consonants = "bcdfghjklmnpqrstvwxyzBCDFGHJKLMNPQRSTVWXYZ"
count = 0
for char in data:
    if char in consonants:
        count += 1

print(f"Number of consonants in the file: {count}")