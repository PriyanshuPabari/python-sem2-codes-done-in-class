# Reverse word order
# #PRIYANSHU 590022242

with open("file.txt", "r") as f:
    content = f.read()

words = content.split()
reversed_content = " ".join(words[::-1])

print("Reversed word order:\n")
print(reversed_content)

with open("file.txt", "w") as f:
    f.write(reversed_content)