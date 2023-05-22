# don't use the while loop only define function or other function
v_names = {
    "elder": "Village Elder:",

}


def convo_001():
    print("Press any key to start the game.")
    x = input(">>> ")
    if not x or x:
        print(f"{v_names["elder"]} Hello there, welcome to Talon village!")
    return


def convo_002():
    print("""This village for generation has been
fertile, until one day when the Talon Falls' gets
narower and the river becomes dry.""")
    x = input(">>> ")
    if not x or x:
        print("We really need your help young traveller.")
    x = input(">>> ")
    if not x or x:
        print("Type Yes if you want to help other wise press NO")
    x = input(">>> ").lower()
    if x == "yes":
        print("You're help is much appriciated young traverller")
    elif x == "no":
        print("[T]")


dialouge_001 = convo_001()
