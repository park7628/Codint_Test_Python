import random # random모듈 호출
trap_row_list = [0 for i in range(6)]    #함정의 행값을 받을 리스트 생성
trap_column_list = [0 for i in range(6)]  #함정의 열값을 받을 리스트 생성
trap_row = 0 # 변수선언(꼭 필요하지는 않은듯)
trap_column = 0 # 변수선언(마찬가지?)
for i in range(6): # 반복으로 값을 저장
    trap_row = random.randint(1, 8)    #randint를 활용해 랜덤으로 값을 초기화
    trap_column = random.randint(1, 8)
    trap_row_list[i] = trap_row     # 값을 리스트에 저장
    trap_column_list[i] = trap_column

index_row = [] # 말이 이동한 좌표를 확인하기 위한 행 리스트 생성
index_column = [] # 말이 이동한 좌표를 확인하기 위한 열 리스트 생성
input_data = input('나이트의 위치 a~h, 1~8 입력 하기 : ') # 현재 나이트의 위치 입력받기, a1
row = int(input_data[1]) # 정수형 입력 받음, 1
column = int(ord(input_data[0])) - int(ord('a')) + 1 # 문자열을 아스키 코드로 변환, a

# 나이트가 이동할 수 있는 8가지 방향 정의
steps = [(-2, -1), (-1, -2), (1, -2), (2, -1), (2, 1), (1, 2), (-1, 2), (-2, 1)] 
result = 0 # 이동 횟수 초기화

count=0 # 함정에 도착했을 때의 경우를 카운트 하는 변수 선언 및 초기화
for step in steps:
    next_row = row + step[0] # 이동하고자 하는 위치 확인
    next_column = column + step[1]
    index_row.append(next_row) # 위치값을 행 리스트에 저장
    index_column.append(next_column) # 위치값을 열 리스트에 저장
    #print(next_row, next_column) # 내부 좌표 디버깅
    for i in range(6): #이동한 좌표가 함정의 위치와 겹치는지 확인
        if next_row == trap_row_list[i] and next_column == trap_column_list[i]:
            count+=1 #겹친다면 count의 값을1씩 증가
                    
    if next_row >= 1 and next_row <= 8 and next_column >= 1 and next_column <= 8:
        result += 1 # 해당 위치로 이동이 가능하다면 카운트 증가
print('함정의 좌표 : ', end='') #함정의 좌표 출력
for i in range(6):
    print(f"( {trap_row_list[i]}, {trap_column_list[i]} )", end='')
print()
print('말이 이동한 좌표 : ', end ='') #말이 이동한 좌표 출력
for i in range(6):
    print(f"( {index_row[i]}, {index_column[i]} )", end='')
print()
print(f"{result-count}번 이동할 수 있습니다. (함정{count}번 회피!)") #결과 출력
