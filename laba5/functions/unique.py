class Unique(object):
    def __init__(self, items, **kwargs):
        self.cnt = -1
        if len(kwargs) == 0:
            self.ignore_case = False
        else:
            value = kwargs['ignore_case']
            self.ignore_case = value
        self.items = []
        for elem in items:
            if isinstance(elem, str):
                if self.ignore_case == True:
                    elem_ = elem.lower()
                    if elem_ not in self.items:
                        self.items.append(elem_)
                else:
                    if elem not in self.items:
                        self.items.append(elem)
            else:
                if elem not in self.items:
                    self.items.append(elem)

    def __next__(self):
        if self.cnt < len(self.items) - 1:
            self.cnt += 1
            return self.items[self.cnt]
        else:
            raise StopIteration

    def __iter__(self):
        return self

    def __repr__(self):
        return str(self.items)
