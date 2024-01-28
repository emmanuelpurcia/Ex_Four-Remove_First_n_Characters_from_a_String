# Hello! this program remove the n character from a given string by the user.

# pseudocode

# Accept input string from user
word = input("Enter a word: ")
print("Original String:", word)

# Accept input number of characters to remove from user
n = int(input("Enter the number of characters to remove: "))

# Remove first n characters from string
new_word = word[n:]

# Print modified string
print("Modified String:", new_word)
