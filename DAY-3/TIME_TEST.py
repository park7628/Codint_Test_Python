import time
import random

start_time = time.time() #측정시작
arr = []

for i in range(2000):
    arr.append(random.randint(0,10))
    
for i in arr:
    for j in arr:
        temp = i*j
        
print(temp)
end_time = time.time()
print("time:", end_time - start_time)