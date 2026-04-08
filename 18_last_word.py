# Print last word of each line
# #PRIYANSHU 590022242

with open("file.txt") as f:
    data = f.read()

print(data.split("\n"))
last_words = [line.split()[-1] for line in data.split("\n")
                    if line.split()]  # Check if line is not empty
print(last_words)