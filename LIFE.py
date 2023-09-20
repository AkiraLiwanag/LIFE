import random
import time
import sys
import os

os.system('clear')
os.system("CLS")

print()
print("Incubator Studios presents ~ LIFE GAME ~ Created by A.A.P.L. All Rights Reserved /donate")
print()
time.sleep(3)

def displayIntro():
	print()
	print ("pray, sleep, eat, meditate, draw card, slot, find coins, search for items, fly, drink coffee, drink tea")
	print()


def choice():
	choice = ''
	while choice !='pray' and choice !='slot' and choice !='search for items' and choice !='sleep' and choice !='eat' and choice !='meditate' and choice !='find coins' and choice !='draw card' and choice !='fly' and choice !='drink coffee' and choice !='drink tea':
		print("what do you want to do?")
		choice = input()
		if choice == "pray":
			print("You start praying to a God...")
			time.sleep(7)
			print("You finished praying")
			time.sleep(3)
			print()
		if choice == "meditate":
			print("You sit and start to meditate...")
			time.sleep(16)
			print("You finished meditating")
			time.sleep(3)
			print()
		if choice == "sleep":
			print("You lay down and doze off...")
			time.sleep(29)
			print("You wake up")
			time.sleep(3)
			print()
		if choice == "eat":
			print("You prepare food and start to consume a meal...")
			time.sleep(5)
			print("You have eaten")
			time.sleep(3)
			print()
		if choice == "find coins":
			print("You start to search around for coins...")
			time.sleep(10)
			print("You found:")
			print(random.randint(0,100))
			print("coins")		
			time.sleep(3)
			print()
		if choice == "slot":
			print("You pull on the slot lever...")
			time.sleep(5)
			slot = random.choices(range(10), k=3)
			print(slot)
			time.sleep(3)
			print()
		if choice == "draw card":
			print("You draw a card from a deck...")
			time.sleep(2)
			deck = ["Ace of Hearts", "Two of Hearts", "Three of Hearts", "Four of Hearts", "Five of Hearts", "Six of Hearts", "Seven of Hearts", "Eight of Hearts", "Nine of Hearts", "Ten of Hearts", "Jack of Hearts", "Queen Of Hearts", "King of Hearts", "Ace of Clubs", "Two of Clubs", "Three of Clubs", "Four of Clubs", "Five of Clubs", "Six of Clubs", "Seven of Clubs", "Eight of Clubs", "Nine of Clubs", "Ten of Clubs", "Jack of Clubs", "Queen Of Clubs", "King of Clubs", "Ace of Diamonds", "Two of Diamonds", "Three of Diamonds", "Four of Diamonds", "Five of Diamonds", "Six of Diamonds", "Seven of Diamonds", "Eight of Diamonds", "Nine of Diamonds", "Ten of Diamonds", "Jack of Diamonds", "Queen Of Diamonds", "King of Diamonds", "Ace of Spades", "Two of Spades", "Three of Spades", "Four of Spades", "Five of Spades", "Six of Spades", "Seven of Spades", "Eight of Spades", "Nine of Spades", "Ten of Spades", "Jack of Spades", "Queen Of Spades", "King of Spades", "Joker", "Joker"]
			card = random.sample(deck, 1)
			print("You drew:")
			print(card)
			time.sleep(3)
			print()
		if choice == "search for items":
			print("You search around...")
			time.sleep(10)
			items = ["empty bottle", "bottle of wine", "wine glass", "bottle of iced tea", "energy drink", "lemon juice", "pack of green peas", "shirt", "bed", "headphones", "earphones", "blanket", "tablet", "kindle", "pills", "pack of coffee beans", "cup of coffee", "junkfood", "medicine", "spoon", "fork", "Nintendo Switch", "laptop", "mobile phone", "electric fan", "chair", "guitar", "keyboard", "piano", "tv", "monitor", "oil", "hashish", "marijuana", "cigarette", "vape", "pillow", "dog food", "bike", "car", "scooter", "skateboard", "printer", "shards of glass", "garbage", "strips of sleather", "food", "bottle of water", "bible", "Dhammapada", "yoga mat", "helmet", "chewing gum", "vitamins", "shirt", "sweater", "pants", "working pants", "skirt", "underwear", "parachute", "gun", "knife", "sword", "katana", "oatmeal", "chain", "slippers", "shoes", "book", "wires", "credit card", "stove", "oven", "hat", "bucket hat", "baseball cap", "beanie", "hoodie", "necklace", "ring", "gold ring", "diamond ring", "diamond", "diamonds", "painting", "pencil", "ballpoint pen", "sketchpad", "crayon", "box of crayons", "paint", "spray paint", "fruit", "lettuce", "carrot", "watermelon", "orange", "apple", "banana", "pear", "gold", "gold bar", "pistol", "lantern", "lamp", "umbrella", "newspaper", "Sega", "ecstasy", "Nintendo 64", "calculator", "brownies", "pie", "loaf bread", "aviator shades", "shutter shades", "CD", "floppy disk", "mp3 player", "walkman", "cassette", "ticket", "food stub", "ski mask", "spear", "nunchucks", "frying pan", "beans", "charger", "guitar pick", "mic", "digicam", "GoPro", "night vision goggles", "sniper rifle", "DS4 Playstation controller", "CDJ", "Raybans", "smartwatch", "modem", "axe"]
			item = random.sample(items, 2)
			print("You found:")
			print(item)
			time.sleep(3)
			print()
		if choice == "fly":
			print("You go to the airport and board a plane...")
			time.sleep(15)
			print("You arrived in:")
			countries = ["Canada", "Sweden", "China", "Beijing", "New York", "California", "L.A.", "San Francisco", "Detroit", "Colorado", "Newark", "New Jersey", "Australia", "Gold Coast", "Thailand", "North Korea", "Pyongyang", "Seoul", "Tokyo", "Osaka", "Japan", "Fujian", "Kyoto", "Manila", "Palawan", "Siargao", "Sultan Kudarat", "Davao", "Sydney", "Poland", "Uzebkistan", "Kyrgystan", "Turkey", "Iraq", "Iran", "Bolivia", "Iceland", "Lithuania", "Greenland", "UK", "France", "Spain", "Rome", "Greece", "Amsterdam", "Netherlands", "Boracay", "Indonesia", "Russia", "Ukraine", "Africa", "Antarctica", "Alaska", "South Carolina", "North Carolina", "Philadelphia", "Brooklyn", "Mexico", "Brazil", "Taiwan", "Burma", "Cambodia", "Vietnam", "India", "Bangladesh", "New Delhi", "Bombay", "Philippines"]
			country = random.sample(countries, 1)
			print(country)
			time.sleep(3)
			print()
		if choice == "drink coffee":
			print("You have coffee and feel the effect of caffeine...")
			time.sleep(7)
			print("You finished drinking your coffee")
			time.sleep(3)
			print()
		if choice == "drink tea":
			print("You have tea...")
			time.sleep(7)
			print("You finish your tea")
			time.sleep(3)
			print()
		if choice == "donate":
			print("Contact me at akiraliwanag@gmail.com")
			time.sleep(5)
		if choice == "exit":
			exit()
		if choice == "close":
			exit()
		if choice == "quit":
			exit()


chooseAgain = "yes"
while chooseAgain:
	displayIntro()
	choice()
	print()

chooseAgain = input()







