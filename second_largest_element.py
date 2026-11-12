numbers = [12, 5, 27, 8, 19]


def approach_1(numbers):
    largest = numbers[0]

    #finding the largest
    for num in numbers:
        if num > largest:
            largest=num

    #largest number removed from list 
    numbers.remove(largest)

    #again finding largest - now the largest will be second_largest
    largest = numbers[0]
    for num in numbers:
        if num > largest:
            largest=num

    print("Second largest element of list: ",largest)

def approach_2(numbers):
    largest = numbers[0]
    second_largest = None

    for num in numbers:
        if num > largest:
            second_largest = largest
            largest = num

        elif second_largest is None or num > second_largest:
            second_largest = num

    print("Second largest element of list: ",second_largest)



#initial approach - sending copy of list(distinct values)
approach_1(numbers.copy())
#better - improved approach (distinct values)
approach_2(numbers)


