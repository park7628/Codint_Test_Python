
def left(x):
    if x>0:
        x-=1
    return x

def right(x):
    if x<3:
        x+=1
    return x

def up(y):
    if y>0:
        y-=1
    return y

def down(y):
    if y<3:
        y+=1
    return y

x = 0
y = 0
n = int(input('2차원 행렬의 크기를 입력하세요 : '))
arr = [[0]*n for i in range(n)]
move = list(map(str, input('움직일 경로를 입력하세요(L, R, U, D)').split()))

for i in range(len(move)):
    if move[i]  == 'L':
        x = left(x)
    elif move[i]  == 'R':
        x = right(x)
    elif move[i]  == 'U':
        y = up(y)
    elif move[i]  == 'D':
        y = down(y)
    
print('최종 위치 =', y+1, ',', x+1)
    