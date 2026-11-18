
def calculate_average(marks):

    total = sum(marks)

    average = total / len(marks)

    return average


marks = [80, 70, 90, 60, 100]

answer = calculate_average(marks)

print("Average Marks:", answer)
