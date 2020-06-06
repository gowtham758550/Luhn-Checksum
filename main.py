#author = <gowtham758550@gmail.com>
#Check a credit card is valid or not
#Luhn Algorithm - With this algorithm credit, debit card numbera are generated
#Make use of that algorithm logic to validate card numbers
#Many websites gives free card numbers based on this algorithm
#Some of indentification number issued by the government follow this algorithm
#If u found any bug in this program or logical error
#please make pull request or an issue

#import requires os module
import os

#function to clear screen
def clear_screen():
	x = input("\n\nPress enter to continue")
	os.system('clear' if os.name == 'posix' else 'cls')


#Function to check a input is a valid card number
def check(card,length):
	sum = 0
	list = [int(x) for x in card]
	second = False
	for i in list:
		if second == True:
			i = i*2
		#to sum the digits if it is more than 9
		sum += i//10
		sum += i%10
		#to make the above if condition true 
		second = not(second)
	if sum%10 == 0:
		return True
	else:
		return False

while(True):
	print("   ____              _              _ _     _       _             ")
	print(" / ___|__ _ _ __ __| | __   ____ _| (_) __| | __ _| |_ ___  _ __ ")
	print("| |   / _` | '__/ _` | \ \ / / _` | | |/ _` |/ _` | __/ _ \| '__|")
	print("| |__| (_| | | | (_| |  \ V / (_| | | | (_| | (_| | || (_) | |   ")
	print(" \____\__,_|_|  \__,_|   \_/ \__,_|_|_|\__,_|\__,_|\__\___/|_|   ")
	print("\n\nEnter the credit card number : ",end = '')
	while(True):
		try:
			card = int(input())
			break
		except:
			print("\n\nEnter the credit card number : ",end = '')
	card = str(card)
	card = card[::-1]
	length = len(card)
	condition1 = check(card,length)
	condition2 = True if length == 16 else False
	
	#check is the card is issued by airlines
	if card.endswith('1' or '2') and condition1:
		print("\n\nIt is a valid card\nCard Issued by Airlines")
		
	#check if the card is issued by american express
	elif card.endswith("3") and length == 15 and condition1:
		print("\n\nIt is a valid card\nFor travel and entertainment\nIssued by American Express")
		
	#check if the card is issued by visa
	elif card.endswith("4") and condition1 and condition2:
		print("\n\nIt is a valid card\nBank card\nIssued by Visa Debit and Credit cards")
		
	#check if the card is issued by mastercards
	elif card.endswith("5") and condition1 and condition2:
		print("\n\nIt is a valid card\nBank card\nIssued by Mastercards")
		
	#check if the card is issued by Discover
	elif card.endswith("6") and condition1 and condition2:
		print("\n\nIt is a valid card\nBank card\nIssued by Discover credit cards")
		
	#check for the number satisfied luhn algorithm
	elif condition1:
		print("\n\nYour number follows a luhns algorithm but not a credit or debit card. It may be any other number following luhns algorithm.")
		
	#If all the above condition is false then it is not a valid number generated using luhn algorithm
	else:
		print("\n\nIt is not a valid card number\nOr you may enter a wrong number")
		

	print("\n\nWant to check another (y/n) : ",end = '')
	if input().lower() == 'y':
		clear_screen()
		pass
	else:
		break
	