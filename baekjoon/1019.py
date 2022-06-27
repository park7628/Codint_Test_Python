#백준 1019 / 시간초과뜸 다시 생각하기

n = int(input())
L = []
for i in range(0, 10):
    cnt = 0
    for j in range(1, n+1):
        if str(i) in str(j):
            num_j = j
            for k in range(len(str(j))):
                x = num_j%10
                if x==i:
                    cnt += 1
                num_j//=10
                
    L.append(cnt)
    
for i in L:
    print(i, end=' ')
        