# Program 2: Word Frequency and Pattern Analyzer

import string

text = input("Enter a sentence or paragraph: ")

# Remove punctuation
clean_text = text.translate(str.maketrans("", "", string.punctuation))

# Convert to lowercase and split into words
words = clean_text.lower().strip().split()

# Word frequency
frequency = {}

for word in words:
    frequency[word] = frequency.get(word, 0) + 1

print("\n--- Word Frequency ---")

for word, count in frequency.items():
    print(word, ":", count)

# Detect palindrome words
palindromes = []

for word in words:
    if len(word) > 1 and word == word[::-1]:
        if word not in palindromes:
            palindromes.append(word)

print("\n--- Palindrome Words ---")

if palindromes:
    print(", ".join(palindromes))
else:
    print("No palindrome words found.")

# Basic text analysis
print("\n--- Text Analysis ---")
print("Total words:", len(words))
print("Distinct words:", len(frequency))
print("Total characters:", len(text))