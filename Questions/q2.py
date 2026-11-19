# 2. Write a program to swap two numbers without using a third variable.
num1 = int(input("num1: "))
num2 = int(input("num2: "))

# we need to swap it means num1 = num2 and num2 = num1 
num1 = num1 + num2
num2 = num1 - num2 
num1 = num1 - num2

print("new num1:",num1,"new num2:",num2)