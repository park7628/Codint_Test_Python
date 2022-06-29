n, k = map(int, (input('화폐 개수와 거스름 돈의 값을 입력해주세요 : ').split()))
coin_L=[]
for i in range(n):
    a = int(input('동전 가격을 갯수만큼 입력 : '))
    coin_L.append(a)
coin_L.sort()
coin_L.reverse()
count = 0
for i in coin_L:
    count += k//i
    k = k%i
print('거슬러 준 동전 화폐의 수 :', count)