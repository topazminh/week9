# Node của danh sách liên kết
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

# Danh sách liên kết đơn
class LinkedList:
    def __init__(self):
        self.head = None

    # Thêm vào cuối danh sách
    def append(self, data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
            return
        cur = self.head
        while cur.next:
            cur = cur.next
        cur.next = new_node

    #  Tìm kiếm tuần tự
    def linear_search(self, key):
        cur = self.head
        index = 0
        while cur:
            if cur.data == key:
                return index  # Trả về vị trí tìm thấy
            cur = cur.next
            index += 1
        return -1  # Không tìm thấy

# Demo
ll = LinkedList()
for x in [10, 20, 30, 40]:
    ll.append(x)

k = 30
pos = ll.linear_search(k)
print("Vị trí:", pos)
