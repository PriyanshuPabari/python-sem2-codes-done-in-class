# Print words longer than 5 letters
# #PRIYANSHU 590022242

with open("file.txt") as f:
    data = f.read()

words = data.split()
long_words = [word for word in words if len(word) > 5]
print(long_words)