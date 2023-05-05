# name = "Glenn, Rick, Michonne, Andrea, Carl"
# find_glenn = name.find("Glenn"), int(name.find("nn,")) + 2
# glenn = name[0:6]
# find_rick = name.find("Rick"), int(name.find("ck,")) + 2
# rick = name[7:11]
# find_michonne = name.find("Michonne"), int(name.find("ne,")) + 2
# michonne = name[13:21]
# find_andrea = name.find("Andrea"), int(name.find("ea,")) + 2
# andrea = name[23:29]
# find_carl = name.find("Carl"), int(name.find("rl")) + 2
# carl = name[31:35]
# print(glenn, find_glenn)
# print(rick, find_rick)
# print(michonne, find_michonne)
# print(andrea, find_andrea)
# print(carl, find_carl)

# name = ["Glenn", "Rick", "Michonne", "Andrea", "Carl"]
# initials = input("Type: ")
# if initials.lower() == "g" or initials.upper() == "G":
#     print(name[0])
# elif initials.lower() == "r" or initials.upper() == "R":
#     print(name[1])
# elif initials.lower() == "m" or initials.upper() == "M":
#     print(name[2])
# elif initials.lower() == "a" or initials.upper() == "A":
#     print(name[3])
# elif initials.lower() == "c" or initials.upper() == "C":
#     print(name[4])
# else:
#     print("invalid")

name = []
name.append("Glenn")
name.append("Rick")
name.append("Michonne")
name.append("Andrea")
name.append("Carl")
for namelist in name:
    print(namelist, len(name))
