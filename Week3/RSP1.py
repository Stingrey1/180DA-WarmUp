

print("Please enter R, S or P for rock, paper scissors respectively")
input1 = input("Player One ")
input2 = input("Player Two ")


if input1 == "R":
	if input2 == "R":
		print("draw")
		exit()
	if input2 == "S":
		print("Player 1 wins")
		exit()
	if input2 == "P": 
		print("Player 2 wins")
		exit()
	else: 
		print("someone f'ed up!")
		exit()

if input1 == "S":
	if input2 == "R":
		print("Player 2 wins")
		exit()
	if input2 == "S":
		print("draw")
		exit()
	if input2 == "P": 
		print("Player 1 wins")
		exit()
	else: print("someone f'ed up!")


if input1 == "P":
	if input2 == "R":
		print("Player 1 wins")
	if input2 == "S":
		print("Player 2 wins")
	if input2 == "P": 
		print("draws")

	else: print("someone f'ed up!")


else: print("someone f'ed up!")


'''
if input1 == input2:
	print("draw")
else:
	print("NOOOOO")
'''



'''
if input1 > input2:
	print("player one wins")

else: 
	print("player two wins")

	#check for input
while(True):
	if input1 != "R" or "S" or "P":
		print("choose valid")
		input1 = input("Player One ")
	else:
		break
'''


