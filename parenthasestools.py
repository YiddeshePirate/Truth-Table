import re


# x = "~((p^q)v)r"

# print(re.findall("s|t|r", x))

# Python program to find index of closing 
# bracket for a given opening bracket. 
from collections import deque 

def getIndex(s, i): 

	# If input is invalid. 
	if s[i] != '(': 
		return -1

	d = deque() 

	for k in range(i, len(s)): 

		if s[k] == ')': 
			d.popleft() 
		elif s[k] == '(': 
			d.append(s[i]) 
		if not d: 
			return k

	return -1





def getreversedindex(s, i):
	if s [i] != ")":
		return -1



	d = deque()

	for k in range(i, -1, -1):
		
		if s[k] == "(":
			d.popleft()
		elif s[k] == ")":
			d.append(s[i])
		if not d:
			return k
	return -1
	
# print(getreversedindex("kdj(dk(dk))", 9))
# print(getreversedindex("(fds)", 4))
# print(getIndex("(fds)", 0))

# string = "(d(k)@)"

def getparenthasesstatement(string):
	listof_paren = []
	for j, i in enumerate(string):
		if i == "(":
			listof_paren.append(getIndex(string, j))
	return listof_paren



# print(getparenthasesstatement("~(~h^(b^j))^(~h^j)"))