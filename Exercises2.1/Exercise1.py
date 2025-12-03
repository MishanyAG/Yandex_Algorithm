data = [0]
q = int(input())
results = []

for _ in range(q):
    request = input().split()
    n = int(request[0])
    x = int(request[1])
    if n == 1:
        data.insert(x + 1, request[2])
    elif n == 2:
        results.append(data[x])
    elif n == 3:
        del data[x]

for result in results:
    print(result)