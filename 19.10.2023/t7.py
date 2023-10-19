X = [5, -3, 7, 0, -8, -1, 12, 9, -4, -6, 2, -11, 14, -15, 10, -13]
Y = []
for x in X:
    if x < 0:
        Y.append(-x)
    else:
        Y.append(x) 
print("Заданий масив X:", X)
print("Отриманий масив Y:", Y)
