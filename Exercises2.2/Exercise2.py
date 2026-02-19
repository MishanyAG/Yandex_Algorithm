n = int(input())
base = set(map(int, input().split()[1:]))
for _ in range(n-1):
    base.update(set(map(int, input().split()[1:])))
print(len(base))