#!/usr/bin/python3
def no_c(my_string):
    # Create an empty string to store our result
    new_string = ""
    
    # Iterate through every character in the original string
    for char in my_string:
        # Check if the character is NOT 'c' and NOT 'C'
        if char != 'c' and char != 'C':
            # Add the character to our new string
            new_string += char
            
    return new_string
