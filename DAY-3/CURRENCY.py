import time
import os
import psutil

process = psutil.Process(os.getpid()) # 공간 복잡도를 위한 프로세스 id 얻기
start_time = time.time()
n = 1260

#n = int(input('거스름돈의 값을 입력해 주세요 (정수) : '))
cnt = 0

array = [500, 100, 50, 10]
for coin in array:
    cnt += n // coin
    n %= coin

print(f"동전의 거스름돈 최소 개수는 : {cnt}개")

end_time = time.time()
print(f"time : {format(end_time - start_time, '10f')}") # 정확도 소수 아래 10자리로 ㅅ행 시간 출력
print(f"MB bytes : {process.memory_info().rss / (1024.0*1024.0)}") # 해당 프로세스 메모리 공간, 메가 바이트 단위 출력