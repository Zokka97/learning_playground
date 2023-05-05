# temp = int(input("Insert temp: "))
# cold = 32
# # mild = 50   # I don't need another variable if I'm trying to compare 3 range of numbers
# hot = 70
# if temp <= cold:
#     print(f"It's cold!")
# elif cold < temp <= hot:
#     print(f"Alright!")
# elif temp >= hot:
#     print(f"WARNING: Drink plenty of water!")
# else:
#     print()
my_hp = 500
enemy_hp = 1000
my_atk_dmg = 30
my_spcl_atk_dmg = 100
enemy_atk_dmg = 20
enemy_spcl_dmg = 70
my_atk_char = "x"
my_spcl_atk_char = "s"
atk_input = input("""Your turn Select an attack 
Press \"X\" to attack
Press \"S\" for special attack\n""")
enemy_turn = my_hp - enemy_atk_dmg if atk_input == ""else print(
    "")  # variables can't be bellow the statement being used to
# because python reads the code from top to bottom. It's like saying
# how many slices of pizza did I eat when I haven't ordered a pizza yet.
my_turn = my_atk_dmg if atk_input == my_atk_char else my_spcl_atk_dmg if atk_input == my_spcl_atk_char else enemy_turn
print(enemy_hp - my_turn)
