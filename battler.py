#Battle Simulation
import random

def monsterSelect():
    monsterFile = open("monsters.txt", "r" )
    monsters = monsterFile.read().split("\n")
    monsterFile.close()

    for i in range(len(monsters)):
        monsters[i] = monsters[i].split(",")

    return monsters[random.randint(0,len(monsters)-1)]

def battle():
    monster = monsterSelect()
    monsterName, monsterHP, monsterMinDamage, monsterMaxDamage = monster[0], int(monster[1]), int(monster[2]),int(monster[3])
    playerName, playerHP, playerMinDamage, playerMaxDamage = "Joe", 20, 5, 10

    while playerHP > 0 and monsterHP > 0:
        print(monsterName)
        print("HP:" , monsterHP , "\n")
        #right now, attack is the only command
        command = input("What do you want to do? (attack) ")

        if command == "attack":
            print(playerName + " attacks!")
            damage = random.randint(playerMinDamage, playerMaxDamage)
            print(playerName + " deals" , damage , "damage points" + "\n")
            monsterHP -= damage

            print(monsterName + " attacks!")
            damage = random.randint(monsterMinDamage, monsterMaxDamage)
            print(monsterName + " deals" , damage , "damage points" + "\n")
            playerHP -= damage

battle()