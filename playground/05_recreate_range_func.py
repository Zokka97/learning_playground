def scope(start, stop=None, step=1):
    result = 0
    if stop is None:
        stop = start
        start = 0
        result = 0
    else:
        result = start
    print(result)
    while result < stop:
        result += step
        print(result)


print(scope(22))
# I need to make the "start" the default value if "stop" is not specified
# I need to make a loop that if "step" is defined then it will increase by increament of the given "step"
# Using a while loop that if "step" is less than "start" it will continue to print the increaments until "step" is >= than "start"
# Make sure that it prints the value every line in the terminal

"""
What I've learned

# You cannot use return as a replacement to print since the return immediately ends the loop and return the value



"""
