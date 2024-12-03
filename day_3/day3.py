import re


def data(corrupted_data):
    with open(corrupted_data, 'r') as file:
        file = file.read()
    return file


def part_1_find_data(raw_data):
    matches = re.findall(r'mul\((\d+,\d+)\)', raw_data)
    return matches


def part_1():
    total = 0
    for mul in part_1_find_data(data("data.txt")):
        mul = mul.split(",")
        total += int(float(mul[0])) * int(float(mul[1]))
    return total


def part_2():
    total = 0
    segments = data("data.txt").split("do()")

    for segment in segments:
        valid_part = segment.split("don't()")[0]
        total += part_2_do_maphs(valid_part)

    return total


def part_2_do_maphs(result):
    total = 0
    matches = re.findall(r"mul\((\d+),(\d+)\)", result)

    for a, b in matches:
        total += int(a) * int(b)

    return total


print(part_1())
print(part_2())


