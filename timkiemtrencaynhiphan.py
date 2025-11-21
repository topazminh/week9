# =====================================
# CẤU TRÚC NODE CỦA CÂY BST
# =====================================

class Node:
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None


# =====================================
# HÀM CHÈN NODE VÀO BST
# =====================================

def insert(root, key):
    if root is None:
        return Node(key)
    if key < root.key:
        root.left = insert(root.left, key)
    else:
        root.right = insert(root.right, key)
    return root


# =====================================
# XÂY DỰNG BST TỪ MẢNG
# =====================================

def build_bst(arr):
    root = None
    for x in arr:
        root = insert(root, x)
    return root


# =====================================
# TÌM GIÁ TRỊ NHỎ NHẤT TRONG BST
# =====================================

def find_min(root):
    if root is None:
        return None
    while root.left is not None:
        root = root.left
    return root.key


# =====================================
# TÌM GIÁ TRỊ LỚN NHẤT TRONG BST
# =====================================

def find_max(root):
    if root is None:
        return None
    while root.right is not None:
        root = root.right
    return root.key


# =====================================
# TÌM KIẾM TRONG BST + ĐẾM SỐ SO SÁNH
# =====================================

def search_bst(root, key):
    comparisons = 0
    current = root

    while current is not None:
        comparisons += 1
        if current.key == key:
            return True, comparisons
        elif key < current.key:
            current = current.left
        else:
            current = current.right

    return False, comparisons


# =====================================
# VÍ DỤ CHẠY THỬ
# =====================================

if __name__ == "__main__":
    arr = [50, 30, 20, 40, 70, 60, 80]

    root = build_bst(arr)
    print("BST ĐÃ TẠO TỪ MẢNG:", arr)

    print("Giá trị nhỏ nhất:", find_min(root))
    print("Giá trị lớn nhất:", find_max(root))

    key = 60
    found, count = search_bst(root, key)
    print(f"Tìm {key}: {'Thấy' if found else 'Không thấy'}, số lần so sánh = {count}")
