"""
7. Grade Point Average

Problem Description
Each course grade is assigned a letter: A, B, C, D, or F. For calculating the Grade Point Average (GPA), the grades correspond to the following point values:

A = 4 points

B = 3 points

C = 2 points

D = 1 point

F = 0 points

Input Description
There are multiple test cases. Each input line contains one test case, consisting of one or more uppercase letters separated by spaces.

Output Description
Each output line corresponds to one test case.

If all the letters in the input are from the set {A, B, C, D, F}, output the average GPA, rounded to two decimal places.

Otherwise, output "Unknown".

Input Example
A B C D F
B F F C C A
D C E F
Output Example
2.00
1.83
Unknown
"""

def grade_to_point(grade):
    mapping = {'A': 4, 'B': 3, 'C': 2, 'D': 1, 'F': 0}
    return mapping.get(grade)

def calculate_gpa(line):
    grades = line.strip().split()
    points = []

    for grade in grades:
        point = grade_to_point(grade)
        if point is None:
            return "Unknown"
        points.append(point)

    average = sum(points) / len(points)
    return f"{average:.2f}"

# Example usage:
input_lines = [
    "A B C D F",
    "B F F C C A",
    "D C E F"
]

for line in input_lines:
    print(calculate_gpa(line))
