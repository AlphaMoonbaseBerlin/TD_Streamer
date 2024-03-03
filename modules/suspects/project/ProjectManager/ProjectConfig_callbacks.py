'''Info Header Start
Name : ProjectConfig_callbacks
Author : Wieland@AMB-ZEPH15
Saveorigin : Project.toe
Saveversion : 2022.35320
Info Header End'''
from typing import Type

def GetConfigSchema(configModule:"SchemaObjects", configComp:"JsonConfig") -> dict:
	positiveValue = configModule.ConfigValue(default = 4, validator = lambda value : value > 0)
	
	return {
		"Resolution" : configModule.CollectionDict({
			"w" : configModule.ConfigValue( default = 1920, validator = lambda value : value > 0),
			"h" : configModule.ConfigValue( default = 1080, validator = lambda value : value > 0),
		}),
		"ViewportWidth" : configModule.ConfigValue(default = 16, validator = lambda value : value > 1)
		}
		
		
#def GetConfigData():
#	return a jsonString. Can be used to fetch API data or similiar.
#	return ""