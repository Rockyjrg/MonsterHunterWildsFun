from numpy import random

monsterHunterWeapons = ["Great Sword","Long Sword", "Sword and Shield", "Dual Blades", "Hammer",
                    "Hunting Horn", "Gunlance", "Switch Axe","Charge Blade", "Insect Glaive",
                    "Light Bow Gun", "Heavy Bow Gun", "Bow"]

ranged = [10,11,12]
melee = list(range(10))

monsterList = ["Doshaguma", "Balahara", "Chatacabra", "Rathalos", "Dalthydon", 
               "Yian kut-ku", "Lala Barina", "Rey Dau", "Arkveld", "Quematrice",
               "Uth Duna", "Gore Magala","Congalala", "Gypceros", "Gravios", "Nerscylla",
               "Blangonga", "Nu Udra", "Rompopolo", "Ajarkan", "Hirabami", "Jin Dahaad",
               "Guardian Doshaguma", "Guardian Rathalos","Xu Wu", "Guardian Ebony Odogaron",
               "Guardian Arkveld", "Rathian", "Guardian Fulgur Anjanath"]

monster = random.choice(monsterList)
weapon = random.choice(monsterHunterWeapons)

#print all weapons
print("\nThe list of weapons are: ")
for weapon_name in monsterHunterWeapons:
    print(f" - {weapon_name}")

print("\nThe melee weapons are:")
print(", ".join(monsterHunterWeapons[i] for i in melee))

print("\nThe ranged weapons are: ")
print(", ".join(monsterHunterWeapons[i] for i in ranged))
    
#print a random monster to hunt with a random weapon
print(f"\nThe monster you are tasked to hunt this time is {monster} with the weapon {weapon}")

