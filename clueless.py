from numpy import random

def choosingRandomHunt():
    monsterHunterWeapons= ["Great Sword","Long Sword", "Sword and Shield", "Dual Blades", "Hammer",
                       "Hunting Horn", "Gunlance", "Switch Axe","Charge Blade", "Insect Glaive",
                       "Light Bow Gun", "Heavy Bow Gun", "Bow"]
    
    monsterList = ["Doshaguma", "Balahara", "Chatacabra", "Rathalos", "Dalthydon", "Yian kut-ku", "Lala Barina", "Rey Dau", "Arkveld", "Quematrice", "Uth Duna", "Gore Magala",
                   "Congalala", "Gypceros", "Gravios", "Nerscylla", "Blangonga", "Nu Udra", "Rompopolo", "Ajarkan", "Hirabami", "Jin Dahaad", "Guardian Doshaguma", "Guardian Rathalos",
                   "Xu Wu", "Guardian Ebony Odogaron", "Guardian Arkveld", "Rathian", "Guardian Fulgur Anjanath"]
    
    monster = random.choice(monsterList)
    weapon = random.choice(monsterHunterWeapons)
    
    #print a random monster to hunt with a random weapon
    return f"The monster you are tasked to hunt this time is {monster} with the weapon {weapon}"
    
    #print("The monster you are tasked to hunt is the: " + random.choice(monsterList) + " and the weapon you are tasked to beat it with is: " + random.choice(monsterHunterWeapons))

def main():
    print(choosingRandomHunt())
    
if __name__ == "__main__":
    main()
    
# randomMonster = random.choice(monsterList)
# randomWeapon = random.choice(monsterHunterWeapons)
#MonsterHunterWeapons[1] = "Light Bow Gun"
# print(len(monsterHunterWeapons))

# print("The monster you are tasked to hunt is the: " + random.choice(monsterList) + " and the weapon you are tasked to beat it with is: " + random.choice(monsterHunterWeapons))
# iteratingNumber = 0
# for i in range(len(monsterList)):
#     iteratingNumber += 1
#     print("The monster you are tasked to hunt is the: " + random.choice(monsterList))