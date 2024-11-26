def calculator():
    num1=int(input("Enter first number: "))
    num2=int(input("Enter the second number: "))
    operator=input("Enter opertaor for computation {+ , - , * , / } = ")

    match operator:
        case '+':
            print(num1+num2)
        case '-':
            if num1>=num2:
                {
                    print(num1-num2)
                }
            else:
                {
                    print("First number is less than second number thus a negative result",num1-num2)
                }
        case '*':
            print(num1*num2)
        case '/':
            print(num1/num2)
        case _:
            print("Invalid operator")   

calculator()              
