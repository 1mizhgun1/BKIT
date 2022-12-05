''' Числа Падована:
    P(0) = P(1) = P(2) = 1
    P(n) = P(n - 2) + P(n - 3)  '''

def Padovan(n):
    p = [1, 1, 1]
    for i in range(min(3, n + 1)):
        yield p[i]
    for i in range(3, n + 1):
        next = p[0] + p[1]
        p[0] = p[1]
        p[1] = p[2]
        p[2] = next
        yield next