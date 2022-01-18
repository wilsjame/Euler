"""
Ulam's spiral implementaion sum diagonals
7 8 . .
6 1 2 .
5 4 3 .

1001 x 1001 spiral
1001*1001 = 1002001 is the final digit
must end in corner, any corner is ok
work backwards 
number of concentric squares including '1' is 1001//2 + 1
"""
n = 1001
k = n*n
ans = 0
for sq in range(n//2 + 1):
    # dimension of concentric square ex) 5, 3, 1
    dim = n - sq * 2
    if dim > 1:
        # length between corners in square
        l = dim - 2 
        # walk perimeter of square
        for i in range(4 + 4 * l):
            k -= 1
            # corner!
            if i % (l + 1) == 0:
                ans += k + 1
    else:
        ans += 1
print(ans)
