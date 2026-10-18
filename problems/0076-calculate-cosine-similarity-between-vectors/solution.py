import numpy as np

def cosine_similarity(v1, v2):
	"""
	Calculate the cosine_similarity of two vectors.
	Args:
		vec1 (numpy.ndarray): 1D array representing the first vector.
		vec2 (numpy.ndarray): 1D array representing the second vector.
	Returns:
		The cosine_similarity of the two vectors.
	"""
	dot_prod = np.dot(v1,v2)
	len_v1 = np.dot(v1,v1)**0.5
	len_v2 = np.dot(v2,v2)**0.5

	return dot_prod/(len_v1 * len_v2)