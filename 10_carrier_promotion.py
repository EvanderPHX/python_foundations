"""
10. Carrier Promotion
Problem Description
Xiaoming spends 1 yuan of phone credit per day. The mobile carrier is running a promotion: for every K yuan recharged, you get 1 extra yuan of bonus credit.
At the beginning, Xiaoming recharges M yuan.
How many days can he use the phone at most?
Note: The bonus credit can also be used to earn more bonus credit — i.e., the reward is recursive.

Input Description
The input contains multiple test cases.
Each test case contains two integers: M and K, where 2 ≤ K ≤ M ≤ 1000.
The input ends when M = 0 and K = 0.

Output Description
For each test case, output a single integer: the maximum number of days Xiaoming can use the phone with M yuan, considering the promotion.

Input Example:
2 2
4 3
13 3
0 0
Output Example:
3
5
19
Explanation Hint (for the last case "13 3"):

Start with 13 yuan.

13 ÷ 3 = 4 bonus yuan, with 1 yuan left → total 5 yuan.

5 ÷ 3 = 1 bonus yuan, with 2 left → total 3 yuan.

3 ÷ 3 = 1 bonus yuan, with 0 left → total 1 yuan.

1 yuan can’t earn more bonus.

Total days:
13 (initial) + 4 (bonus) + 1 (bonus) + 1 (bonus) = 19 days
"""

def max_days(m, k):
    total = m
    current = m
    while current >= k:
        bonus = current // k
        remainder = current % k
        total += bonus
        current = bonus + remainder
    return total

# Read multiple test cases
while True:
    line = input().strip()
    if not line:
        continue
    m, k = map(int, line.split())
    if m == 0 and k == 0:
        break
    print(max_days(m, k))


"""
total: total days Xiaoming can use his balance (initial + all bonuses).

current: current usable credit (initially M, then updated with bonuses).

While there's enough credit to get at least 1 bonus (current >= k):

Get bonus = current // k

Remaining = current % k

Add bonus to total days

Update current = bonus + remainder and repea
"""