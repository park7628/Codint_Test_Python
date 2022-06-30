s = input('문자를 입력하세요 : ')
abc = [-1 for i in range(26)]
check = []
k = 0
for i in range(len(s)):
    if s[i] in check:
        k+=1
        continue
    else:
        for j in range(26):
            if chr(97+j) in s[i]:
                abc[j] = k
                check.append(chr(97+j))
                k+=1                            
for i in abc:
    print(i, end=' ')