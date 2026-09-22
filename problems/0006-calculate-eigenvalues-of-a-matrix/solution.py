import math

def calculate_eigenvalues(matrix: list[list[float|int]]) -> list[float]:
	b = matrix[0][0] + matrix[1][1]
	c = matrix[0][0] * matrix[1][1] - matrix[0][1] * matrix[1][0]
	solver1 = lambda b, c : (b + math.sqrt(b**2 - 4 * c)) / 2
	solver2 = lambda b, c : (b - math.sqrt(b**2 - 4 * c)) / 2

	return [solver1(b, c), solver2(b, c)]