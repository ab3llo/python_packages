# Define a Minimal class with an attribute
class MyClass:
	"""A minimal class example
	
	:param value: The value to sett as the ``attribute`` attribute
	:ivar attribute: contains the contents of ``value`` passed to init  
	"""
	
	# Method to create an instance of MyClass
	def __init__(self, value):
		# Define attribute with contents of the value parameter
		self.attribute = value