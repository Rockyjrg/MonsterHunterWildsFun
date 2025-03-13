from numpy import random
class Hunter:
    def __init__(self, name, age):
        self.hunterName = name
        self.hunterAge = age
        self.weapon = None
        self.level = 0
        self.exp = 10
        self.hunterHealth = 15
        
    def earnWeapon(self, weapon):
        self.weapon = weapon
              
    def canHunt(self):
        if self.hunterAge < 18:
            return False
        elif self.hunterAge >= 18:
            return True
            
    def gainExp(self, amount):
        self.exp += amount
        if self.exp >= 100:
            self.level += 1
            
class Monster:
    def __init__(self, name, health, attack, defense):
        self.name = name
        self.health = health
        self.attack = attack
        self.defense = defense
        
    def takeDamage(self, amount):
        self.health -= amount
        print("Monster health is now: " + self.health)
        
    def isDefeated(self):
        if self.health <= 0:
            return True
        else:
            return False
    
    def displayStats(self):
        print(f"\n{self.name} stats are: health - {self.health}, attack - {self.attack}, defense - {self.defense} ")
        
class BattleSystem:
    def __init__(self):
        pass
    
    def startBattle(hunter, monster):
        if hunter.hunterHealth > 0 and monster.health > 0:
            print(f"You have started a battle with {monster.name}.")

#get random monster for user to fight
def randomMonster():
    monster = ["Doshaguma", "Balahara", "Chatacabra", "Rathalos", "Dalthydon", 
               "Yian kut-ku", "Lala Barina", "Rey Dau", "Arkveld", "Quematrice",
               "Uth Duna", "Gore Magala","Congalala", "Gypceros", "Gravios", "Nerscylla",
               "Blangonga", "Nu Udra", "Rompopolo", "Ajarkan", "Hirabami", "Jin Dahaad",
               "Guardian Doshaguma", "Guardian Rathalos","Xu Wu", "Guardian Ebony Odogaron",
               "Guardian Arkveld", "Rathian", "Guardian Fulgur Anjanath"]
    return random.choice(monster)

#deal with the user input
def getUserInput():
    name = input("What is your name: ")
    age = int(input("What is your age: "))
    weapon = input("What weapon would you like to use: ")
    
    hunter = Hunter(name, age)
    hunter.earnWeapon(weapon)
    
    #hunter.canHunt()
    if hunter.canHunt() == False:
        print(f"\nHello {name}, age {age}. I see you have a {weapon}, but I am sorry you must turn back. You are too young to go out and fight. Please come back once you are of age.")
    else:
        print(f"\nHello {name}, age {age}. I see you have a {weapon} with you. You meet the age requirement, welcome on in.")
        
    newMonster = randomMonster()
    anotherMonster = Monster(newMonster, 14, 4, 3)
    print("\nThe monster that you have been tasked with fighting is " + newMonster + ".")
    anotherMonster.displayStats()
    BattleSystem.startBattle(hunter, anotherMonster)
#run silly little program
getUserInput()






       

        
        
#monsterHunterWeapons = ["Great Sword","Long Sword", "Sword and Shield", "Dual Blades", "Hammer",
                    # "Hunting Horn", "Gunlance", "Switch Axe","Charge Blade", "Insect Glaive",
                    # "Light Bow Gun", "Heavy Bow Gun", "Bow"]


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