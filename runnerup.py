'''
getting the second largest number
'''
arr = [2, 3, 4, 5, 6]
max_ = max(arr)
arr.remove(max_)
print(max(*arr))

''' 
the previous way doesnt work for list with duplicate max
'''
arr_ = [1,2,3,4,5,6,6]
x = max(arr_)
while max(arr_) == x:
	arr_.remove(max(arr_))
print(max(arr_))
