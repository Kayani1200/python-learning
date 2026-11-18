
# Function 1: Check Prime Number
def check_prime(num):

    if num <= 1:
        return False

    for i in range(2, num):
        if num % i == 0:
            return False

    return True


# Function 2: Find Maximum Value
def find_max(numbers):

    maximum = numbers[0]

    for num in numbers:
        if num > maximum:
            maximum = num

    return maximum


# Function 3: Calculate Average Marks
def calculate_average(marks):

    total = sum(marks)
    average = total / len(marks)

    return average


# Function 4: Calculate Factorial
def factorial(num):

    result = 1

    for i in range(1, num + 1):
        result = result * i

    return result


# Main Program

number = 7
numbers = [10, 25, 5, 40, 15]
marks = [80, 70, 90, 60, 100]

print("Prime Number:", check_prime(number))

print("Maximum Value:", find_max(numbers))

print("Average Marks:", calculate_average(marks))

print("Factorial:", factorial(number))
