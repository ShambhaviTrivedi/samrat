numbers=[1,2,3,4,5]
print(numbers)
numbers2=numbers.copy()
numbers.append(20)     # adds number to the ending of list
print(numbers)
print(numbers2)
numbers.insert(0,20)  # adds number to the specific index of list
print(numbers)
numbers.remove(20)     # removes first occurance of that number
print(numbers)
numbers.remove(20)
print(numbers)
numbers.pop()          # pops out last value
print(numbers)
# To know index values
print(numbers.index(1)) # gives index  number in list
print(numbers.index(3))
#print(numbers.index(50))
numbers=[6,7,8,9,10]
print( 6 in numbers)
print(50 in numbers)
numbers=[10,10,10,11,2,2,2,2,6,6,6]
# to know the count of repeating numbers
print(numbers.count(10))
print(numbers.count(11))
print(numbers.count(2))
print(numbers.count(6))
numbers.sort()  # sorts in ascending order
print(numbers)
numbers.reverse() # sorts in descending order
print(numbers)
numbers.clear()        # clears all 
print(numbers)