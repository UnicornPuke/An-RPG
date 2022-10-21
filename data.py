import time
import random
from stringcolor import *
import steps

money = 0
level = 1
xp = 0
token = 0
maxp = 0
weapon = 0
armor = 0
wand = 0
charm = 0
tutorial = True
wincrease = 0
aincrease = 0
mincrease = 0
cincrease = 0
charmconfirm = False
grassconfirm = False
leafconfirm = False
stoneconfirm = False
rubyconfirm = False
titanconfirm = False
holyconfirm = False
tconfirm = False
earthconfirm = False
ironconfirm = False
chainconfirm = False
emeraldconfirm = False
mapleconfirm = False
soulconfirm = False
basicconfirm = False
starconfirm = False
flowerconfirm = False
goldconfirm = False
amethystconfirm = False
pineconeconfirm = False
grandconfirm = False
iceconfirm = False
coralconfirm = False
waterconfirm = False
obsidianconfirm = False
fireconfirm = False
emberconfirm = False
blazeconfirm = False
brimconfirm = False
lavaconfirm = False

player = {
	"maxhp": 20,
	"hp": 20,
	"attack": 20,
	"defense": 20,
	"magic": 20,
	"luck": 1
}

enemy = {
	"maxhp": 0,
	"hp": 0,
	"attack": 0,
	"defense": 0,
	"magic": 0,
	"luck": 0
}

dirt_monster = {
	"maxhp": 20,
	"hp": 20,
	"attack": 21,
	"defense": 22,
	"magic": 10,
	"luck": 1
}

goblin = {
  	"maxhp": 20,
	"hp": 20,
	"attack": 20,
	"defense": 20,
	"magic": 20,
	"luck": 2
}

zombie = {
  	"maxhp": 20,
	"hp": 20,
	"attack": 17,
	"defense": 17,
	"magic": 26,
	"luck": 2
}

grass_monster = {
  	"maxhp": 20,
	"hp": 20,
	"attack": 21,
	"defense": 22,
	"magic": 10,
	"luck": 1
}

rat = {
  	"maxhp": 1,
	"hp": 1,
	"attack": 1,
	"defense": 1,
	"magic": 1,
	"luck": 1
}

hydro_mage = {
  	"maxhp": 25,
	"hp": 25,
	"attack": 18,
	"defense": 22,
	"magic": 30,
	"luck": 3
}

shark = {
  	"maxhp": 30,
	"hp": 29,
	"attack": 20,
	"defense": 25,
	"magic": 15,
	"luck": 1
}

salmon_school = {
  	"maxhp": 25,
	"hp": 25,
	"attack": 18,
	"defense": 20,
	"magic": 16,
	"luck": 2
}

demon = {
  	"maxhp": 25,
	"hp": 25,
	"attack": 30,
	"defense": 23,
	"magic": 25,
	"luck": 1
}

lava_monster = {
  	"maxhp": 27,
	"hp": 27,
	"attack": 20,
	"defense": 20,
	"magic": 10,
	"luck": 2
}

def resc():
	for x in range(0, 1000):
		print("")
	
	print("Level", level, "XP:", xp, "/ 100        ", "Health: ", player["hp"], "/", player["maxhp"] , "      Money:", money)
	print("")
	print("")
	print("")
	print("")

def step():
	global tutorial
	global money
	global xp
	global level
	global token
	global maxp
	mashp = level
	maxp = 95 + level * 5
	mincrease = random.randint(3,6)
	xincrease = random.randint(2,4)
	money += mincrease
	xp += xincrease
	if xp >= maxp:
		xp -= maxp
		level += 1
		token += 1
	for x in range(0, 1000):
		print("")
	
	if mashp != level:
		print("You leveled up!")
		time.sleep(1.2)
		for x in range(0, 1000):
			print("")
		stats()
		print("")
		lvlup = input("Choose a stat to boost, Defemse, Magic, Luck, Max HP, or Attack. [d/m/l/hp/a (no caps)]")
		
		if lvlup == "d":
			player["defense"] += 6
		elif lvlup == "m":
			player["magic"] += 6
		elif lvlup == "l":
			player["luck"] += 1
			if player["luck"] > 10:
				player["luck"] = 10
		elif lvlup == "hp":
			player["maxhp"] += 3
			player["hp"] = player["maxhp"]
		else:
			player["attack"] += 6
	
	for x in range(0, 1000):
		print("")

	print("Level", level, "XP:", xp, "/ 100        ", "Health: ", player["hp"], "/", player["maxhp"] , "      Money:", money)
	print("")
	print("")
	print("")
	print("")

def stats():
	time.sleep(0.5)
	print("")
	print("HP:", player["maxhp"])
	time.sleep(0.5)
	print("")
	print("Attack:", player["attack"])
	time.sleep(0.5)
	print("")
	print("Defense:", player["defense"])
	time.sleep(0.5)
	print("")
	print("Magic:", player["magic"])
	time.sleep(0.5)
	print("")
	print("Luck:", player["luck"],"%")
	time.sleep(1)
	print("")
	input("Click enter to move on. ")

def shop():
	global tutorial
	global money
	global jeep
	global player
	global wincrease
	global aincrease
	global mincrease
	global cincrease
	global grassconfirm
	global iceconfirm
	global leafconfirm
	global coralconfirm
	global waterconfirm
	global tconfirm
	global earthconfirm
	global ironconfirm
	global chainconfirm
	global emeraldconfirm
	global mapleconfirm
	global soulconfirm
	global basicconfirm
	global starconfirm
	global flowerconfirm
	global goldconfirm
	global amethystconfirm
	global pineconeconfirm
	global grandconfirm
	global obsidianconfirm
	global fireconfirm
	global emberconfirm
	global blazeconfirm
	global lavaconfirm
	global brimconfirm

	for x in range(0, 1000):
		print("")
	print("Weapons")
	print("")
	print("Armor")
	print("")
	print("Wands")
	print("")
	print("Charms")
	print("")
	if tutorial == True:
		shopsy = input("Write 'weapons'. (no caps) ")
		if shopsy == "weapons":
			for x in range(0, 1000):
				print("")	
			print(cs("Stick $15", "orange3"))
			print("")
			print(cs("Grass Sword UNAVAILABLE", 'chartreuse4'))
			print("")
			print(cs("Leaf Sword UNAVAILABLE", "darkgoldenrod"))
			print("")
			print(cs("Stone Sword UNAVAILABLE", "lightgrey12"))
			print("")
			print(cs("Ruby Sword UNAVAILABLE", "red4"))
			print("")
			print(cs("Titanium Sword UNAVAILABLE", "lightgrey7"))
			print("")
			print(cs("Holy Sword UNAVAILABLE", "gold"))
			print("")
			sloppy = input("Write stick to buy it. (no caps) ")
			if sloppy == "stick":
				money -= 15
				wincrease = 3
				player["attack"] += wincrease
			else:
				print("You have failed the game, sorry.")
				exit()	  				
		else:
			print("You have failed the game, sorry.")
			exit()	  
	else:
		shopsy = input("Choose your item, or write 'exit' to leave. (no caps) ")
		if shopsy == "weapons":
			for x in range(0, 1000):
				print("")
			print(cs("Stick BOUGHT", "orange3"))
			print("")
			if grassconfirm == True:
				print(cs("Grass Sword BOUGHT", "chartreuse4"))
			else:
				print(cs("Grass Sword $50", "chartreuse4"))
			print("")
			if leafconfirm == True:
				print(cs("Leaf Sword BOUGHT", "darkgoldenrod"))
			else:
				print(cs("Leaf Sword $50", "darkgoldenrod"))
			print("")
			if iceconfirm == True:
				print(cs("Ice Spear BOUGHT", "cyan"))
			else:
				print(cs("Ice Spear $65", "cyan"))
			print("")
			if stoneconfirm == True:
				print(cs("Stone Sword BOUGHT", "lightgrey12"))
			else:
				print(cs("Stone Sword $130", "lightgrey12"))
			print("")
			if rubyconfirm == True:
				print(cs("Ruby Sword BOUGHT", "red4"))
			else:
				print(cs("Ruby Sword $250", "red4"))
			print("")
			if titanconfirm == True:
				print(cs("Titanium Sword BOUGHT", "lightgrey7"))
			else:
				print(cs("Titanium Sword $525", "lightgrey7"))
			print("")
			if fireconfirm == True:
				print(cs("Fire Sword BOUGHT", "red2"))
			else:
				print(cs("Fire Sword $530", "red2"))
			print("")
			if emberconfirm == True:
				print(cs("Ember Blade BOUGHT", "darkorange3"))
			else:
				print(cs("Ember Blade $550", "darkorange3"))
			print("")
			if holyconfirm == True:
				print(cs("Holy Sword BOUGHT", "gold"))
			else:
				print(cs("Holy Sword $1000", "gold"))
			print("")
			sloppy = input("Choose your weapon. (no caps) ")
			if sloppy == "stick":
				print("Sorry, unfortunately, you have already purchased this item.")
			if sloppy == "grass sword":
				if grassconfirm == True:
					print("")
					print("Sorry, unfortunately, you have already purchased this item.")
				else:
					if money < 50:
						print("")
						print("Sorry you do not have enough money.")
					else:
						money -= 50
						wincrease = 6
						player["attack"] += wincrease
						player["defense"] += 2
						grassconfirm = True
			if sloppy == "ice spear":
				if iceconfirm == True:
					print("")
					print("Sorry, unfortunately, you have already purchased this item.")
				else:
					if money < 65:
						print("")
						print("Sorry you do not have enough money.")
					else:
						money -= 65
						wincrease = 7
						player["attack"] += wincrease
						player["magic"] += 3
						iceconfirm = True
			if sloppy == "leaf sword":
				if leafconfirm == True:
					print("")
					print("Sorry, unfortunately, you have already purchased this item.")
				else:
					if money < 50:
						print("")
						print("Sorry you do not have enough money.")
					else:
						money -= 50
						wincrease = 6
						player["attack"] += wincrease
						player["magic"] += 2
						leafconfirm = True
			elif sloppy == "stone sword":
				if stoneconfirm == True:
					print("")
					print("Sorry, unfortunately, you have already purchased this item.")
				else:
					if money < 130:
						print("")
						print("Sorry you do not have enough money.")
					else:
						money -= 130
						wincrease = 10
						player["attack"] += wincrease
						stoneconfirm = True
			elif sloppy == "ruby sword":
				if rubyconfirm == True:
					print("")
					print("Sorry, unfortunately, you have already purchased this item.")
				else:
					if money < 250:
						print("")
						print("Sorry you do not have enough money.")
					else:
						money -= 250
						wincrease = 15
						player["attack"] += wincrease
						player["maxhp"] += 2
						player["hp"] = player["maxhp"]
						rubyconfirm = True
			elif sloppy == "titanium sword":
				if titanconfirm == True:
					print("")
					print("Sorry, unfortunately, you have already purchased this item.")
				else:
					if money < 525:
						print("")
						print("Sorry you do not have enough money.")
					else:
						money -= 525
						wincrease = 19
						player["attack"] += wincrease
						titanconfirm = True
			elif sloppy == "fire sword":
				if fireconfirm == True:
					print("")
					print("Sorry, unfortunately, you have already purchased this item.")
				else:
					if money < 530:
						print("")
						print("Sorry you do not have enough money.")
					else:
						money -= 530
						wincrease = 20
						player["attack"] += wincrease
						player["magic"] += 3
						fireconfirm = True
			elif sloppy == "ember blade":
				if emberconfirm == True:
					print("")
					print("Sorry, unfortunately, you have already purchased this item.")
				else:
					if money < 550:
						print("")
						print("Sorry you do not have enough money.")
					else:
						money -= 550
						wincrease = 21
						player["attack"] += wincrease
						player["magic"] += 5
						emberconfirm = True
			elif sloppy == "holy sword":
				if holyconfirm == True:
					print("")
					print("Sorry, unfortunately, you have already purchased this item.")
				else:
					if money < 1000:
						money -= 1000
						print("")
						print("Sorry you do not have enough money.")
					else:
						wincrease = 32
						player["attack"] += wincrease
						player["magic"] += 6
						holyconfirm = True
			else:
				print("")
				print("What do you mean?")
				time.sleep(2.5)
				for x in range(0, 1000):
					print("")
				shop()
		elif shopsy == "armor":
			for x in range(0, 1000):
				print("")
			if tconfirm == True:
				print(cs("T-Shirt BOUGHT", "lightcyan"))
			else:
				print(cs("T-Shirt $30", "lightcyan"))
			print("")
			if earthconfirm == True:
				print(cs("Earth Armor BOUGHT", 'orange2'))
			else:
				print(cs("Earth Armor $110", 'orange2'))
			print("")
			if ironconfirm == True:
				print(cs("Iron Armor BOUGHT", "lightgrey2"))
			else:
				print(cs("Iron Armor $200", "lightgrey2"))
			print("")
			if chainconfirm == True:
				print(cs("Chainmail BOUGHT", "grey7"))	
			else:
				print(cs("Chainmail $325", "grey7"))
			print("")
			if brimconfirm == True:
				print(cs("Brimstone Armor BOUGHT", "salmon"))	
			else:
				print(cs("Brimstone Armor $375", "salmon"))
			print("")
			if emeraldconfirm == True:
				print(cs("Emerald Armor BOUGHT", "seagreen3"))
			else:
				print(cs("Emerald Armor $420", "seagreen3"))
			print("")
			if lavaconfirm == True:
				print(cs("Lava Armor BOUGHT", "darkred"))
			else:
				print(cs("Lava Armor $500", "darkred"))
			print("")
			if mapleconfirm == True:
				print(cs("Maple Armor BOUGHT", "maroon"))
			else:
				print(cs("Maple Armor $585", "maroon"))
			print("")
			if obsidianconfirm == True:
				print(cs("Obsidian Armor BOUGHT", "darkgrey"))
			else:
				print(cs("Obsidian Armor $750", "darkgrey"))
			print("")
			if soulconfirm == True:
				print(cs("Soul Armor BOUGHT", "grey6"))
			else:
				print(cs("Soul Armor $1020", "grey6"))
			print("")
			sloppy = input("Choose your armor. (no caps) ")
			if sloppy == "t-shirt":
				if tconfirm == True:
					print("")
					print("Sorry, unfortunately, you have already purchased this item.")
				else:
					if money < 30:
						print("")
						print("Sorry you do not have enough money.")
					else:
						money -= 30
						aincrease = 5
						player["defense"] += aincrease
						tconfirm = True
			elif sloppy == "earth armor":
				if earthconfirm == True:
					print("")
					print("Sorry, unfortunately, you have already purchased this item.")
				else:
					if money < 110:
						print("")
						print("Sorry you do not have enough money.")
					else:
						money -= 110
						aincrease = 11
						player["defense"] += aincrease
						player["attack"] += 1
						earthconfirm = True
			elif sloppy == "iron armor":
				if ironconfirm == True:
					print("")
					print("Sorry, unfortunately, you have already purchased this item.")
				else:
					if money < 200:
						print("")
						print("Sorry you do not have enough money.")
					else:
						money -= 200
						aincrease = 15
						player["defense"] += aincrease
						ironconfirm = True
			elif sloppy == "chainmail":
				if chainconfirm == True:
					print("")
					print("Sorry, unfortunately, you have already purchased this item.")
				else:
					if money < 325:
						print("")
						print("Sorry you do not have enough money.")
					else:
						money -= 325
						aincrease = 10
						player["defense"] += aincrease
						chainconfirm = True
			elif sloppy == "brimstone armor":
				if brimconfirm == True:
					print("")
					print("Sorry, unfortunately, you have already purchased this item.")
				else:
					if money < 375:
						print("")
						print("Sorry you do not have enough money.")
					else:
						money -= 375
						aincrease = 15
						player["defense"] += aincrease
						player["magic"] += 2
						brimconfirm = True
			elif sloppy == "emerald armor":
				if emeraldconfirm == True:
					print("")
					print("Sorry, unfortunately, you have already purchased this item.")
				else:
					if money < 420:
						print("")
						print("Sorry you do not have enough money.")
					else:
						money -= 420
						aincrease = 17
						player["defense"] += aincrease
						player["maxhp"] += 1
						player["hp"] = player["maxhp"]
						emeraldconfirm = True
			elif sloppy == "lava armor":
				if lavaconfirm == True:
					print("")
					print("Sorry, unfortunately, you have already purchased this item.")
				else:
					if money < 500:
						print("")
						print("Sorry you do not have enough money.")
					else:
						money -= 500
						aincrease = 20
						player["defense"] += aincrease
						player["attack"] += 2
						player["magic"] += 3
						lavaconfirm = True
			elif sloppy == "maple armor":
				if mapleconfirm == True:
					print("")
					print("Sorry, unfortunately, you have already purchased this item.")
				else:
					if money < 585:
						print("")
						print("Sorry you do not have enough money.")
					else:
						money -= 585
						aincrease = 23
						player["defense"] += aincrease
						player["maxhp"] += 1
						player["hp"] = player["maxhp"]
						player["magic"] += 1
						player["attack"] += 1
						mapleconfirm = True
			elif sloppy == "obsidian armor":
				if obsidianconfirm == True:
					print("")
					print("Sorry, unfortunately, you have already purchased this item.")
				else:
					if money < 750:
						print("")
						print("Sorry you do not have enough money.")
					else:
						money -= 750
						aincrease = 28
						player["defense"] += aincrease
						player["maxhp"] += 2
						player["magic"] += 1
						player["hp"] = player["maxhp"]
						obsidianconfirm = True
			elif sloppy == "soul armor":
				if soulconfirm == True:
					print("")
					print("Sorry, unfortunately, you have already purchased this item.")
				else:
					if money < 1000:
						print("")
						print("Sorry you do not have enough money.")
					else:
						money -= 1000
						aincrease = 40
						player["defense"] += aincrease
						player["maxhp"] += 6
						soulconfirm = True
			else:
				print("")
				print("What do you mean?")
				time.sleep(2.5)
				for x in range(0, 1000):
					print("")
				shop()
		elif shopsy == "wands":
			for x in range(0, 1000):
				print("")
			if basicconfirm == True:
				print(cs("Basic Wand BOUGHT", "lightgoldenrod3"))
			else:
				print(cs("Basic Wand $35", "lightgoldenrod3"))
			print("")
			if blazeconfirm == True:
				print(cs("Blaze Wand BOUGHT", 'red2'))
			else:
				print(cs("Blaze Wand $100", 'red2'))
			print("")
			if starconfirm == True:
				print(cs("Star Wand BOUGHT", 'yellow2'))
			else:
				print(cs("Star Wand $120", 'yellow2'))
			print("")
			if flowerconfirm == True:
				print(cs("Flower Wand BOUGHT", "violet"))
			else:
				print(cs("Flower Wand $195", "violet"))
			print("")
			if goldconfirm == True:
				print(cs("Gold Wand BOUGHT", "gold"))	
			else:
				print(cs("Gold Wand $330", "gold"))
			print("")
			if coralconfirm == True:
				print(cs("Coral Wand BOUGHT", "pink5"))	
			else:
				print(cs("Coral Wand $400", "pink5"))
			print("")
			if waterconfirm == True:
				print(cs("Water Wand BOUGHT", "blue3"))	
			else:
				print(cs("Water Wand $400", "blue3"))
			print("")
			if amethystconfirm == True:
				print(cs("Amethyst Wand BOUGHT", "mediumpurple"))
			else:
				print(cs("Amethyst Wand $450", "mediumpurple"))
			print("")
			if pineconeconfirm == True:
				print(cs("Pinecone Wand BOUGHT", "darkorange2"))
			else:
				print(cs("Pinecone Wand $655", "darkorange2"))
			print("")
			if grandconfirm == True:
				print(cs("Grand Staff BOUGHT", "lightskyblue"))
			else:
				print(cs("Grand Staff $950", "lightskyblue"))
			print("")
			sloppy = input("Choose your wand. (no caps) ")
			if sloppy == "basic wand":
				if basicconfirm == True:
					print("")
					print("Sorry, unfortunately, you have already purchased this item.")
				else:
					if money < 35:
						print("")
						print("Sorry you do not have enough money.")
					else:
						money -= 35
						mincrease = 6
						player["magic"] += mincrease
						basicconfirm = True
			if sloppy == "blaze wand":
				if blazeconfirm == True:
					print("")
					print("Sorry, unfortunately, you have already purchased this item.")
				else:
					if money < 100:
						print("")
						print("Sorry you do not have enough money.")
					else:
						money -= 100
						mincrease = 9
						player["magic"] += mincrease
						player["attack"] += 3
						blazeconfirm = True
			elif sloppy == "star wand":
				if starconfirm == True:
					print("")
					print("Sorry, unfortunately, you have already purchased this item.")
				else:
					if money < 120:
						print("")
						print("Sorry you do not have enough money.")
					else:
						money -= 120
						mincrease = 12
						player["magic"] += mincrease
						player["defense"] += 1
						starconfirm = True
			elif sloppy == "flower wand":
				if flowerconfirm == True:
					print("")
					print("Sorry, unfortunately, you have already purchased this item.")
				else:
					if money < 195:
						print("")
						print("Sorry you do not have enough money.")
					else:
						money -= 195
						mincrease = 16
						player["magic"] += mincrease
						player["maxhp"] += 2
						player["hp"] = player["maxhp"]
						flowerconfirm = True
			elif sloppy == "gold wand":
				if goldconfirm == True:
					print("")
					print("Sorry, unfortunately, you have already purchased this item.")
				else:
					if money < 330:
						print("")
						print("Sorry you do not have enough money.")
					else:
						money -= 330
						mincrease = 21
						player["magic"] += mincrease
						goldconfirm = True
			elif sloppy == "coral wand":
				if coralconfirm == True:
					print("")
					print("Sorry, unfortunately, you have already purchased this item.")
				else:
					if money < 400:
						print("")
						print("Sorry you do not have enough money.")
					else:
						money -= 400
						mincrease = 24
						player["magic"] += mincrease
						player["defense"] += 3
						coralconfirm = True
			elif sloppy == "water wand":
				if waterconfirm == True:
					print("")
					print("Sorry, unfortunately, you have already purchased this item.")
				else:
					if money < 400:
						print("")
						print("Sorry you do not have enough money.")
					else:
						money -= 400
						mincrease = 24
						player["magic"] += mincrease
						player["attack"] += 3
						waterconfirm = True
			elif sloppy == "amethyst wand":
				if amethystconfirm == True:
					print("")
					print("Sorry, unfortunately, you have already purchased this item.")
				else:
					if money < 450:
						print("")
						print("Sorry you do not have enough money.")
					else:
						money -= 450
						mincrease = 25
						player["magic"] += mincrease
						player["maxhp"] += 1
						player["hp"] = player["maxhp"]
						player["magic"] += 2
						amethystconfirm = True
			elif sloppy == "pinecone wand":
				if pineconeconfirm == True:
					print("")
					print("Sorry, unfortunately, you have already purchased this item.")
				else:
					if money < 655:
						print("")
						print("Sorry you do not have enough money.")
					else:
						money -= 655
						mincrease = 28
						player["magic"] += mincrease
						pineconeconfirm = True
			elif sloppy == "grand staff":
				if grandconfirm == True:
					print("")
					print("Sorry, unfortunately, you have already purchased this item.")
				else:
					if money < 950:
						print("")
						print("Sorry you do not have enough money.")
					else:
						money -= 950
						mincrease = 31
						player["magic"] += mincrease
						player["maxhp"] += 6
						grandconfirm = True
			else:
				print("")
				print("What do you mean?")
				time.sleep(2.5)
				for x in range(0, 1000):
					print("")
				shop()
		elif shopsy == "charms":
			for x in range(0, 1000):
				print("")
			print("Remember, you can only buy one charm!")
			print("")
			if charmconfirm == True:
				print(cs("Terra Charm $400", "lightgoldenrod3"))
				print("")
				print(cs("Star Charm $400", 'yellow2'))
				print("")
				print(cs("Glass Charm $400", "violet"))
				print("")
				print(cs("Aqua Charm $400", "blue"))
				print("")
				print(cs("Ignis Charm $400", "red3"))
				print("")
				sloppy = input("Choose you charm (no caps) ")
			else:
				print("YOU HAVE USED YOUR ONE CHARM PURCHASE.")
				time.sleep(3)
				for x in range(0, 1000):
					print("")
				shop()
			if sloppy == "terra charm":
				if money < 400:
					print("Sorry you do not have enough money.")
				else:
					money -= 400
					cincrease = 1
					player["luck"] += cincrease
					if player["luck"] < 10:
						player["luck"] = 10
					player["defense"] += 10
					charmconfirm = True
			elif sloppy == "star charm":
				if money < 400:
					print("Sorry you do not have enough money.")
				else:
					money -= 400
					cincrease = 1
					player["luck"] += cincrease
					if player["luck"] < 10:
						player["luck"] = 10
					player["magic"] += 10
					charmconfirm = True
			elif sloppy == "glass charm":
				if money < 400:
					print("Sorry you do not have enough money.")
				else:
					money -= 400
					cincrease = 1
					player["luck"] += cincrease
					if player["luck"] < 10:
						player["luck"] = 10
					player["attack"] += 10
					charmconfirm = True
			elif sloppy == "aqua charm":
				if money < 400:
					print("Sorry you do not have enough money.")
				else:
					money -= 400
					cincrease = 1
					player["luck"] += cincrease
					if player["luck"] < 10:
						player["luck"] = 10
					player["magic"] += 5
					player["attack"] += 5
					charmconfirm = True
			elif sloppy == "ignis charm":
				if money < 400:
					print("Sorry you do not have enough money.")
				else:
					money -= 400
					cincrease = 1
					player["luck"] += cincrease
					if player["luck"] < 10:
						player["luck"] = 10
					player["magic"] += 2
					player["attack"] += 8
					charmconfirm = True
			else:
				print("")
				print("What do you mean?")
				time.sleep(2.5)
				for x in range(0, 1000):
					print("")
				shop()
		elif shopsy == "exit":
			time.sleep(0.1)
		else:
			shop()
		resc()
		input("Click enter to move on.")

	

def combat():
	global enemy
	global player
	global money
	global xp
	for x in range(0, 1000):
		print("")
	if tutorial == False:
		for x in range(0, 1000):
			for x in range(0, 1000):
				print("")
			print("Opponent:", enemy["hp"], "/", enemy["maxhp"], "                                You:", player["hp"], "/", player["maxhp"])
			print("")
			print("")
			print("")
			print("")
			comresp = input("Magic/Attack/Heal [m/a/h (no caps)] ")
			if comresp == "m":
				mag = round(player["magic"] / 4) - round(enemy["defense"] / 10)
				if mag < 0:
					mag = 0
				crit = random.randint(1, 100)
				if crit <= player["luck"]:
					mag += round(mag / 2)
				enemy["hp"] -= mag
			elif comresp == "a":
				atta = round(player["attack"] / 4) - round(enemy["defense"] / 10)
				if atta < 0:
					atta = 0
				crit = random.randint(1, 100)
				if crit <= player["luck"]:
					atta += round(atta / 2)
				enemy["hp"] -= atta
			else:
				player["hp"] += 4
				if player["hp"] > player["maxhp"]:
					player["hp"] = player["maxhp"]

			enemydis = random.randint(1,3)
			if enemydis == 1:
				mag = round(enemy["magic"] / 4) - round(player["defense"] / 10)
				if mag < 0:
					mag = 0
				crit = random.randint(1, 100)
				if crit <= enemy["luck"]:
					mag += round(mag / 2)
				player["hp"] -= mag
			elif enemydis == 2:
				atta = round(enemy["attack"] / 4) - round(player["defense"] / 10)
				if atta < 0:
					atta = 0
				crit = random.randint(1, 100)
				if crit <= enemy["luck"]:
					atta += round(atta / 2)
				player["hp"] -= atta
			elif enemydis == 3:
				enemy["hp"] += 2
				if enemy["hp"] > enemy["maxhp"]:
					enemy["hp"] = enemy["maxhp"]

			if player["hp"] <= 0:
				print("")
				print(cs("You died.", "red"))
				exit()
			elif enemy["hp"] <= 0:
				enemy["hp"] = enemy["maxhp"]
				break
		print("")
		print("You have won the battle.")
		money += 50
		xp += 15
		print("")
		time.sleep(2)
		resc()
		input("Click enter to move on.")
	else:
		print("Opponent: 10 / 10                                 You: 20 / 20")
		print("")
		print("")
		print("")
		print("")
		tutresp = input("This is the combat menu. writing 'a' attacks, 'm' to use magic, and 'h' to heal. Write 'a' (no caps) to attack. ")
		if tutresp != "a":
			print("")
			tutresp = input("Follow my instructions!")
			if tutresp != "a":
				print("")
				print("YOU FAILED!")
				exit()
		for x in range(0, 1000):
			print("")
		print("Opponent: 4 / 10                                 You: 18 / 20")
		print("")
		print("")
		print("")
		print("")
		tutresp = input("The opponent can also attack you. Now that the opponent only has 4 hp, write 'm' (no caps) to magic it away! ")
		if tutresp != "m":
			print("")
			tutresp = input("Follow my instructions!")
			if tutresp != "m":
				print("")
				print("YOU FAILED!")
				exit()
		print("")
		print("You win!")
		time.sleep(2)
		resc()
		


print("booting...")