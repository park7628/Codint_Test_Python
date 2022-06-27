s = input('주민등록 번호를 입력해주세요(구분은 -로 합니다.) :').split('-')
print(s[0],s[1], sep ="")

print(''.join(s))