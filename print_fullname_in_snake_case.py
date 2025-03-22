# Prog10: Create a program that ask the user to input their fullname in incorrect casing. Print the input in snake case.

# ask the user to input fullname in incorrect casing
name = input("Enter your fullname in incorrect casing: ")
# convert the input to proper casing
proper_cased = (name.title())
# replace spaces with underscore
# print output
print(proper_cased)