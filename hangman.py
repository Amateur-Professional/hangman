# -*- coding: utf-8 -*-
"""
Created on Sun Dec 24 12:29:03 2023
Hangman - a single player game
@author: Michael Mangano
"""
import random
 
#Draws the hangman platform
def draw_board(errors):
    first_line = "     ______"
    second_line = "     |    |"
    third_line = "     |    "
    fourth_line = "     |   "
    fifth_line = "     |   "
    sixth_line = "     |"
    seventh_line = "------------"
    if errors > 0:
        third_line += "0"
    if errors > 1:
        fourth_line += "/"
    if errors > 2:
        fourth_line += "|"
    if errors > 3:
        fourth_line += "\\"
    if errors > 4:
        fifth_line += "/"
    if errors > 5:
        fifth_line += " \\"
        print("GAME OVER")
    print(first_line, second_line, third_line, fourth_line, fifth_line, sixth_line, seventh_line, sep = '\n')


#Picks a random answer from the user's selected category
def select_answer():
  word_bank ={"animals": ["giraffe", "gorilla", "penguin", "porpoise", "rhinoceros"], "cocktails": ["bloody mary", "mudslide", "manhattan", "martini", "long island iced tea"]}

  category = None
  while category not in word_bank.keys():
    category = input("Select your category from the following choices: " + str(list(word_bank.keys())) + "\n").strip().lower()

  index = random.randint(0, len(word_bank[category])-1)
  answer = word_bank[category][index]
  return answer

def track_guesses(answer, guesses):
  hidden_answer = ""
  for letter in answer:
    if letter.isalpha():
      if letter in guesses:
        hidden_answer += letter
      else:
        hidden_answer += "_"
    else:
      hidden_answer += letter
  return hidden_answer

def track_alphabet(guesses):
  build_alphabet = ""
  for ordinal in range(ord('a'), ord('z')+1):
    if chr(ordinal) in guesses:
      continue
    else:
      build_alphabet += chr(ordinal)
  return build_alphabet
  
def get_guess():
  guess = '0'
  while ord(guess) < ord('a') or ord(guess) > ord('z'):
    guess = input("What is your next guess: \n")
    while not guess.isalpha() or len(guess) != 1:
      guess = input("Invalid guess, please input a single letter: \n")
    guess = guess.lower()
  return guess

#Counts the number of incorrect guesses
def get_errors(answer, guesses):
  errors = 0
  if len(guesses) > 0:
    for letter in guesses:
      if letter not in answer:
        errors += 1
  return errors

#Here's where we implement play
answer = select_answer()
guesses = []
errors = 0
current_answer = None

while errors <= 5 and current_answer != answer:
  current_answer = track_guesses(answer, guesses)
  print("Your word to guess is:", current_answer)
  print("Remaining letters: ", track_alphabet(guesses))
  errors = get_errors(answer, guesses)
  draw_board(errors)
  if errors > 5 or current_answer == answer:
    if errors > 5:
      print("*" * 21)
      print(" " * 6 + "GAME OVER")
      print("*"* 21)
      print("The correct answer was: ", answer)
    else:
      print("*" * 20)
      print(" " * 6 + "YOU WIN!")
      print("*" * 20)
    keep_going = input("Would you like to play again? (Y/N): ")
    if keep_going.upper() == "Y" or keep_going.upper() == "YES":
      errors = 0
      guesses = []
      answer = select_answer()
    else:
      print("Thank you for playing!")
    continue
  guesses.append(get_guess())
