import random


def is_safe(board, row, col):
    # строка
    for i in range(col):
        if board[row][i] == 1:
            return False
    # Верхний диагональ слева
    for i, j in zip(range(row, -1, -1), range(col, -1, -1)):
        if board[i][j] == 1:
            return False
    # Нижний диагональ слева
    for i, j in zip(range(row, len(board)), range(col, -1, -1)):
        if board[i][j] == 1:
            return False

    return True


def n_ferz(board, col, solutions):
    if col == len(board):
        solutions.append([[row.index(1) + 1, col + 1] for row in board])
        return True

    safe = False
    for i in range(len(board)):
        if is_safe(board, i, col):
            board[i][col] = 1
            n_ferz(board, col + 1, solutions)
            board[i][col] = 0

    return safe


def f_ferz():
    board = [[0 for _ in range(8)] for _ in range(8)]
    solutions = []
    n_ferz(board, 0, solutions)
    return solutions



solutions = f_ferz()
# выводит все варианты расстановок
# print('Количество расстановок:', len(solutions))
# print("Координаты 8 ферзей, не бьющих друг друга:")
# for i, solution in enumerate(solutions):
#     print(f"Расстановка {i + 1}: {solution}")

random_4 = random.sample(range(len(solutions)), 4)

print(f'Случайные 4 расстановки из {len(solutions)}: ')
for i, index in enumerate(random_4):
    print(f'Расстановка {i + 1}: {solutions[index]}')