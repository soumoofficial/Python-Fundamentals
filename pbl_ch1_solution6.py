# Programm to check a given number is prime or not

class Prime :
    n = int(input("Enter a number :"))
    m = (int)(n/2)
    if(n>0):
        for i in range(1,m):
            if(n%i==0):
                print("Prime Number")
                break;
    