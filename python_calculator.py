# Python Calculator

def add(num1,num2): # Function for Addition
    return num1+num2

def sub(num1,num2): # Function for Subtraction
    return num1-num2

def mult(num1,num2): # Function for Multiplication
    return num1*num2

def div(num1,num2): # Function for  Division
    return num1/num2

def avg(num1,num2): # Function for Average
    return (num1+num2)/2

# Display calculator menu

print("select an operation:\n " "1.addition \n" "2.subtraction\n" 
      "3.multiplication\n" "4.division \n" "5.average\n" )

select=int(input("select an operation from 1,2,3,4,5:")) # Take operation input from user


# Take number inputs

number1=int(input("enter first number"))
number2=int(input("enter second number"))


# Perform selected operation

if select==1:
    print(number1,"+", number2, "=", add(number1,number2))

elif select==2:
    print(number1,"-", number2, "=", sub(number1,number2))

elif select==3:
    print(number1,"*", number2, "=", mult(number1,number2))

elif select==4:
    print(number1,"/", number2, "=", div(number1,number2))

elif select==5:
    print((number1,"+", number2), "/2","=", avg(number1,number2))

else:
    print("invalid operation, select again dear")


