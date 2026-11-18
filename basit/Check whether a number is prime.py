num = 7

if num > 1:
    for i in range(2, num):
        if num % i == 0:
            print("Not Prime Number")
        else:
            print("Prime Number")
            break
else:
    print("Not Prime Number")