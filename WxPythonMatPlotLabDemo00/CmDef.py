import numpy as np
import wx

class CmDef:
	instFrmWrap = None
	
	IsTest = True 
	
	multiCnt = 50

	timeLine = 0
	maxTimeLine = 100

	MultiX = np.array(np.zeros(multiCnt))
	MultiY = np.array(np.zeros(multiCnt))
	MultiZ = np.array(np.zeros(multiCnt))

	SingleX = np.array(np.zeros(1))
	SingleY = np.array(np.zeros(1))
	SingleZ = np.array(np.zeros(1))

	RandomX = []
	RandomY = []
	RandomZ = []
	
	imgList = ['C:\\Temp\\img\\0.png', 'C:\\Temp\\img\\1.png', 'C:\\Temp\\img\\2.png']
	imgIdx = 0

	IsImgTest = False
	
	@classmethod
	def CheckVariable(cls, strVariableName):
		if strVariableName in cls.__dict__.keys():
			print('True')
		else:
			print('False')
