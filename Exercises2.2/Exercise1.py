q = int(input())
a = set()
for i in range(q):
    request = list(map(int, input().split()))
    if request[0] == 1:
        a.add(request[1])
    else:
        if request[1] in a:
            print(1)
        else:
            print(0)
