import numpy as np
import wx

from CmDef import CmDef
np.random.seed()

class CmUtil:
	CtlLogCtl = None
	IsInitLog = False
    
	@classmethod
	def SetLogCtl( cls, ctlLogCtl ):
		cls.CtlLogCtl = ctlLogCtl
		cls.IsInitLog = True
		
	@classmethod
	def Log( cls, msg ):
		if cls.IsInitLog == True:
			cls.CtlLogCtl.AppendText(msg + "\n")
		else:
			print("CtlLog is not Init!!!")
	
	
	@classmethod
	def RandRange( cls, n, vmin, vmax):
		return (vmax - vmin)*np.random.rand(n) + vmin
	
	@classmethod
	def InitTest( cls ):
		CmDef.RandomX = CmUtil.RandRange(CmDef.multiCnt, -200, 200)
		CmDef.RandomY = CmUtil.RandRange(CmDef.multiCnt, -200, 200)
		CmDef.RandomZ = CmUtil.RandRange(CmDef.multiCnt, -200, 200)
		
		for i in range(0, CmDef.multiCnt, 1):
			CmDef.MultiX[i] = CmDef.RandomX[i]
			CmDef.MultiY[i] = CmDef.RandomY[i]
			CmDef.MultiZ[i] = CmDef.RandomZ[i]
		
		CmDef.RandomX = CmUtil.RandRange(1, -20, 20)
		CmDef.RandomY = CmUtil.RandRange(1, -20, 20)
		CmDef.RandomZ = CmUtil.RandRange(1, -20, 20)
		
		CmDef.SingleX[0] = CmDef.RandomX[0]
		CmDef.SingleY[0] = CmDef.RandomY[0]
		CmDef.SingleZ[0] = CmDef.RandomZ[0]
		
	@classmethod
	def MakeRandForTestMulti( cls ):
		CmDef.RandomX = CmUtil.RandRange(CmDef.multiCnt, -10, 10)
		CmDef.RandomY = CmUtil.RandRange(CmDef.multiCnt, -10, 10)
		CmDef.RandomZ = CmUtil.RandRange(CmDef.multiCnt, -10, 10)
			
		for i in range(0, CmDef.multiCnt, 1):
			CmDef.MultiX[i] = CmDef.MultiX[i] + CmDef.RandomX[i]
			CmDef.MultiY[i] = CmDef.MultiY[i] + CmDef.RandomY[i]
			CmDef.MultiZ[i] = CmDef.MultiZ[i] + CmDef.RandomZ[i]
			
	@classmethod
	def MakeRandForTestSingle( cls ):
		CmDef.RandomX = CmUtil.RandRange(1, -3, 3)
		CmDef.RandomY = CmUtil.RandRange(1, -3, 3)
		CmDef.RandomZ = CmUtil.RandRange(1, -3, 3)
			
		for i in range(0, 1, 1):
			CmDef.SingleX[i] = CmDef.SingleX[i] + CmDef.RandomX[i]
			CmDef.SingleY[i] = CmDef.SingleY[i] + CmDef.RandomY[i]
			CmDef.SingleZ[i] = CmDef.SingleZ[i] + CmDef.RandomZ[i]