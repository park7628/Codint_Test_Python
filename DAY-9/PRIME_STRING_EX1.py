# 에라토스테네스의 체 적용
import math
import time
import os
import psutil

process = psutil.Process(os.getpid()) # 공간 복잡도를 위한 프로세스 id 얻기

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

# 모든 소수 출력
for i in range(2, n + 1):
	if array[i]:
		print(i, end=' ')
        

print(f"MB bytes : {process.memory_info().rss / (1024.0*1024.0)}") # 해당 프로세스 메모리 공간, 메가 바이트 단위 출력