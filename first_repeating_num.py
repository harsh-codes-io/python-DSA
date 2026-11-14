
numbers = [4, 2, 7, 2, 8, 4, 9]

seen = set()

for num in numbers:
    if num in seen:
        print("first repeating number is: ",num)
        break
    else:
        seen.add(num)
    