"""
5. A+B Problem V
Problem Description
Your task is to compute the sum of two integers.

Input Description
The input contains multiple lines. Each line consists of two integers a and b, separated by a space.

Output Description
For each pair of input values, output the sum of a and b, followed by a blank line after each result.

Input Example
2 4
11 19
Output Example
6

30


5. A+B问题V
题目描述
你的任务是计算两个整数的和。
输入描述
输入包含若干行，每行输入两个整数a和b，由空格分隔。
输出描述
对于每组输入，输出a和b的和，每行输出后接一个空行。
输入示例
2 4
11 19
输出示例
6

30

"""

import sys

lines = sys.stdin.readlines()
for line in lines:
    if not line:
        continue   # skip empty lines
    a,b = map(int,line.strip().split())
    print(a+b)
    print()        # print a blank line