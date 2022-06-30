data = input('숫자 문자 조합 데이터를 입력 : ')
result = []
value = 0
for x in data: # 문자를 하나씩 확인하며
    if x.isalpha(): # 알파벳(한글 포함)인 경우
        result.append(x) # 리스트에 삽입
    else:
        value += int(x) # 숫자는 따로 더하기
        result.sort() # 알파벳을 오름차순으로 정렬
    
if value != 0: # 숫자가 하나라도 존재하는 경우 가장 뒤에 삽입
    result.append(str(value))
    print(''.join(result)) # 최종 결과 출력(리스트를 문자열로 변환하여 출력, join 함수)
