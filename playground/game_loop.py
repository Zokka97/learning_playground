# Game State
import random
state = {
    "player_health": 500,
    "enemy_health": 100,
    "turns": 0
}
invalid = "Unrecognized input, please try again."
game_running = True
# False == "exit"
print("Welcome to game! Please follow instructions.")

# Game Loop
while game_running:
    print("")
    print("Enemy Health: %d" % state["enemy_health"])
    print("Player Health: %d" % state["player_health"])
    print("Turns Taken: %d" % state["turns"])

    user_attack = input(
        """
Select an attack:
'X' -> Punch
'S' -> Kick
"""
    ).upper()

    if user_attack == "X":
        # process punch
        state["enemy_health"] -= random.randrange(20, 36)
    elif user_attack == "S":
        # process kick
        state["enemy_health"] -= random.randrange(40, 71)
    elif user_attack == "exit":
        not game_running
    else:
        # unrecognized input
        print(invalid)
    state["turns"] += 1
    state["player_health"] -= random.randrange(20, 51)
# if user input and attack
# state["player_health"] -= random.randrange(20, 51)
# will be executed
    if state["player_health"] <= 0 or state["enemy_health"] <= 0:
        break
    continue
print("Thanks for Playing!")

""" 
# TODO: handle edge-case where the user inputs upper/lower case values
      we want to accept both. We can do this by turning all user-input
      into uppper-case.
      user_attack = user_attack.upper()

# TODO: if the enemy health is <= 0, then we should exit the game loop.

# TODO: have the enemy attack the player!

# TODO: if the player health is <= 0, exit the game loop

# TODO: have attacks deal random amounts of damage, so the game is less boring.
      https://www.programiz.com/python-programming/examples/random-number

TODO: allow the user to restart the battle when someone dies, instead of exiting the program.
NOTE: this will require functions, and may be a bit complex, so don't hesitate to ask for help!
"""
