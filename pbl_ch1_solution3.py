# Enter two numbers if they have same last digit then print yes else no
class Number :
    num1 = int(input("Enter a number :"))
    num2 = int(input("Enter a number :"))

    if(num1 and num2 != 0):
        dig1 = num1 % 10
        dig2 = num2 % 10

        print(dig1)
        print(dig2)

        if(dig1 == dig2):
            print("true")

        else :
            print("false")