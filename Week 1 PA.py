
name = input("Please enter your name: ")
studentID = input("Please enter your Student ID: ")

number1 = int(input("Pkease enter a whole number: "))
number2 = int(input("Please enter a different second whole number: "))

multiplication = number1 * number2
division = number1 / number2
addition = number1 + number2


print(f"The result of {number1} times {number2} is: {multiplication:.2f}")
print(f"The result of {number1} divided by {number2} is: {division:.2f}")
print(f"The result of {number1} plus {number2} is: {addition:.2f}")


if number1 > number2:
    print("Number 1 is larger than Number 2")
elif number1 < number2:
    print("Number 1 is smaller than Number 2")
else:
    print("Number 1 is equal to Number 2")

    
print(name)
print(studentID)



