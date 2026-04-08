# Count words starting with vowel
# #PRIYANSHU 590022242

with open("file.txt") as f:
    data = f.read()

words = data.split()
vowel_words = []
vowels = "aeiouAEIOU"

for word in words:
    if word and word[0] in vowels:
        vowel_words.append(word)

print(f"Words starting with a vowel: {vowel_words}")
print(f"Number of such words: {len(vowel_words)}")