
n = int(input())
a = list(map(int, input().split()))
b = []
for i in range(n):
    for j in range(i, n):
        x = a[i]
        for m in a[i:j+1][::-1]:
            x |= m
        b.append(x)
print(len(set(b)))
            
