import sys

def guess_fruit(basket):
  for numGuesses in range(0,5,1):
    print('Please enter a fruit to see if it\'s in your basket:')
    fruitGuess = str(input()).lower()
    if fruitGuess in basket:
      print('Yes that is in your basket!')
      break
    else:
      print('No, that is not in your basket.')
  print('Thank you for using FB3000.')
  main()

def main():
  print('\nHELLO! I\'m your fruit basket organizer program. Call me FB3000 because, well the 2000 model came and went and I\'m supposed to be good until the year 3000!\n')
  fruitBasket = ['apple', 'pear', 'peach', 'orange', 'pineapple']
  
  while True:
    print('\n To begin using me please type "u". To exit please type "e".')
    userCommand = str(input()).lower()
    if userCommand == "u":
      guess_fruit(fruitBasket)
    elif userCommand == "e":
      sys.exit()
  
main() 