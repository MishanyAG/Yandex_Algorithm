n = int(input())
a = list(map(int, input().split()))
d = {}
for i in range(n):
    d[a[i]] = d.get(a[i], 0) + 1
d = sorted(d.items(), key = lambda x: (-x[1], x[0]))
print(d)
result = [d[0][0], d[1][0], d[2][0]]
print(*sorted(result))