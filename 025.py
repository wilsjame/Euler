"""
dp find the first fibonacci term to contain 1000 digits
"""
dp: dict[int, int] = {}
dp[0] = 0
dp[1] = 1

i = 2
while True:
    dp[i] = dp[i-1] + dp[i-2]
    if len(str(dp[i])) == 1000:
        break
    i += 1
print(i)
