dic = {}
key =[]
value =[]
print('키와 값을 입력하세요(단 값은 정수, 구분은 space)')
for i in range(5):
    a,b = input().split()
    b = int(b)
    key.append(a)
    value.append(b)
    dic[a] = b

dic = sorted(dic)
dic.reverse()
print(type(dic))
print(dic)

