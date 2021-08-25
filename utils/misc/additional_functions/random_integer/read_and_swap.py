def read_and_swap(data):
    if len(data) == 2:
        a, b = map(int, data)
    elif len(data) == 3:
        a, b = map(int, data[1:])
    if a > b:
        a, b = b, a
    return a, b
