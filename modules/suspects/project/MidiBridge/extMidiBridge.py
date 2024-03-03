'''Info Header Start
Name : extMidiBridge
Author : Wieland@AMB-ZEPH15
Saveorigin : Project.toe
Saveversion : 2022.35320
Info Header End'''
from commandModule import commandDict, _empty

class extMidiBridge:
	"""
	extMidiBridge description
	"""
	def __init__(self, ownerComp):
		# The component to which this extension is attached
		self.ownerComp = ownerComp

	def ApplyMapping(self, message, channel, index):
		if message != "Note On": return
		commandObject = op("MidiMapping").Data.Channels.get(f"{channel}.{index}", None)
	
		if commandObject is None: return
	
		commandFunc = commandDict.get(commandObject.Command.Value, _empty)
	
		commandFunc(**{key : argument.Value for key,argument in commandObject.Args.items()})