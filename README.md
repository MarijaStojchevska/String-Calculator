# String Calculator
<!-- Project description -->
This file explains the implementation and the testing of a simple String Calculator in Python that can be used as a service for various applications and programs. The String Calculator has the functionality to calculate the sum of the given numbers in an input string. The implementation can easily be extended so that the calculator supports more arithmetic operations.

## Prerequisities
* Make sure python is already installed on your local machine. If it is installed, you can check the python version via the command line by entering the command `python --version`.
* Install the inflect and unittest libraries by entering the following commands on the command line: `pip install inflect` and `pip install unittest`.

## Implementation
* The calculator entity is represented via the Calculator class written in the *string_calculator.py* file. This class contains four private and one public method:
   
   **Private methods**
     - `validate_delimiter`: validates the correctness of the delimiter type.
     - `extract_numbers`: extracts the numbers from the input string using the delimiter of interest.
     - `validate_numbers`: validates multiple requirements (treats empty or null input as zero, does not support negative numbers, ignores numbers       greater than 100, does not support non-digit characters).
     - `check_overflow`: checks if a given value fits in the memory. We call it to check for overflow on the input string and the output value.
     
   **Public method**
     - `calculate_sum`: returns the sum of the numbers present in the input string if all the requirements defined in the private methods are satisfied.

* We create an object of the Calculator class in the *main.py* file.
* The solution is designed so that initially the user has to enter an input string and a delimiter type via the command line. Calculating the sum of the numbers in the input array is done by passing the user inputs as arguments to the `calculate_sum` method of the created object.

## Testing 
Code testing is done with unit tests written in TestCalculator class inside the *test.py* file. Calling the `unittest.main()` method in the main function produces a test report which tells us whether the `calculate_sum` function (the unit) behaves as expected across all test cases. 

Example output:
```bash
Ran 8 tests in 0.002s
OK
```
* The test output is given in the following test report form: "OK" if all tests are satisfied, and "FAILED (failures, errors)" otherwise.

## Running the project from the terminal

```bash
# Enter the project directory by replacing '.' with the local path where the directory is saved on your machine
cd './calculator'
# Execute the code
python main.py
```
Example output:
```bash
Enter the delimiter type: /
Please enter the input values separated by the delimiter of your choice: 2/5/1
The calculated sum is:  8.0
Do you want to enter a new input into the calculator (yes / no)? no
```
* The calculator implementation requires user input and execution continues if all requirements are satisfied.
* If no exception is thrown, the calculated sum is printed on the output.
* Тhe user has the option to choose if they want to enter a new input into the calculator.
