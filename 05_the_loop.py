# the for loop
# is a condition that plugs the list of something in a variable
# and calling it using that given variable. the for loop
# is mainly associated with the range function
for x in range(5):
    print("hello")
# in for loop, range is a valuable function that
# gives different numbers of irritable lines of number of words

for x in range(1, 5+1):
    print(x)
# range have start, end and steps. range(start, end, steps)
# make sure from start to end, 1-10, to include 10 you need to
# +1 or instead of 10 use 11 this is because the range function
# uses a <= x < b. in terms include start but exclude end

backpack_content = ["apple", "attack", "x-potion"]

for x in backpack_content:
    print(x)
# in this contex when using a list or libraries, instead of using range
# to create multiple iterration for the variable "x".
# you can use list[], tupple(), set{} or dict{}

# the if, then and else loop
# is a loop that check if the condition is true or not
temp = 70
if temp >= 100:
    print("it's hot!")
elif 70 <= temp < 100:
    print("it's warm!")
elif 0 <= temp < 70:
    print("it's cold!")
else:
    print("it's freezing!")

# turnery operator
# this allows the if, then and esle loop to be stored in a variable
x = 100
y = 12
yes = True if y == 10 and x == 100 or x == 120 else False
if yes is True:
    print("Yes!")
else:
    print("No!")

# if and in loop
# similar to if, then and else loop but with a combination
# of a for loop. this allows the condition to know if
# the data is in the variable
list = ["apple", "youtube", "seventh heaven"]
if "seventh heaven" in list:
    print("Tifa")
elif "re7" in list:
    print("Ethan")
else:
    print("Meh")

# while loop
# is a conditional statement that determine if the condition is True
# of False. this create an infinite loop that until the condition is
# not True anymore. otherwise once the condition is met then using a
# break function to end the loop
x = True
while True:
    if x is True:
        print("Press x")
        user_input = input("> ").lower()
        if user_input == "x":
            print("You've press x")
            break
        elif user_input != "x":
            print("You've not selected x")
            x = False
    if not x:
        print("Press c to continue\nPress q to quit")
        user_input = input("> ").lower()
        if user_input == "c":
            x = True
        elif user_input == "q":
            break

# nested loop
# is a loop that's inside of a loop
for x in range(5, 100 + 1, 5):
    for y in range(1, 10 + 1):
        print(x + 5, y * "XD")
