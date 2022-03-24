''' 
first of all the user must input the number of commands he gonna use
then type every command with its parametres
'''
n = int(input())
arr = []
'''
for i in range(n):
	comm = input().split()
	if comm[0] == 'insert':
		arr.insert(int(comm[1]), int(comm[2]))
	if comm[0] == 'print':
		print(arr)
	if comm[0] == 'remove':
		arr.remove(int(comm[1]))
	if comm[0] == 'append':
		arr.append(int(comm[1]))
	if comm[0] == 'sort':
		arr.sort()
	if comm[0] == 'pop':
		arr.pop(len(arr)-1)
	if comm[0] == 'reverse':
		arr.reverse()
'''
'''
using eval instead
'''

for i in range(n):
	comm = input().split()
	args = comm[1:]
	if comm[0] == 'print':
		print(arr)
	else:
		eval(f'arr.{comm[0]}{tuple(map(int, comm[1:]))}')
	
		
