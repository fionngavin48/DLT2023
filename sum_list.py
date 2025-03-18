# Sum list as denominators with a numerator of 1
denominators = list(map(int, input("Enter numbers separated by spaces: ").split()))
x = 0
for i in denominators:
	x += (1/i)
print(x)