# Programm to print sum of digits of a number

class Sum:
    num = int(input("Enter a number :"))
    num1 = num
    sum1 = 0
    while(num1!=0):
        dig = num1%10
        sum1 = sum1 + dig
        num1 = (int)(num1/10)
    print(sum1) 