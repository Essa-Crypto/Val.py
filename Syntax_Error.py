try:
    num1, num2 = eval(input("Enter two numbers, seperated by a comma : "))
    result = num1 / num2
    print("Result is", result)

except ZeroDivisionError:
    print("Divisions by zero is error !!")

except ZeroDivisionError:
    print("Comma is missing. Enter numbers seperated from commas like this 1, 2")

except:
    print("Wrong input")

else:
    print("No exceptions")

finally:
    print("This will execute no matter what")

