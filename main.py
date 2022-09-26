from data import *
from stringcolor import * 
import time
import random

for x in range(0, 1000):
	print("")

print ("Welcome to "+cs("A", "red2") +cs("n", "orangered") +cs(" R", "yellow3") +cs("P", "green") +cs("G", "skyblue") +cs("!", "violet"))
time.sleep(1.5)
print("")
print ("Here in "+cs("A", "red2") +cs("n", "orangered") +cs(" R", "yellow3") +cs("P", "green") +cs("G", "skyblue") +cs(", You'll explore a vast land filled with wonder and mystery!", "white"))
time.sleep(2.75)
print("")
print("Here are your stats:")
stats()
time.sleep(2.5)
print("")
print("You probably don't know what these mean, however you will later.")
time.sleep(2.5)
print("")
print("Let's go somewhere else shall we?")
time.sleep(2.5)

for x in range(0, 1000):
	print("")

time.sleep(1)
print("This place feels much better.")
time.sleep(1.59)
print("")
input("Press enter to continue,")
print("")
input("You'll have to do this a lot.")
print("")
input("Anyways, I'll explain your stats,")
print("")
input("First, Max HP, this is how much your health can go to.")
print("")
input("Second, Attack, this is how much damage physical attacks do.")
print("")
input("Third, Magic, this is how much damage magical attacks do.")
print("")
input("Finally, Luck, this is your chance of hitting a critical hit.")
print("")
input("Now that you're all caught up, let's go on an adventure")

resc()
input("Take a step by pressing enter.")
step()
input("Take another one,")
step()
input("Another,")
step()
input("Another,")
step()
input("Great!") 
step()
thing = input("Now to access the shop, write 'shop' (no caps) and click enter. ")
if thing == "shop":
	shop()
else:
	print("You have failed the game, sorry.")
	exit()