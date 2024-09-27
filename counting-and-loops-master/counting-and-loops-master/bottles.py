for i in range(100, 0, -1):
	print(i, "bottles of beer on the wall")
	print(i, "bottles of beer")
	print("Take one down, pass it around")
	print(i-1, "bottles of beer on the wall")
	if (i == 6):
		print(i, "bottles of beer on the wall")
		print(i, "bottles of beer")
		print("If one of those bottles should happen to fall,", i-1, "bottles of beer on the wall...")
print("No more bottles of beer on the wall, no more bottles of beer.")
print("We've taken them down and passed them around; now we're drunk and passed out!")