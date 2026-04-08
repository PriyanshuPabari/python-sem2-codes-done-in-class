# Copy only even lines
# #PRIYANSHU 590022242

with open("file.txt", "r") as f:
    lines = f.readlines()

with open("file.txt", "w") as f:
    for i in range(len(lines)):
        if (i + 1) % 2 == 0:
            f.write(lines[i])

print("File updated with only even lines!")