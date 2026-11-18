
numbers = [10, 20, 10, 30, 10, 20, 40]

most_frequent = numbers[0]
max_count = 0

for num in numbers:
    count = numbers.count(num)

    if count > max_count:
        max_count = count
        most_frequent = num

print("Most frequent element:", most_frequent)
print("Frequency:", max_count)
