# Write a python program to get the command-line arguments 

import sys

arguments = sys.argv
print("This is the name/path of the script: ",arguments[0])
print(f"('Number of arguments:', {len(arguments)})")
print("('Argument List:',\"", arguments,'")')