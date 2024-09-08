word = input("Enter the word: ")
duplicate = ""
for i in word:
    if i not in duplicate:
        duplicate = duplicate + i
print(duplicate)

word = input("Enter a word: ")
unique_characters = []
for char in word:
    if char not in unique_characters:
        unique_characters.append(char)
result = ''.join(unique_characters)
print('char are', result)