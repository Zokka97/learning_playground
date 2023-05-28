# don't use the while loop only define function or other function
# bad idea
# while loop is important, idk why i did it but already started it. no turning back

# this is the dictionary area
v_names = {
    "elder": "Village Elder:",

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

# this is the enemy area


def enemy_001(flying_coconuts=100):

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
# convo_001()
# convo_002()
# convo_003()
# restult_004 = convo_004()
# convo_005(restult_004)
# convo_006()
store()
convo_007()
# NOTE: go in a linear pattern, choices matters

"""
WHAT I'VE LEARNED:

# def fuction will reset the parameters when you call the arguement.
# 
"""
