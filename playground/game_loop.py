"""
Game project
"""

import random
state = {
    "player_health": 700,
    "buhamut_health": 1500,
    "player_turn_taken": 0,
    "buhamut_turn_taken": 0
}
condition = {
    "game_status": True,
    "player_input": input().upper(),
    "start": input(),
    "critical_hit": {0, random.randrange(20, 25)},
    "buhamut_attack": {0, random.randrange(20, 50)},
    "buhamut_prev_attack": state["player_health"]
}
Print(f"""
    Welcome to the game
    Press any key to start
    {condition["start"]}
""")

while condition["game_status"]:
    print(f"""
        Game Status
        Health: {state["player_health"]}
        Turns Taken: {state["player_turn_taken"]}
        
        Buhamat Health: {state["buhamut_health"]}
        Buhamat Turns Taken: {state["buhamut_turn_taken"]}

        Press X to use Buster Sword
        Press Z to use Rasengan
        Press C to use Copy Enemy Attack
    """)
    if condition["player_input"] == "X":
        state["buhamut_health"] -= random.randrange(1, 21)
        - condition["critical_hit"]
    elif condition["player_input"] == "Z":
        state["buhamut_health"] -= 50
    elif condition["player_input"] == "C":
        condition["buhamut_attack"]
    elif condition["player_input"] == "C":
