text = input("Enter a word: ")

vowels = 0
consonants = 0

for letter in text.lower():

    if letter in "aeiou":
        vowels = vowels + 1

    elif letter.isalpha():
        consonants = consonants + 1

print("Total Vowels:", vowels)
print("Total Consonants:", consonants)
