# Replace a word
# #PRIYANSHU 590022242

with open("file.txt") as f:
    data = f.read()

print(data)
word_to_replace = input("Enter the word to replace: ")
replacement_word = input("Enter the replacement word: ")
new_data = data.replace(word_to_replace, replacement_word)
with open("file.txt", "w") as f:
    f.write(new_data)
print("Word replaced successfully.")
