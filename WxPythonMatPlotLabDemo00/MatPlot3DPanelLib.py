from concurrent.futures import thread
import matplotlib
matplotlib.use('WXAgg')
from matplotlib.backends.backend_wxagg import FigureCanvasWxAgg as FigureCanvas
from matplotlib.backends.backend_wx import NavigationToolbar2Wx

import wx

from matplotlib.figure import Figure
import matplotlib.pyplot as plt

from CmUtil import CmUtil

import math

import time
import threading

class MatPlot3DPanel(wx.Panel):
	
	def __init__(self, parent):
		
		CmUtil.Log("MatPlot3DPanel.__init__")	#not work
		
		wx.Panel.__init__(self, parent)
		
		CmUtil.Log("MatPlot3DPanel.__init__")	#not work
		
		self.figure = Figure(figsize=(1, 1))
		
		self.axes = self.figure.add_subplot(111, projection='3d')
		self.canvas = FigureCanvas(self, -1, self.figure)
		
		self.sizer = wx.BoxSizer(wx.VERTICAL)
		self.sizer.Add(self.canvas, 1, wx.LEFT | wx.TOP | wx.GROW)
		
		toolbar = NavigationToolbar2Wx(self.canvas, wx.TB_BOTTOM)
		self.sizer.Add(toolbar, 0, wx.LEFT | wx.TOP)
		self.toolbar = toolbar

		self.SetSizer(self.sizer)

		self.axes.set_xlabel('X Label')
		self.axes.set_ylabel('Y Label')
		self.axes.set_zlabel('Z Label')
		
		self.axes.invert_zaxis()
		
		plt.ion()

	def TestStart( self ):
		
		CmUtil.Log("MatPlot3DPanel.TestStart")
		
		self.plotMulti = self.axes.plot(CmDef.MultiX,CmDef.MultiY,CmDef.MultiZ, 'ob', markersize=3)[0]
		self.plotSingle = self.axes.plot(CmDef.SingleX,CmDef.SingleY,CmDef.SingleZ, 'or',markersize=3)[0]
		
		self.DoPlot()
		#doPlot = threading.Thread(target=self.DoPlot)
		#doPlot.start();
		
	
	def DoPlot( self ):
		while CmDef.IsTest:
			CmUtil.MakeRandForTest()
			#self.plotMulti.set_data_3d(CmDef.MultiX, CmDef.MultiY, CmDef.MultiZ)
			self.plotSingle.set_data_3d(CmDef.SingleX, CmDef.SingleY, CmDef.SingleZ)
			self.canvas.draw_idle()
			self.canvas.flush_events()
			#plt.pause(0.01)
			
	def InitPlot( self ):
		self.plotMulti = self.axes.plot(CmDef.MultiX,CmDef.MultiY,CmDef.MultiZ, 'ob', markersize=3)[0]
		
		#self.canvas.draw()
		#self.background = self.canvas.copy_from_bbox(self.axes.bbox)
		
		self.plotSingle = self.axes.plot(CmDef.SingleX,CmDef.SingleY,CmDef.SingleZ, 'or',markersize=3)[0]
		#print('self.background', self.background)
	def DoSinglePlot( self ):
		#CmUtil.MakeRandForTestMulti()
		#self.plotMulti.set_data_3d(CmDef.MultiX, CmDef.MultiY, CmDef.MultiZ)
		
		self.plotSingle.set_data_3d(CmDef.SingleX, CmDef.SingleY, CmDef.SingleZ)
		self.canvas.draw_idle()
		self.canvas.flush_events()
		plt.pause(0.001)
		
	def DoSinglePlotExt( self ):
		self.canvas.restore_region(self.background)
		self.plotSingle.set_data_3d(CmDef.SingleX, CmDef.SingleY, CmDef.SingleZ)
		self.axes.draw_artist(self.plotSingle)
		self.canvas.blit(self.axes.bbox)
		self.canvas.flush_events()
		plt.pause(0.001)