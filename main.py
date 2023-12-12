from getpass import getpass as input

print("It's time to start this battle, select your move (s, r or p)")
while True:
  while True:    
    player_1 = input("Player 1: ")
    if player_1.lower() != 's' and player_1.lower() != 'r' and player_1.lower() != 'p':
      print("Not valid, please select your move (s, r or p)")
    else:
      break
  
  while True:
    player_2 = input("Player 2: ")
    if player_2.lower() != 's' and player_2.lower() != 'r' and player_2.lower() != 'p':
      print("Not valid, please select your move (s, r or p)")
    else:
      break
      

  if (player_1.lower() == 'r' and player_2.lower() == 's') or \
     (player_1.lower() == 's' and player_2.lower() == 'p') or \
     (player_1.lower() == 'p' and player_2.lower() == 'r'):
      print("¡Player 1 wins!")
  elif (player_2.lower() == 'r' and player_1.lower() == 's') or \
       (player_2.lower() == 's' and player_1.lower() == 'p') or \
       (player_2.lower() == 'p' and player_1.lower() == 'r'):
      print("¡Player 2 wins!")
  else:
      print("It's a tie")

  
  pa = input("¿do you want to play again? (y/n): ")
  if pa.lower() != 'y':
      break