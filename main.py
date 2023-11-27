# A Hash tag in python starts a comment
# This file is a quick intro to the python coding language

# import and need modules here
# syntax:
# import module
# alternatively if you just want a part of the module
# you can say
# from module import part_x
import random

# you can write scripts in python that just run when you parse
# the source code with the python parser [the run button on Replit]
# or you can create classes that can be object oriented or just 
# functional. Its up to you, the programmer!
#
# In this example, we will create a class that you will fill out.
# Our goal is to write a little number guessing game. We'll create
# a class with the functions to run our game. At the end of this file,
# will use some syntax to run if the file is called to execute from
# the parser.

class GuessNumber:
  """GuessNumber is a class to implement the mechanics of a number guessing game."""
  def __init__(self, max=10, min=0):
    self.max = max
    self.min = min
    self.secret_number = 0

  def DisplayIntro(self):
    print("\t\t\tC3 Python Into Number Guessing Game\n")
    long_string = """This is a number guessing game. You will be prompted to enter a number. If you want to quit, enter a negative number.\n\n"""
    print(long_string)

  def AssignNumber(self):
    self.secret_number = random.randint(self.min,self.max)    

  def RunGameLoop(self):
    """This is the core of the game."""
    keepPlaying = True
    needNumber = True
    the_prompt = "Enter a guess between {0} and {1}. [< 0 quits] --> ".format(self.max, self.min)
    
    while(keepPlaying):
      if needNumber:
        self.AssignNumber()
        needNumber = False

      print("Debug: secret number = {0}".format(self.secret_number))
      guess = input(the_prompt)
      #num_guess = int(guess)
      num_guess = -1
      
      if num_guess < 0:
        print("Thanks for playing. Hope you had fun.")
        keepPlaying = False
      elif num_guess == self.secret_number:
        print("You guessed it! Great job.")
        keepPlaying = False
      else:
        print("Nope! Try again.\n")

      
# In python there are some internal variables of the form
# __somename__ that have special meaning. Below we check to see
# if the __name__ special variable is equal to the string 
# '__main__', if it is the code below it will run. 
    
if __name__ == '__main__':
	# code to be executed if the module is run as the main program

  numberGame = GuessNumber()
  numberGame.DisplayIntro()
  numberGame.RunGameLoop()