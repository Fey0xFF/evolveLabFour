# call sys module
import sys

# define guessFruit function
def guessFruit(basket):
  for numGuesses in range(0,5,1): # set range to 5 guesses
    print('Please enter a fruit to see if it\'s in your basket:')
    fruitGuess = str(input()).lower()
    if fruitGuess in basket: # check for fruit in basket
      print('Yes that is in your basket!')
      break 
    else:
      print('No, that is not in your basket.') 
  print('Thank you for using FB3000.')
  main() # return to main

# define main function
def main():
  print('\nHELLO! I\'m your fruit basket organizer program. Call me FB3000 because, well the 2000 model came and went and I\'m supposed to be good until the year 3000!\n')
  fruitBasket = ['apple', 'pear', 'peach', 'orange', 'pineapple'] # set basket values
  
  while True: # begin user input prompts
    print('\n To begin using me please type "u". To exit please type "e".')
    userCommand = str(input()).lower()
    if userCommand == "u":
      guessFruit(fruitBasket)
    elif userCommand == "e":
      sys.exit() # exit script
  
main() 