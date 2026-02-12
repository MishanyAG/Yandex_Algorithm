n = int(input())
a = list(map(int, input().split()))
b = []
for i in range(n):
    if i == 0:
        b.append(a[i])
    else:
        b.append(min(a[i], b[i - 1]))
print(*b)