'''Info Header Start
Name : commandModule
Author : Wieland@AMB-ZEPH15
Saveorigin : Project.toe
Saveversion : 2022.35320
Info Header End'''
def _empty(**kwargs):
	return

def _select( index = 0):
	rendererName = op("findRenderer")[ int(index) , "name"]
	iop.Store.Switcher.Select( rendererName )

def _take( time = 1 ):
	iop.Store.Switcher.Take( float(time) 
						 )
commandDict = {
	"Select" : _select,
	"Take" : _take
}