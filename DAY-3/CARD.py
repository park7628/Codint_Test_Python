n, m = map(int, input('행의 수 n과 열의 수 m을 입력하세요 : ').split())
min_num=0
L = [0 for i in range(n)]
card_list=[]
print(L)
for i in range(n):
    L[i] = list(map(int, input().split()))
    
for i in range(n):
    min_num = min(L[i])
    card_list.append(min_num)

print(L)
print('행의 가장 작은 값중 가장 큰값은 :', max(card_list))

    