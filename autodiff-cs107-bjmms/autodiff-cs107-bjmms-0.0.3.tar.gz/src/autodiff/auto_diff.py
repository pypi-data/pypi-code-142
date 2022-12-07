from .dual_numbers import DualNumber
import numpy as np

class Differentiator():
	"""
	Differentiator class

	Attributes
	----------
	f : callable
	    Function to differentiate
	x : list
	    point at which the derivative is taken
	"""
	def __init__(self, f=None, x=None):
		"""
		Constructor for Differentiator class

		Parameters
		----------
		f : callable
	    	Function to differentiate

		Returns
		-------
		None
		"""
		self.f = f
		self.x = x

	def __call__(self, order=None):
		"""
		Callable of Differentiator class

		Parameters
		----------
		order : dynamic type
	    	Can be either:

	    	1) A tuple (n, v) where n means the n-th
	    	derivative and v with respect to variable 
	    	of index v starting at 1.

	    	2) A list of indices v starting. For example
	    	[3, 4, 2, 1, 2], indicates taking the partial
	    	derivative first with respect to the third
	    	variable then fourth, then second, then first,
	    	and then second.

	    	3) A list of seed vectors. Each seed vector
	    	represents one gradient, the next seed vector
	    	take the gradient on top of the previous one.

		Returns
		-------
		Matrix
		"""
		if order is None:
			return self.jacobian()
		elif type(order) == tuple and len(order) == 2 and type(order[0]) == int:
			der, var = order
			p = [0] * len(self.x)
			p[var - 1] = 1
			seeds = [p] * der
			return self.derivative(seeds)
		elif type(order) == list and type(order[0]) == int:
			seeds = []
			for var in order:
				p = [0] * len(self.x)
				p[var - 1] = 1
				seeds.append(p)
			return self.derivative(seeds)
		elif type(order) == list and type(order[0]) == list and type(order[0][0]) == int:
			seeds = order
			return self.derivative(seeds)


	def derivative(self, seeds=None):
		"""
		Changes the function to differentiate

		Parameters
		----------
		seeds : list of float lists
	    	Matrix that defines derivation sequence

		Returns
		-------
		None
		"""
		if seeds is None:
			return self.jacobian()

		if type(seeds[0]) != list:
			seeds = [seeds]

		n = len(self.x)

		#Base case of dual numbers
		duals = [DualNumber(xi, pi) for xi, pi in zip(self.x, seeds[0])]

		#Recursive definition for higher order derivatives
		for i in range(n):
			for p in seeds[1:]:
				duals[i] = DualNumber(duals[i], p[i])

		duals = [di ** 1 if xi != 0 else di for xi, di in zip(self.x, duals)]
		
		#Extract last derivative
		derivatives = []
		for dual in self.f(*duals):
			while type(dual) == DualNumber:
				dual = dual.b
			derivatives.append(dual)

		return np.array(derivatives)

	def function(self, f):
		"""
		Changes the function to differentiate

		Parameters
		----------
		f : callable
	    	Function to differentiate

		Returns
		-------
		None
		"""
		self.f = f

	def point(self, x):
		"""
		Changes the point to evaluate

		Parameters
		----------
		x : float list
	    	Point to evaluate

		Returns
		-------
		None
		"""
		self.x = x

	def jacobian(self):
		"""
		Computes the Jacobian matrix for the function in the attribute

		Parameters
		----------
		None

		Returns
		-------
		jacobian : list of float lists
			Jacobian matrix of self.f evaluated at x
		"""
		n = len(self.x)
		jac = []
		for i in range(n):
			#Seed unit vector for each variable in the input space
			p = [1.0 if i == j else 0.0 for j in range(n)]
			partial = self.derivative([p])
			jac.append(partial)

		return np.array(jac).T

	def hessian(self):
		"""
		Computes the Hessian matrix for the function in the attribute

		Parameters
		----------
		None

		Returns
		-------
		hessian : list of float lists
			Hessian matrix of self.f evaluated at x
		"""
		n = len(self.x)
		seeds = [[0.0] * n, [0.0] * n]

		hes = []
		for i in range(n):
			seeds[0][i] = 1.0
			hes.append([])
			for j in range(n):
				seeds[1][j] = 1.0
				partial = self.derivative(seeds)
				hes[i].append(partial)

				seeds[1][j] = 0.0
			seeds[0][i] = 0.0

		return np.moveaxis(np.array(hes), [1, 0], [2, 1])