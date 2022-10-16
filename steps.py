import random
import data
from stringcolor import *

jeep = " "
shtep = 0

def sheep():
    global shtep
    
    shtep = random.randint(1,100)

    if shtep == 1 or shtep == 2 or shtep == 43:
        data.enemy = data.rat
        input("Aaah! It's a rat, hope he doesn't cook some cheeses! ")
        data.combat()
    
    elif shtep == 3 or shtep == 4 or shtep == 5 or shtep == 6 or shtep == 7:
        jeep = "You walk forward and literally nothing interesting happens. (Your life is boring!) "
        shlep = input(jeep)
        if shlep == "stats":
            data.stats()
        if shlep == "shop":
            data.shop()
    
    elif shtep == 8 or shtep == 42:
        jeep = "An old lady screams at you for some 'You killed my son' junk. "
        shlep = input(jeep)
        if shlep == "stats":
            data.stats()
        if shlep == "shop":
            data.shop()
    elif shtep == 9 or shtep == 10 or shtep == 11:
        data.enemy = data.grass_monster
        jeep = "Some grass pops out of the ground and attacks you! (No, you can't eat it Jerry!) "
        input(jeep)
        data.combat()
    elif shtep == 11 or shtep == 12:
        jeep = "A river crossing comes ahead, and you cross it. What? Did you want something extrvagant? It's a bridge. "
        shlep = input(jeep)
        if shlep == "stats":
            data.stats()
        if shlep == "shop":
            data.shop()
    elif shtep == 13 or shtep == 50:
        jeep = "You see a rainbow and are immediately washes you with regret. From what? Taxes, Obviously. "
        shlep = input(jeep)
        if shlep == "stats":
            data.stats()
        if shlep == "shop":
            data.shop()
    elif shtep == 14 or shtep == 15 or shtep == 16:
        data.enemy = data.dirt_monster
        jeep = "Some dirt pops out of the ground and attacks you! (No, it's not pudding Jerry!) "
        input(jeep)
        data.combat()
    elif shtep == 17 or shtep == 18 or shtep == 19:
        jeep = "You check your phone for the time, then you realise that phones haven't been invented. "
        shlep = input(jeep)
        if shlep == "stats":
            data.stats()
        if shlep == "shop":
            data.shop()
    elif shtep == 20 or shtep == 21 or shtep == 41:
        data.enemy = data.goblin
        jeep = "'Heh, heh heh' As you hear that you think 'It's a bird, it's a plane, no, it's a goblin!' "
        input(jeep)
        data.combat()
    elif shtep == 22 or shtep == 23:
        jeep = "An old guy screams: 'The world is flat! The end is nigh! We are all doooooooooommmed!' "
        shlep = input(jeep)
        if shlep == "stats":
            data.stats()
        if shlep == "shop":
            data.shop()
    elif shtep == 24 or shtep == 25 or shtep == 26 or shtep == 27 or shtep == 28:
        jeep = "You drink a mysterious potion on the ground and you heal. "
        shlep = input(jeep)
        data.player["hp"] = data.player["maxhp"]
        if shlep == "stats":
            data.stats()
        if shlep == "shop":
            data.shop()
    elif shtep == 29 or shtep == 30:
        jeep = "You drink a mysterious potion on the ground and you feel like you got salmonella. "
        shlep = input(jeep)
        data.player["hp"] -= 5
        if data.player["hp"] <= 0:
            print("")
            print(cs("You died.", "red"))
            exit()
        if shlep == "stats":
            data.stats()
        if shlep == "shop":
            data.shop()
    elif shtep == 31 or shtep == 32:
        jeep = "You eat some strawberries, and then realise that you are allergic. "
        shlep = input(jeep)
        if shlep == "stats":
            data.stats()
        if shlep == "shop":
            data.shop()
    elif shtep == 33 or shtep == 34 or shtep == 35:
        jeep = "You feel as if someone is watching you, you tremble and shake, and continue onwards. "
        shlep = input(jeep)
        if shlep == "stats":
            data.stats()
        if shlep == "shop":
            data.shop()
    elif shtep == 36 or shtep == 37:
        jeep = "You find a deadly bomb that could kill millions. Anyways, you get distracted by a pretty flower. "
        shlep = input(jeep)
        if shlep == "stats":
            data.stats()
        if shlep == "shop":
            data.shop()
    elif shtep == 38 or shtep == 39 or shtep == 40:
        jeep = "You find a deadly bomb that could kill millions. Anyways, you get distracted by a pretty flower. "
        shlep = input(jeep)
        if shlep == "stats":
            data.stats()
        if shlep == "shop":
            data.shop()
    elif shtep == 44 or shtep == 45:
        jeep = "You see people fighting in a love hexagon. No, not a love triangle, a hexagon, with 6 people. "
        shlep = input(jeep)
        if shlep == "stats":
            data.stats()
        if shlep == "shop":
            data.shop()
    elif shtep == 46 or shtep == 47 or shtep == 48:
        jeep = "You ride the waves (dude). Except, they're not water, it's dirt waves! "
        shlep = input(jeep)
        if shlep == "stats":
            data.stats()
        if shlep == "shop":
            data.shop()
    elif shtep == 49:
        jeep = "You accidentally drink some mud from a river. Gross, dude! "
        shlep = input(jeep)
        data.player["hp"] -= 3
        if data.player["hp"] <= 0:
            print("")
            print(cs("You died.", "red"))
            exit()
        if shlep == "stats":
            data.stats()
        if shlep == "shop":
            data.shop()
    elif shtep == 51 or shtep == 52:
        jeep = "You ride the waves (dude). Except, they're not water, it's dirt waves! "
        shlep = input(jeep)
        if shlep == "stats":
            data.stats()
        if shlep == "shop":
            data.shop()
    elif shtep == 53 or shtep == 54 or shtep == 55:
        jeep = "You try to eat a potato chip and fail miserably. "
        shlep = input(jeep)
        if shlep == "stats":
            data.stats()
        if shlep == "shop":
            data.shop()
    elif shtep == 56 or shtep == 57 or shtep == 58 or shtep == 59 or shtep == 60:
        jeep = "You just chill...that's literally it. "
        shlep = input(jeep)
        if shlep == "stats":
            data.stats()
        if shlep == "shop":
            data.shop()
    elif shtep == 61 or shtep == 62:
        jeep = "You hitup your friend Jimmy...by carrier pigeon. "
        shlep = input(jeep)
        if shlep == "stats":
            data.stats()
        if shlep == "shop":
            data.shop()
    elif shtep == 63 or shtep == 64 or shtep == 65:
        jeep = "You find someone who is definitely not a spy. "
        shlep = input(jeep)
        if shlep == "stats":
            data.stats()
        if shlep == "shop":
            data.shop()
    elif shtep == 66 or shtep == 67:
        jeep = "You fart and try to hide it, but 20 people stare at you. "
        shlep = input(jeep)
        if shlep == "stats":
            data.stats()
        if shlep == "shop":
            data.shop()
    elif shtep == 68 or shtep == 69 or shtep == 70 or shtep == 71 or shtep == 72:
        jeep = "You drink some healing water and feel holy all of a sudden. "
        data.player["hp"] = data.player["maxhp"]
        shlep = input(jeep)
        if shlep == "stats":
            data.stats()
        if shlep == "shop":
            data.shop()
    elif shtep == 73 or shtep == 74 or shtep == 75:
        jeep = "Someone keeps asking you spill the beans. So you steal his can, and dumped it out on his head. "
        shlep = input(jeep)
        if shlep == "stats":
            data.stats()
        if shlep == "shop":
            data.shop()
    elif shtep == 76 or shtep == 77:
        jeep = "... Oh yeah, I got bored of narration. "
        shlep = input(jeep)
        if shlep == "stats":
            data.stats()
        if shlep == "shop":
            data.shop()
    elif shtep == 78 or shtep == 79 or shtep == 80:
        jeep = "You hear a car horn, then you realise it's a trumpet. "
        shlep = input(jeep)
        if shlep == "stats":
            data.stats()
        if shlep == "shop":
            data.shop()
    elif shtep == 81 or shtep == 82:
        jeep = "You want to check twitter, then you cry inside. "
        shlep = input(jeep)
        if shlep == "stats":
            data.stats()
        if shlep == "shop":
            data.shop()
    elif shtep == 83 or shtep == 84 or shtep == 85:
        jeep = "You cry inside realising this is your life now. "
        shlep = input(jeep)
        if shlep == "stats":
            data.stats()
        if shlep == "shop":
            data.shop()
    elif shtep == 86 or shtep == 87 or shtep == 88 or shtep == 89 or shtep == 90:
        jeep = "You prick your finger. "
        shlep = input(jeep)
        data.player["hp"] -= 1
        if data.player["hp"] <= 0:
            print("")
            print(cs("You died.", "red"))
            exit()
        if shlep == "stats":
            data.stats()
        if shlep == "shop":
            data.shop()
    elif shtep == 91 or shtep == 89:
        jeep = "You pick up your paycheck at work. "
        shlep = input(jeep)
        data.money += 15
        if shlep == "stats":
            data.stats()
        if shlep == "shop":
            data.shop()
    elif shtep == 93 or shtep == 94 or shtep == 95:
        jeep = "You eat some Chinese food and feel good inside. "
        shlep = input(jeep)
        if shlep == "stats":
            data.stats()
        if shlep == "shop":
            data.shop()
    elif shtep == 96 or shtep == 97:
        jeep = "It starts raining pasta, then you realise you are hallucinating from heat exhaustion. "
        shlep = input(jeep)
        if shlep == "stats":
            data.stats()
        if shlep == "shop":
            data.shop()
    elif shtep == 98 or shtep == 99 or shtep == 100:
        jeep = "You propose to the love of your life, a cactus. "
        shlep = input(jeep)
        if shlep == "stats":
            data.stats()
        if shlep == "shop":
            data.shop()
