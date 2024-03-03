'''Info Header Start
Name : extSwitcher
Author : Wieland@AMB-ZEPH15
Saveorigin : Project.toe
Saveversion : 2022.35320
Info Header End'''


class extSwitcher:
	"""
	extSwitcher description
	"""
	def __init__(self, ownerComp):
		# The component to which this extension is attached
		self.ownerComp = ownerComp

	@property
	def _stateComp(self):
		return self.ownerComp.op("State")
	

	def Select(self, name:str):
		self._Select( iop.Store.Renderer.op("Items").op(name) )

	def _Select(self, renderer:COMP):
		self._stateComp.par.Prvw = renderer

	def Take(self, time = 1):
		if not self._stateComp.par.Prvw.eval(): 
			self.ownerComp.op("top_switcher").SelectTop(
				None, time
			)
			return
		self.ownerComp.op("top_switcher").SelectTop(
			self._stateComp.par.Prvw.eval().op("VideoOut"), time
		)
	
	def Reset(self):
		self._stateComp.par.Prvw.val = ""
		self._stateComp.par.Prgm.val = ""
		self.ownerComp.op("top_switcher").initializeExtensions()

	def _PostTake(self):
		prvw = self._stateComp.par.Prvw.eval()
		prgm = self._stateComp.par.Prgm.eval()
		self._stateComp.par.Prvw.val = prgm
		self._stateComp.par.Prgm.val = prvw