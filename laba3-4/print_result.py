from gen_random import gen_random
import types

def print_result(func):
    def wrap(*args, **kwargs):
        print(func.__name__)
        result = func(*args, **kwargs)
        if isinstance(result, list):
            for elem in result:
                print(elem)
        elif isinstance(result, types.GeneratorType):
            print(*result)
        elif isinstance(result, dict):
            for key, value in result.items():
                print('{} = {}'.format(key, value))
        else:
            print(result)
        return result
    return wrap

@print_result
def test_1():
    return 1


@print_result
def test_2():
    return 'iu5'


@print_result
def test_3():
    return {'a': 1, 'b': 2}


@print_result
def test_4():
    return [1, 2]

@print_result
def test_5():
    return gen_random(5, 1, 3)

def main():
    test_1()
    test_2()
    test_3()
    test_4()
    test_5()

if __name__ == '__main__':
    main()