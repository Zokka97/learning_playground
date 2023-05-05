# Strings == "this is a string"
# 'A'  -> Character
# "AB" -> String
# Strings are made-up of Characters

# Strings are encoded of **ASCII** characters.
# More information on strings:
# https://youtu.be/gagrpB09tEY

# "AB" == [65, 66] == [0x41, 0x42]

print("Hello, world!")

print("Amazing, {1} {0}".format("world", "today!"))

name = "fruits"
apple = 25
orange = 30
banana = 5.5

print("The %s contains %d apple, %d orange and %f banana" %
      (name, apple, orange, banana))
