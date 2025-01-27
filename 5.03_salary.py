names = ['Bob', 'Alice', 'Martin']
salaries = [20000, 25000, 35000]
percents = ['10.25%', '13.50%', '6.75%']

res = {names[i]: [salaries[j] * float(percents[j][:-1]) / 100 for j in range(len(salaries))][i] for i in range(len(names))}

print(res)