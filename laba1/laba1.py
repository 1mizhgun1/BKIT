import sys
from math import sqrt

def input_coef(index, text):
    try:
        s = sys.argv[index]
    except:
        s = input(text)
    return float(s)

def solve(a, b, c):
    roots = []
    if b == 0.0 and c == 0.0:
        roots.append(0.0)
    elif b == 0.0 and c / a < 0.0:
        roots.append(sqrt(sqrt(-c / a)))
        roots.append(-sqrt(sqrt(-c / a)))
    elif c == 0.0:
        roots.append(0.0)
        if b / a < 0.0:
            roots.append(sqrt(-b / a))
            roots.append(-sqrt(-b / a))
    else:
        d = b ** 2 - 4.0 * a * c
        if d == 0.0 and b / 2.0 / a < 0.0:
            roots.append(sqrt(-b / 2.0 / a))
            roots.append(-sqrt(-b / 2.0 / a))
        elif d > 0.0:
            t1 = (-b + sqrt(d)) / 2.0 / a
            t2 = (-b - sqrt(d)) / 2.0 / a
            if t1 > 0.0:
                roots.append(sqrt(t1))
                roots.append(-sqrt(t1))
            if t2 > 0.0:
                roots.append(sqrt(t2))
                roots.append(-sqrt(t2))
    return roots

def main():
    a = input_coef(1, 'Введите A: ')
    if a == 0.0:
        print('A не может быть равным 0.')
        sys.exit()
    b = input_coef(2, 'Введите B: ')
    c = input_coef(3, 'Введите C: ')
    
    ans = solve(a, b, c)
    cnt = 0
    for i in ans:
        cnt += 1
    print()
    if cnt == 0:
        print('Нет корней.')
    elif cnt == 1:
        print('1 корень:')
    else:
        print(cnt, 'корня:')
    for i in ans:
        print(i)
        
if __name__ == "__main__":
    main()