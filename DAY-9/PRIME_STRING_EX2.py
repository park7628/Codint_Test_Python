import math

num_list = []
while True:
    string_num = input()
    if string_num == '0':
        break
    num_list.append(string_num)
    
soosu_check = []


n = 100000 # 2부터 1,000까지의 모든 수에 대하여 소수 판별
# 처음엔 모든 수가 소수(True)인 것으로 초기화(0과 1은 제외)
array = [True for i in range(n + 1)]
# 에라토스테네스의 체 알고리즘 수행
# 2부터 n의 제곱근까지의 모든 수를 확인하며
for i in range(2, int(math.sqrt(n)) + 1):
    if array[i] == True: # i가 소수인 경우(남은 수인 경우)
    # i를 제외한 i의 모든 배수를 지우기
        j = 2
        while i * j <= n:
            array[i * j] = False
            j += 1
    
for i in range(len(num_list)):
    soosu = 0
    for j in range(2, n+1):
        if array[j]:
            if str(j) in num_list[i]:
                soosu = j
                
    soosu_check.append(soosu)
            
print( *soosu_check, sep = "\n")