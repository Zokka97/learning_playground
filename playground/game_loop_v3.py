# Imports
import random
# Dictionaries
state = {
    "player_health": 1000,
    "player_turn": 0,
    "player_previous_attack": 0,
    "enemy_health": 1000,
    "enemy_turn": 0,
    "enemy_previous_attack": 0
}
# Start of the Game loop
while True:
    enemy_attack = random.choice((0, random.randrange(30, 50)))
    user_input = input("").upper
    print(f"""
    Welcome to the game

    press Enter to start: {user_input}
    """)
    if user_input != "":
        print(f"""
        Game Status

            Health: {state["player_health"]}
            Attack Damage: {state["player_previous_attack"]}
            Turns Taken: {state["player_turn"]}

            Buhamat Health: {state["enemy_health"]}
            Attack Damage: {state["enemy_previous_attack"]}
            Buhamat Turns Taken: {state["enemy_turn"]}

            Press X to use Buster Sword
            Press Z to use Rasengan
            Press C to use Copy Justsu
        """)
    # else:
    #     break
    if user_input == "X":
        state["enemy_health"] -= random.choice((0, random.randrange(20, 50)))
    elif user_input == "Z":
        state["enemy_health"] -= 80
    elif user_input == "C":
        state["enemy_health"] -= state["enemy_previous_attack"]
    # state["enemy_health"] -= random.choice((0,
    #                                         0, 0, 0, 0, random.randrange(10, 30)))
    if state["player_previous_attack"] >= 100:
        state["enemy_previous_attack"] = state["player_health"] - 100
        state["player_health"] -= 100
    else:
        state["player_health"] -= enemy_attack
        state["enemy_previous_attack"] = enemy_attack
