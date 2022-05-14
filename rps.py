import random

valid_choices = ["Rock", "Paper", "Scissors"]
repeat ="y"

while repeat =="y":
  user_choice = input("Rock Paper Scissors 1 2 3 shoot:")
  computer_choice = valid_choices[random.randint(0,2)]
  print("The computer chose: "+ computer_choice)
  print("The user chose: "+ user_choice)
  
  while not any(user_choice == valid_choice for valid_choice in valid_choices):
    print("Choose rock, paper, or scissors")
    choice = input("Rock paper scissors 1 2 3 shoot:")
  
  if user_choice != computer_choice:
    if user_choice == valid_choices[0]:
      if computer_choice == valid_choices[2]:
        print("You win!")
      else:
        print("You lost")
    if user_choice == valid_choices[1]:
      if computer_choice == valid_choices[0]:
        print("You win")
      else:
        print("You lost")
    if user_choice == valid_choices[2]:
      if computer_choice == valid_choices[1]:
        print("You win")
      else:
        print("You lost")
  else:
     print("Draw")

  repeat = input("Press y to play again:")