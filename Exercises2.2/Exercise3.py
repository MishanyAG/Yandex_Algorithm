n = int(input())
base = set(map(int, input().split()[1:]))
for i in range(n-1):
    base.intersection_update(set(map(int, input().split()[1:])))

print(len(base))