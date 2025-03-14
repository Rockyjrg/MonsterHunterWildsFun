from numpy import random
class Hunter:
    def __init__(self, name, age):
        self.hunterName = name
        self.hunterAge = age
        self.weapon = None
        self.level = 0
        self.exp = 10
        self.hunterHealth = 15
    
    #store a weapon object inside of the weapon    
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
            
#weapon class for correct attributes
class Weapon:
    def __init__(self, weaponName, damage, durability):
        self.weaponName = weaponName
        self.damage = damage
        self.durability = durability

            
class Monster:
    def __init__(self, name, health, attack, defense):
        self.name = name
        self.health = health
        self.attack = attack
        self.defense = defense
        
    def takeDamage(self, weapon):
        self.health -= weapon.damage
        weapon.durability -= 1
        print(f"Monster health is now: {self.health}")
        print(f"Player health is {Hunter.hunterHealth}")
        
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
        print(f"You have started a battle with {monster.name}.")
        
        # while hunter.hunterHealth > 0 and monster.health > 0:
        #     hunter.

#get random monster for user to fight
def randomMonster():
    monster = ["Doshaguma", "Balahara", "Chatacabra", "Rathalos", "Dalthydon", 
               "Yian kut-ku", "Lala Barina", "Rey Dau", "Arkveld", "Quematrice",
               "Uth Duna", "Gore Magala","Congalala", "Gypceros", "Gravios", "Nerscylla",
               "Blangonga", "Nu Udra", "Rompopolo", "Ajarkan", "Hirabami", "Jin Dahaad",
               "Guardian Doshaguma", "Guardian Rathalos","Xu Wu", "Guardian Ebony Odogaron",
               "Guardian Arkveld", "Rathian", "Guardian Fulgur Anjanath"]
    return random.choice(monster)


#print valid weapons
def printWeaponNames():
    print("\nI will now present you with a selection of weapons for you to choose from, they are: ")
    weaponChoice = ["Great Sword","Long Sword", "Sword and Shield", "Dual Blades", "Hammer",
                    "Hunting Horn", "Gunlance", "Switch Axe","Charge Blade", "Insect Glaive",
                    "Light Bow Gun", "Heavy Bow Gun", "Bow"]
    for w in weaponChoice:
        print(f" - {w}")

#make sure the user is using a weapon available
def correctWeapon(weapon):
    weaponNames = ["Great Sword","Long Sword", "Sword and Shield", "Dual Blades", "Hammer",
                    "Hunting Horn", "Gunlance", "Switch Axe","Charge Blade", "Insect Glaive",
                    "Light Bow Gun", "Heavy Bow Gun", "Bow"]
    
    return weapon in weaponNames
    #SIMPLIFIED TO THE ABOVE CODE
    # if weapon not in weaponNames:
    #     return False
    # else:
    #     return True


#deal with the user input
def getUserInput():
    name = input("What is your name: ")
    age = int(input("What is your age: "))
    
    printWeaponNames()
    
    #check to see if user input matches a valid weapon
    #while loop to check user input
    #TODO: Make sure the user doesn't have to worry about capitilization
    while True:
        weapon = input("\nWhat weapon would you like to use: ")
        if correctWeapon(weapon):
            break
        print("Please choose a correct weapon.")
            
    
    hunter = Hunter(name, age)
    validWeapon = Weapon(weapon, random.randint(10, 15), random.randint(1,5))
    hunter.earnWeapon(validWeapon)
    print(f"Damage = {hunter.weapon.damage}, Durability = {hunter.weapon.durability}")
    
    if hunter.canHunt() == False:
        print(f"\nHello {name}, age {age}. I see you have chosen a {weapon}, but I am sorry you must turn back. You are too young to go out and fight. Please come back once you are of age.")
        return -1
    else:
        print(f"\nHello {name}, age {age}. I see you have chosen a {weapon}. You meet the age requirement, welcome on in.")
    
    #make the monster
    newMonster = randomMonster()
    anotherMonster = Monster(newMonster, 14, 4, 3)
    print("\nThe monster that you have been tasked with fighting is " + newMonster + ".")
    anotherMonster.displayStats()

#run silly little program
getUserInput()
        
#def runBattle():   
    #BattleSystem.startBattle(hunter, anotherMonster)