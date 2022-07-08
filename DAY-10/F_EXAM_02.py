from bisect import bisect_left, bisect_right
import sys
import random
import time
import os
import psutil
# 값이 [left_value, right_value]인 데이터의 개수를 반환하는 함수
def count_by_range(a, left_value, right_value):
    right_index = bisect_right(a, right_value)
    left_index = bisect_left(a, left_value)
    return right_index - left_index
process = psutil.Process(os.getpid()) # 공간 복잡도를 위한 프로세스 id 얻기

#매장에 있는 물품의 갯수
n =int(sys.stdin.readline())
# 전자매장이 보유한 부품 종류 리스트
#a = list(map(int, sys.stdin.readline().split())) # 입력받는것을 주석처리, sys를 활용해 입력받음
a = [0]*n # 빈 리스트 생성
for i in range(n):
    a[i] = random.randint(1, 10) #랜덤값을 저장
a.sort()


#손님이 찾는 물품의 갯수
m = int(sys.stdin.readline())
# 손님이 찾는 부품 종류 리스트
# x = list(map(int, sys.stdin.readline().split()))  # 입력받는것을 주석처리
x = [0]*m # 빈 손님 리스트 생성
for i in range(m):
    x[i] = random.randint(1, 10) #랜덤값을 저장
x.sort()

start_time = time.time() #처음 시간 기록
# 반복문을 돌면서 값이 x[i]인 데이터가 있는지 확인 
for i in range(m):
    k = count_by_range(a, x[i], x[i])
    '''if k == 0:
        print('NO', end=' ')
    else:
        print('YES', end = ' ')'''
end_time = time.time() #마지막 시간 기록 
print(f"동작 시간 : {format(end_time - start_time, '.10f')}") # 시간을 소수점 10자리 기준으로 출력
print(f"MB bytes : {process.memory_info().rss / (1024.0*1024.0)}") # 해당 프로세스 메모리 공간, 메가 바이트 단위 출력
