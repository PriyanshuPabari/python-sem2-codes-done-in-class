# Count repeated words
# #PRIYANSHU 590022242

with open("file.txt") as f:
    data = f.read()

print(data.split())
words = data.split()
word_count = {}
for word in words:
    word_count[word] = word_count.get(word, 0) + 1
repeated_words = {word: count for word, count in word_count.items() if count > 1}
print(repeated_words)