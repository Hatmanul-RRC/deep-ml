import numpy as np

def calculate_matrix_mean(matrix: list[list[float]], mode: str) -> list[float]:

	if mode == 'column':
		means = [np.average(list(i)) for i in zip(*matrix)]
	elif mode == 'row':
		means = [np.average(row) for row in matrix]

	return means