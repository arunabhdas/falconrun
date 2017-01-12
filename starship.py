class Starship:

	def __init__(self, **kwargs):
		self.energy = kwargs.get('energy', 1)
		self.wavelength = kwargs.get('wavelength', 'blue')
		self.payload = kwargs.get('payload', 'lasers')
		self.engine = kwargs.get('engine', 'warpdrive')

	def engage(self):
		return self.engine.upper()

