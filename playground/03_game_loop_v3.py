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
print("""
    Welcome to the game

    press Enter to start
""")
input()
while True:
    enemy_attack = random.choice((0, random.randrange(30, 50)))
    critical_hit = random.choice((0,
                                  0, 0, 0, 0, random.randrange(10, 30)))
    buster_sword = random.choice((0, random.randrange(20, 50)))
    if state["enemy_health"] > 0 < state["player_health"]:
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
        user_input = input("> ").upper()
        if user_input == "X":
            state["player_previous_attack"] = buster_sword + critical_hit
            state["enemy_health"] -= state["player_previous_attack"]
        elif user_input == "Z":
            state["player_previous_attack"] = 100 + critical_hit
            state["enemy_health"] -= state["player_previous_attack"]
        elif user_input == "C":
            state["player_previous_attack"] = state["enemy_previous_attack"]
            state["enemy_health"] -= state["player_previous_attack"]
        if user_input in ["X", "Z", "C"]:
            state["player_turn"] += 1
        if state["player_previous_attack"] >= 100:
            state["enemy_previous_attack"] = 150
            state["player_health"] -= state["enemy_previous_attack"]
        else:
            state["player_health"] -= enemy_attack
            state["enemy_previous_attack"] = enemy_attack
        state["enemy_turn"] += 1
    elif state["enemy_health"] <= 0:
        user_input = input("""
            You've Won!\n
            Press Q to quit
            Press S to Start a new game
            > """).upper()
        if user_input == "Q":
            break
        if user_input == "S":
            state["player_health"] = 1000
            state["enemy_health"] = 1000
            state["enemy_turn"] = 0
            state["player_turn"] = 0
            state["enemy_previous_attack"] = 0
            state["player_previous_attack"] = 0
    elif state["player_health"] <= 0:
        user_input = input("""
            Game Over!\n
            Press Q to quit
            Press S to Start a new game
            > """).upper()
        if user_input == "Q":
            break
        if user_input == "S":
            state["player_health"] = 1000
            state["enemy_health"] = 1000
            state["enemy_turn"] = 0
            state["player_turn"] = 0
            state["enemy_previous_attack"] = 0
            state["player_previous_attack"] = 0
print("""
    Thanks for playing!
    """)
