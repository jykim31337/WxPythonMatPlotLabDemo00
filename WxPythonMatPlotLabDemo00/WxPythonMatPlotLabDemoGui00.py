# -*- coding: utf-8 -*-

###########################################################################
## Python code generated with wxFormBuilder (version 4.1.0-0-g733bf3d)
## http://www.wxformbuilder.org/
##
## PLEASE DO *NOT* EDIT THIS FILE!
###########################################################################

import wx
import wx.xrc
#matPlot3DPanel Start
import matplotlib
matplotlib.use('WXAgg')
from matplotlib.backends.backend_wxagg import FigureCanvasWxAgg as FigureCanvas
from matplotlib.backends.backend_wx import NavigationToolbar2Wx
from matplotlib.figure import Figure
import matplotlib.pyplot as plt
import numpy as np
import MatPlot3DPanelLib
#matPlot3DPanel End
#MatPlotPanel Start
from matplotlib.backends.backend_wxagg import FigureCanvasWxAgg as FigureCanvas
from matplotlib.backends.backend_wx import NavigationToolbar2Wx
from matplotlib.figure import Figure
from matplotlib import pyplot as plt
import cv2
import MatPlotPanelLib
#MatPlotPanel End

###########################################################################
## Class frmMain
###########################################################################

class frmMain ( wx.Frame ):

	def __init__( self, parent ):
		wx.Frame.__init__ ( self, parent, id = wx.ID_ANY, title = wx.EmptyString, pos = wx.DefaultPosition, size = wx.Size( 800,600 ), style = wx.DEFAULT_FRAME_STYLE|wx.TAB_TRAVERSAL )

		self.SetSizeHints( wx.DefaultSize, wx.DefaultSize )

		gbSizer2 = wx.GridBagSizer( 0, 0 )
		gbSizer2.SetFlexibleDirection( wx.BOTH )
		gbSizer2.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )

		self.m_panel60 = wx.Panel( self, wx.ID_ANY, wx.DefaultPosition, wx.Size( -1,0 ), wx.TAB_TRAVERSAL )
		self.m_panel60.SetMinSize( wx.Size( -1,0 ) )
		self.m_panel60.SetMaxSize( wx.Size( -1,0 ) )

		gbSizer2.Add( self.m_panel60, wx.GBPosition( 0, 0 ), wx.GBSpan( 1, 1 ), wx.EXPAND |wx.ALL, 5 )

		self.m_panel601 = wx.Panel( self, wx.ID_ANY, wx.DefaultPosition, wx.Size( -1,0 ), wx.TAB_TRAVERSAL )
		self.m_panel601.SetMinSize( wx.Size( -1,0 ) )
		self.m_panel601.SetMaxSize( wx.Size( -1,0 ) )

		gbSizer2.Add( self.m_panel601, wx.GBPosition( 0, 1 ), wx.GBSpan( 1, 1 ), wx.EXPAND |wx.ALL, 5 )

		self.m_panel602 = wx.Panel( self, wx.ID_ANY, wx.DefaultPosition, wx.Size( -1,0 ), wx.TAB_TRAVERSAL )
		self.m_panel602.SetMinSize( wx.Size( -1,0 ) )
		self.m_panel602.SetMaxSize( wx.Size( -1,0 ) )

		gbSizer2.Add( self.m_panel602, wx.GBPosition( 0, 2 ), wx.GBSpan( 1, 1 ), wx.EXPAND |wx.ALL, 5 )

		self.m_panel603 = wx.Panel( self, wx.ID_ANY, wx.DefaultPosition, wx.Size( -1,0 ), wx.TAB_TRAVERSAL )
		self.m_panel603.SetMinSize( wx.Size( -1,0 ) )
		self.m_panel603.SetMaxSize( wx.Size( -1,0 ) )

		gbSizer2.Add( self.m_panel603, wx.GBPosition( 0, 3 ), wx.GBSpan( 1, 1 ), wx.EXPAND |wx.ALL, 5 )

		self.m_panel604 = wx.Panel( self, wx.ID_ANY, wx.DefaultPosition, wx.Size( -1,0 ), wx.TAB_TRAVERSAL )
		self.m_panel604.SetMinSize( wx.Size( -1,0 ) )
		self.m_panel604.SetMaxSize( wx.Size( -1,0 ) )

		gbSizer2.Add( self.m_panel604, wx.GBPosition( 0, 4 ), wx.GBSpan( 1, 1 ), wx.EXPAND |wx.ALL, 5 )

		self.m_panel605 = wx.Panel( self, wx.ID_ANY, wx.DefaultPosition, wx.Size( -1,0 ), wx.TAB_TRAVERSAL )
		self.m_panel605.SetMinSize( wx.Size( -1,0 ) )
		self.m_panel605.SetMaxSize( wx.Size( -1,0 ) )

		gbSizer2.Add( self.m_panel605, wx.GBPosition( 0, 5 ), wx.GBSpan( 1, 1 ), wx.EXPAND |wx.ALL, 5 )

		self.m_panel606 = wx.Panel( self, wx.ID_ANY, wx.DefaultPosition, wx.Size( -1,0 ), wx.TAB_TRAVERSAL )
		self.m_panel606.SetMinSize( wx.Size( -1,0 ) )
		self.m_panel606.SetMaxSize( wx.Size( -1,0 ) )

		gbSizer2.Add( self.m_panel606, wx.GBPosition( 0, 6 ), wx.GBSpan( 1, 1 ), wx.EXPAND |wx.ALL, 5 )

		self.m_panel607 = wx.Panel( self, wx.ID_ANY, wx.DefaultPosition, wx.Size( -1,0 ), wx.TAB_TRAVERSAL )
		self.m_panel607.SetMinSize( wx.Size( -1,0 ) )
		self.m_panel607.SetMaxSize( wx.Size( -1,0 ) )

		gbSizer2.Add( self.m_panel607, wx.GBPosition( 0, 7 ), wx.GBSpan( 1, 1 ), wx.EXPAND |wx.ALL, 5 )

		self.m_panel608 = wx.Panel( self, wx.ID_ANY, wx.DefaultPosition, wx.Size( -1,0 ), wx.TAB_TRAVERSAL )
		self.m_panel608.SetMinSize( wx.Size( -1,0 ) )
		self.m_panel608.SetMaxSize( wx.Size( -1,0 ) )

		gbSizer2.Add( self.m_panel608, wx.GBPosition( 0, 8 ), wx.GBSpan( 1, 1 ), wx.EXPAND |wx.ALL, 5 )

		self.m_panel609 = wx.Panel( self, wx.ID_ANY, wx.DefaultPosition, wx.Size( -1,0 ), wx.TAB_TRAVERSAL )
		self.m_panel609.SetMinSize( wx.Size( -1,0 ) )
		self.m_panel609.SetMaxSize( wx.Size( -1,0 ) )

		gbSizer2.Add( self.m_panel609, wx.GBPosition( 0, 9 ), wx.GBSpan( 1, 1 ), wx.EXPAND |wx.ALL, 5 )

		self.m_panel610 = wx.Panel( self, wx.ID_ANY, wx.DefaultPosition, wx.Size( -1,0 ), wx.TAB_TRAVERSAL )
		self.m_panel610.SetMinSize( wx.Size( -1,0 ) )
		self.m_panel610.SetMaxSize( wx.Size( -1,0 ) )

		gbSizer2.Add( self.m_panel610, wx.GBPosition( 0, 10 ), wx.GBSpan( 1, 1 ), wx.EXPAND |wx.ALL, 5 )

		self.m_panel611 = wx.Panel( self, wx.ID_ANY, wx.DefaultPosition, wx.Size( -1,0 ), wx.TAB_TRAVERSAL )
		self.m_panel611.SetMinSize( wx.Size( -1,0 ) )
		self.m_panel611.SetMaxSize( wx.Size( -1,0 ) )

		gbSizer2.Add( self.m_panel611, wx.GBPosition( 0, 11 ), wx.GBSpan( 1, 1 ), wx.EXPAND |wx.ALL, 5 )

		self.m_panelMatPlot3d = wx.Panel( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		gSizer1 = wx.GridSizer( 1, 1, 0, 0 )


		self.matPlot3DPanel = MatPlot3DPanelLib.MatPlot3DPanel(self.m_panelMatPlot3d)

		self.matPlot3DPanel.SetMinSize( wx.Size( 100,100 ) )

		gSizer1.Add( self.matPlot3DPanel, 0, wx.ALL|wx.EXPAND, 5 )


		self.m_panelMatPlot3d.SetSizer( gSizer1 )
		self.m_panelMatPlot3d.Layout()
		gSizer1.Fit( self.m_panelMatPlot3d )
		gbSizer2.Add( self.m_panelMatPlot3d, wx.GBPosition( 1, 0 ), wx.GBSpan( 2, 6 ), wx.EXPAND |wx.ALL, 5 )

		self.m_panelMatPlotImg = wx.Panel( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		gSizer2 = wx.GridSizer( 1, 1, 0, 0 )


		self.matPlotImgPanel = MatPlotPanelLib.MatPlotPanel(self.m_panelMatPlotImg)
		self.matPlotImgPanel.SetMinSize( wx.Size( 100,100 ) )

		gSizer2.Add( self.matPlotImgPanel, 0, wx.ALL|wx.EXPAND, 5 )


		self.m_panelMatPlotImg.SetSizer( gSizer2 )
		self.m_panelMatPlotImg.Layout()
		gSizer2.Fit( self.m_panelMatPlotImg )
		gbSizer2.Add( self.m_panelMatPlotImg, wx.GBPosition( 1, 6 ), wx.GBSpan( 1, 4 ), wx.EXPAND |wx.ALL, 5 )

		self.m_panelMatPlot2d = wx.Panel( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		gSizer21 = wx.GridSizer( 1, 1, 0, 0 )


		self.matPlot2DPanel = MatPlotPanelLib.MatPlotPanel(self.m_panelMatPlot2d)
		self.matPlot2DPanel.SetMinSize( wx.Size( 100,100 ) )

		gSizer21.Add( self.matPlot2DPanel, 0, wx.ALL|wx.EXPAND, 5 )


		self.m_panelMatPlot2d.SetSizer( gSizer21 )
		self.m_panelMatPlot2d.Layout()
		gSizer21.Fit( self.m_panelMatPlot2d )
		gbSizer2.Add( self.m_panelMatPlot2d, wx.GBPosition( 2, 6 ), wx.GBSpan( 1, 4 ), wx.EXPAND |wx.ALL, 5 )

		self.m_panelMenu = wx.Panel( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		bSizer1 = wx.BoxSizer( wx.VERTICAL )

		self.m_button1 = wx.Button( self.m_panelMenu, wx.ID_ANY, u"MyButton", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer1.Add( self.m_button1, 0, wx.ALL|wx.EXPAND, 5 )


		self.m_panelMenu.SetSizer( bSizer1 )
		self.m_panelMenu.Layout()
		bSizer1.Fit( self.m_panelMenu )
		gbSizer2.Add( self.m_panelMenu, wx.GBPosition( 1, 10 ), wx.GBSpan( 2, 2 ), wx.EXPAND |wx.ALL, 5 )

		self.m_textCtrl1 = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, wx.TE_MULTILINE )
		self.m_textCtrl1.SetMinSize( wx.Size( -1,140 ) )

		gbSizer2.Add( self.m_textCtrl1, wx.GBPosition( 3, 0 ), wx.GBSpan( 1, 12 ), wx.ALL|wx.EXPAND, 5 )


		gbSizer2.AddGrowableCol( 0 )
		gbSizer2.AddGrowableCol( 1 )
		gbSizer2.AddGrowableCol( 2 )
		gbSizer2.AddGrowableCol( 3 )
		gbSizer2.AddGrowableCol( 4 )
		gbSizer2.AddGrowableCol( 5 )
		gbSizer2.AddGrowableCol( 6 )
		gbSizer2.AddGrowableCol( 7 )
		gbSizer2.AddGrowableCol( 8 )
		gbSizer2.AddGrowableCol( 9 )
		gbSizer2.AddGrowableCol( 10 )
		gbSizer2.AddGrowableCol( 11 )
		gbSizer2.AddGrowableRow( 1 )
		gbSizer2.AddGrowableRow( 2 )

		self.SetSizer( gbSizer2 )
		self.Layout()

		self.Centre( wx.BOTH )

	def __del__( self ):
		pass


