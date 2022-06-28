'''#방법1
def avg():
    k = sum(L)
    avg = k/len(L)
    return avg
    
    
global L
L=[]
n=int(input('몇 개의 수를 입력하시겠습니까? '))
for i in range(n):
    s = int(input())
    L.append(s)
    
print(avg())'''

#방법2
def avg(*n):
    L=[]
    print(type(n))
    for i in n:
        L.append(i)
    sum = 0
    for i in range(len(L)):
        sum += i
    return sum / len(L)

print('입력한 정수의 평균을 출력 :', avg(1, 3, 4, 2,5,2, 4, 10, 2, 8))
        