n = int(input())
d = {}

for i in range(n):
    q = list(map(int, input().split()))
    if q[0] == 1:
        d.update({q[1]:q[2]})
    else:
        if q[1] not in d:
            d.update({q[1]:-1})
        print(d[q[1]])
