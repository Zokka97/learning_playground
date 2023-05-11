import random
game_status = True
player_health = 1000
enemy_health = 1000

enemy_attack_store = 0
while game_status:
    user_choice = input("your turn:").upper()
    print(f"""
    {player_health}
    {enemy_health}
    {enemy_attack_store}
    """)
    if user_choice == "X":
        enemy_health -= random.randrange(20, 70)
    elif user_choice == "C":
        enemy_health -= enemy_attack_store
    elif user_choice == "Q":
        break
    else:
        continue
    enemy_attack = random.randrange(30, 90)
    enemy_attack_store = enemy_attack
    player_health -= enemy_attack
print("Game Over!")

"""
NOTE: chatgpt just simply place the "enemy_attack = random.randrange(30, 90)"
      inside the while loop because it won't generate new numbers if the 
      random.range is outside the while loop.

"""
