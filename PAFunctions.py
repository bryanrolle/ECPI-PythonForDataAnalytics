def functionOne():
    print("My Student ID is bryrol6946")

def functionTwo():
    num1 = int(input("Please enter a number: "))
    num2 = int(input("Please enter a number: "))

    sumNumbers = num1 + num2

    print("The sum of", num1, "and", num2, "is", sumNumbers)

    return sumNumbers

def functionThree(sumNumbers):
    if sumNumbers > 5:
        print("The sum is greater than 5.")
    else:
        print("The sum is 5 or less.")

    return 1234


def main():
    functionOne() #Calls functionOne to display studentID
    sumNumbers = functionTwo() #Calls functionTwo and stores the returned sum
    studentId = functionThree(sumNumbers) #Passes the sum to functionThree and stores the returned student ID
    print("functionThree returned the value of", studentId) #Displays the value returned by functionThree


main()
