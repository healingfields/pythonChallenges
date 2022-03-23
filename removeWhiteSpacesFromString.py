'''
removing spaces from a string w/o using string methods
'''

x = "    this is a string   "

def remove_spaces(s):
	if len(s) == 0:
		return s
	elif s[0] == " ":
		return remove_spaces(s[1:])
	elif s[-1] == " ":
		return remove_spaces(s[:-1])
	else:
		return s
		
print(remove_spaces(x))


#second way


idxs = [] 
for i, v in enumerate(x):
	if v != " ":
		idxs.append(_)
		
print(x[idxs[0]:idxs[-1]+1])
