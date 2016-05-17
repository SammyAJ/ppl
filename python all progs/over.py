class EEEEE(Exception):
	def __init__(self, v) :
		self.value = v
	def __str__(self) :
        	return repr(self.value)

c = EEEEE(3)
print c
