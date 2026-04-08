# Count vowels in file
# #PRIYANSHU 590022242

with open("file.txt") as f:
    data = f.read()

vowels = "aeiouAEIOU"
count = 0
for char in data:
    if char in vowels:
        count += 1

print(f"Number of vowels in the file: {count}")