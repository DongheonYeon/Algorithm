import sys

N = int(sys.stdin.readline())
for _ in range(N):
    input = list(sys.stdin.readline().rstrip())
    pstack=[]
    is_VPS="YES"
    for ps in input:
        if ps == "(":
            pstack.append(ps)
        else:
            if not pstack:
                # ')' 가 남아있는데 pstack이 비어있을 경우
                is_VPS = "NO"
                break
            else:
                pstack.pop()
    
    if pstack:
        is_VPS = "NO"
        
    print(is_VPS)