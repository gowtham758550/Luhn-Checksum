#author = <gowtham758550@gmail.com>
#Check a credit card is valid or not
#Luhn Algorithm - With this algorithm credit, debit card numbera are generated
#Make use of that algorithm logic to validate card numbers
#Many websites gives free card numbers based on this algorithm
#Some of indentification number issued by the government follow this algorithm
#If u found any bug in this program or logical error
#please make pull request or an issue
	




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
		print("\n\nIt is a valid card number")
	else:
		print("\n\nIt is not a valid card number\nOr you may enter the wrong number")

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
	check(card,length)
	print("\n\nWant to check another (y/n) : ",end = '')
	if input().lower() == 'y':
		pass
	else:
		break
	
			
