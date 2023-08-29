# -*- coding: utf-8 -*-
"""
Created on Sun Aug  7 19:04:47 2022

@author: lizhenzhu
"""


# -*- coding: utf-8 -*
from __future__ import print_function
import os
from __main__ import vtk, qt, ctk, slicer
import time
#
# SlicerLeapModule
#

class liZhenZhuARsurgery(object):
    def __init__(self, parent):
        parent.title = "liZhenZhuARsurgery"
        parent.categories = ["LiZhenZhu_tool"]
        parent.dependencies = []
        parent.contributors = ["LiZhenZhu"]
        parent.helpText = "This is a simple asistant for deep learning or radiomic in 3D Slicer."
        parent.acknowledgementText = "li zhenzhu from the department neurosurgery of NingBoErYuan Hospital"


class liZhenZhuARsurgeryWidget(object):
    def __init__(self, parent = None):
        
        if not parent:
            self.parent = slicer.qMRMLWidget()
            self.parent.setLayout(qt.QVBoxLayout())
            self.parent.setMRMLScene(slicer.mrmlScene)
        else:
            self.parent = parent
        self.layout = self.parent.layout()
        if not parent:
            self.setup()
            self.parent.show()

    def setup(self):
        global index,state,mainWindow,panelDockWidget,volumePropertyNodeWidget,slider,sliderN,vrstep
        #
        parametersCollapsibleButton = ctk.ctkCollapsibleButton()
        parametersCollapsibleButton.text = "Parameters"
        self.layout.addWidget(parametersCollapsibleButton)
        parametersFormLayout = qt.QFormLayout(parametersCollapsibleButton)


        
        self.start = qt.QPushButton("Restart Slicer")
        self.start.setMinimumWidth(4)
        self.start.toolTip = "start"
        self.start.checkable = True
        parametersFormLayout.addRow(self.start)

        self.sPy = qt.QPushButton("PythonCli")
        self.sPy.setMinimumWidth(4)
        parametersFormLayout.addRow(self.sPy)
	
        
        self.start.connect('clicked(bool)', self.starting)
        
        self.layout.addStretch(1)
        
        slicer.util.messageBox("Don't use the slicerARsurgery module in surgery!",standardButtons=qt.QMessageBox.Ok|qt.QMessageBox.Cancel)

        
        controllerWidget = slicer.app.layoutManager().threeDWidget(0).threeDController()
        buttonLayout = slicer.util.findChild(controllerWidget, 'qMRMLThreeDViewControllerWidget').layout()
        mainWindow = slicer.util.mainWindow()
        panelDockWidget = slicer.util.mainWindow().findChildren('QDockWidget','PanelDockWidget')[0]
        
        volumePropertyNodeWidget=None


        # Adjust the transfer function
        

        
        button = qt.QToolButton()
        button.text="LZZARsurgery"
        buttonLayout.addWidget(button)
        


  
        button1 = qt.QToolButton()
        button1.text="ExitARsurgery"
        buttonLayout.addWidget(button1)
        
    


       

        ###################################################################
        button.clicked.connect(ar)
        
        button1.clicked.connect(arexist)
        
        #slider.valueChanged.connect(sliderRun)
        ########################################################
        slicer.util.messageBox("all AR-function Button in 3D viewer Tools! You can contact me with lizhenzhu1@sina.com if any question,have a good day!"
                               ,standardButtons=qt.QMessageBox.Ok|qt.QMessageBox.Cancel)



    def slicerPy(self):
        slicer.util.pythonShell().show()
    
    def starting(self):
        
        q=slicer.util.messageBox("restart slicer?",standardButtons=qt.QMessageBox.Ok|qt.QMessageBox.Cancel)
        if q == qt.QMessageBox.Ok:
            slicer.util.restart()
