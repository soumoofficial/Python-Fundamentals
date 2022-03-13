# Programm to print a number in reverse

class Reverse_num:
    num = int(input("Enter a number :"))
    num1 = num
    rev1 = 0
    while (num1!=0):
        dig = num1 % 10
        rev1 = rev1*10 + dig
        num1 //= 10
    print(rev1)