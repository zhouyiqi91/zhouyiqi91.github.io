grid = [[1,1,0],[1,1,1],[1,2,1]]
more,less = [],[]
for i, row in enumerate(grid):
    for j, x in enumerate(row):
        if x > 1: 
            more.extend([(i,j)] * (x-1))
        elif x==0:
            less.append((i,j))

n = len(more)
used = [False] * n
path = []
print(more,less)

res = []
def per(i):
    print(i,n)
    if i==n:
        res.append(path.copy())
    for j,x in enumerate(less):
        if not used[j]:
            path.append(x)
            used[j] = True
            #print(j,i+1)
            per(i+1)
            path.pop()
            used[j] = False

ans = 1000
per(0)
print(res)
for p in res:
    print('run')
    cur = 0
    print(more,p)
    for (x1,y1),(x2,y2) in zip(more,p):
        print(x1,y1,x2,y2)
        cur += abs(x1-x2) + abs(y1-y2)
    ans = min(ans, cur)
print(ans)
