# To find whether a given no is positive negative or zero
class Problem :
    num = int(input("Enter a number :"))

    # Code to check whether the number is postive negative or zero
    if(num < 0):
        print(f"The number {num} is negative number")
    elif(num == 0):
        print(f"The enter {num} is zero")
    else :
        print(f"The number {num} is positive")