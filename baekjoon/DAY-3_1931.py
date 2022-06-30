n = int(input())
L = [0 for i in range(n)]

for i in range(n):
    L[i] = list(map(int, input().split()))
L.sort(key = lambda x : (x[1], x[0]))

count=1
value = L[0][1]
for i in range(1,n):
    if L[i][0] >= value:
        count+=1
        value = L[i][1]
    
print(count)
#정답
    