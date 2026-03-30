#!/usr/bin/python3
def print_reversed_list_integer(my_list=[]):
    if my_list:
        # We reverse the list and iterate through it
        for i in my_list[::-1]:
            # Using str.format() as required by the prompt
            print("{:d}".format(i))
