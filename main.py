from random import randint

def get_luckies() -> list:
	# _ 라는 건 ignore, for 문에서 내부 변수를 사용하지 않고 있으므로 ignore를 사용한 것
	return [randint(1,45) for _ in range(6)]

if __name__ == '__main__':
	print(get_luckies())
