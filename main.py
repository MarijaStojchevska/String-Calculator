from test import *


if __name__ == '__main__':
   #Uncomment the line below if you want to validate the tests
   #unittest.main(exit=False)

   c = Calculator()
   while True:
      delimiter = input("Enter the delimiter type: ")
      input_string = input("Please enter the input values separated by the delimiter of your choice: ")
      print("The calculated sum is: ", c.add_numbers(input_string, delimiter))

      enter_input = input("Do you want to enter a new input into the calculator (yes / no)? ")
      while enter_input.lower() not in ["yes", "no"]:
         enter_input = input("Do you want to enter a new input into the calculator (yes / no)? ")
      if enter_input.lower() == "yes":
         continue
      else: break