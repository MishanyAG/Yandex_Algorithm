n = int(input())
a = []
d = {}
for i in range(n):
    a.append(list(map(int, input().split())))
    f, s = a[i][0], a[i][1]
    while s:
        f, s = s, f % s
    a[i][0] //= f
    a[i][1] //= f
    keyy = tuple(a[i])
    d[keyy] = d.get(keyy, 0) + 1
d = sorted(d.items(), key=lambda x: (-x[1],x[0][0]/x[0][1]))
print(*d[0][0])