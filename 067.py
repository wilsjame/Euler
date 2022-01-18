"""
dp[i][j] stores the max path sum from the top at each row i if we end on element j
this prob leans more greedy than dynamic programming feels like
"""
a: list[list[int]] = []
with open('p067_triangles.txt') as f:
    for line in f:
        a.append([int(x) for x in line.strip().split(' ')])

dp: dict[tuple[int, int], int] = {}
dp[(0,0)] = a[0][0]
h: int = len(a)
for i in range(1,h):
    n = len(a[i])
    for j in range(n):
        if j == 0:
            dp[(i,j)] = dp[(i-1,j)] + a[i][j]
        elif j == n-1:
            dp[(i,j)] = dp[(i-1,j-1)] + a[i][j]
        else:
            labove, rabove = dp[(i-1,j-1)], dp[(i-1,j)]
            dp[(i,j)] = max(labove, rabove) + a[i][j]

ans = -1
for k in range(len(a[h-1])):
    ans = max(ans, dp[(h-1,k)])
print(ans)
