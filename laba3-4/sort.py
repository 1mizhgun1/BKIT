def my_sort_with_lambda(data):
    return sorted(data, key = lambda x: abs(x))

def my_sort_without_lambda(data):
    return sorted(data, key = abs)

def main():
    data = [4, -30, 30, 100, -100, 123, 1, 0, -1, -4]
    print(my_sort_with_lambda(data))
    print(my_sort_without_lambda(data))

if __name__ == '__main__':
    main()