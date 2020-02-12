from parenthasestools import getreversedindex, getIndex, getparenthasesstatement
import re

    

def get_tables(exp):
    list_of_exp_with_symbol = []
    symbols = ["|", "^", ">"]
    for symbol in symbols:
        for i, j, k, l in zip(list(range(len(exp))), exp, exp[1:], exp[2:]):
            if k == symbol:
                # print(k)
                if j == ")":
                    starting_point = getreversedindex(exp, i)
                    # print(starting_point)
                else:
                    starting_point = i

                if l == "(":
                    ending_point = getIndex(exp, i+2)+1
                    print(ending_point)
                    # print(i+2)
                    # print(exp[i+2])
                    # print(ending_point)
                else:
                    ending_point = i+3
                list_of_exp_with_symbol.append(exp[starting_point:ending_point])
 
    list_of_exp_with_symbol.sort(key= lambda x : len(x))
    return(list_of_exp_with_symbol)

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
 



# def truth_value(statement, **kwargs):
#     # print(statement, kwargs)
#     if ">" not in statement:
#         symbols_dict = {"^":"and", "|":"or", "~":"not", "(":"(", ")":")"}
#         # makes it easier to find and replace, also to accomadate replacing variables with a boolean Truth value
#         x = list(statement)
#         for i in x:
#             # replace letters with True or False
#             if i in kwargs.keys():
#                 x = [j if j != i else kwargs[i] for j in x]
#                 pass
#             # replace symbols with "and" or "or" 
#             elif i in symbols_dict.keys():
#                 # x = [j for j in x if j != i else symbols_dict[i]]
#                 x = [j if j != i else symbols_dict[i] for j in x]
#             else:
#                 pass
#         # have to replace the boolean Truth values with a string to run eval()
#         x = [str(x) for x in x]
#         # back to a string from list
#         x = " ".join(x)
#         # print(x)
#         y = eval(x)
#         # print(x, y)
#         return (y)
#     else:
#         cleartemp()
#         loop_over_non_parentheses(statement)
#         print(symbols)
#         x = statement[:symbols[0][1]]
#         y = statement[symbols[0][1]+1:]
#         # return None
#         truth_y = truth_value(y, **kwargs)
#         truth_x = truth_value(x, **kwargs)

        # return not(truth_x) or truth_y
# print(truth_value("q>x", q=True, x=False))