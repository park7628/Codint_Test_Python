s = input('문자열을 입력하세요 : ')
sum = 0
s = list(s)

for i in range(len(s)):
    if ord(s[i]) <= ord('9') and ord(s[i]) >= ord('0'):
        sum += int(s[i])
        s[i] = '0'
s.sort()
a = s.count('0')
for i in range(a):
    s.pop(0)
s.append(str(sum))
print(*s, sep ='')


    