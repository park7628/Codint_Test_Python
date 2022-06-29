n = int(input('거스름 돈을 알려주세요 : '))
L = [500, 100, 50, 10]
money = 0
i = 0
count = 0
while True:
    if (money + L[i]) <= n:
        money+=L[i]
        count+=1
    else:
        i+=1
        
    if money == n:
        break
        
print(count)
    