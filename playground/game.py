# Game State
state = {
  "player_health": 100,
  "enemy_health": 100,
  "turns": 0
}

game_running = True

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
  )

  if user_attack == "X":
    # process punch
    state["enemy_health"] -= 10
  elif user_attack == "S":
    # process kick
    state["enemy_health"] -= 5
  else:
    # unrecognized input
    print("Unrecognized input, please try again.")

  state["turns"] += 1


"""
TODO: handle edge-case where the user inputs upper/lower case values
      we want to accept both. We can do this by turning all user-input
      into uppper-case.
      user_attack = user_attack.upper()

TODO: if the enemy health is <= 0, then we should exit the game loop.

TODO: have the enemy attack the player!

TODO: if the player health is <= 0, exit the game loop

TODO: have attacks deal random amounts of damage, so the game is less boring.
      https://www.programiz.com/python-programming/examples/random-number

TODO: allow the user to restart the battle when someone dies, instead of exiting the program.
NOTE: this will require functions, and may be a bit complex, so don't hesitate to ask for help!
"""
