from datetime import datetime

student_id = "Bryrol6946"

menu_options = [
    "1 Input Data",
    "2 View Current Data",
    "3 Generate Report"
    ]

print(student_id + "'s Spreadsheet Automation Menu")
print("Choose a number from the following options")

# option represents each menu choice in the menu_options list
for option in menu_options:
    print(option)

choice = input()

if choice == "1":
    print("You selected", choice, "at", datetime.now())
elif choice == "2":
    print("You selected", choice, "at", datetime.now())
elif choice == "3":
    print("You selected", choice, "at", datetime.now())
else:
    print("Error: invalid choice selected")
