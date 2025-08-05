"""
4. A+B Problem IV
Problem Description
Your task is to compute the sum of several integers.

Input Description
Each line starts with an integer N, which indicates that there are N integers following it on the same line.
If N = 0, it means the end of input, and that line should not be processed.

Output Description
For each valid line of data, output the sum of the numbers on a separate line.

Input Example:
4 1 2 3 4
5 1 2 3 4 5
0
Output Example:
10
15


4. A+B问题IV
题目描述
你的任务是计算若干整数的和。

输入描述
每行的第一个数N，表示本行后面有N个数。

如果N=0时，表示输入结束，且这一行不要计算。

输出描述
对于每一行数据需要在相应的行输出和。

输入示例
4 1 2 3 4
5 1 2 3 4 5
0
输出示例
10
15

"""

import sys

lines = sys.stdin.readlines()  # Read all input lines at once
for line in lines:
    nums = list(map(int, line.strip().split()))  # Convert each line into a list of ints
    N = nums[0]  # First number tells how many numbers follow
    if N == 0:
        break  # Stop processing if N == 0
    print(sum(nums[1:]))  # Sum the next N numbers and print

"""
tips:
Reading all lines at once, parsing them, checking for N == 0, and printing the sum of the following N numbers.
"""