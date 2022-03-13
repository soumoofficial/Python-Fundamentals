# Programm to find a number is palindrome or not

class Palindrome :
    num = int(input("Enter a number :"))
    num1 = num
    rev1 = 0
    while (num1!=0):
        dig = num1 % 10
        rev1 = rev1*10 + dig
        num1 //= 10
    
    if rev1 == num :
        print(f"Palindrome Number is {num}")
    else :
        print("Not palindrome number")