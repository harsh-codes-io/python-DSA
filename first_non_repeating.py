
numbers = [4, 2, 7, 2, 8, 4, 9]



def approach_1(numbers):
    seen = set()
    for num in numbers:
        if num in seen:
            repeated = num
            numbers = [x for x in numbers if repeated != x]
        else:
            seen.add(num)

    print("first non repeating number: ",numbers[0])


def approach_2(numbers):
    frequency = {}

    for num in numbers:
        if num in frequency:
            frequency[num] = frequency[num]+1
        else:
            frequency[num] = 1

    for key in frequency:
        if frequency[key] == 1:
            print("First non repeating number: ",key)
            break  



approach_1(numbers.copy())

approach_2(numbers.copy())

