n = int(input())
a = list(map(int, input().split()))
maxV = 0
maxI = 0
for i in range(n):
    if maxV <= a[i]:
        maxV = a[i]
        maxI = i

del a[maxI]
print(*a)