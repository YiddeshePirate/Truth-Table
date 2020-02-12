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


def cleartemp():
    global count, symbols
    count = 0
    symbols = []
def loop_over_non_parentheses(exp):
    global count, symbols
    list_with_index = []
    # print(exp)
    for j, i in enumerate(exp):
        # print((j, i))
        if i == "(":
            # print(j)
            new_start = getIndex(exp, j)
            expnew = exp[new_start+1:]
            # print(exp)
            count += new_start+1
            loop_over_non_parentheses(expnew)
            break
        elif i == ">":
            symbols.append((i, count+j))
    return symbols
# print(getparenthasesstatement("~(~h^(b^j))^(~h^j)"))