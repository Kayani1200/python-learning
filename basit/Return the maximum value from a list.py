
def find_max(numbers):

    maximum = numbers[0]

    for num in numbers:
        if num > maximum:
            maximum = num

    return maximum


numbers = [10, 25, 5, 40, 15]

answer = find_max(numbers)

print("Maximum Value:", answer)
