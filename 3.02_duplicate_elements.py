"""
Дан список повторяющихся элементов. Вернуть список с дублирующимися элементами.
В результирующем списке не должно быть дубликатов.
"""

list_1 = [1, 2, 9, 8, 9, 3, 1, 5, 6, 4, 7, 4, 4, 4]
without_duplicate = list(set(list_1))
duplicate_elements = []

for el in without_duplicate:
    if list_1.count(el) > 1:
        duplicate_elements.append(el)

print(f"Дан список, где некоторые элементы повторяются: --- {list_1}")
print(f"Список элементов без повторов: -------------------- {without_duplicate}")
print(f"Список повторяющихся элементов: ------------------- {duplicate_elements}")
