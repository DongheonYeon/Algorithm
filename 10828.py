import sys

class stack:
    def __init__(self):
        self.stack_arr = []
    
    def push(self, num):
        self.stack_arr.append(num)
        
    def pop(self):
        if self.empty() == 1:
            return -1
        else:
            return self.stack_arr.pop()
        
    def size(self):
        return len(self.stack_arr)
        
    def empty(self):
        if self.size() == 0:
            return 1
        else:
            return 0
        
    def top(self):    
        if self.empty() == 1:
            return -1
        else:
            return self.stack_arr[-1]

N = int(sys.stdin.readline())
new_stack = stack()
for i in range(0, N):
    command = sys.stdin.readline().split()
    if command[0] == "push":
        new_stack.push(int(command[1]))
    elif command[0] == "pop":
        res = new_stack.pop()
        print(res)
    elif command[0] == "size":
        res = new_stack.size()
        print(res)
    elif command[0] == "empty":
        res = new_stack.empty()
        print(res)
    elif command[0] == "top":
        res = new_stack.top()
        print(res)