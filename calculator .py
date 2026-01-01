num1=int(input("Enter a number1: "))
num2=int(input("Enter a number2: "))
operation =input("enter the operation(+,-,*,/):")
if operation=="+":
    print("the sum of the numbers is:",num1+num2)
elif operation=="-":
    print("the differnce of the number is:",num1-num2)
elif operation=="*":
    print("the product of the number is:",num1*num2)
elif operation=="/":
    print("the division of the number is:",num1/num2)
else:
    print("invalid operation")
