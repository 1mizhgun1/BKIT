import requests
import matplotlib.pyplot as plt

def graphic(content, start, finish, n):
    x = [i for i in range(0, n + 1, 1)]
    y = content[start: finish].split(', ')

    plt.figure(figsize=(12, 8))
    plt.title('First {} Padovan`s numbers'.format(n))
    plt.xlabel('index')
    plt.ylabel('Padovan`s numbers')
    plt.plot(x, y, 'ro', linewidth=2, color='r')
    plt.grid(which='major', color='k', linewidth=1)
    plt.show()

def query(n):
    url = 'http://127.0.0.1:5000/padovan'

    param = {'N': str(n)}
    with requests.Session() as s:
        p = s.post(url, data=param)

    content = str(p.content)
    start = content.find('<h3>') + 4
    finish = content.find('</h3>')

    graphic(content, start, finish, n)

def main():
    n = int(input('Введите n: '))
    query(n)

if __name__ == '__main__':
    main()