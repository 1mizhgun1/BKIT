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
