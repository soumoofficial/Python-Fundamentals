# Programm to print prime no beetween 10 and 99

class Prime :
    lower = 10
    upper = 99

    print("Prime numbers between", lower, "and", upper, "are:")

    for num in range(lower, upper + 1):
    # all prime numbers are greater than 1
        if num > 1:
            for i in range(2, num):
                if (num % i) == 0:
                    break
            else:
                print(num)