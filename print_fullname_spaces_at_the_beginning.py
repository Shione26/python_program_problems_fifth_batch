# Prog01: Create a program that ask the user to input their fullname with several space characters at the beginning. Print the input without the spaces in the beginning.

# ask for user input
name = str(input("Input your fullname: "))
# use python string method to remove extra spaces in the beginning then print
print(name.strip())