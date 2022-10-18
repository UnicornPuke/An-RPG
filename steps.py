import random
import data
from stringcolor import *

jeep = " "
shtep = 0

def sheep():
    global shtep
    global enemy
    
    shtep = random.randint(1,200)

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
        jeep = "You hit up your friend Jimmy...by carrier pigeon. "
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
    elif shtep == 101 or shtep == 102:
        data.enemy = data.hydro_mage
        input("Some old guy says he's a mage and that you're on his territory. ")
        data.combat()
    elif shtep == 103 or shtep == 104 or shtep == 105:
        data.enemy = data.shark
        input("A shark tries to bite you! ")
        data.combat()
    elif shtep == 106 or shtep == 107:
        data.enemy = data.salmon_school
        input("Remember that piece of salmon you ate 2 years ago? Yeah, his friends are coming after you. ")
        data.combat()
    elif shtep == 108 or shtep == 109 or shtep == 110:
        jeep = "Some 7 year old squirts you with a water gun. "
        shlep = input(jeep)
        if shlep == "stats":
            data.stats()
        if shlep == "shop":
            data.shop()
    elif shtep == 111 or shtep == 112:
        jeep = "You miss your mommy. "
        shlep = input(jeep)
        if shlep == "stats":
            data.stats()
        if shlep == "shop":
            data.shop()
    elif shtep == 113 or shtep == 114 or shtep == 115:
        jeep = "You eat some [REDACTED] brand cereal with some [REDACTED] brand granola bars. "
        shlep = input(jeep)
        if shlep == "stats":
            data.stats()
        if shlep == "shop":
            data.shop()
    elif shtep == 116 or shtep == 117:
        jeep = "You think of a really good comeback of an argument you had 7 years ago. "
        shlep = input(jeep)
        if shlep == "stats":
            data.stats()
        if shlep == "shop":
            data.shop()
    elif shtep == 118 or shtep == 119 or shtep == 120:
        jeep = "You read an article in the paper about a tsunami washing over a large city. "
        shlep = input(jeep)
        if shlep == "stats":
            data.stats()
        if shlep == "shop":
            data.shop()
    elif shtep == 121 or shtep == 122:
        jeep = "You find 20 dollars on the ground. "
        data.money += 20
        shlep = input(jeep)
        if shlep == "stats":
            data.stats()
        if shlep == "shop":
            data.shop()
    elif shtep == 123 or shtep == 124 or shtep == 125:
        jeep = "You walk. (I'm running out of ideas, okay?) "
        shlep = input(jeep)
        if shlep == "stats":
            data.stats()
        if shlep == "shop":
            data.shop()
    elif shtep == 126 or shtep == 127:
        jeep = "You collect an XP orb. "
        data.xp += 20
        shlep = input(jeep)
        if shlep == "stats":
            data.stats()
        if shlep == "shop":
            data.shop()
    elif shtep == 128 or shtep == 129 or shtep == 130:
        jeep = "You trip and fall down the stairs for 2 minutes straight. "
        data.player["hp"] -= 3
        if data.player["hp"] <= 0:
            print("")
            print(cs("You died.", "red"))
            exit()
        shlep = input(jeep)
        if shlep == "stats":
            data.stats()
        if shlep == "shop":
            data.shop()
    elif shtep == 131 or shtep == 132:
        jeep = "You get your nails done. "
        shlep = input(jeep)
        if shlep == "stats":
            data.stats()
        if shlep == "shop":
            data.shop()
    elif shtep == 133 or shtep == 134 or shtep == 135:
        jeep = "Hey! Wake up! Stop sleeping! "
        shlep = input(jeep)
        if shlep == "stats":
            data.stats()
        if shlep == "shop":
            data.shop()
    elif shtep == 136 or shtep == 137:
        jeep = "A seaman shouts at you about something related to you stealing his catch. "
        shlep = input(jeep)
        if shlep == "stats":
            data.stats()
        if shlep == "shop":
            data.shop()
    elif shtep == 138 or shtep == 139 or shtep == 140:
        jeep = "You hear beautiful piano music. You later realise that a parakeet is singing. "
        shlep = input(jeep)
        if shlep == "stats":
            data.stats()
        if shlep == "shop":
            data.shop()
    elif shtep == 141 or shtep == 142:
        jeep = "Some sailors start singing a sea chanty and you join in. "
        shlep = input(jeep)
        if shlep == "stats":
            data.stats()
        if shlep == "shop":
            data.shop()
    elif shtep == 143 or shtep == 144 or shtep == 145:
        jeep = "I'm bored! Can you be more interesting? "
        shlep = input(jeep)
        if shlep == "stats":
            data.stats()
        if shlep == "shop":
            data.shop()
    elif shtep == 146 or shtep == 147:
        jeep = "A clown is juggling balls unicycling around town. "
        shlep = input(jeep)
        if shlep == "stats":
            data.stats()
        if shlep == "shop":
            data.shop()
    elif shtep == 148 or shtep == 149 or shtep == 150:
        jeep = "You enter a mall and you see Jerry and you run up for a hug. "
        shlep = input(jeep)
        if shlep == "stats":
            data.stats()
        if shlep == "shop":
            data.shop()
    elif shtep == 151 or shtep == 152:
        jeep = "You see a birthday party for a 6 year old. They think that you are the 6 year old, and pull you over. "
        shlep = input(jeep)
        if shlep == "stats":
            data.stats()
        if shlep == "shop":
            data.shop()
    elif shtep == 153 or shtep == 154 or shtep == 155:
        jeep = "A person eats an apple and collapses. Then you see a witch grinning in the background. "
        shlep = input(jeep)
        if shlep == "stats":
            data.stats()
        if shlep == "shop":
            data.shop()
    elif shtep == 156 or shtep == 157:
        jeep = "You get on a sailboat. The sailors kick you out, since this is not your boat. "
        shlep = input(jeep)
        if shlep == "stats":
            data.stats()
        if shlep == "shop":
            data.shop()
    elif shtep == 158 or shtep == 159 or shtep == 160:
        jeep = "You break out into a spontaneous musical number. "
        shlep = input(jeep)
        if shlep == "stats":
            data.stats()
        if shlep == "shop":
            data.shop()
    elif shtep == 161 or shtep == 162:
        jeep = "The president awards you a medal of honor. Then he says 'Whoops!' and takes it from you. "
        shlep = input(jeep)
        if shlep == "stats":
            data.stats()
        if shlep == "shop":
            data.shop()
    elif shtep == 163 or shtep == 164 or shtep == 165:
        jeep = "The moon shines on you and only you. "
        shlep = input(jeep)
        if shlep == "stats":
            data.stats()
        if shlep == "shop":
            data.shop()
    elif shtep == 166 or shtep == 167:
        jeep = "Hmmm Hmm! Oh, sorry I was humming. "
        shlep = input(jeep)
        if shlep == "stats":
            data.stats()
        if shlep == "shop":
            data.shop()
    elif shtep == 168 or shtep == 169 or shtep == 170:
        jeep = "You dance randomly. "
        shlep = input(jeep)
        if shlep == "stats":
            data.stats()
        if shlep == "shop":
            data.shop()
    elif shtep == 171 or shtep == 172 or shtep == 173:
        data.enemy = data.zombie
        jeep = "Ah! It's a zombie! "
        data.combat()
    elif shtep == 174 or shtep == 175:
        jeep = "Ew! You stepped in dog poop! "
        shlep = input(jeep)
        if shlep == "stats":
            data.stats()
        if shlep == "shop":
            data.shop()
    elif shtep == 176 or shtep == 178 or shtep == 179:
        jeep = "Why do I hear boss music? "
        shlep = input(jeep)
        if shlep == "stats":
            data.stats()
        if shlep == "shop":
            data.shop()
    elif shtep == 180 or shtep == 181 or shtep == 185:
        jeep = "You get pickpocketed by a shady figure named Randy. "
        data.money -= 50
        if data.money < 0:
            data.money = 0
        shlep = input(jeep)
        if shlep == "stats":
            data.stats()
        if shlep == "shop":
            data.shop()
    elif shtep == 182 or shtep == 183 or shtep == 184:
        jeep = "You run and run training for the fight against your self-confidence. "
        shlep = input(jeep)
        if shlep == "stats":
            data.stats()
        if shlep == "shop":
            data.shop()
    elif shtep == 186 or shtep == 187:
        jeep = "Let's go! You murdered 2 civilians while trying to get a hot dog! "
        shlep = input(jeep)
        if shlep == "stats":
            data.stats()
        if shlep == "shop":
            data.shop()
    elif shtep == 188 or shtep == 189 or shtep == 190:
        jeep = "Beep boop, I am a robot. Oh, sorry, I was doing personal stuff. "
        shlep = input(jeep)
        if shlep == "stats":
            data.stats()
        if shlep == "shop":
            data.shop()
    elif shtep == 191 or shtep == 192:
        jeep = "Do you ever feel, like a- oh? We'll get sued by Katy Perry if I keep singing? Ok. "
        shlep = input(jeep)
        if shlep == "stats":
            data.stats()
        if shlep == "shop":
            data.shop()
    elif shtep == 193 or shtep == 194 or shtep == 195:
        jeep = "You play some Just Dance 2023 edition! "
        shlep = input(jeep)
        if shlep == "stats":
            data.stats()
        if shlep == "shop":
            data.shop()
    elif shtep == 196 or shtep == 197:
        jeep = "You see a poster and realise that the FBI is coming for you. "
        shlep = input(jeep)
        if shlep == "stats":
            data.stats()
        if shlep == "shop":
            data.shop()
    elif shtep == 198 or shtep == 199 or shtep == 200:
        jeep = "Your pal Jimmy calls you and says something about how he's dying and you need to help him. But you hang up. "
        shlep = input(jeep)
        if shlep == "stats":
            data.stats()
        if shlep == "shop":
            data.shop()