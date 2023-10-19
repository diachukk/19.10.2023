s1 = []
for i in range(16):
    while True:
        try:
            s2 = int(input(f"Введіть {i+1}-й елемент масиву: "))
            s1.append(s2)
            break  
        except ValueError:
            print("Будь ласка, введіть ціле число.")

max = max(s1)
print(f"Максимальний елемент в масиві: {max}")

reversed = s1[::-1]
print("Масив у зворотньому порядку:", reversed)
