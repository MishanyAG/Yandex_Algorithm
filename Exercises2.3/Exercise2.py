n = int(input())
a = list(map(int, input().split()))
b = {}
for i in range(n):
    b[a[i]] = b.get(a[i], 0) + 1
b = sorted(b.items(), key = lambda x: (-x[1], x[0])) #ага  кортежи... угу. 
print(b[0][0])