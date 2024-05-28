if __name__ == "__main__":
	import sys
	from os import path
	appPath = path.dirname(path.dirname(path.abspath(__file__)))

import wx 
import WxPythonMatPlotLabDemoGuiwrap00

class Frame(WxPythonMatPlotLabDemoGuiwrap00.frmWrap): 
	def __init__(self,parent): 
		WxPythonMatPlotLabDemoGuiwrap00.frmWrap.__init__(self,parent)  

if __name__ == "__main__":
	print("main Start")
	try:
		app = wx.App(False) 
		frame = Frame(None) 
		frame.Show(True) 
		app.MainLoop()
	except Exception as exptn:
		print("main exception")
		print(type(exptn))		# the exception type
		print(exptn.args)		# arguments stored in .args
		print(exptn)			# __str__ allows args to be printed directly,
	else:
		print("main End")