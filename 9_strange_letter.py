"""
9. Strange Letter

Problem Description
One day, Xiaoming received a strange letter. The letter asks Xiaoming to calculate the sum of all even digits in a given number.
For example, for the number 5548, the result is 12, since 4 + 8 = 12.
Xiaoming is puzzled and asks for your help to solve this problem.

Input Description
The input consists of multiple test cases.
Each line contains one positive integer, guaranteed to be within the 32-bit signed integer range.

Output Description
For each input line, output the sum of even digits.
Each result should be followed by an empty line.

Input Example
415326
3262
Output Example
12

10
"""

def sum_even_digits(number_str):
    return sum(int(ch) for ch in number_str if ch.isdigit() and int(ch) % 2 == 0)

try:
    while True:
        line = input().strip()
        if not line:
            continue
        result = sum_even_digits(line)
        print(result)
        print()  # Print empty line after each result
except EOFError:
    pass

"""
sum_even_digits function:

Iterates over each character in the input string.

Converts the character to an integer only if it's an even digit (int(ch) % 2 == 0).

Sums them up.

The main loop:

Reads input line-by-line.

Stops at EOF (End of File) — good for multiple test cases.

Skips empty lines if any.

Outputs the result and an extra empty line as required.
"""