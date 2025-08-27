# Header

print("********************************************")
print("* Jennifer Dang                            *")
print("* IS 826: Application Programming          *")
print("* Assignment 3: Data Structure & Algorithm *")
print("* Date: 08/27/2025                         *")
print("********************************************\n")

print("""Purpose: \n""")

# Prompt the user to enter a string that returns the input

def getInput():
    input_user = input("Enter a string to evaluate:")
    return input_user

def characterCount(input_string):
    count = 0
    for char in input_string:
        count +=1
    return count

