<center> <h1>Truth Table Python 1</h1> </center>

This is a command line program to take in logical statements and return a matching truth table

The logical operators it can handle are 
```
>: implies, |:or, ^: and, ~:not
```
Noted bugs are the inability to use imply multiple times without parentheses

Features I plan on adding include use of the ```<>:iff``` operator and better error checking.

In the distant future I might add add tables with matplotlib

Usage:

Make sure to have the tools.py in the same directory

```
c:>python truth table.py

What is the expression you would like to make a truth table for?

```
Entry:
```
~(q|~p)^w
```

Returns:

```
| p | q | w | ~p | q|~p | ~(q|~p) | (q|~p)^q |
|---|---|---|----|------|---------|----------|
| 1 | 1 | 1 | 0  | 1    | 0       | 1        |
| 1 | 1 | 0 | 0  | 1    | 0       | 0        |
| 1 | 0 | 1 | 0  | 0    | 1       | 0        |
| 1 | 0 | 0 | 0  | 0    | 1       | 0        |
| 0 | 1 | 1 | 1  | 1    | 0       | 1        |
| 0 | 1 | 0 | 1  | 1    | 0       | 0        |
| 0 | 0 | 1 | 1  | 1    | 0       | 1        |
| 0 | 0 | 0 | 1  | 1    | 0       | 0        |
```

The way the table looks will be slightly different specificaly the output of
```
Tabulate(table, tablefmt="fancy_grid")
```

Enjoy!




