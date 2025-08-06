"""
8. Leveling the Blocks

Problem Description
Xiaoming loves playing with building blocks. One day, he stacked many blocks into several piles of different heights. Each pile is a vertical stack of blocks. Now, he wants all the piles to be of the same height. However, he's lazy and wants to move as few blocks as possible to achieve this. Can you help him?

Input Description
The input consists of multiple test cases.
Each test case starts with a positive integer n — the number of block piles Xiaoming has created.
The next line contains n positive integers, each representing the height h of a pile (each block has a height of 1).
Constraints:

1 <= n <= 50

1 <= h <= 100

The total number of blocks is guaranteed to be divisible by the number of piles.
The input ends when n = 0.

Output Description
For each test case, output the minimum number of blocks that need to be moved to make all piles the same height.
Print an empty line after each result.

Input Example
6
5 2 4 1 7 5
0
Output Example
5

"""

def min_moves_to_level(piles):
    average = sum(piles) // len(piles)
    moves = 0
    for height in piles:
        if height > average:
            moves += height - average
    return moves

while True:
    n = int(input())
    if n == 0:
        break
    heights = list(map(int, input().split()))
    result = min_moves_to_level(heights)
    print(result)
    print()  # Print empty line after each result

"""
Read the number of piles n. If n == 0, the input ends.
Read n integers representing the height of each pile.
Compute the average height.
Count how many blocks need to be moved from piles higher than the average (since we can only remove from taller piles).
Output the result followed by an empty line.
"""