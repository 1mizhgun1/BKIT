from time import time, sleep
from contextlib import contextmanager

class cm_timer_1:
    def __init__(self):
        self.time = 0
        
    def __enter__(self):
        self.time = time()
        return self.time
    
    def __exit__(self, type_, value_, tb_):
        self.time = time() - self.time
        print(self.time)
        
@contextmanager
def cm_timer_2():
    time_ = 0
    try:
        time_ = time()
        yield time_
    finally:
        time_ = time() - time_
        print(time_)

def main():
    with cm_timer_1():
        sleep(5.5)
    with cm_timer_2():
        sleep(5.5)

if __name__ == '__main__':
    main()