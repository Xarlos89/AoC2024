def make_columns(plans: str):
    column = []

    with open(plans, 'r') as file:
        for line in file:
            levels = line.strip().split()
            column.append([int(float(item)) for item in levels])
    return column


def rules_apply(plan):
    is_increasing = all(plan[i] < plan[i + 1] for i in range(len(plan) - 1))
    is_decreasing = all(plan[i] > plan[i + 1] for i in range(len(plan) - 1))
    valid_differences = all(1 <= abs(plan[i] - plan[i + 1]) <= 3 for i in range(len(plan) - 1))

    return (is_increasing or is_decreasing) and valid_differences

def the_dampener(some_plan):
    """ This is for part 2 """
    for i in range(len(some_plan)):
        modified_plan = some_plan[:i] + some_plan[i+1:]
        if rules_apply(modified_plan):
            return True
    return False


def safety_check(all_plans):
    safe = 0
    unsafe = 0
    for plan in all_plans:
        if rules_apply(plan):
            safe += 1
        else:
            unsafe += 1
    return safe, unsafe

def safety_check_with_dampener(all_plans):
    """ This is for part 2 """
    safe = 0
    unsafe = 0
    for plan in all_plans:
        if rules_apply(plan):
            safe += 1
        else:
            if the_dampener(plan):
                safe +=1
            else:
                unsafe += 1
    return safe, unsafe

# Part 1
print(safety_check(make_columns(("data.txt"))))

# Part 2
print(safety_check_with_dampener(make_columns(("data.txt"))))
