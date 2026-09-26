import numpy as np

def transform_matrix(A: list[list[int|float]], T: list[list[int|float]], S: list[list[int|float]]) -> list[list[int|float]]:
	
	t = np.array(T)
	t_det = np.linalg.det(t)
	
	if t_det == 0:
		return -1

	s = np.array(S)
	s_det = np.linalg.det(s)
	
	if s_det == 0:
		return -1
	
	transform_matrix = np.linalg.inv(t) @ np.array(A) @ s

	return transform_matrix.tolist()
