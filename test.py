
import wx

class Myframe(wx.Frame):
	def __init__(self,parent,title):
		wx.Frame.__init__(self,parent,title=title,size=(400,200))

		self.control=wx.TextCtrl(self,style=wx.TE_MULTILINE)

		self.CreateStatusBar()
		
		filemenu=wx.Menu()

		menuabout=filemenu.Append(wx.ID_ABOUT, "&About"," Information about this program") 
		filemenu.AppendSeparator() 
		menuexit=filemenu.Append(wx.ID_EXIT,"E&xit"," Terminate the program")  

		'''
		helpmenu=wx.Menu()
		helpmenu.Append(wx.ID_HELP, "&Help"," Help about this program") 
		helpmenu.AppendSeparator() 
		helpmenu.Append(wx.ID_HELP_CONTEXT,"help context"," help the program") 
		'''

		menuBar=wx.MenuBar()
		menuBar.Append(filemenu,"&File") 
		#menuBar.Append(helpmenu,"&Help")
		self.SetMenuBar(menuBar)



		self.Bind(wx.EVT_MENU, self.OnAbout, menuabout)
		self.Bind(wx.EVT_MENU, self.OnExit, menuexit)


		self.Show(True)

	def OnAbout(self,e):
		dlg=wx.MessageDialog(self, "A small text editor", "About Sample Editor")
		dlg.ShowModal() # Show it
		dlg.Destroy() # finally destroy it when finished.


	def OnExit(self,e):
		self.Close(True)



app=wx.App(False)

mf=Myframe(None,'NICE')

app.MainLoop()


