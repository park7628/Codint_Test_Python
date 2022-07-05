L = []
n = int(input())

for i in range(n):
    arr = list(map(str, input().split()))
    L.append(arr)
    
L.sort(key = lambda x: x[0])
print()

for i in range(n):
    print(*L[i])