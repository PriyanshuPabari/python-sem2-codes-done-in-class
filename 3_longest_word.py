# Find longest word
# #PRIYANSHU 590022242

with open("file.txt") as f:
    data = f.read()

words = data.split()
longest_word = ""
for word in words:
    if len(word) > len(longest_word):
        longest_word = word

print(f"Longest word in the file: {longest_word}")