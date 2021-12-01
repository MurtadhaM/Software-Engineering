def add_all():
    total = 0
    for i in range(1, 1001):
        total += i
    return total
def print_all():
    for i in range(1, 1001):
        print(i)
def shortest_path():
    for i in range(1, 1001):
        for j in range(1, 1001):
            if i + j == 1000:
                return i * j