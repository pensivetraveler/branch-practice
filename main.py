from random import randint
from random import choice

def get_randint() -> list:
    return [randint(1,50) for _ in range(6)]

def get_choice() -> list:
    return [choice(range(1,50+1)) for _ in range(6)]

if __name__ == '__main__':
    print(get_randint())
    print(get_choice())
