"""
Создайте словарь со списком вещей для похода в качестве ключа и их массой в качестве значения.
Определите какие вещи влезут в рюкзак передав его максимальную грузоподъёмность.
Достаточно вернуть один допустимый вариант.
*Верните все возможные варианты комплектации рюкзака.
"""

things = {
    'Фонарь': 300,
    'Вода': 500,
    'Палатка': 2500,
    'Спички': 10,
    'Куртка': 400,
    'Мангал': 1000,
    'Матрас': 3000,
    'Спрей от комаров': 200,
    'Фотоаппарат': 800,
}

tonnage = 3300

results = []
thing_keys = sorted(list(things.keys()), key=lambda x: things[x], reverse=True)
for i in range(len(things)):
    if things[thing_keys[i]] <= tonnage:
        temp_things = {}
        for j in range(i, len(things)):
            if sum(temp_things.values()) + things[thing_keys[j]] <= tonnage:
                temp_things[thing_keys[j]] = things[thing_keys[j]]
        results.append(temp_things)





combinations_for_delete = set()
for i in range(len(results) -1, -1, -1):
    if not i in combinations_for_delete:
        for j in range(i -1, -1, -1):
            if set(results[i].keys()).issubset(set(results[j].keys())):
                combinations_for_delete.add(i)
for i in sorted(list(combinations_for_delete), reverse=True):
    results.pop(i)

for result in results:
    print(f"{list(result.keys())}. Суммарный вес - {sum(result.values())} г.")

