s = input('문자열을 입력하세요 : ')
sum = 0
s = list(s)
print(s)
print(len(s))
for i in range(len(s)):
    if ord(s[i]) <= ord('9') and ord(s[i]) >= ord('0'):
        sum += int(s[i])
        s.pop(i)
    
s.sort()
s.append(str(sum))

s = str(s)

print(s)
# 다 풀이 못함