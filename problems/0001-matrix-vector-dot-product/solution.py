def matrix_dot_vector(a: list[list[int|float]], b: list[int|float]) -> list[int|float]:
	# Return a list where each element is the dot product of a row of 'a' with 'b'.
	# If the number of columns in 'a' does not match the length of 'b', return -1.
	if len(b) != len(a[0]):
		return -1
	
	else:
		result = [0] * len(b)
		for i in range(len(b)):
			total = 0
			for j in range(len(b)):
				total += a[i][j] * b[j]
			
			result[i] = total
	
	return result
