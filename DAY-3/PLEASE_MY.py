a, b = map(int, input().split())
count = 0
while True:
    if a % b == 0:
        a = a//b
        count+=1
    else:
        while ((a%b) != 0):
            a -= 1
            count +=1
            if a==1:
                break   
        if a==1:
            break
        a = a//b
        count+=1  
    if a==1:
        break
        
print(count)