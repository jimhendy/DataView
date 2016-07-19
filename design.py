# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'DataView.ui'
#
# Created by: PyQt4 UI code generator 4.11.4
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui
from PyQt4.QtCore import *
from PyQt4.QtGui import *
import pandas as pd
import sys, math
from matplotlib.backends.backend_qt4agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.figure import Figure
from matplotlib.backends.backend_qt4agg import NavigationToolbar2QT as NavigationToolbar
import matplotlib.pyplot as plt

import MyTableModel
import SelectDialog
plt.style.use('ggplot')

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)
    
class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName(_fromUtf8("Data View"))
        #MainWindow.resize(539, 600)
        
        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))

        self.verticalLayout = QtGui.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.splitter = QtGui.QSplitter(self.centralwidget)
        self.splitter.setOrientation(QtCore.Qt.Horizontal)
        self.splitter.setObjectName(_fromUtf8("splitter"))        

        # File navigation
        self.fileSystemModel = QtGui.QDirModel(self.splitter)
        self.fileSystemModel.setObjectName(_fromUtf8("fileSystemModel"))
        currentDir = str(QtCore.QDir.currentPath())
        index = self.fileSystemModel.index(currentDir)
        self.treeView = QtGui.QTreeView(self.splitter)
        self.treeView.setObjectName(_fromUtf8("treeView"))
        self.treeView.setModel(self.fileSystemModel)
        if len(sys.argv)>1:
            self.currentFile = currentDir + '/' + sys.argv[1]
        else:
            self.currentFile = None
        self.recursive_expand( index, self.treeView )
        tVheader = self.treeView.header()
        for i in range(1,4): tVheader.hideSection(i)
        self.treeView.doubleClicked.connect(self.on_treeView_doubleClicked)

        # Plots tab
        self.tabWidget = QtGui.QTabWidget(self.splitter)
        self.tabWidget.setObjectName(_fromUtf8("tabWidget"))
        self.tab = QtGui.QWidget()
        self.tab.setObjectName(_fromUtf8("tab"))
        self.verticalLayout_2 = QtGui.QVBoxLayout(self.tab)
        self.verticalLayout_2.setObjectName(_fromUtf8("verticalLayout_2"))
        self.figure = plt.figure(figsize=(15,5))    
        self.canvas = FigureCanvas(self.figure)
        self.canvas.setObjectName(_fromUtf8("canvas"))
        self.toolbar = NavigationToolbar(self.canvas, self)
        self.toolbar.hide()
        self.verticalLayout_2.addWidget(self.canvas)

        # Plot buttons
        self.horizontalLayout = QtGui.QHBoxLayout()
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout_plotButtons"))
        self.plotTypeCombo = QtGui.QComboBox(self.tab)
        self.plotTypeCombo.setObjectName(_fromUtf8("plotTypeCombo"))
        self.plotTypeCombo.currentIndexChanged.connect(self.ChangePlotType)
        self.horizontalLayout.addWidget(self.plotTypeCombo)
        self.btnPlot = QtGui.QPushButton(self.tab)
        self.btnPlot.setObjectName(_fromUtf8("btnPlot"))
        self.btnPlot.clicked.connect(self.drawPlot)
        self.horizontalLayout.addWidget(self.btnPlot)
        self.btnZoom = QtGui.QPushButton(self.tab)
        self.btnZoom.setObjectName(_fromUtf8("btnZoom"))
        self.btnZoom.clicked.connect(self.plotZoom)
        self.horizontalLayout.addWidget(self.btnZoom)
        self.btnPan = QtGui.QPushButton(self.tab)
        self.btnPan.setObjectName(_fromUtf8("btnPan"))
        self.btnPan.clicked.connect(self.plotPan)
        self.horizontalLayout.addWidget(self.btnPan)
        self.btnHome = QtGui.QPushButton(self.tab)
        self.btnHome.setObjectName(_fromUtf8("btnHome"))
        self.btnHome.clicked.connect(self.plotHome)
        self.horizontalLayout.addWidget(self.btnHome)
        self.verticalLayout_2.addLayout(self.horizontalLayout)

        # x axis options
        self.horizontalLayout_xAxis = QtGui.QHBoxLayout()
        self.horizontalLayout_xAxis.setObjectName(_fromUtf8("horizontalLayout_xAxis"))
        self.xColSelect = QtGui.QComboBox(self.tab)
        self.xColSelect.setObjectName(_fromUtf8("xColSelect"))
        self.horizontalLayout_xAxis.addWidget(self.xColSelect)
        self.horizontalLayout_xAxis.setStretchFactor(self.xColSelect,2)
        self.xbinsLabel = QtGui.QLabel(self.tab)
        self.xbinsLabel.setText("X Bins:")
        self.horizontalLayout_xAxis.addWidget( self.xbinsLabel )
        self.xnBinsSpin = QtGui.QSpinBox(self.tab)
        self.xnBinsSpin.setObjectName(_fromUtf8("xnBinsSpin"))
        self.horizontalLayout_xAxis.addWidget( self.xnBinsSpin )
        self.horizontalLayout_xAxis.setStretchFactor(self.xnBinsSpin,2)
        self.xminLabel = QtGui.QLabel(self.tab)
        self.xminLabel.setText("X Min:")
        self.horizontalLayout_xAxis.addWidget( self.xminLabel )
        self.xnMinSpin = QtGui.QSpinBox(self.tab)
        self.xnMinSpin.setObjectName(_fromUtf8("xnMinSpin"))
        self.horizontalLayout_xAxis.addWidget( self.xnMinSpin )
        self.horizontalLayout_xAxis.setStretchFactor(self.xnMinSpin,2)
        self.xmaxLabel = QtGui.QLabel(self.tab)
        self.xmaxLabel.setText("X Max:")
        self.horizontalLayout_xAxis.addWidget( self.xmaxLabel )
        self.xnMaxSpin = QtGui.QSpinBox(self.tab)
        self.xnMaxSpin.setObjectName(_fromUtf8("xnMaxSpin"))
        self.horizontalLayout_xAxis.addWidget( self.xnMaxSpin )
        self.horizontalLayout_xAxis.setStretchFactor(self.xnMaxSpin,2)
        self.xTypeCombo = QtGui.QComboBox(self.tab)
        self.xTypeCombo.setObjectName(_fromUtf8("xTypeCombo"))
        self.horizontalLayout_xAxis.addWidget(self.xTypeCombo)
        self.horizontalLayout_xAxis.setStretchFactor(self.xTypeCombo,2)
        self.verticalLayout_2.addLayout(self.horizontalLayout_xAxis )
        
        # y axis options
        self.horizontalLayout_yAxis = QtGui.QHBoxLayout()
        self.horizontalLayout_yAxis.setObjectName(_fromUtf8("horizontalLayout_yAxis"))
        self.yColSelect = QtGui.QComboBox(self.tab)
        self.yColSelect.setObjectName(_fromUtf8("yColSelect"))
        self.horizontalLayout_yAxis.addWidget(self.yColSelect)
        self.horizontalLayout_yAxis.setStretchFactor(self.yColSelect,2)
        self.ybinsLabel = QtGui.QLabel(self.tab)
        self.ybinsLabel.setText("Y Bins:")
        self.horizontalLayout_yAxis.addWidget( self.ybinsLabel )
        self.ynBinsSpin = QtGui.QSpinBox(self.tab)
        self.ynBinsSpin.setObjectName(_fromUtf8("ynBinsSpin"))
        self.horizontalLayout_yAxis.addWidget( self.ynBinsSpin )
        self.horizontalLayout_yAxis.setStretchFactor(self.ynBinsSpin,2)
        self.yminLabel = QtGui.QLabel(self.tab)
        self.yminLabel.setText("Y Min:")
        self.horizontalLayout_yAxis.addWidget( self.yminLabel )
        self.ynMinSpin = QtGui.QSpinBox(self.tab)
        self.ynMinSpin.setObjectName(_fromUtf8("ynMinSpin"))
        self.horizontalLayout_yAxis.addWidget( self.ynMinSpin )
        self.horizontalLayout_yAxis.setStretchFactor(self.ynMinSpin,2)
        self.ymaxLabel = QtGui.QLabel(self.tab)
        self.ymaxLabel.setText("Y Max:")
        self.horizontalLayout_yAxis.addWidget( self.ymaxLabel )
        self.ynMaxSpin = QtGui.QSpinBox(self.tab)
        self.ynMaxSpin.setObjectName(_fromUtf8("ynMaxSpin"))
        self.horizontalLayout_yAxis.addWidget( self.ynMaxSpin )
        self.horizontalLayout_yAxis.setStretchFactor(self.ynMaxSpin,2)
        self.yTypeCombo = QtGui.QComboBox(self.tab)
        self.yTypeCombo.setObjectName(_fromUtf8("yTypeCombo"))
        self.horizontalLayout_yAxis.addWidget(self.yTypeCombo)
        self.horizontalLayout_yAxis.setStretchFactor(self.yTypeCombo,2)
        #self.verticalLayout_2.addLayout(self.horizontalLayout_yAxis )
        self.yAxisItems = [ self.yColSelect, self.ybinsLabel, self.ynBinsSpin, self.yminLabel, self.ynMinSpin,
                            self.ymaxLabel, self.ynMaxSpin, self.yTypeCombo ]
        [ y.hide() for y in self.yAxisItems ]
        
        # Data tab
        self.tabWidget.addTab(self.tab, _fromUtf8(""))
        self.tab_2 = QtGui.QWidget()
        self.tab_2.setObjectName(_fromUtf8("tab_2"))
        self.verticalLayout_3 = QtGui.QVBoxLayout(self.tab_2)
        self.verticalLayout_3.setObjectName(_fromUtf8("verticalLayout_3"))
        self.tableView = QtGui.QTableView(self.tab_2)
        self.tableView.setObjectName(_fromUtf8("tableView"))
        self.verticalLayout_3.addWidget(self.tableView)
        
        # Filter text entry
        self.filterHorLayout = QtGui.QHBoxLayout()
        self.filterHorLayout.setObjectName(_fromUtf8("filterHorLayout"))
        self.filterBox = QtGui.QLineEdit(self.centralwidget)
        self.filterBox.setObjectName(_fromUtf8("filterBox"))
        self.btnFilter = QtGui.QPushButton(self.centralwidget)
        self.btnFilter.setObjectName(_fromUtf8("btnFilter"))
        self.btnFilter.clicked.connect(self.updateTable)
        self.filterHorLayout.addWidget(self.filterBox)
        self.filterHorLayout.addWidget(self.btnFilter)
        self.verticalLayout.addLayout(self.filterHorLayout)
        
        # Setup
        self.treeView.raise_()
        self.tabWidget.addTab(self.tab_2, _fromUtf8(""))
        self.verticalLayout.addWidget(self.splitter)
        self.splitter.setStretchFactor(1, 2)
        self.centralwidget.showFullScreen()
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtGui.QStatusBar(MainWindow)
        self.statusbar.setObjectName(_fromUtf8("statusbar"))
        MainWindow.setStatusBar(self.statusbar)

        self.plotTypeCombo.addItems( ['Scatter','Line','Hist','Hist2d'] )
        
        
        self.fileName = ""
        self.df = None
        self.orig_df = None
        self.filterStr = None
        self.lastFilterStr = None
        
        self.retranslateUi(MainWindow)
        self.tabWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

        if self.currentFile is not None:
            print self.currentFile
            self.treeView.setCurrentIndex( self.fileSystemModel.index( self.currentFile ) )
            self.recursive_expand( index, self.treeView )
            self.on_treeView_doubleClicked(  self.fileSystemModel.index( self.currentFile ) )
            
        
    def setupCsv(self):
        self.data()
        self.columns = self.df.columns.tolist()
        self.xColSelect.clear()
        self.xColSelect.addItems( self.columns )
        self.yColSelect.clear()
        self.yColSelect.addItems( self.columns )
        self.updateTable()

    def setupH5(self):
        self.h5keys = self.hdfStore.keys()
        if len(self.h5keys) > 1:
            self.chosen_h5key = str( SelectDialog.SelectDialog.getOptions( self.h5keys ) )
        else:
            self.chosen_h5key = ""
        if self.chosen_h5key == "":
            self.orig_df = self.hdfStore[ self.h5keys[0] ]
        else:
            self.orig_df = self.hdfStore[ self.chosen_h5key ]
        self.setupCsv()
        
    def plotHist(self):
        if self.data() is None: return
        plt.clf()
        col = str( self.xColSelect.currentText() )
        plt.hist( self.df[ col ].tolist() )
        plt.xlabel( col )
        self.canvas.draw()
        
    def plotScatter(self):
        if self.data() is None: return
        plt.clf()
        xCol = str( self.xColSelect.currentText() )
        yCol = str( self.yColSelect.currentText() )
        ax = plt.gca()
        ax.scatter( self.df[ xCol ].tolist(), self.df[ yCol ].tolist(), label=xCol + ' v ' + yCol )
        ax.set_xlabel( xCol )
        ax.set_ylabel( yCol )
        self.canvas.draw()

    def data(self):
        if self.orig_df is None: return None
        self.filterStr = str(self.filterBox.text())
        if self.filterStr is not None and self.filterStr != "":
            if self.filterStr != self.lastFilterStr:
                try:
                    exec("self.df = self.orig_df[" +  self.filterStr.replace("df","self.orig_df") + "]" )
                    self.lastFilterStr = self.filterStr
                except Exception as e:
                    msg = QMessageBox()
                    msg.setIcon(QMessageBox.Warning)
                    msg.setText("Filtering failed")
                    msg.setWindowTitle("Error")
                    msg.setDetailedText( str(e) )
                    msg.setStandardButtons(QMessageBox.Ok)
                    msg.exec_()
                    pass
                pass
            pass
        else:
            self.df = self.orig_df
        return True
    
    def updateTable(self):
        if self.data() is None: return
        header = self.columns
        tm = MyTableModel.MyTableModel(self.df.values, header, self)
        self.tableView.setModel(tm)
        vh = self.tableView.verticalHeader()
        vh.setVisible(False)
        hh = self.tableView.horizontalHeader()
        hh.setStretchLastSection(True)
        self.tableView.setSortingEnabled(True)
        self.tableView.sortByColumn(0);

    def plotZoom(self): self.toolbar.zoom()
    def plotPan(self): self.toolbar.pan()
    def plotHome(self): self.toolbar.home()
        
    def on_treeView_doubleClicked(self, index ):
        fileName = str(index.model().filePath(index))
        if self.fileName == fileName: return
        if fileName.endswith( ".csv" ):
            self.fileName = fileName
            self.isCsv = True
            self.isH5 = False
            self.orig_df = pd.read_csv( fileName )
            self.setupCsv()
        elif fileName.endswith(".h5"):
            self.fileName = fileName
            self.isCsv = False
            self.isH5 = True
            self.hdfStore = pd.HDFStore( fileName, 'r' )
            self.setupH5()
        
    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow", None))
        #self.btnScatter.setText(_translate("MainWindow", "Scatter", None))
        #self.btnHist.setText(_translate("MainWindow", "Hist", None))
        self.btnZoom.setText(_translate("MainWindow", "Zoom", None))
        self.btnPlot.setText(_translate("MainWindow", "Draw", None))
        self.btnPan.setText(_translate("MainWindow", "Pan", None))
        self.btnHome.setText(_translate("MainWindow", "Reset", None))
        self.btnFilter.setText(_translate("MainWindow","Update Table", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), _translate("MainWindow", "Plot", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), _translate("MainWindow", "Data", None))

    def recursive_expand(self, index, treeView):
        treeView.expand( index )
        parent = index.parent()
        if parent != index:
            self.recursive_expand( parent, treeView )


    def drawPlot(self):
        pType = self.plotTypeCombo.currentText()
        if pType == 'Scatter': self.plotScatter()
        elif pType == 'Hist': self.plotHist()

    def ChangePlotType(self):
        pType = self.plotTypeCombo.currentText()
        if pType == 'Scatter' or pType == 'Line' or pType == 'Hist2d':
            [ x.show() for x in self.yAxisItems ]
            found = False
            for i in range( self.verticalLayout_2.count() ):
                if self.verticalLayout_2.itemAt(i) == self.horizontalLayout_yAxis: found=True
            if not found: self.verticalLayout_2.addLayout( self.horizontalLayout_yAxis )
        else:
            [ x.hide() for x in self.yAxisItems ]
            for i in range( self.verticalLayout_2.count() ):
                if self.verticalLayout_2.itemAt(i) == self.horizontalLayout_yAxis:
                    self.verticalLayout_2.removeItem( self.horizontalLayout_yAxis )
        self.verticalLayout_2.update()
