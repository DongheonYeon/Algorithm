import sys

N = int(sys.stdin.readline().rstrip())

cnt = 1
stack = []
op = []
valid = True

for i in range(N):
    current = int(sys.stdin.readline().rstrip())
    while cnt <= current:
        stack.append(cnt)
        op.append('+')
        cnt += 1
    
    if stack[-1] == current:
        stack.pop()
        op.append('-')
    else:
        valid = False
        break
    
if valid == True:
    for i in op:
        print(i)
else:
    print("NO")