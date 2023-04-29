############ NUMBER GUESSING PROJECT ##################
from art import logo
import random
from replit import clear

def play():
  print(logo)
  print("Welcome to the Number Guessing Game!")
  print("I'm thinking of a number between 1 and 100")


  #Create number list
  nr_list = list(range(1, 101, 1))
  
  #Set game start/end
  game_over = False
  #used_nr = [] #Empty list to check guessed nr later
  #Set initial attempts
  difficulty = input("Choose a difficulty. Type 'easy' or 'hard': ")
    
  if difficulty == 'easy':
    attempts = 10
  elif difficulty == 'hard':
    attempts = 5
  else:
    print('You entered a non valid option. Game set to Hard mode')
    attempts = 5
    
  while game_over == False:
    #Number selection
    chosen_nr = random.choice(nr_list)
    #print(chosen_nr)

    while attempts != 0:
      print(f"\nYou have {attempts} attempts remaining to guess the number")
      #Make a guess
      guess = int(input("Make a guess: "))
      #Check guess
      
      if guess == chosen_nr:
        print(f"You got it! The number was {chosen_nr}\n\n")
        check_continue = input("Would you like to play again? Type 'y' if Yes, or type 'n' if No: ")
        if check_continue == 'n':
          game_over = True
          print("Come back soon!")
          break
        else:
          clear()
          play()
          
      elif guess < chosen_nr:
        print("Too low")
        attempts -= 1
      
      elif guess > chosen_nr:
        print("Too high")
        attempts -= 1

      
    if attempts == 0:
      print(f'You lose! The number was {chosen_nr}\n')
      check_continue = input("Would you like to play again? Type 'y' if Yes, or type 'n' if No: ")
      if check_continue == 'n':
        game_over = True
        print("Come back soon!")
      else:
        clear()
        play()
          
play()
