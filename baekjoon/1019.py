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
    
    '''방법 2 메모리 에러
    #백준 1019

n = int(input())
num_L=['0','1','2','3','4','5','6','7','8','9']
L = []

chek=[]

for h in range(n):
    L.append(str(h+1))
    
cnt = 0
for j in range(10):
    for k in range(n):
        for a in range(len(L[k])):
            if num_L[j] == L[k][a]:
                cnt+=1
                
    chek.append(cnt)
    cnt = 0
    
for i in chek:
    print(i, end=' ')
    '''
        