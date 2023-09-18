def are_ferz(ferz):
    for i in range(len(ferz)):
        for j in range(i + 1, len(ferz)):
            x1, y1 = ferz[i]
            x2, y2 = ferz[j]
            if x1 == x2 or y1 == y2:
                return False
            if abs(x1 - x2) == abs(y1 - y2):
                return False
    return True

ferz = [(1, 7), (2, 4), (3, 2), (4, 8), (5, 6), (6, 1), (7, 3), (8, 5)]

if are_ferz(ferz):
    print("Ферзи не бьют друг друга.")
else:
    print("Ферзи бьют друг друга.")