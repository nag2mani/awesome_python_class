"""
A module with 2 clases to show inheritance
"""

class Employee(object):
	"""
	A class representing an employee with a salary.

	This class has attributes for name, start date and
	salary. However, they are only accessible via the 
	getters and setters of the same name.
	"""
	# HIDDEN INSTANCE ATTRIBUTES:
	# Attribute _name: Employee's name
	# Invariant: _name is a non-empty string
	#
	# Attribute: _start: Year in which employee was hired
	# Invariant: _start is an int > 1970; -1 if undefined
	#
	# Attribute _salary: Employee's salary
	# Invariant: _salary is an int or float >= 0
	#
	# Getters/Setters
	def getName(self):
		"""
		Returns the employee's name.
		The name is a non-empty string.
		"""
		return self._name

	def setName(self,value):
		"""
		Sets the employee's name to the given value

		Parameter value: the new name
		Precondition: value is a nonempty string
		"""
		assert type(value) == str and value != '', 'name should be a non-empty string'
		self._name = value

	def getStart(self):
		"""
		Returns the year in which employee was hired.

		The year is an int>1970 or -1 (if undefined)
		"""
		return self._start

	def setStart(self,value):
		"""
		Sets the year hired to the given value.

		Parameter value: the new year
		Precondition: value is an int > 1970, or -1 if undefined.
		"""
		assert type(value) == int, repr(value)+' is not an integer'
		assert value > 1970 or value ==-1, repr(value)+' is not in the valid range'
		self._start = value

	def getSalary(self):
		"""
		Returns the annual salary
		The salary is a number >= 0
		"""
		return self._salary

	def setSalary(self,value):
		"""
		Sets the annual salary to the given value.

		Parameter value: the new salary
		Precondition: value is a number (int or float) >=0.
		"""
		assert type(value) in (int, float), repr(value)+' must be a number'
		assert value >= 0, repr(value)+' is negative'
		self._salary = value

	def getCompensation(self):
		"""
		Returns the annual compensation (overridden)

		The same as salary for base employees.
		"""
		return self._salary

	def __init__(self, n, d=-1, s=50000.0):
		"""
		Initializes an employee with name n, year hired d, salary 50000.0

		Parameter n: employee's name
		Precondition: n is a nonempty string

		Parameter d: employee's start date (optional)
		Precondition: d is an int > 1970 or -1 if undefined (default)

		Parameter s: employee's salry (optional)
		Precondition: s is an int or float >= 0 (50000.0 default)
		"""
		self.setName(n)
		self.setStart(d)
		self.setSalary(s)
		# self._name=n
		# self._start=d
		# self._salary=s
		# #here you have to put assert if you will not call setname etc.

	# OPERATIONS
	def __str__(self):
		"""
		Returns the string representation of this Employee
		"""
		return self._name + ","+str(self._start) + ","+str(self._salary)

	def __repr__(self):
		"""
		Returns the unambiguous representation of this employee
		"""
		return str(self.__class__)+'<'+str(self)+'>'


# e1=Employee("Nagmani",2008,65000)
# print(e1)
# print(str(e1))
# print(repr(e1))
# print(e1._salary)
# print(e1.getName())
# e1.setName("Kaju")
# print(e1.getName())
# e1=Employee("Nagmani",65000)
# print(e1)
# e1=Employee("Nagmani",1911,65000)
# print(e1)


class Executive(Employee):
	"""
	A class representing an Employee with a bonus.
	This class has an additional attribute for an annual bonus.
	This attribute is only acessible via setters and getters.
	"""
	# HIDDEN INSTANCE ATTRIBUTES:
	# Attribute _bonus: The annual bonus
	# Invariant: _bonus is an int or float >= 0

	# GETTERS/SETTERS
	def getBonus(self):
		"""
		Returns the annual bonus

		The bonus is a number >=0
		"""
		return self._bonus

	def setBonus(self,value):
		"""
		Sets the annual bonus salary to the given value

		Parameter value: the new bonus
		Precondition: value is a number (int or float) >= 0
		"""
		assert type(value) in (int,float), repr(value)+' must be a number'
		assert value >=0, repr(value)+' cannot be negative'
		self._bonus = value

	def getCompensation(self):
		"""
		Returns the annual compenstion (to be overridden)

		For executives, this is the salary + annual _bonus
		"""
		return self._salary + self._bonus


	def __init__(self,n,d,b=0.0):
		"""
		Initializes an Executive w/ name n, year hired d and bonus b

		Default salary is 50k

		Parameter n: executive's name
		Precondition: n is a nonempty string

		Parameter d: Executive's start date (optional)
		Precondition: d is an int > 1970 or -1 (if undefined)

		Parameter b: executive's bonus (optional)
		Precondition: b is an int or float >= 0
		(0.0 default)
		"""
		# Asserts precondition for n and d
		super().__init__(n,d,50000)
		self.setBonus(b)


	# OPERATIONS
	def __str__(self):
		"""
		returns a string representation of this executive
		"""

		# Add on to the string representation of the base class
		return super().__str__() + ', bonus ' + str(self._bonus)
		#return self._name + ', year ' + str(self._start) + ' , salary ' + str(self._salary) + ', bonus ' + str(self._bonus)



f=Executive("Nagmani",9090,78000)
print(f)
print(f._bonus)
print(f.getName())
f.setName("nagu")
print(f.getName())
print(repr(f))



