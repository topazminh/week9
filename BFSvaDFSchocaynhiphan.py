from collections import deque

# --------------------------
# CẤU TRÚC NODE CỦA CÂY NHỊ PHÂN
# --------------------------
class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None


# --------------------------
# DFS (Duyệt theo chiều sâu)
# 3 kiểu: Preorder, Inorder, Postorder
# --------------------------

def dfs_preorder(root):
    if root is None:
        return
    print(root.val, end=" ")
    dfs_preorder(root.left)
    dfs_preorder(root.right)

def dfs_inorder(root):
    if root is None:
        return
    dfs_inorder(root.left)
    print(root.val, end=" ")
    dfs_inorder(root.right)

def dfs_postorder(root):
    if root is None:
        return
    dfs_postorder(root.left)
    dfs_postorder(root.right)
    print(root.val, end=" ")


# --------------------------
# BFS (Duyệt theo chiều rộng)
# --------------------------

def bfs(root):
    if root is None:
        return
    q = deque([root])
    while q:
        node = q.popleft()
        print(node.val, end=" ")
        if node.left:
            q.append(node.left)
        if node.right:
            q.append(node.right)


# --------------------------
# VÍ DỤ CHẠY
# --------------------------

if __name__ == "__main__":
    root = Node(1)
    root.left = Node(2)
    root.right = Node(3)
    root.left.left = Node(4)
    root.left.right = Node(5)

    print("DFS Preorder:")
    dfs_preorder(root)
    print("\nDFS Inorder:")
    dfs_inorder(root)
    print("\nDFS Postorder:")
    dfs_postorder(root)
    print("\nBFS:")
    bfs(root)
