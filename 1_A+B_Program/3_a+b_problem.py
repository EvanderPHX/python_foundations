"""
3. A+B Problem III
Problem Description
Your task is still to compute the sum of a + b.

Input Description:
Each line of the input contains a pair of integers a and b.
There will be one pair 0 0 which indicates the end of input, and this pair should not be included in the computation.

Output Description:
For each input pair a and b, output their sum on a separate line.
For example, the sum of the second pair should appear on the second output line.

Input Example:
2 4
11 19
0 0
Output Example:
6
30

3. A+B问题III
题目描述
你的任务依然是计算a+b。

输入描述
输入中每行是一对a和b。其中会有一对是0和0标志着输入结束，且这一对不要计算。

输出描述
对于输入的每对a和b，你需要在相应的行输出a、b的和。
如第二对a和b，他们的和也输出在第二行。
输入示例
2 4
11 19
0 0
输出示例
6
30
"""

import sys

lines = sys.stdin.readlines()
# print(lines)
for line in lines:
    line = line.strip()
    if not line:
        continue  # Skip empty lines
    a,b = map(int,line.strip().split())
    if a==0 and b==0: # one pair 0 0 which indicates the end of input
        break
    print(a+b)

"""
tips:
sys.stdin.readlines() reads all lines from input.
.strip() removes trailing newlines or spaces.
.split() splits the line into strings.
map(int, ...) turns them into integers.
"""