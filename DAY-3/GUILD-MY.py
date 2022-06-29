# 사실 정렬을 해줘서 max_fear이 필요가 없음
n=int(input())
L= list(map(int, input().split()))
L.sort()
count = 0
guild_num=0
max_fear = 0
for i in L:
    if max_fear<i:
        max_fear = i
    count+=1
    if max_fear <= count:
        guild_num+=1
        count = 0
        max_fear = 0
print('모헌험자 길드의 수 :', guild_num)
