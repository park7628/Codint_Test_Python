'''#백준 1019 / 시간초과뜸 다시 생각하기

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
    print(i, end=' ')'''
    
'''#방법 2 메모리 에러 에서 수정했더니 시간초과뜸...
#백준 1019

n = int(input())
#num_L=['0','1','2','3','4','5','6','7','8','9']
#chek=[]
cnt = 0
for j in range(10):
    for k in range(1,n+1):
        cnt += str(k).count(str(j))                
    #chek.append(cnt)
    print(cnt, end=' ')
    cnt = 0
    
#for i in chek:
#    print(i, end=' ')'''

#코드를 최대한 줄여봄. 그러나 시간초과 아마도 중첩반복문에서 걸리는듯
n = int(input())
cnt = 0
for j in range(10):
    for k in range(1,n+1):
        cnt += str(k).count(str(j))                
    print(cnt, end=' ')
    cnt = 0

#사이트 참고
# https://nerogarret.tistory.com/36
# https://pacific-ocean.tistory.com/240
        