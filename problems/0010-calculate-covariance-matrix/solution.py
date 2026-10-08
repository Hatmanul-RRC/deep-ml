def coveariance(x: list[float], y: list[float], mean_x: float, mean_y: float) -> float:
	m = len(x)
	result = 0
	for k in range(m):
		result += (x[k] - mean_x) * (y[k] - mean_y)

	return result / (m - 1)

def calculate_covariance_matrix(vectors: list[list[float]]) -> list[list[float]]:
	# Your code here
	means = [sum(vector) / len(vector) for vector in vectors]
	n = len(vectors)

	coveariance_mat = []

	for i in range(n):
		row = []
		for j in range(n):
			row.append(coveariance(vectors[i], vectors[j], means[i], means[j]))
		coveariance_mat.append(row)

	return coveariance_mat