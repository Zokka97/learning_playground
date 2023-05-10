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
    # "player_input": input().upper(),
    # "start": input(),
    # NOTE: Might not be possible to add an input into a variables
    #       outside the while loop because it must ask a
    #       a input as a place holder
    # "critical_hit": int({0, random.randrange(20, 25)}),
    # "buhamut_attack": int({0, random.randrange(20, 50)}),
    # NOTE: set{} is not a good method to do a random integers
    #       instead use random.choice
    "critical_hit": random.choice([0, random.randrange(20, 25)]),
    "buhamut_attack": random.choice([0, random.randrange(30, 70)]),
    "buhanut_soaring_fire": 100,
    "buhamut_prev_attack": state["player_health"]
}
enemy_list = []
starter = input("""
            Welcome to the game
            Press any key to start
""")
if starter != "":
    while condition["game_status"]:
        print(f"""
_________________________________________________      
            Game Status

            Health: {state["player_health"]}
            Turns Taken: {state["player_turn_taken"]}
            
            Buhamat Health: {state["buhamut_health"]}
            Buhamat Turns Taken: {state["buhamut_turn_taken"]}

            Press X to use Buster Sword
            Press Z to use Rasengan
            Press C to use Copy Enemy Attack
        """)
        player_input = input().upper()
        if player_input == "X":
            state["buhamut_health"] -= (random.randrange(1,
                                        21) + condition["critical_hit"])
        elif player_input == "Z":
            state["buhamut_health"] -= 50
        elif player_input == "C":
            state["player_health"] -= buhamut_prev_attack
        state["player_turn_taken"] += 1

        # elif condition["player_input"] == "C":
        #     condition["buhamut_attack"]
        enemy_list.append(buhamut_prev_health) = (state["buhamut_health"])
        if state["buhamut_health"] <= (buhamut_prev_health - 30):
            state["player_health"] -= condition["buhamut_soaring_fire"]
        # NOTE: if 1470 <= (1500 - 90):
        else:
            state["player_health"] -= condition["buhamut_attack"]
        buhamut_prev_attack = condition["buhamut_attack"]
        state["buhamut_turn_taken"] += 1
        if state["buhamut_health"] <= 0:
            print("""Congratulations!
            You've Won.""")
            break
        elif state["player_health"] <= 0:
            print("""Game Over!
            You've lost.""")
            break
    print("start a new game")
else:
    print("Invalid key!")
"""
NOTE: Store Buhamut attack damage into a variable
      after the condition loop back
NOTE: Use percent instead of whole number

 """
