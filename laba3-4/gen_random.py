from random import randint

def gen_random(cnt, begin, end):
    for i in range(cnt):
        yield randint(begin, end)

def main():
    answer = gen_random(5, 1, 3)
    print(*answer, sep=', ')

if __name__ == '__main__':
    main()