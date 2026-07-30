from datetime import datetime

print("bryrol6946 Spreadsheet Automation Menu")
print("CHoose a number from the following options")
print("1. Input Data")
print("2. View Current Data")
print("3. Generate Report")

# The next line retrieves the inputted option and stores into the variable
# called "option"

option = input()

print("You selected", option)
print("The time and date is", str(datetime.now()))
