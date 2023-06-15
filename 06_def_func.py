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

# def attack(singularity, particle_rain):
#     return singularity if random.randrange(0, 2) == 0 else particle_rain


# result = attack(200, 100)
# print(result)


def scope(a=1, b=0, c=1):
    b1 = 0
    while b1 != b:
        x = a * b
        b1 += 1
        return x


print(scope(b=10))
# a = 2

# b = 10
# c = 1
# while not 10 or less than 10 then continue
# x = a * c  # iterrate a
# print(x)
# NOTE: i can use randrange as random choice with if and the statement
# NOTE: def is mainly use for organizing codes to more readable parameters and arguments <- False
# NOTE: return is like the print statement of def <- False
# NOTE: after creating a parameters inside the def, it's better to put it into
# another parameter ouside the define function to make the code more readable and neat
# y = mx + b
