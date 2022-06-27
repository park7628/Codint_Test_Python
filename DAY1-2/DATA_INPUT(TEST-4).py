n = int(input())
sum = 0
if n>0 and n<101:
    for i in range(1, n+1):
        if i%2 ==0:
            sum+=i
print(sum)


while(1):
    k = input()
    if k =='q':
        break
    print(k)