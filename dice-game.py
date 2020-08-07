import random
print("Enter player1's name")
player1 = input()
print("Enter player2's name")
player2 = input()
print("It's " +player1 +"'s turn")
print("Press enter to roll the dice")
input()
num1 = random.randint(1, 6)
print(player1, "'s number is" ,num1)
print("It's " +player2 +"'s turn")
print("Press enter to roll the dice")
input()
num2 = random.randint(1, 6)
print(player2, "'s number is" ,num2)
if num1 > num2:
    print(player1+ " won!")
elif num1 == num2:
    print("Draw")
else:print (player2+ " won!")
input()


