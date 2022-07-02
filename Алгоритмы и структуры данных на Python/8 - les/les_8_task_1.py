# 1. На улице встретились N друзей. Каждый пожал руку всем остальным друзьям (по одному разу).
# Сколько рукопожатий было?
# Примечание. Решите задачу при помощи построения графа.

friends = int(input("Введите N друзей: "))

gr = []
for i in range(friends):
    row = [1] * friends
    row[i] = 0
    gr.append(row)

print(gr)

hands_haked = 0
for row in gr:
    for i in row:
        hands_haked  += i

print(f"Кол-во рукоприкладств = {hands_haked}")
