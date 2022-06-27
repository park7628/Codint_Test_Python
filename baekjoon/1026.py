#백준 1026

n = int(input())
sum = 0
a  = list(map(int, input().split()))
b = list(map(int, input().split()))

a.sort()

for i in range(n):
    index = 0
    max_num = 0
    for h in range(len(b)):
        if b[h] > max_num:
            max_num = b[h]
            index = h
    sum += a[i]*b[index]
    b.pop(index)
    
print(sum)
    
    