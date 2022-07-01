s, x = map(str, input().split(',')) # 문자열 s와 없앨 수의 갯수인 x를 ,를 활용하여 입력

x = int(x) # 문자형태의 x값을 int형으로 변환
s_list = list(s) # 문자열 s를 리스트로 저장
len_last_num = len(s)-x # 최종적으로 출력해야 될 문자의 길이
while True:
    max_index = s.find(max(s_list)) # 리스트에서 가장 큰 값을 찾고, 문자열에서 그 위치값을 받아옴
    if len(s[max_index : ]) >= len_last_num: # 문자열 슬라이싱을 하여 가장 큰 수부터 끝까지의 길이가 최종적으로 출력해야 될 문자의 길이보다 크다면
        s = s[max_index : ] # 슬라이싱한 문자열을 다시 s에 저장
        break 
    else: # 위 조건에 만족하지 않는다면
        s_list.pop(max_index) # 가장 큰값을 빼주고 다음으로 큰 값의 위치를 찾음

print(s)
while True:
    if len(s) == len_last_num: # 문자열의 길이가 최종적으로 출력할 수의 길이와 동일하다면
        print(*s, sep='') # 출력
        break
    else: # 위 조건에 맞지 않다면
        new_s_list = list(s) # 새로운 문자열 s에 대한 리스트 행성
        new_max_index = s.find(max(new_s_list)) # 리스트에서 가장 작은값을 찾고 문자열에서 위치값을 바당옴
        if new_max_index > 1: # 받아온 위치값이 1보다 크다면, (새로운 문자열s에 첫 0번째 값과 가장 큰 값 사이에 다른 수가 있다면)
            new_s_list.pop(1) # 사이값을 제거
            s = ''.join(s for s in new_s_list) # 문자열 s를 다시 초기화
        else: # 가장 큰 값이 문자열의 1번 인덱스에 위치한다면
            min_index = s.find(min(new_s_list)) #가장 작은 값은 찾음
            new_s_list.pop(min_index) #가장 작은 값을 빼줌
            s = ''.join(s for s in new_s_list) # 문자열 s를 다시 초기화
