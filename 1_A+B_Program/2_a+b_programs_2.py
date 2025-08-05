"""
2. A+B Problem II
Problem Description
Compute the sum of a + b, but the input format is slightly different.

Input Description
The first line contains an integer N, indicating that there will be N lines following, each containing two integers a and b separated by a space.

Output Description
For each pair of a and b, output their sum on a new line, in the corresponding order.
For example, the second pair of a and b should produce output on the second line.

Input Example

Copy
Edit
2
2 4
9 21
Output Example

Copy
Edit
6
30
Hint
Note that there may be multiple test cases, not just one group of data.
In other words, input will continue with new values of N followed by corresponding pairs of a and b.

2. A+B问题II
题目描述
计算a+b，但输入方式有所改变。

输入描述
第一行是一个整数N，表示后面会有N行a和b，通过空格隔开。

输出描述
对于输入的每对a和b，你需要在相应的行输出a、b的和。
如第二对a和b，对应的和也输出在第二行。
输入示例
2
2 4
9 21
输出示例
6
30
提示信息
注意，测试数据不仅仅一组。也就是说，会持续输入N以及后面的a和b
"""

import sys

lines = sys.stdin.readlines()
# print(lines)
i=0
while i < len(lines):
    N = int(lines[i].strip())
    i+=1

    for _ in range(N):
        a,b = map(int,lines[i].strip().split())
        print(a+b)
        i+=1

"""
✅ Summary:
Pattern	Meaning
for _ in range(N)	Loop N times, ignore the index
_ = value	        Assign but don't use
x, _, y = ...	    Ignore part of tuple unpacking
"""

# if __name__ == '__main__':
#     pass