'''Info Header Start
Name : jsonConfig_callbacks
Author : Wieland@AMB-ZEPH15
Saveorigin : Project.toe
Saveversion : 2022.35320
Info Header End'''
from typing import Type

def GetConfigSchema(configModule:"SchemaObjects", configComp:"JsonConfig") -> dict:
	positiveValue = configModule.ConfigValue(default = 4, validator = lambda value : value > 0)
	
	return {
		"Channels" : configModule.NamedList(
			default_member = configModule.CollectionDict({
				"Command" : configModule.ConfigValue(default = "Take", typecheck = str),
				"Args" : configModule.NamedList( 
					default_member = configModule.ConfigValue( typecheck = (str,float, int) )
				)
			})
		),
		}
		
		
#def GetConfigData():
#	return a jsonString. Can be used to fetch API data or similiar.
#	return ""