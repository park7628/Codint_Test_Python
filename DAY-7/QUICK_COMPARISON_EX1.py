from random import randint
import time
# 배열에 10,000개의 정수를 삽입
array = []
for _ in range(80000):
	# 1부터 100 사이의 랜덤한 정수
	array.append(randint(1, 100))
    
# 퀵 정렬 프로그램 성능 측정
start_time = time.time()

# 퀵 정렬 프로그램 소스코드
def quick_sort(array):
	# 리스트가 하나 이하의 원소만을 담고 있다면 종료
	if len(array) <= 1:
		return array
    
	pivot = array[0] # 피벗은 첫 번째 원소
	tail = array[1:] # 피벗을 제외한 리스트
    
	left_side = [x for x in tail if x <= pivot] # 분할된 왼쪽 부분
	right_side = [x for x in tail if x > pivot] # 분할된 오른쪽 부분
    
	# 분할 이후 왼쪽 부분과 오른쪽 부분에서 각각 정렬 수행하고, 전체 리스트 반환
	return quick_sort(left_side) + [pivot] + quick_sort(right_side)
#print(quick_sort(array))
quick_sort(array)
    
# 측정 종료
end_time = time.time()
# 수행 시간 출력
#print(array)
print("퀵 정렬 성능 측정:", end_time - start_time)

# 배열을 다시 무작위 데이터로 초기화 
array = []
for _ in range(80000):
	# 1부터 100 사이의 랜덤한 정수
	array.append(randint(1, 100))
    
# 기본 정렬 라이브러리 성능 측정
start_time = time.time()
# 기본 정렬 라이브러리 사용
array.sort()
# 측정 종료
end_time = time.time()
# 수행 시간 출력
#print(array)
print("병합 정렬 라이브러리 성능 측정:", end_time - start_time)
