numbers = [12, 5, 27, 8, 19]

#Direct for loop to print 
for num in numbers:
    print(num,end=" ")

#index based traversal using range() 
print("\n\n")
for i in range(len(numbers)):
    print(f"index:{i},value:{numbers[i]}  ")

#Enumerator to print index and value
print("\n\n")
for index,value in enumerate(numbers):
    print(f"index:{index},value:{value}  ")


#Enumerator to print index and value - index start from 1
print("\n\n")
for index,value in enumerate(numbers,start=1):
    print(f"index:{index},value:{value}  ")