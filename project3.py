from datetime import datetime

def convertData(data):
    convertedValue = (data - 32) * 5 / 9
    return convertedValue

def getInput():

    entries = int(input("How many entries are you inputting? "))

    for count in range(entries):

        date = input("Enter a date: ")

        value = float(input("Enter the highest temp for the inputted date:"))

        convertedValue = convertData(value)

        print("The following was saved at", datetime.now(), ":")
        print(date, value, convertedValue, sep=",")


def main():

    print("bryrol6946's Spreadsheet Automation Menu")
    print("Choose a number from the following options")
    print("1 Input Data")
    print("2 View Current Data")
    print("3 Generate Report")

    choice = int(input())

    if choice < 1 or choice > 3:
        print("Error: Invalid menu selection")

    elif choice == 1:
        print("You selected", choice, "at", datetime.now())
        getInput()

    else:
        print("Error: The chosen functionality is not implemented yet")

main()
