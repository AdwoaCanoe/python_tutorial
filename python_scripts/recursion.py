def timer(number):
	if number <= 0:
		print("Addictive python")
	else:
		print(number)
		timer(number - 1)

print(timer(number=5))