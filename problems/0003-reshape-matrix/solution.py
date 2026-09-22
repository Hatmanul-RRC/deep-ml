import numpy as np

def reshape_matrix(a: list[list[int|float]], new_shape: tuple[int, int]) -> list[list[int|float]]:
	#Write your code here and return a python list after reshaping by using numpy's tolist() method
	row_num = len(a)
	col_num = len(a[0])

	if row_num * col_num != new_shape[0] * new_shape[1]:	
		return []

	reshaped_matrix = np.reshape(np.array(a), new_shape).tolist()

	return reshaped_matrix