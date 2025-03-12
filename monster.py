from numpy import random
class Hunter:
    def __init__(self, name, age):
        self.hunterName = name
        self.hunterAge = age
        self.weapon = None
        
    def earnWeapon(self, weapon):
        self.weapon = weapon
              
    def canHunt(self):
        if self.hunterAge < 18:
            print(f"Hello {self.hunterName}, age {self.hunterAge}. I see you have a {self.weapon}, but I am sorry you must turn back. You are too young to go out and fight. Please come back once you are of age")
        elif self.hunterAge >= 18:
            print(f"Hello {self.hunterName}, age {self.hunterAge}. I see you have a {self.weapon} with you. You meet the age requirement, welcome on in.")

def getUserInput():
    name = input("What is your name: ")
    age = int(input("What is your age: "))
    weapon = input("What weapon would you like to use: ") 
    
    hunter = Hunter(name, age)
    hunter.earnWeapon(weapon)
    
    print(hunter.canHunt())

# firstHunter = Hunter("Tommy", int(userAge))
# firstHunter.earnWeapon(userWeapon)

#run silly little program
getUserInput()

       

        
# monsterHunterWeapons = ["Great Sword","Long Sword", "Sword and Shield", "Dual Blades", "Hammer",
#                     "Hunting Horn", "Gunlance", "Switch Axe","Charge Blade", "Insect Glaive",
#                     "Light Bow Gun", "Heavy Bow Gun", "Bow"]

# ranged = [10,11,12]
# melee = list(range(10))

# monsterList = ["Doshaguma", "Balahara", "Chatacabra", "Rathalos", "Dalthydon", 
#                "Yian kut-ku", "Lala Barina", "Rey Dau", "Arkveld", "Quematrice",
#                "Uth Duna", "Gore Magala","Congalala", "Gypceros", "Gravios", "Nerscylla",
#                "Blangonga", "Nu Udra", "Rompopolo", "Ajarkan", "Hirabami", "Jin Dahaad",
#                "Guardian Doshaguma", "Guardian Rathalos","Xu Wu", "Guardian Ebony Odogaron",
#                "Guardian Arkveld", "Rathian", "Guardian Fulgur Anjanath"]

# monster = random.choice(monsterList)
# weapon = random.choice(monsterHunterWeapons)

# #print all weapons
# print("\nThe list of weapons are: ")
# for weapon_name in monsterHunterWeapons:
#     print(f" - {weapon_name}")

# print("\nThe melee weapons are:")
# print(", ".join(monsterHunterWeapons[i] for i in melee))

# print("\nThe ranged weapons are: ")
# print(", ".join(monsterHunterWeapons[i] for i in ranged))
    
# #print a random monster to hunt with a random weapon
# print(f"\nThe monster you are tasked to hunt this time is {monster} with the weapon {weapon}")

# asking = input("\nDo you prefer a ranged or melee weapon: ")

# if asking == "melee":
#     print("Your weapon will be: " + random.choice(monsterHunterWeapons))
# else:
#     print ("Your weapon will be: " + monsterHunterWeapons[i] for i in ranged)