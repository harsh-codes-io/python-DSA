
#In this scenario aur previous code will give 10 as second largest instead of 8
numbers = [10, 10, 8, 5]

largest = numbers[0]
second_largest = None

for num in numbers:
    if num > largest:
        second_largest = largest
        largest = num

    elif num!=largest and(second_largest is None or num > second_largest):
        second_largest = num

print("Second Largest number: ",second_largest)




