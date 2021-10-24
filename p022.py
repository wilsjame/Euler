def score( word ):
    n = 0
    for c in word:
        n += ord(c) - ord('A') + 1
    return n

def solve():
    with open('p022_names.txt') as f:
        read_data = f.read()
    f.closed
    names = [x.strip('"') for x in read_data.split(',')] 
    names.sort()
    ans = 0
    n = 0
    for name in names:
        n += 1
        ans += score(name) * n
    print(ans)

solve()
