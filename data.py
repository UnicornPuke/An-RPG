import time
import random

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

def shop():
	global tutorial
	for x in range(0, 1000):
		print("")
	print("Weapons")
	print("")
	print("Armor")
	print("")
	print("Wands")
	print("")
	print("Charms")
	if tutorial == True:
		shopsy = input("Write 'weapons'. (no caps)")
	else:
		shopsy = input("Choose your items. (no caps)")

def resc():
	for x in range(0, 1000):
		print("")
	
	print("Level", level, "XP:", xp, "/ 100", "      Money:", money)
	print("")
	print("")
	print("")
	print("")

def step():
	global money
	global xp
	global level
	global token
	global maxp
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
	
	print("Level", level, "XP:", xp, "/ 100", "      Money:", money)
	print("")
	print("")
	print("")
	print("")

def stats():
	time.sleep(0.5)
	print("")
	print("HP:", player.maxhp)
	time.sleep(0.5)
	print("")
	print("Attack:", player.attack)
	time.sleep(0.5)
	print("")
	print("Defense:", player.defense)
	time.sleep(0.5)
	print("")
	print("Magic:", player.magic)
	time.sleep(0.5)
	print("")
	print("Luck:", player.luck,"%")


class player:
	maxhp = 20
	hp = 20
	attack = 20
	defense = 20
	magic = 20
	luck = 1
