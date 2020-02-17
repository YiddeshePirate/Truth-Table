# MIT License
#
# Copyright (c) 2017 Christian Lyder Jacobsen
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in all
# copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.


import numpy as np

from tabulate import tabulate
from tools import getparenthasesstatement, getIndex, getreversedindex, cleartemp, loop_over_non_parentheses



# This function takes in an expression and an unpacked dictionary consisting of truth values
# it replaces variables with truth values and symbols with logical boolean operater and runs
# eval() on the finished string
# not sure if I need an unpacked dictionary
def get_vars_from_exp(expression):
    # print(expression)
    list_vars = [x for x in expression if x.isalpha()]
    list_vars = [x for x in list_vars if x is not "C"]
    list_vars = list(set(list_vars))
    list_vars.sort()
    return list_vars



def truth_value(statement, F=False, **kwargs):
    # print(statement, kwargs)
    if ">" not in statement:
        symbols_dict = {"^":"and", "|":"or", "~":"not", "(":"(", ")":")"}
        # makes it easier to find and replace, also to accomadate replacing variables with a boolean Truth value
        x = list(statement)
        for i in x:
            # replace letters with True or False
            if i in kwargs.keys():
                x = [j if j != i else kwargs[i] for j in x]
                pass
            # replace symbols with "and" or "or" 
            elif i in symbols_dict.keys():
                # x = [j for j in x if j != i else symbols_dict[i]]
                x = [j if j != i else symbols_dict[i] for j in x]
            else:
                pass
        # have to replace the boolean Truth values with a string to run eval()
        x = [str(x) for x in x]
        # back to a string from list
        x = " ".join(x)
        # print(x)
        C = False
        y = eval(x)
        # print(x, y)
        return (y)
    else:
        cleartemp()
        symbols = loop_over_non_parentheses(statement)
        x = statement[:symbols[0][1]]
        y = statement[symbols[0][1]+1:]
        # return None
        truth_y = truth_value(y, **kwargs)
        truth_x = truth_value(x, **kwargs)

        return not(truth_x) or truth_y


# creates initial array with just variables
def variable_array(expression):
    list_of_vars = [x for x in expression if x.isalpha() == True]
    list_of_vars = [x for x in expression if x is not "C"]

    num_variables = set(list_of_vars)
    num_variables = len(num_variables)
    width = num_variables
    # double the first period
    height = 2 * (2 ** (num_variables-1))
    # first period

    period = 2 ** (num_variables-1)
    # original amount of times period repeats
    sets = 1
    array = np.empty((height, width), dtype=bool)
    for i in range(int(num_variables)):
        true = [True for x in range(period)]
        false = [False for x in range(period)]
        total_period = true + false
        full_column = total_period * sets
        # each succesive row will have a period half of the previous one
        period = int(period / 2)
        # and double the ammount of sets
        sets *= 2
        array[:, i] = full_column



        

        

    return array


def dict_vals(expression):
    list_vals = get_vars_from_exp(expression)
    potential_array = variable_array(list_vals)
    dict_val_table = {}
    for j, i in enumerate(list_vals):
        # print(j, i)
        dict_val_table[i] = list(potential_array[:, j])
    
    if "C" in expression:
        lenofcolumn = len(dict_val_table[list(dict_val_table.keys())[0]])
        clist = [False for x in range(lenofcolumn)]
        dict_val_table["C"] = clist

    return dict_val_table

# takes an expression, one of the columns on the table, creates list of values for it.
def add_exp_to_dict(expression, values_dict):


    global final_table
    # get variables we are working with
    working_values = {x for x in expression if x.isalpha() == True}  
    expressions_truth_vals = []
    # convoluted way to get the range of the first list in dictionary
    for i in range(len(list(values_dict.values())[0])):
        
        # termporary dictionary of values for p
        tempdict = {j:values_dict[j][i] for j in values_dict}
        expressions_truth_vals.append(truth_value(expression, **tempdict))

    derived_table_values[expression] = expressions_truth_vals
    return values_dict
        

# function to get expression for rest of tables
def get_table_names(exp):
    # eventual list
    list_of_exp_with_symbol = []

    symbols = ["|", "^", ">"]
    # iterate through list and get the index the letter before and the letter after
    for i, j, k, l in zip(list(range(len(exp))), exp, exp[1:], exp[2:]):

        if k in symbols:
            # if the symbol before was a parentheses
            if j == ")":
                # start the expression from the other side of parentheses
                starting_point = getreversedindex(exp, i)

            else:
                starting_point = i if exp[i-1] != "~" else i-1

            if l == "(":
                ending_point = getIndex(exp, i+2)+1

            else:
                # if its a letter end at the letter if its a ~ sign end the next character
                ending_point = i+3 if exp[i+2] != "~" else i+4

            list_of_exp_with_symbol.append(exp[starting_point:ending_point])

        elif k == "~":

            if l == "(":
                ending_point = getIndex(exp, i+2)+1

            else:
                ending_point = i+3
            starting_point=i+1
            list_of_exp_with_symbol.append(exp[starting_point:ending_point])


 
    list_of_exp_with_symbol.sort(key= lambda x : len(x))
    return(list_of_exp_with_symbol)


def making_of_a_table(statement):
    global derived_table_values
    variables = get_vars_from_exp(statement)
    # variables.remove("C")
    dictionary_val = dict_vals(statement)
    # print(dictionary_val)
    derived_tables = get_table_names(statement)
    derived_table_values = {}
    for i in derived_tables:
        add_exp_to_dict(i, dictionary_val)
    dictionary_val.update(derived_table_values)
    x = dictionary_val
    # x = making_of_a_table(statement)

    table = list(x.values())
    # we currently have a dictionary with th values and rows,
    # needed to turn it into an array to flip it to be the right format for tabulate
    table = np.array(table, dtype=bool)
    table = np.rot90(table)
    table = np.flipud(table)
    grid = tabulate(table, headers=x.keys(), tablefmt="fancy_grid")
    print(grid)






expression = str(input("\nWhat is the expression you would like to make a truth table for?\n\n"))

# wrapped in parentheses to make it a bit clearer for me to code

making_of_a_table(f"({expression})")
 





