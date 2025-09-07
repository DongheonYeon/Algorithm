# 노드
# 포인터

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self, value):
        self.head = Node(value)

    # LinkedList의 맨 끝 노드에 새로운 노드 추가
    def append(self, value):
        cur = self.head
        while cur.next is not None:
            cur = cur.next
        cur.next = Node(value)
        
    # LinkedList의 모든 노드의 값을 출력
    def print_all(self):
        cur = self.head
        while cur is not None:
            print(cur.data)
            cur = cur.next
            
    def get_node(self, index):
        cur = self.head
        for i in range(index):
            cur = cur.next
        return cur
    
    def add_node(self, index, value):
        new_node = Node(value)
        if index == 0:
            new_node.next = self.head
            self.head = new_node
            return
        prev_node = self.get_node(index-1)
        next_node = prev_node.next
        prev_node.next = new_node
        new_node.next = next_node

    def delete_node(self, index):
        if index == 0:
            self.head = self.head.next
            return
        prev_node = self.get_node(index-1)
        next_node = prev_node.next.next
        prev_node.next = next_node

linked_list = LinkedList(5)
linked_list.append(3)
linked_list.append(12)
linked_list.print_all()

print("idx 1 노드: ", linked_list.get_node(1).data)

linked_list.add_node(0, 1)
linked_list.print_all()

linked_list.delete_node(0)
linked_list.print_all()

#  0      1      2
# [5] -> [3] -> [12]