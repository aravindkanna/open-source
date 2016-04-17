class EOMMethod(object):
	def __init__(self, fl=None, bl = None):
		self._fl = fl if fl else []
		self._bl = bl if bl else []

	@property
	def forcelist(self):
		return self._fl

	@property
	def bodylist(self):
		return self._bl

class KanesMethod(EOMMethod):
	def __init__(self, fl=None, bl=None):
		self._fl = fl if fl else []
		self._bl = bl if bl else []

class LagrangesMethod(EOMMethod):
	def __init__(self, fl=None, bl=None):
		self._fl = fl if fl else []
		self._bl = bl if bl else []