# INTENTIONAL LOGIC BUG: use for guided debugging.
def add_value(total, value):
    return total + value


def calculate_total(values):
    total = 0
    for value in values:
        total = 0
        total = add_value(total, value)
    return total


values = [12, 8, 15, 10, 5]
print("Total:", calculate_total(values))
