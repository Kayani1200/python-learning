
# Data Filtering and Transformation

numbers = [10, 15, 20, 25, 30, 35, 40]

# Step 1: Filter numbers greater than 20

filtered_numbers = []

for num in numbers:

    if num > 20:
        filtered_numbers.append(num)


# Step 2: Transform filtered numbers

transformed_numbers = []

for num in filtered_numbers:

    transformed_numbers.append(num * 2)


# Step 3: Display results

print("Original Data:", numbers)

print("Filtered Data:", filtered_numbers)

print("Transformed Data:", transformed_numbers)
