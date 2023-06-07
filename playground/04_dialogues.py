# don't use the while loop only define function or other function
# bad idea
# while loop is important, idk why i did it but already started it. no turning back
# forgot to add enemy attack to player
import random
# this is the dictionary area
v_names = {
    "elder": "Village Elder:",
    "person_1": "Violet:",
    "person_2": "Ben:",
    "person_3": "Gloria:",
    "person_4": "Vincent:",
    "person_5": "Ching:",
}
player_status = {
    "health": 300,
    "bullets": 0

}
store_item = {
    "bullets": 5,
    "fish_crackers": 500
}

enemies = {
    "flying_coconuts": 100,
    "crawling_snakes": 200,
    "four_legged_bird": 150,
    "humongous_centipede": 200,
    "howling_corns": 500
}
# this is the conversation area


def convo_001():
    print("Press any key to start the game.")
    x = input(">>> ")
    if not x or x:
        print(f"{v_names['elder']} Hello there, welcome to Talon village!")


def convo_002():
    x = input(">>> ").lower()
    if not x or x:
        print(f"""{v_names['elder']} This village for generation has been
fertile, until one day when the Talon Falls' gets
narower and the river becomes dry.""")
    x = input(">>> ")
    if not x or x:
        print(f"{v_names['elder']} We really need your help young traveller.")
    x = input(">>> ")
    if not x or x:
        print("Type YES if you want to help otherwise press NO")
    x = input(">>> ").lower()
    if x == "yes":
        print(
            f"{v_names['elder']} You're help is much appriciated young traverller")
    elif x == "no":
        print(
            f"{v_names['elder']} [Pointed a gun] you're not leaving until you help us.")
        print("Press any key to continue.")
        x = input(">>> ").lower()
        if not x or x:
            print(f"{v_names['elder']} Good, come follow me!")


def convo_003():
    x = input(">>> ").lower()
    if not x or x:
        print(
            f"{v_names['elder']} By the way, what is your name young traveller?")


def convo_004(player_name=None):
    player_name = input("Type your name: ").title()
    if not player_name:
        print("Okay I'll name you Ingeborg")
        player_name = "Ingeborg"
    else:
        pass
    return player_name


def convo_005(name):
    print(f"Nice to meet you {name}")


def convo_006():
    x = input(">>> ").lower()
    if not x or x:
        print("Here's your mission\n")
        print("You'll have to kill all monsters in our village with this gun.")
    x = input(">>> ").lower()
    if not x or x:
        print("Earned a pistol \nEarned 5 bullets")
    player_status["bullets"] = 5


def convo_007():
    x = input(">>> ").lower()
    if not x or x:
        print(
            f"{v_names['elder']} You'll be able to enter the store after each battle")
        print(
            f"{v_names['elder']} You must kill all the monster to be able to exit the village")
        print(f"{v_names['elder']} Goodluck with your mission!")
    x = input(">>> ")


def convo_008():
    x = input(">>> ").lower()
    if not x or x:
        print(f"{v_names['person_1']} Thanks for saving me mister!")
    choice_1 = "No problem!"
    choice_2 = "Get loss!"
    print(f"""Press X for {choice_1}
or Press Z for {choice_2}""")
    x = input(">>> ").lower()
    if x == "x":
        print(f"{v_names['person_1']} This us for you mister")
        print("You've earned +2 bullets")
        player_status["bullets"] += 2
    elif x == "z":
        print(f"{v_names['person_1']} Rude. Well thanks any way!")
    else:
        print("... bye!")


def convo_009():
    x = input(">>> ").lower()
    if not x or x:
        print(
            f"{v_names['person_2']} I-I... I thought I was dead. Thanks man, you're a lifesaver!")
    choice_1 = "No problem!"
    choice_2 = "Get loss!"
    print(f"""Press X for {choice_1}
or Press Z for {choice_2}""")
    x = input(">>> ").lower()
    if x == "x":
        print(f"{v_names['person_2']} This us for you mister")
        print("You've earned +50 health")
        player_status["health"] += 50
    elif x == "z":
        print(f"{v_names['person_2']} Bring me home would yah!")
    else:
        print(f"{v_names['person_2']} Bring me home.")
        # this is the enemy area


def convo_010():
    x = input(">>> ").lower()
    if not x or x:
        print(f"{v_names['person_3']} A strong man with a gun...")
    choice_1 = "No problem!"
    choice_2 = "Get loss!"
    print(f"""Press X for {choice_1}
or Press Z for {choice_2}""")
    x = input(">>> ").lower()
    if x == "x":
        print(
            f"{v_names['person_3']} Did I say thank you? I could have handle that myself!")
    elif x == "z":
        print(f"{v_names['person_3']} Hot!!")
        print("You've earned +5 bullets and a kiss")
        player_status["bullets"] += 5
    else:
        print("...")


def convo_011():
    x = input(">>> ").lower()
    if not x or x:
        print(f"""{v_names['person_4']} Hahahaha, that's it,I could've shot that with one bullet.
You're weak""")
    choice_1 = "I've just save you're life"
    choice_2 = "Get loss!"
    print(f"""Press X for {choice_1}
or Press Z for {choice_2}""")
    x = input(">>> ").lower()
    if x == "x":
        print(
            f"{v_names['person_4']} Hahahah, No you didn't. Here take this, bullets are just for the weak. Hahahaha")
        print("You've earned +1 bullets")
        player_status["bullets"] += 1
    elif z == "z":
        print(
            f"{v_names['person_4']} Maybe you should. getta out of here. Hahahaha")
    else:
        print("HAHAHAHA, WEAK!!")


def convo_012():
    x = input(">>> ").lower()
    if not x or x:
        print(
            f"{v_names['person_5']} Omg, I thought I'm gonna die. Th-thank you!")
    choice_1 = "No problem!"
    choice_2 = "Get loss!"
    print(f"""Press X for {choice_1}
or Press Z for {choice_2}""")
    x = input(">>> ").lower()
    if x == "x":
        print(
            f"{v_names['person_5']} To tell you the truth you're the strongest man in this village")
        print("You've earned a useless amount of +9999 bullets +9999 health")
        player_status["bullets"] += 9999
        player_status["health"] += 9999
    elif x == "z":
        print(f"{v_names['person_5']} That is not cool at all!")
    else:
        print("Goodluck!")


def convo_013():
    x = input(">>> ").lower()
    if x != "x" or x == "x":
        print(f"{v_names['elder']} You did it, you've defeated all enemies")
    x = input(">>> ").lower()
    if x != "x" or x == "x":
        print(f"{v_names['elder']} As a reward. You are free now!")
# this is the enemy area


def enemy_atk():
    brak = random.randrange(100, 230)
    attack = [30, brak]
    result = random.choices(attack)
    return result


outcome = enemy_atk()[0]


def enemy_001():
    x = input("Press x to attack:\n").lower
    if not x or x:
        if player_status["bullets"] < 2:
            print("You've lost!")
        elif player_status["bullets"] >= 2:
            player_status["bullets"] -= 2
            enemies["flying_coconuts"] -= 100
    if enemies["flying_coconuts"] == 0:
        print("You've won!")
    player_status["health"] -= outcome
    print("You're health", player_status["health"],
          "Bullets", player_status["bullets"])


def enemy_002():
    x = input("Press x to attack:\n").lower
    if not x or x:
        if player_status["bullets"] < 4:
            print("You've lost!")
        elif player_status["bullets"] >= 4:
            player_status["bullets"] -= 4
            enemies["crawling_snakes"] -= 200
    if enemies["crawling_snakes"] == 0:
        print("You've won!")
    player_status["health"] -= outcome
    print("You're health", player_status["health"],
          "Bullets", player_status["bullets"])


def enemy_003():
    x = input("Press x to attack:\n").lower
    if not x or x:
        if player_status["bullets"] < 3:
            print("You've lost!")
        elif player_status["bullets"] >= 3:
            player_status["bullets"] -= 3
            enemies["four_legged_bird"] -= 150
    if enemies["four_legged_bird"] == 0:
        print("You've won!")
    player_status["health"] -= outcome
    print("You're health", player_status["health"],
          "Bullets", player_status["bullets"])


def enemy_004():
    x = input("Press x to attack:\n").lower
    if not x or x:
        if player_status["bullets"] < 4:
            print("You've lost!")
        elif player_status["bullets"] >= 4:
            player_status["bullets"] -= 4
            enemies["humongous_centipede"] -= 200
    if enemies["humongous_centipede"] == 0:
        print("You've won!")
    player_status["health"] -= outcome
    print("You're health", player_status["health"],
          "Bullets", player_status["bullets"])


def enemy_005():
    x = input("Press x to attack:\n").lower
    if not x or x:
        if player_status["bullets"] < 4:
            print("You've lost!")
        elif player_status["bullets"] >= 4:
            player_status["bullets"] -= 4
            enemies["howling_corns"] -= 500
    if enemies["howling_corns"] == 0:
        print("You've won!")
    player_status["health"] -= outcome
    print("You're health", player_status["health"],
          "Bullets", player_status["bullets"])


# def enemy_001():
#     while enemies["flying_coconuts"] != 0:
#         x = input("Press x to attack:\n").lower
#         if not x or x:
#             if player_status["bullets"] < 2:
#                 print("You've lost!")
#                 print("You've earned 2 bullets")
#                 player_status["bullets"] += 2
#             elif player_status["bullets"] >= 2:
#                 player_status["bullets"] -= 2
#                 enemies["flying_coconuts"] -= 100
#                 print("You've won!")

# this is the store area


def bullets():
    bullets_before = store_item["bullets"]
    store_item["bullets"] -= 1
    player_status["bullets"] += 1
    print(f"""
There is {store_item['bullets']} out of {bullets_before} bullets
You've have {player_status['bullets']} bullets
    """)


def foods():
    fish_cracker_before = store_item["fish_crackers"]
    store_item["fish_crackers"] -= 100
    player_status["health"] += 100
    print(f"""
There is {store_item['fish_crackers']} out of {fish_cracker_before} fish crackers
You've have {player_status['health']} health
    """)


def store():
    x = input(">>> ").lower()
    if not x or x:
        print("You've entered the store.")
    x = input(">>> ").lower()
    if not x or x:
        print("Please select a choice.")
        print("B for bullets C for fish crackers.")
    x = input(">>> ").lower()
    if x == "b":
        bullets()
    elif x == "c":
        foods()


# this is the execution area
convo_001()
convo_002()
convo_003()
restult_004 = convo_004()
convo_005(restult_004)
convo_006()
store()
convo_007()
enemy_001()
convo_008()
store()
enemy_002()
convo_009()
store()
enemy_003()
convo_010()
store()
enemy_004()
convo_011()
store()
enemy_005()
convo_012()
convo_013()


# NOTE: go in a linear pattern, [choices matters] not anymore

"""
WHAT I'VE LEARNED:

# def fuction will reset the parameters when you call the arguement.
# if a parameter have multiple strings or integers separated with commas then it will default with tuples.
# when printing a parameter with a list, tuple, sets and or dictionary. you can use the slice method to [0] next
to the parameter to pick one of the list. if instead printing the parameter itself, it would result into having
brackets to specify the type of a data group.
"""
