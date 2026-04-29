import random

choices = ['rock', 'paper', 'scissor']

user_choice = input("Enter your choice (rock/paper/scissor): ").lower()
comp_choice = random.choice(choices)

print("You chose:", user_choice)
print("Computer chose:", comp_choice)

if user_choice == comp_choice:
    print("It's a draw!")

elif (user_choice == "rock" and comp_choice == "scissor") or \
     (user_choice == "scissor" and comp_choice == "paper") or \
     (user_choice == "paper" and comp_choice == "rock"):
    print("You win!")

else:
    print("Computer wins!")