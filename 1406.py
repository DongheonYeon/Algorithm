import sys

class editor:
    def __init__(self, arr):
        self.l_stack = list(arr)
        self.r_stack = []	# reversed
    
    def L(self):
        if len(self.l_stack) != 0:
            self.r_stack.append(self.l_stack.pop())
            
    def D(self):
        if len(self.r_stack) != 0:
            self.l_stack.append(self.r_stack.pop())
    
    def B(self):
        if len(self.l_stack) != 0:
            self.l_stack.pop()
    
    def P(self, char):
        self.l_stack.append(char)
        
    def print_editor(self):
        print(''.join(self.l_stack + self.r_stack[::-1]))

new_editor = editor(sys.stdin.readline().rstrip())
M = int(sys.stdin.readline())
for i in range(0, M):
    cmd = sys.stdin.readline().split()
    if cmd[0] == "L":
        new_editor.L()
    elif cmd[0] == "D":
        new_editor.D()
    elif cmd[0] == "B":
        new_editor.B()
    elif cmd[0] == "P":
        new_editor.P(cmd[1])

new_editor.print_editor()