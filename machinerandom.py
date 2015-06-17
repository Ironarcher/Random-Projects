import random

def guess(startnum, endnum):
	guess = 50
	c = [0, 25, 13, 6, 3, 1, 1, 1]
	num = random.randint(startnum, endnum)
	number_of_guesses = 1

	while guess != num:
		if guess > num:
			#Too high
			guess = guess - c[number_of_guesses]
		elif guess < num:
			#Too low
			guess = guess + c[number_of_guesses]

		number_of_guesses += 1

	return number_of_guesses

def main():
	stack = []
	for x in range(1,100000):
		stack.append(guess(1,100))
		print(x)
	avg = reduce(lambda x, y: x+y, stack) / float(len(stack))
	print(avg)

if __name__ == "__main__":
	main()