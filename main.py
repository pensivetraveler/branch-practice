from random import sample

def get_luckies() -> list:
	return sample(range, 1, 45+1), k=6)

if __name__ == '__main__':
	print(get_luckies())
