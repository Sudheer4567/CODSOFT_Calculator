num1=int(input("Enter the first number: "))
num2=int(input("Enter the second number: "))
operation=input("Enter the operation(+,-,*,/): ")

if operation=='+':
    result= num1 + num2
elif operation == '-':
    result= num1 - num2
elif operation == '*':
    result= num1 * num2 
elif operation == '/':
    if num2 !=0:
        result= num1 /num2  
    else:
        result= "Error : division by zero" 
else:
    result="Invalid operation"           

print("The result is:",result)         
