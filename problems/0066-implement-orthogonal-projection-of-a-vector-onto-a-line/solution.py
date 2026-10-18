
def orthogonal_projection(v, L):
	"""
	Compute the orthogonal projection of vector v onto line L.

	:param v: The vector to be projected
	:param L: The line vector defining the direction of projection
	:return: List representing the projection of v onto L
	"""
	import numpy as np
	scaling_factor = np.dot(v,L)/np.dot(L,L)
	return scaling_factor * np.array(L)
