# don't use the while loop only define function or other function
# bad idea
# while loop is important idk, why i did it but already started it. no turning back
v_names = {
    "elder": "Village Elder:",

}
player_status = {
    "health": 300,
    "bullets": 0

}


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
            f"{v_names['elder']}By the way, what is your name young traveller?")


def convo_004(player_name=None):
    player_name = input("Type your name: ").title()
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


def shop(bullets=10, fish_crakers=5):
    """Buy Items from the shop"""
    x = input(">>> ").lower()
    if not x or x:
        print(f"Buy 1 bullet? {bullets}")
        print(f"Buy 1 fish crakers? {fish_crakers}")
    buy = input("Press X to buy bullets \nPress Z to buy fish crakers: ").lower()
    if buy == "x":
        bullets -= 1
        player_status["bullets"] += 1
        return str(bullets) + " left from the shop"
    elif buy == "z":
        fish_crakers -= 1
        player_status["health"] += 1
        return str(fish_crakers) + " left from the shop"


# def health_shop():
# def enemy_001():
# def enemy_002():
# def enemy_003():
# def enemy_004():
# def enemy_005():


convo_001()

convo_002()

restult_004 = convo_004()
# print(restult_004)

convo_005(restult_004)
convo_006()
result_005 = shop()
print(result_005)

# NOTE: go in a linear pattern, choices matters
