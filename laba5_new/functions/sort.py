def my_sort_with_lambda(data):
    return sorted(data, key = lambda x: abs(x))

def my_sort_without_lambda(data):
    return sorted(data, key = abs)
