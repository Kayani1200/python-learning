
print("===== STRING ANALYZER AND LIST UTILITY =====")

print("\n1. String Analyzer")
print("2. List Utility")

choice = int(input("Select your choice (1 or 2): "))


# STRING ANALYZER

if choice == 1:

    text = input("Enter your text: ")

    print("\n===== STRING ANALYSIS =====")

    print("Total characters:", len(text))

    vowels = 0

    for letter in text.lower():
        if letter in "aeiou":
            vowels = vowels + 1

    print("Total vowels:", vowels)

    print("Reverse string:", text[::-1])

    print("Uppercase:", text.upper())

    print("Lowercase:", text.lower())


# LIST UTILITY

elif choice == 2:

    numbers = input("Enter numbers separated by spaces: ")

    numbers = list(map(int, numbers.split()))

    print("\n===== LIST UTILITY =====")

    print("Original list:", numbers)

    print("Largest number:", max(numbers))

    print("Smallest number:", min(numbers))

    print("Sorted list:", sorted(numbers))

    unique_numbers = []

    for num in numbers:
        if num not in unique_numbers:
            unique_numbers.append(num)

    print("List without duplicates:", unique_numbers)


else:
    print("Invalid choice! Please select 1 or 2.")
