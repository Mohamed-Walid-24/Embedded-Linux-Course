# Task_1.2
# Write a Python program to test whether a passed letter is a 7 vowel or not.

vowels = "aeiou"
letter = input("Enter a letter: ")
letter = letter.lower()
print(letter in vowels)