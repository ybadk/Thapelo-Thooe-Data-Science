vowel = ['a', 'e', 'i', 'o', 'u']

word = "kgothatso"

count = 0

for character in word:
    if character not in vowel:
        count += 1

print(count)
