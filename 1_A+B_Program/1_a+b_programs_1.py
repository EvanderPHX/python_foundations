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

for line in sys.stdin:
    a,b = map(int,line.split())
    print(a+b)



