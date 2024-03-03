'''Info Header Start
Name : extProjectManager
Author : Wieland@AMB-ZEPH15
Saveorigin : Project.toe
Saveversion : 2022.35320
Info Header End'''
from pathlib import Path
class extProjectManager:
	"""
	extProjectManager description
	"""
	def __init__(self, ownerComp):
		# The component to which this extension is attached
		self.ownerComp = ownerComp


	def _saveItems(self, component, projectPath, compType = baseCOMP):
		SourcePath = Path( projectPath, component.name )
		for SourceComp in component.Items.findChildren( type = compType, depth = 1):
			SourceComp.save( Path(SourcePath, SourceComp.name).with_suffix(".tox") , createFolders = True )


	def SaveProject(self, folderPath = None):
		projectFolderPath = Path( folderPath or self.ownerComp.par.Project.eval() )
		projectFolderPath.mkdir( parents=True, exist_ok=True )
		
		self._saveItems( iop.Store.Sources, projectFolderPath )
		self._saveItems( iop.Store.Scenes, projectFolderPath, compType=geometryCOMP )
		self._saveItems( iop.Store.Outputs, projectFolderPath )

		#SourcePath = Path( projectFolderPath, "Sources" )
		#for SourceComp in iop.Store.Sources.op("Items").findChildren( type = baseCOMP, depth = 1):
		#	SourceComp.save( Path(SourcePath, SourceComp.name).with_suffix(".tox") , createFolders = True )

		#ScenePath = Path( projectFolderPath, "Scenes" )
		#for SceneComp in iop.Store.Scenes.op("Items").findChildren( type = geometryCOMP, depth = 1):
		#	SceneComp.save( Path(ScenePath, SceneComp.name).with_suffix(".tox") , createFolders = True )


		

		self.ownerComp.op("ProjectConfig").Save()

	def ReloadProject(self):
		iop.Store.Sources.op("consitentReplicator").Replicate()
		iop.Store.Scenes.op("consitentReplicator").Replicate()
		iop.Store.Outputs.op("consitentReplicator").Replicate()


	def LoadProject(self, filepath):
		self.ownerComp.par.Project.val = filepath
		self.ownerComp.op("ProjectConfig").LoadConfig()
		iop.Store.Sources.op("consitentReplicator").Replicate(preClear = True)
		iop.Store.Scenes.op("consitentReplicator").Replicate( preClear = True)
		iop.Store.Outputs.op("consitentReplicator").Replicate( preClear = True)
		iop.Store.Switcher.Reset()