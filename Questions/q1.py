# 1. Create a calculator that performs addition, subtraction, multiplication, division, floor division and modulus.

print("Calculator")
user_input = input("Enter numbers seperated by ,: ")
user_input = list(map(float,user_input.split(",")))
operator_input = input("Enter the operation to be performed i.e. addition , subtraction , multiplication , division , floor division , modulus: ")
sum = 0
mul = 1
for i in user_input:
    sum1 += i
    mul *= i

first_digit = user_input[0]
first_digit1 = first_digit2 = first_digit 
first_digit3 = first_digit2 = first_digit4 = first_digit
for i in range(1,len(user_input)):
    first_digit1 =  first_digit1 - user_input[i]
    first_digit2 = first_digit2 / user_input[i]
    first_digit3 = first_digit3 // user_input[i]
    first_digit4 = first_digit4 % user_input[i]
   

    

if operator_input.lower() == "addition":
    print(sum1)
elif operator_input.lower() == "modulus":
    print(first_digit4)
elif operator_input.lower() == "subtraction":
    print(first_digit1)
elif operator_input.lower() == "multiplication":
    print(mul)
elif operator_input.lower() == "division":
    print(first_digit2)
elif operator_input.lower() == "floor division":
    print(first_digit3)
else:
    print("enter a valid operator")

