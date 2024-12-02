def make_columns(file_path):
    column_1, column_2 = [], []

    with open(file_path, 'r') as file:
        for line in file:
            parts = line.strip().split()
            column_1.append(int(parts[0]))
            column_2.append(int(parts[1]))

    column_1.sort()
    column_2.sort()
    return column_1, column_2

def part_1(data):
    column_1, column_2 = make_columns(data)
    differences = sum(abs(a - b) for a, b in zip(column_1, column_2))
    return differences


def part_2(data):
    column_1, column_2 = make_columns(data)
    similarity = sum(num * column_2.count(num) for num in column_1)
    return similarity


print(part_1("data.txt"))
print(part_2("data.txt"))
