X = [2, -5, 7, 0, -12, 8, -3, 10, -15, 20, -25, 30, 0, -35, 40, -45]
M = 15
Y = []
for x in X:
    if abs(x) > M:
        Y.append(x)
print(f"Число M: {M}")
print(f"Заданий масив X: {X}")
print(f"Отриманий масив Y: {Y}")