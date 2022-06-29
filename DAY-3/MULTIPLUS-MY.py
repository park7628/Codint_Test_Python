n = input('수를 입력하세요 : ')
n = list(n)
num=0
while(num == 0):
    num = int(n[0])
    n.pop(0)

for i in n:
    if ( num*int(i) > num+int(i)):
        num *= int(i)
    else:
        num += int(i)
print(num)
    
    



