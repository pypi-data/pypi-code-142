import math
from autodiff import functions as ad

class DualNumber():
	"""
	Class for dual number representation

	Parameters
    ----------
    a : float
        Real part
    b : float
        Dual part
	"""
	def __init__(self, a, b = 0):
		"""
		Constructor for DualNumber class

		Parameters
		----------
		a : float
		    Real part
		b : float
		    Dual part

		Returns
		-------
		None
		"""

		if not isinstance(a, (float, int, DualNumber)):
			raise TypeError('Dual Numbers can only be created with real types int, float.')

		elif not isinstance(b, (float, int, DualNumber)):
			raise TypeError('Dual Numbers can only be created with dual types int, float.')

		self.a = a
		self.b = b

	#Implementation of dunder methods

	#Unary
	def __str__(self):
		
		return f"(a={self.a}, b={self.b})"

	def __repr__(self):
		return f"DualNumber(a={self.a}, b={self.b})"

	def __abs__(self):
		return self._abs(self)

	def __neg__(self):
		return self._neg(self)

	#Binary
	def __add__(self, d):
		return self.add(self, d)

	def __radd__(self, d):
		return self.add(d, self)

	def __sub__(self, d):
		return self.sub(self, d)

	def __rsub__(self, d):
		return self.sub(d, self)

	def __mul__(self, d):
		return self.mul(self, d)

	def __rmul__(self, d):
		return self.mul(d, self)

	def __truediv__(self, d):
		return self.div(self, d)

	def __rtruediv__(self, d):
		return self.div(d, self)

	def __pow__(self, d):
		return self.pow(self, d)

	def __rpow__(self, d):
		return self.pow(d, self)

	def __eq__(self, d):
		return self.a == d.a and self.b == d.b

	def __ne__(self, d):
		return self.a != d.a or self.b != d.b

	def __lt__(self, d):
		return self.a < d.a

	def __gt__(self, d):
		return self.a > d.a

	def __le__(self, d):
		return self.a <= d.a

	def __ge__(self, d):
		return self.a >= d.a


	#Implementation of public methods
	def add(self, d1, d2):
		"""
		Adds two numbers d1 and d2. No more than one dual number.
		
		Args:
			d1 (Dual Number or Int/Float): First argument to add.
			d2 (Dual Number or Int/Float): Second argument to add.

		Returns:
			DualNumber: Addition result.
		"""
		return self._add(d1, d2)

	def sub(self, d1, d2):
		"""
		Subtracts two numbers d1 from d2. No more than one dual number.
		
		Args:
			d1 (Dual Number or Int/Float): First argument to subtract from.
			d2 (Dual Number or Int/Float): Second argument to subtract.

		Returns:
			DualNumber: Subtraction result.
		"""
		return self._sub(d1, d2)

	def mul(self, d1, d2):
		"""
		Multiplies two numbers d1 and d2. No more than one dual number.
		
		Args:
			d1 (Dual Number or Int/Float): First argument to multiply.
			d2 (Dual Number or Int/Float): Second argument to multiply.

		Returns:
			DualNumber: Multiplication result.
		"""
		return self._mul(d1, d2)

	def div(self, d1, d2):

		"""
		Divides two numbers d1 over d2. No more than one dual number.
		
		Args:
			d1 (Dual Number or Int/Float): Dividend argument for division.
			d2 (Dual Number or Int/Float): Divisor argument for division.

		Returns:
			DualNumber: Division result.
		"""

		return self._div(d1, d2)

	def log(self, d1, d2):

		"""
		Calculates the logarithmic operation log_{d2} of (d1).
		
		Args:
			d1 (Dual Number or Int/Float): Logarithm operation input.
			d2 (Dual Number or Int/Float): Logarithm base.

		Returns:
			DualNumber: Log result.
		"""
		return self._log(d1, d2)

	def pow(self, d1, d2):

		"""
		Evaluates the mathematical power function pow() as d1^d2.

    	Args:
        	d1 (Dual Number or Int/Float): Argument as coefficient
        	d2 (Dual Number or Int/Float): Argument use as exponent

    	Returns:
        	DualNumber: Power function result. 
    	"""
		return self._pow(d1, d2)

	def sin(self, d1):
		"""
		Evaluates trigonometric function sin() for given input.

    	Args:
        	d1 (Dual Number): Argument to evaluate

    	Returns:
        	DualNumber: Returns sin(d1) result.
    	"""
		return self._sin(d1)

	def cos(self, d1):
		"""
		Evaluates trigonometric function cos() for given input.

    	Args:
        	d1 (Dual Number): Argument to evaluate

    	Returns:
        	DualNumber: Returns cos(d1) result.
    	"""
		return self._cos(d1)

	def tan(self, d1):
		"""
		Evaluates trigonometric function tan() for given input.

    	Args:
        	d1 (Dual Number): Argument to evaluate

    	Returns:
        	DualNumber: Returns tan(d1) result.
    	"""
		return self._tan(d1)
	
	def ln(self, d1):
		"""
		Evaluates trigonometric function ln() for given input.

    	Args:
        	d1 (Dual Number): Argument to evaluate

    	Returns:
        	DualNumber: Returns ln(d1) result.
    	"""
		return self._ln(d1)
	
	def exp(self, d1):
		"""
		Evaluates trigonometric function exp() for given input.

    	Args:
        	d1 (Dual Number): Argument to evaluate

    	Returns:
        	DualNumber: Returns exp(d1) result.
    	"""
		return self._exp(d1)

	def sqrt(self, d1):
		"""
		Evaluates square root function sqrt() for given input.

    	Args:
        	d1 (Dual Number): Argument to evaluate

    	Returns:
        	DualNumber: Returns sqrt(d1) result.
    	"""
		return self._sqrt(d1)

	def sinh(self, d1):

		"""
		Evaluates the hyperbolic function sinh() for given input.

    	Args:
        	d1 (Dual Number): Argument to evaluate

    	Returns:
        	DualNumber: Returns sinh(d1) result.
    	"""
		return self._sinh(d1)

	def cosh(self, d1):

		"""
		Evaluates the hyperbolic function cosh() for given input.

    	Args:
        	d1 (Dual Number): Argument to evaluate

    	Returns:
        	DualNumber: Returns cosh(d1) result.
    	"""
		return self._cosh(d1)
	
	def tanh(self, d1):

		"""
		Evaluates the hyperbolic function tanh() for given input.

    	Args:
        	d1 (Dual Number): Argument to evaluate

    	Returns:
        	DualNumber: Returns tanh(d1) result.
    	"""
		return self._tanh(d1)

	def asin(self, d1):

		"""
		Evaluates the arcsin, asin() for given input.

    	Args:
        	d1 (Dual Number): Argument to evaluate

    	Returns:
        	DualNumber: Returns asin(d1) result.
    	"""
		return self._asin(d1)

	def acos(self, d1):

		"""
		Evaluates the arccos, acos() for given input.

    	Args:
        	d1 (Dual Number): Argument to evaluate

    	Returns:
        	DualNumber: Returns acos(d1) result.
    	"""
		return self._acos(d1)

	def atan(self, d1):

		"""
		Evaluates the arctan, atan() for given input.

    	Args:
        	d1 (Dual Number): Argument to evaluate

    	Returns:
        	DualNumber: Returns atan(d1) result.
    	"""
		return self._atan(d1)

	#Implementation of unary operators private functions
	@classmethod
	def _neg(cls, d):
		return cls._sub(0.0, d)

	@classmethod
	def _conj(cls, d):
		return DualNumber(d.a, -d.b)

	@classmethod
	def _abs(cls, d):
		return DualNumber(d.a ** 2, 0.0)

	@classmethod
	def _exp(cls, d):
		if type(d.a) == DualNumber:
			return DualNumber(ad.exp(d.a), ad.exp(d.a) * d.b)
		else:
			return DualNumber(math.exp(d.a), math.exp(d.a) * d.b)

	@classmethod
	def _sqrt(cls, d):
		return ad.pow(d, 0.5)

	@classmethod
	def _ln(cls, d):
		if type(d.a) == DualNumber:
			return DualNumber(ad.ln(d.a), d.b / d.a)
		else:
			return DualNumber(math.log(d.a), d.b / d.a)

	@classmethod	
	def _cos(cls, d):
		if type(d.a) == DualNumber:
			return DualNumber(ad.cos(d.a), -ad.sin(d.a) * d.b)
		else:
			return DualNumber(math.cos(d.a), -math.sin(d.a) * d.b)

	@classmethod
	def _sin(cls, d):
		if type(d.a) == DualNumber:
			return DualNumber(ad.sin(d.a), ad.cos(d.a) * d.b)
		else:
			return DualNumber(math.sin(d.a), math.cos(d.a) * d.b)
	
	@classmethod
	def _tan(cls, d):
		return ad.div(ad.sin(d), ad.cos(d))

	@classmethod
	def _sinh(cls, d):
		return (ad.exp(d) - ad.exp(-d))/2

	@classmethod
	def _cosh(cls, d):
		return (ad.exp(d) + ad.exp(-d))/2

	@classmethod
	def _tanh(cls, d):
		return ad.sinh(d)/ad.cosh(d)

	@classmethod
	def _asin(cls, d):
		if type(d.a) == DualNumber:
			return DualNumber(ad.asin(d.a), d.b/ad.sqrt(1-d.a**2))
		else:
			return DualNumber(math.asin(d.a), d.b/ad.sqrt(1-d.a**2))

	@classmethod
	def _acos(cls, d):
		if type(d.a) == DualNumber:
			return DualNumber(ad.acos(d.a), -d.b/ad.sqrt(1-d.a**2))
		else:
			return DualNumber(math.acos(d.a), -d.b/ad.sqrt(1-d.a**2))

	@classmethod
	def _atan(cls, d):
		if type(d.a) == DualNumber:
			return DualNumber(ad.atan(d.a), d.b/(1+d.a**2))
		else:
			return DualNumber(math.atan(d.a), d.b/(1+d.a**2))

	#Implementation of binary operators private functions
	@classmethod
	def _add(cls, d1, d2):
		"""
		Private function for addition.
		
		Args:
			d1 (Dual Number or Int/Float): First argument to add.
			d2 (Dual Number or Int/Float): Second argument to add.

		Returns:
			DualNumber: Addition result.
		"""

		if type(d1) == DualNumber and type(d2) == DualNumber:
			return DualNumber(d1.a + d2.a, d1.b + d2.b)
		elif type(d1) == DualNumber:
			return DualNumber(d1.a + d2, d1.b)
		elif type(d2) == DualNumber:
			return DualNumber(d1 + d2.a, d2.b)
	
	@classmethod
	def _sub(cls, d1, d2):

		"""
		Private function for subtraction.
		
		Args:
			d1 (Dual Number or Int/Float): First argument to subtract from.
			d2 (Dual Number or Int/Float): Second argument to subtract.

		Returns:
			DualNumber: Subtraction result.
		"""

		if type(d1) == DualNumber and type(d2) == DualNumber:
			return DualNumber(d1.a - d2.a, d1.b - d2.b)
			
		elif type(d1) == DualNumber:
			return DualNumber(d1.a - d2, d1.b)

		elif type(d2) == DualNumber:
			return DualNumber(d1 - d2.a, -d2.b)
		
	@classmethod
	def _mul(cls, d1, d2):

		"""
		Private function for multiplication.
		
		Args:
			d1 (Dual Number or Int/Float): First argument to multiply.
			d2 (Dual Number or Int/Float): Second argument to multiply.

		Returns:
			DualNumber: Multiplication result.
		"""

		if type(d1) == DualNumber and type(d2) == DualNumber:
			return DualNumber(d1.a * d2.a, d1.a * d2.b + d2.a * d1.b)
		elif type(d1) == DualNumber:
			return DualNumber(d1.a * d2, d1.b * d2)
			
		elif type(d2) == DualNumber:
			return DualNumber(d1 * d2.a, d1 * d2.b)

	@classmethod
	def _div(cls, d1, d2):

		"""
		Private function for division.
		
		Args:
			d1 (Dual Number or Int/Float): Dividend argument for division.
			d2 (Dual Number or Int/Float): Divisor argument for division.

		Returns:
			DualNumber: Division result.
		"""
		
		if type(d1) == DualNumber and type(d2) == DualNumber:
			if d1.a == d2.a and d1.b == d2.b:
				return DualNumber(1, 0)
			return DualNumber(d1.a / d2.a, (d1.b * d2.a - d1.a * d2.b) / d2.a **  2)
		elif type(d1) == DualNumber:
			return DualNumber(d1.a / d2, (d1.b * d2) / d2 **  2)
		elif type(d2) == DualNumber:
			return DualNumber(d1 / d2.a, (- d1 * d2.b) / d2.a **  2)

	@classmethod
	def _log(cls, d1, d2):

		"""
		Private function for logarithmic operation log_{d1} of (d2).
		
		Args:
			d1 (Dual Number or Int/Float): Logarithm base.
			d2 (Dual Number or Int/Float): Logarithm operation input.

		Returns:
			DualNumber: Log result.
		"""
		return ad.div(ad.ln(d1), ad.ln(d2))

	@classmethod
	def _pow(cls, d1, d2):

		"""
		Private function for power function pow() as d1^d2.

    	Args:
        	d1 (Dual Number or Int/Float): Argument as coefficient
        	d2 (Dual Number or Int/Float): Argument use as exponent

    	Returns:
        	DualNumber: Power function result. 
    	"""
		if type(d1) == DualNumber and type(d2) == DualNumber:
			d = d1.a
			while type(d) == DualNumber:
				d = d.a
			if d == 0:
				return DualNumber(0, 0)
			return ad.exp(ad.mul(d2, ad.ln(d1)))
		elif type(d1) == DualNumber:
			if type(d1.a) != DualNumber and d1.a == 0:
				return DualNumber(0, d2 * d1.a * d1.b)
			return DualNumber(d1.a ** d2, d2 * d1.a ** (d2 - 1) * d1.b)
		elif type(d2) == DualNumber:
			if d1 == 0:
				return DualNumber(0, 0)
			return DualNumber(d1 ** d2.a,  d2.b * math.log(d1) * d1 ** d2.a)


