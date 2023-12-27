'''
Created on 18-Dec-2023

@author: samir
'''
import keyword

print(len(keyword.kwlist))

def count_character_occurrences(input_string):
    # Creating an empty dictionary to store character counts
    char_count = {}

    # Iterating through each character in the input string
    for char in input_string:
        # Incrementing the count for each character or setting count to 1 if character not seen before
        char_count[char] = char_count.get(char, 0) + 1

    return char_count

# Example usage:
input_string = "Hello, World!"
result = count_character_occurrences(input_string)

# Displaying the character counts
for char, count in result.items():
    print(f"'{char}' occurs {count} times")
