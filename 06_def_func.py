import random


# def attack(random_choices):
#     singularity = 500
#     particle_rain = 200
#     choices = random.choice(singularity, particle_rain)
#     return choices


# print(attack(random_choices))

# def attack():
#     basic = 200
#     critical = random.randrange(1, 50)
#     combine = basic + critical
#     return combine


# print(attack())

def attack(singularity, particle_rain):
    return singularity if random.randrange(0, 2) == 0 else particle_rain


result = attack(200, 100)
print(result)

# NOTE: i can use randrange as random choice with if and the statement
# NOTE: def if mainly use for organizing codes to more readable parameters and arguments
# NOTE: return is like the print statement of def
# NOTE: after creating a parameters inside the def, it's better to put it into
# another parameter ouside the define function to make the code more readable and neat
