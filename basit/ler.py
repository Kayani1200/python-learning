numbers = [2,3,6,5,9,10,12,14,21]

def even (num):
    return num % 2 == 0

result = filter(even, numbers)
print (list (result))