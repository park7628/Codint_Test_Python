s = input('문자열을 입력하세요 : ')
s= list(s)
i = 0
while(i<len(s)):
    if s[i] == 'g':
        i+=2
    else:
        print(s[i], end='')
        i+=1
        
