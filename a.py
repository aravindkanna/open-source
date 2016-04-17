class EOMMethod(object):
	def __init__(self, fl=None, bl = None):
		self._fl = fl
		self._bl = bl

	@property
	def forcelist(self):
		return self._fl

class KanesMethod(EOMMethod):
	def __init__(self, fl=None, bl=None):
		self._fl = fl
		self._bl = bl

class LagrangesMethod(EOMMethod):
	def __init__(self, fl=None):
		self._fl = fl