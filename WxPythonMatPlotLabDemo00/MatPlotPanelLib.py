import matplotlib
from matplotlib import axes 

from matplotlib.backends.backend_wxagg import FigureCanvasWxAgg as FigureCanvas
from matplotlib.backends.backend_wx import NavigationToolbar2Wx
from matplotlib.figure import Figure
from matplotlib import pyplot as plt

import wx
import cv2

import matplotlib.animation as animation

from CmUtil import CmUtil

import time

class MatPlotPanel(wx.Panel):

	def __init__(self, parent, IsToolbar=True, IsXaxis=True, IsYaxis=True):
		wx.Panel.__init__(self, parent)

		self.initShow()

		self.sizer = wx.BoxSizer(wx.VERTICAL)
		self.sizer.Add(self.canvas, 1, wx.LEFT | wx.TOP | wx.GROW)

		if IsToolbar:
			toolbar = NavigationToolbar2Wx(self.canvas, wx.TB_BOTTOM)
			self.sizer.Add(toolbar, 0, wx.LEFT | wx.TOP)
			self.toolbar = toolbar

		if IsXaxis == False:
			self.axes.xaxis.set_visible(False)
		if IsYaxis == False:
			self.axes.yaxis.set_visible(False)

		self.SetSizer(self.sizer)
		self.Fit()
		
		#plt.ion()
		
	def initShow(self):
		self.figure = Figure(figsize=(1, 1))
		self.axes = self.figure.add_subplot(111)
		self.canvas = FigureCanvas(self, -1, self.figure)

	def imshow(self, imgPath):
		img = plt.imread(imgPath)
		self.axes.imshow(img)

	def imshowCv2(self, cv2Img):
		self.initShow()
		self.axes.imshow(cv2Img)

	def imshowInit(self):
		self.figure = Figure(figsize=(1, 1))
		self.axes = self.figure.add_subplot(111)
		self.canvas = FigureCanvas(self, -1, self.figure)

	def imshowExt(self, imgPath):
		#print('imgPath: ', imgPath)
		
		self.img = plt.imread(imgPath)
		
		if 'imgData' not in self.__dict__.keys():
			self.imgData = self.axes.imshow(self.img)
		else:
			self.imgData.set_data(self.img)
		
		#self.canvas.draw()
		self.canvas.draw_idle()
		self.canvas.flush_events()
		#plt.pause(0.01)
		
		#self.canvas.bitmap = cv2Img

		#if self.sizer.ItemCount != 0:
		#	self.sizer.Clear(True)
		#	self.sizer = wx.BoxSizer(wx.VERTICAL)
		#	self.sizer.Add(self.canvas, 1, wx.LEFT | wx.TOP | wx.GROW)
		#	toolbar = NavigationToolbar2Wx(self.canvas, wx.TB_BOTTOM)
		#	self.sizer.Add(toolbar, 0, wx.LEFT | wx.TOP)
		#	self.toolbar = toolbar
		#	self.SetSizer(self.sizer)
		#	self.Layout()

	def imshowCv2_BGR2RGB_ORG(self, cv2Img):
		cv2ImgBgr2rgb = cv2.cvtColor(cv2Img, cv2.COLOR_BGR2RGB)
		self.axes.imshow(cv2ImgBgr2rgb)

	def imshowCv2_BGR2RGB(self, cv2Img):
		self.figure = Figure(figsize=(1, 1))
		self.axes = self.figure.add_subplot(111)
		self.canvas = FigureCanvas(self, -1, self.figure)

		cv2ImgBgr2rgb = cv2.cvtColor(cv2Img, cv2.COLOR_BGR2RGB)
		self.axes.imshow(cv2ImgBgr2rgb)

		if self.sizer.ItemCount != 0:
			self.sizer.Clear(True)
			self.sizer = wx.BoxSizer(wx.VERTICAL)
			self.sizer.Add(self.canvas, 1, wx.LEFT | wx.TOP | wx.GROW)
			toolbar = NavigationToolbar2Wx(self.canvas, wx.TB_BOTTOM)
			self.sizer.Add(toolbar, 0, wx.LEFT | wx.TOP)
			self.toolbar = toolbar
			self.SetSizer(self.sizer)
			self.Layout()

	def setLinePoint( self, val ):
		if 'linePointPlot' in self.__dict__.keys():
			self.linePointPlot.set_data(self.probeTipRealTimeX, self.probeTipRealTimeY, self.probeTipRealTimeZ)
			print("move self.plotProbeTipRealTime")
		else:
			self.plotProbeTipRealTime = self.axes.plot(self.probeTipRealTimeX,self.probeTipRealTimeY,self.probeTipRealTimeZ, \
				'oy', markersize=5)[0]
			print("set self.plotProbeTipRealTime")

	def TestStart( self ):
		try:
			CmUtil.Log("MatPlotPanel.TestStart")
			
			self.ViewXSize = 20
			self.line = None
			self.ArrayX = [*range(0,self.ViewXSize)]
			#self.ArrayX = []
			print(self.ArrayX)
			self.ArrayY = [0 for i in range(self.ViewXSize)]
			#self.ArrayY = []
			print(self.ArrayY)
			
			self.plot = self.axes.plot(self.ArrayX, self.ArrayY)[0]
			#plt.ylim(0, 10)
			plt.pause(1)

			self.DoPlot()
			
		except Exception as exptn:
			print("MatPlotPanelLib.TestStart exception")
			print(type(exptn))    # the exception type
			print(exptn.args)     # arguments stored in .args
			print(exptn)          # __str__ allows args to be printed directly,
		else:
			print("MatPlotPanelLib.TestStart ok")
	
	def DoPlot( self ):
		
		while CmDef.IsTest:
			
			if CmDef.timeLine < CmDef.maxTimeLine:
				CmDef.timeLine += 1
			else:
				#CmDef.timeLine = 0
				
				CmDef.timeLine = self.ViewXSize
				self.ArrayX = [*range(0,self.ViewXSize)]
				
			print('CmDef.SingleX[0]: ', CmDef.SingleX[0]);
			self.ArrayY.append(CmDef.SingleX[0])
			self.ArrayX.append(self.ArrayX[-1]+1)
			#self.ArrayX.append(CmDef.timeLine)
				
			self.plot.remove()
				
			self.plot = self.axes.plot(self.ArrayX, self.ArrayY, color='g')[0]
			#plt.xlim(self.ArrayX[0], self.ArrayX[-1])
			self.axes.set_xlim(self.ArrayX[0], self.ArrayX[-1])
				
			if(len(self.ArrayX) > self.ViewXSize):
				self.ArrayX.pop(0)
				self.ArrayY.pop(0)
				#self.ArrayX.clear()
				#self.ArrayY.clear()
			self.canvas.draw()
			self.canvas.flush_events()
			plt.pause(0.01)
	
	def InitPlot(self):
		try:
			CmUtil.Log("MatPlotPanel.InitPlot")
			
			self.ViewXSize = 20
			self.line = None
			self.ArrayX = [*range(0,self.ViewXSize)]
			print(self.ArrayX)
			self.ArrayY = [0 for i in range(self.ViewXSize)]
			print(self.ArrayY)
			
			self.plot = self.axes.plot(self.ArrayX, self.ArrayY)[0]
			plt.pause(1)

		except Exception as exptn:
			print("MatPlotPanelLib.InitPlot exception")
			print(type(exptn))
			print(exptn.args)
			print(exptn)
		else:
			print("MatPlotPanelLib.InitPlot ok")
	def DoSinglePlot(self):
		if CmDef.timeLine < CmDef.maxTimeLine:
			CmDef.timeLine += 1
		else:
			CmDef.timeLine = self.ViewXSize
			self.ArrayX = [*range(0,self.ViewXSize)]
				
		#print('CmDef.SingleX[0]: ', CmDef.SingleX[0]);
		self.ArrayY.append(CmDef.SingleX[0])
		self.ArrayX.append(self.ArrayX[-1]+1)
				
		self.plot.remove()
				
		self.plot = self.axes.plot(self.ArrayX, self.ArrayY, color='g')[0]
		self.axes.set_xlim(self.ArrayX[0], self.ArrayX[-1])
				
		if(len(self.ArrayX) > self.ViewXSize):
			self.ArrayX.pop(0)
			self.ArrayY.pop(0)
		self.canvas.draw_idle()
		self.canvas.flush_events()
		plt.pause(0.001)
		
		
		