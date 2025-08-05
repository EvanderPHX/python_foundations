"""
1. A+B Problem I
Problem Description
Your task is to compute the sum of a and b.

Input Description
The input contains a series of pairs of integers a and b, separated by a space.
Each pair of a and b is given on a separate line.

Output Description
For each input pair of a and b, output their sum on a separate line in the same order as they appear in the input.

Example Input:
3 4
11 40

Example Output:
7
51
"""

import sys

lines = sys.stdin.readlines()
# print(lines)
for line in lines:
    a,b = map(int,line.strip().split())
    print(a+b)


"""
tips

| Use                         | Example                         |
| --------------------------- | ------------------------------- |
| Apply function to each item | `map(str.upper, ['a', 'b'])`    |
| Lambda with map             | `map(lambda x: x*2, [1, 2, 3])` |
| With input processing       | `map(int, input().split())`     |


string.strip()
By default, it removes all leading and trailing whitespace characters, including:
spaces ' '
tabs \t
newlines \n and \r

🔹 Example:
text = "  \n\t Hello World \n\t  "
cleaned = text.strip()
print(cleaned)  # "Hello World"

✅ Strip specific characters:
string.strip(chars)
chars is a string of characters to remove from both ends.
Note: it does not treat chars as a substring, but as a set of characters.

🔹 Example:
filename = "###log.txt###"
cleaned = filename.strip('#')
print(cleaned)  # "log.txt"
You can also combine characters:

s = "abcHelloabc"
print(s.strip('abc'))  # "Hello"


⚠️ Important:
strip() does not remove characters in the middle of the string.

It stops stripping as soon as it hits a character not in the chars set, from both ends.

✅ Summary:
Expression	What it does
s.strip()	Removes whitespace from both ends
s.strip("xyz")	Removes any of x, y, z from both ends
s.lstrip()	Removes from the left only
s.rstrip()	Removes from the right only
"""

"""
✅ str.split() Basic Syntax:
string.split(sep=None, maxsplit=-1)
sep: the separator to split on (default is any whitespace)
maxsplit: how many splits to do (default is no limit)

🔹 Example 1: Default split (by whitespace)
text = "hello world python"
words = text.split()
print(words)  # ['hello', 'world', 'python']
→ Splits by any whitespace (spaces, tabs, newlines)

🔹 Example 2: Custom separator
data = "apple,banana,orange"
fruits = data.split(",")
print(fruits)  # ['apple', 'banana', 'orange']

🔹 Example 3: Limit number of splits (maxsplit)
text = "a b c d"
parts = text.split(" ", maxsplit=2)
print(parts)  # ['a', 'b', 'c d']

🔹 Example 4: Split user input
# user types: 1 2 3
nums = input("Enter numbers: ").split()
nums = list(map(int, nums))
print(nums)  # [1, 2, 3]

✅ Summary:
Usage	        Description
s.split()	    Split by any whitespace
s.split(',')	Split by comma
s.split('\n')	Split by newline
s.split(' ', 1)	Split once on the first space
"""