import random

print("Game Rules: \n ")
print("Rock beats Scissors\n ")
print("Paper beats Rock\n ")
print("Scissors beat Paper")


while True:
  print("\n")
  print("1) Rock")
  print("2) Paper")
  print("3) Scissor")

  selection= int(input("Enter your throw: "))

  if selection == 1:
    player_throw = "Rock"
  elif selection == 2:
    player_throw = "Paper"
  else:
    player_throw = "Scissor"

  print("\n")
  print("Player throw: ", player_throw)

  throws = ["Rock", "Paper", "Scissor"]
  computer_throw = random.choice(throws)

  print("Computer throw: ", computer_throw)

  
  if player_throw == computer_throw:
    print("Tie!")
    
  elif player_throw == "Rock":
    if computer_throw == "Scissor":
      print("Player Wins!")
    elif computer_throw == "Paper":
      print("Computer Wins!")

  elif player_throw == "Paper":
    if computer_throw == "Rock":
      print("Player Wins!")
    elif computer_throw == "Scissor":
      print("Computer Wins!")

  elif player_throw == "Scissor":
    if computer_throw == "Paper":
      print("Player Wins!")
    elif computer_throw == "Rock":
      print("Computer Wins!")

  print("\n")
  print(" 1) Play Again ")
  print(" 2) Quit ")
  selection: int(input("Enter your choice: "))
  if selection == 2:
    break

    
     
   
  




               