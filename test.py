counter = 0.2
accumulator = 0.0
while round(accumulator,2) != 4.0:
	accumulator = accumulator + counter
	print(f"I'm stuck here... {accumulator:.2f}")
print("The end!")
