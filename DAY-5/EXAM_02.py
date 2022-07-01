first, second = map(str, input().split('-')) # - 를 구분으로 앞에 주민등록 앞 번호와 뒷 번호를 문자열 형태로 입력
check = first+second # 문자열 합성으로 문자가 입력 되었는지 확인하는 변수
check_num = 0 # 부울 함수 대신에 확인해주는 변수
for i in range(len(check)): # 문자가 들어 갔는지 확인
    if ord(check[i]) >= ord('0') and ord(check[i]) <= ord('9'): # 아스키 코드를 확용해서 0~9 사이의 값이 맞는지 확인
        continue
    else: # 아니라면 check_num변수를 1로 변경
        check_num = 1

if len(first) != 8 or len(second) != 7 or int(first[:4]) > 2022 or int(first[4:6]) > 12 or check_num == 1: #주민등록 에러가 나는 조건을 입력(앞 주민번호의 길이, 뒷 주민번호의 길이, 년도의 범위, 달의 범위)
    print('주민 등록번호 에러')
else:
    if first[0] == '1' and (second[0] == '3' or second[0] == '4'): # 추가적인 에러 조건 입력, 2000년대 이전 출생자 일때 뒷 주민번호가 잘못입력된 경우
        print('주민 등록번호 에러')
    
    elif first[0] == '2' and (second[0] == '1' or second[0] == '2'): # 추가적인 에러 조건 입력, 2000년대 이후 출생자 일때 뒷 주민번호가 잘못입력된 경우
        print('주민 등록번호 에러')
    else:     # 위 조건에 걸리지 않는다면 올바른 주민번호로 간주
        print('올바른 주민번호 입니다.')
        print(f"생년월일 : {first[:4]}년{first[4:6]}월{first[6:]}일") #조건에 맞게 문자열 슬라이싱을 통해 출력 
        if(second[0] == '1' or second[0] == '3'): #남성의 판별 조건
            print('성별: 남성')
        else:  # 위 조건이 맞지 않는다면 여성
            print('성별: 여성')
        check_city = int(second[1:3]) # 출생등록지 고유번호 저장
        if check_city >=0 and check_city <= 8: #비교 후 출력
            print('서울')
        elif check_city >= 9 and check_city <= 12:
            print('부산')
        elif check_city >= 13 and check_city <= 15:
            print('인천')
        elif check_city >= 16 and check_city <= 25:
            print('경기')