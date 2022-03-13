# To check a number is even or odd
class Check :
    num = int(input("Enter a number :"))
    
    # Code to check even or odd
    if(num > 0):
        if(num % 2 == 0):
            print(f"The number {num} is even")
        else :
            print(f"The number {num} is odd")