
import random

def get_comp_selection():
	options = ['snake', 'water', 'gun']
	return random.choice(options)

user_score = 0
comp_score = 0
tie = 0

play = True
while play:
	user_selection = input("\nEnter your choice (snake, water, gun): ").lower()\
	
	# determine whether the user gave valid input or not
	if (user_selection not in ('snake', 'water', 'gun')):
		print("Inavlid input! Enter again")
		continue    # asks the user again if user enters invalid choice

	else: 
		comp_selection = get_comp_selection()
		print(f"\nThe computer chooses: {comp_selection}")

		if((user_selection == "snake" and comp_selection == "water") or (user_selection == "gun" and comp_selection == "snake") or (user_selection == "water" and comp_selection == "gun")):
			print("\nYou Won!!")
			user_score += 1
		elif((comp_selection == "snake" and user_selection == "water") or (comp_selection == "gun" and user_selection == "snake") or (comp_selection == "water" and user_selection == "gun")):
			print("\nComputer Won!!")
			comp_score += 1
		elif((comp_selection == "snake" and user_selection == "snake") or (comp_selection == "gun" and user_selection == "gun") or (comp_selection == "water" and user_selection == "water")):
			print("\nIt's a tie!!")
			tie += 1

		# display score after every match
		print(f"Your score is: {user_score}")
		print(f"Computer score is: {comp_score}")
		print(f"Tie score is: {tie}")

		while True:
			# asks the user to play further
			play_again = input("\nDo you want to play again? (yes/no): ").lower()
			if (play_again == "no"):
				print("\nYour final scores are:-")
				print(f"\nYour score is: {user_score}")
				print(f"Computer score is: {comp_score}")
				print(f"Tie score is: {tie}")
				print("\nThank you for playing!!!")
				play = False      # breaks the outer loop
				break             # breaks the inner loop
			elif(play_again == "yes"):
				break             # breaks the inner loop
			else:
				print("\nYou entered an invalid choice. Enter 'Yes' or 'No'")