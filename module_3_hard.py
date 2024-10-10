# Подсчет суммы чисел и длин строк в произвольной структуре данных

sum_ = 0


def calculate_structure_sum(data_structure):
    global sum_
    for i in data_structure:
        if isinstance(i, str):
            sum_ += len(i)
            continue
        if isinstance(i, int):
            sum_ += i
            continue
        elif isinstance(i, tuple):
            calculate_structure_sum(i)
            continue
        elif isinstance(i, list):
            calculate_structure_sum(i)
            continue
        elif isinstance(i, set):
            calculate_structure_sum(i)
            continue
        elif isinstance(i, dict):
            calculate_structure_sum(i.keys())
            calculate_structure_sum(i.values())
            continue
    return sum_

data_structure = [
[1, 2, 3],
{'a': 4, 'b': 5},
(6, {'cube': 7, 'drum': 8}),
"Hello",
((), [{(2, 'Urban', ('Urban2', 35))}])
]

result = calculate_structure_sum(data_structure)
print(result)
