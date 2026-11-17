# palindrome is a word that can be written from last it gives the same word
# our task is to check palindrome

user_input = input("Enter a word: ")
is_palindrome = False

if user_input == user_input[::-1]:
    is_palindrome = True
else:
    is_palindrome = False

if is_palindrome == True:
    print("Yes , it is  a Palindrome")
else:
    print("No, it is not a Palindrome")