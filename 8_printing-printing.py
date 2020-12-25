formatter = "{} {} {} {}" # create a variable with arguments format

print(formatter.format(1, 2, 3, 4)) # assign a number to each argument through a function format
print(formatter.format("one", "two", "three", "four")) # assign a string to each argument through a function format
print(formatter.format(True, False, False, True)) # assign a boolean to each argument through a format function
print(formatter.format(formatter, formatter, formatter, formatter)) # assign a variable to each argument through a format function
print(formatter.format(
    "Try your", 
    "Own text here", 
    "Maybe a poem", 
    "Or a song about fear"))