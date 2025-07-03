num1=int(input("Enter Number 1 ="))
num2=int(input("Enter Number 2 ="))
operator=input("choose operation(+,-,/,*)=")
if operator == '+':
    print(num1,"+",num2 ,"=", num1+num2)
elif operator == '-':
    print(num1,"-",num2 ,"=", num1-num2)
elif operator == '/':
    print(num1,"/",num2 ,"=", num1/num2)
elif operator == '*':
    print(num1,"*",num2 ,"=", num1*num2)
else:
    print("Enter correct opreation")