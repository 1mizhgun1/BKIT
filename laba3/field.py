def field(items, *args):
    assert len(args) > 0

    if len(args) == 1:
        answer = []
        for i in range(len(items)):
            answer.append(items[i].get(args[0]))
    else:
        answer = [{} for i in range(len(items))]
        for i in range(len(items)):
            for key in args:
                curr = items[i].get(key)
                if curr is not None:
                    answer[i][key] = curr

    return answer

def main():
    goods = [
        {'title': 'Ковер', 'price': 2000, 'color': 'green'},
        {'title': 'Диван для отдыха', 'price': 5300, 'color': 'black'}
    ]
    answer = field(goods, 'title')
    print(*answer, sep=', ')
    answer = field(goods, 'title', 'price')
    print(*answer, sep=', ')

if __name__ == '__main__':
    main()