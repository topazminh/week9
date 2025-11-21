from collections import deque

GOAL = "123456780"

# Các hướng di chuyển của ô trống
moves = {
    0: [1, 3],
    1: [0, 2, 4],
    2: [1, 5],
    3: [0, 4, 6],
    4: [1, 3, 5, 7],
    5: [2, 4, 8],
    6: [3, 7],
    7: [4, 6, 8],
    8: [5, 7]
}

def bfs_8puzzle(start):
    queue = deque([(start, "")])
    visited = set([start])

    while queue:
        state, path = queue.popleft()

        if state == GOAL:
            return path

        zero = state.index("0")

        for mv in moves[zero]:
            lst = list(state)
            lst[zero], lst[mv] = lst[mv], lst[zero]
            new_state = "".join(lst)

            if new_state not in visited:
                visited.add(new_state)
                queue.append((new_state, path + f"{state} -> {new_state}\n"))

    return None


# --------------------------
# CHẠY THỬ
# --------------------------

start = "125340678"
result = bfs_8puzzle(start)

print("Đường đi:")
print(result if result else "Không giải được")
