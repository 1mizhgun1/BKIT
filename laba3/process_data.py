from field import field
from gen_random import gen_random
from unique import Unique
from print_result import print_result
from cm_timer import cm_timer_1
import json

@print_result
def f1(lst):
    return list(sorted(Unique(field(lst, 'job-name'), ignore_case = True)))

@print_result
def f2(lst):
    return list(filter(lambda elem: elem.startswith('программист'), lst))

@print_result
def f3(lst):
    return [lst[i] + ' с опытом Python' for i in range(len(lst))]

@print_result
def f4(lst):
    return [emp + str(sal) for emp, sal in zip(['{}, зарплата '.format(elem) for elem in lst], gen_random(len(lst), 100000, 200000))]

def main():
    path = 'data_light.json'
    with open(path, encoding = "utf8") as file:
        data = json.load(file)
    with cm_timer_1():
        f4(f3(f2(f1(data))))

if __name__ == '__main__':
    main()
