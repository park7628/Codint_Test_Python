a, b = map(int, input('정수 2개를 입력 받아 차를 계산 : ').split()) #map 활용한 정수 입력 방식
print(a-b)

a,b = input('정수 2개를 입력 받아 차를 계산 : ').split() # 직접 정수 캐스팅
c = int(a)-int(b)
d = int(a)*int(b)
e = int(a)/int(b)
f = int(a)%int(b)
print('차, 곱, 몫, 나머지 연산 결과 : ', c, d, e, f) #사칙 연산 출력

a,b = input('단어 여러번 출력 : ').split()
print(a*int(b)) # 단어 반복

s = int(input('문자 반복 횟수 입력 : '))
s2 = input('문자열 직접 입력 :')
print(s*s2) #문장 반복
