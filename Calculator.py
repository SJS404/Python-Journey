# Imports time function
import time
import colorama
from colorama import Fore, init, Back, Style

init()
num1 = (1)
num2 = (2)
operator = ("")
# prints welcome message for the user
print(Back.WHITE, Fore.BLUE, Style.BRIGHT,"Welcome to the Calculator!", Style.RESET_ALL)  

time.sleep(1) # Waits for 1 second before displaying next message
while True: #Using a while loop, i can validate that the user input is as needed and produce an error message if it is not.
    try:              
      num1 = eval(input("\nPlease Enter Your 1st Number: ")) # Asks user for the first number #
    except (NameError, ValueError, SyntaxError):
      print(Fore.RED, "\bSorry, that is not a valid entry. Please Try Again\n", Fore.RESET)   # if data is not an int or float, this error will show and loop back to start of the block.
      time.sleep(1)      
      continue
    try:
      num2 = eval(input("\nPlease Enter Your 2nd Number: "))
    except (NameError, ValueError, SyntaxError):
      print(Fore.RED, "\bSorry, that is not a valid entry. Please Try Again\n", Fore.RESET)   # if data is not an int or float, this error will show and loop back to start of the block.
      time.sleep(1)      
      continue
          # Dependant on the operator symbol inputted by the user, the calculation will be performed and printed out using the correct mathematical operation 
      # the elif (else if statement) evaluates which operator has been inputted. If it does not match, it move to the next until it matches the required input.

    operator = input("\nWhat would you like to do to these numbers?( + , - , / , * ): ")
    if operator == "+" or operator == "add": # If checks the users input to determine if the correct one has been selected. If it has not, elif will check the next.
      print(Fore.YELLOW, "\n{} + {} = ".format(num1, num2), (num1 + num2), Fore.RESET)
    elif operator == "-" or operator == "subtract" or operator == "take":
      print(Fore.YELLOW, "\n{} - {} = ".format(num1, num2), (num1 - num2), Fore.RESET)
    elif operator == "*" or operator == "multiply" or operator == "times":
      print(Fore.YELLOW, "\n{} * {} = ".format(num1, num2), (num1 * num2), Fore.RESET)
    elif operator == "/" or operator == "divide":
      try: # A try except validation is performed on the division class to check whether the user has tried entering an impossible calculation of dividing by 0.
        print(Fore.YELLOW, Style.BRIGHT, "\n{} / {} = ".format(num1, num2), (num1 / num2), Style.RESET_ALL)
      except: #If the user has entered zero, they will be asked to perform a valid calculator by re-entering a different operator.
        print(Fore.RED, "\nIt Is Not Possible To Divide A Number By 0", Fore.RESET)
        time.sleep(1)
        continue
    else:
      print(Fore.RED, "\"", operator, "\"","Is Not A Valid Operator! Please Try Again", Fore.RESET)
      time.sleep(1)
      continue
    
    again = input("\nWould You Like To Proceed With Another Calculation? \nEnter 'Y' To Continue or Press Any Other Key To Quit: ") 
    again = again.lower()  
    if again == "y" or again == "yes":
      time.sleep(1)
      continue
    else:    
      print("\nGoodbye For Now") # If the user inputs any other value but 'y' or 'yes' then the program will terminate.
      time.sleep(1)
      break
