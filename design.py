# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'DataView.ui'
#
# Created by: PyQt5 UI code generator 4.11.4
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
import pandas as pd
import sys, math
import matplotlib
matplotlib.use('Qt5Agg')
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.figure import Figure
from matplotlib.backends.backend_qt5agg import NavigationToolbar2QT as NavigationToolbar
import matplotlib.pyplot as plt
import datetime
import MyTableModel
import SelectDialog
plt.style.use('ggplot')

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtWidgets.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtWidgets.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtWidgets.QApplication.translate(context, text, disambig)
    
class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName(_fromUtf8("Data View"))
        #MainWindow.resize(539, 600)
        
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))

        self.verticalLayout = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.splitter = QtWidgets.QSplitter(self.centralwidget)
        self.splitter.setOrientation(QtCore.Qt.Horizontal)
        self.splitter.setObjectName(_fromUtf8("splitter"))        

        # File navigation
        self.fileSystemModel = QtWidgets.QDirModel(self.splitter)
        self.fileSystemModel.setObjectName(_fromUtf8("fileSystemModel"))
        currentDir = str(QtCore.QDir.currentPath())
        index = self.fileSystemModel.index(currentDir)
        self.treeView = QtWidgets.QTreeView(self.splitter)
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
        self.tabWidget = QtWidgets.QTabWidget(self.splitter)
        self.tabWidget.setObjectName(_fromUtf8("tabWidget"))
        self.tab = QtWidgets.QWidget()
        self.tab.setObjectName(_fromUtf8("tab"))
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.tab)
        self.verticalLayout_2.setObjectName(_fromUtf8("verticalLayout_2"))
        self.figure = plt.figure(figsize=(15,5))    
        self.canvas = FigureCanvas(self.figure)
        self.canvas.setObjectName(_fromUtf8("canvas"))
        self.toolbar = NavigationToolbar(self.canvas, self)
        self.toolbar.hide()
        self.verticalLayout_2.addWidget(self.canvas)

        # Plot buttons
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout_plotButtons"))
        self.plotTypeCombo = QtWidgets.QComboBox(self.tab)
        self.plotTypeCombo.setObjectName(_fromUtf8("plotTypeCombo"))
        self.plotTypeCombo.currentIndexChanged.connect(self.ChangePlotType)
        self.horizontalLayout.addWidget(self.plotTypeCombo)
        self.btnPlot = QtWidgets.QPushButton(self.tab)
        self.btnPlot.setObjectName(_fromUtf8("btnPlot"))
        self.btnPlot.clicked.connect(self.drawPlot)
        self.horizontalLayout.addWidget(self.btnPlot)
        self.btnZoom = QtWidgets.QPushButton(self.tab)
        self.btnZoom.setObjectName(_fromUtf8("btnZoom"))
        self.btnZoom.clicked.connect(self.plotZoom)
        self.horizontalLayout.addWidget(self.btnZoom)
        self.btnPan = QtWidgets.QPushButton(self.tab)
        self.btnPan.setObjectName(_fromUtf8("btnPan"))
        self.btnPan.clicked.connect(self.plotPan)
        self.horizontalLayout.addWidget(self.btnPan)
        self.btnHome = QtWidgets.QPushButton(self.tab)
        self.btnHome.setObjectName(_fromUtf8("btnHome"))
        self.btnHome.clicked.connect(self.plotHome)
        self.horizontalLayout.addWidget(self.btnHome)
        self.verticalLayout_2.addLayout(self.horizontalLayout)

        # x axis options
        self.horizontalLayout_xAxis = QtWidgets.QHBoxLayout()
        self.horizontalLayout_xAxis.setObjectName(_fromUtf8("horizontalLayout_xAxis"))
        self.xColSelect = QtWidgets.QComboBox(self.tab)
        self.xColSelect.setObjectName(_fromUtf8("xColSelect"))
        self.xColSelect.currentIndexChanged.connect(self.ResetUserSelections)
        self.horizontalLayout_xAxis.addWidget(self.xColSelect)
        self.horizontalLayout_xAxis.setStretchFactor(self.xColSelect,2)
        self.xbinsLabel = QtWidgets.QLabel(self.tab)
        self.xbinsLabel.setText("X Bins:")
        self.horizontalLayout_xAxis.addWidget( self.xbinsLabel )
        self.xnBinsSpin = QtWidgets.QSpinBox(self.tab)
        self.xnBinsSpin.setObjectName(_fromUtf8("xnBinsSpin"))
        self.xnBinsSpin.valueChanged.connect(self.XChangeBinning)
        self.xnBinsSpin.setRange(1,10000)
        self.horizontalLayout_xAxis.addWidget( self.xnBinsSpin )
        self.horizontalLayout_xAxis.setStretchFactor(self.xnBinsSpin,2)
        self.xminLabel = QtWidgets.QLabel(self.tab)
        self.xminLabel.setText("X Min:")
        self.horizontalLayout_xAxis.addWidget( self.xminLabel )
        self.xnMinSpin = QtWidgets.QDoubleSpinBox(self.tab)
        self.xnMinSpin.setObjectName(_fromUtf8("xnMinSpin"))
        self.xnMinSpin.valueChanged.connect(self.XChangeMin)
        self.xnMinSpin.setRange( -1e20, 1e20 )
        self.horizontalLayout_xAxis.addWidget( self.xnMinSpin )
        self.horizontalLayout_xAxis.setStretchFactor(self.xnMinSpin,2)
        self.xmaxLabel = QtWidgets.QLabel(self.tab)
        self.xmaxLabel.setText("X Max:")
        self.horizontalLayout_xAxis.addWidget( self.xmaxLabel )
        self.xnMaxSpin = QtWidgets.QDoubleSpinBox(self.tab)
        self.xnMaxSpin.setObjectName(_fromUtf8("xnMaxSpin"))
        self.xnMaxSpin.setRange( -1e20, 1e20 )
        self.xnMaxSpin.valueChanged.connect(self.XChangeMax)
        self.horizontalLayout_xAxis.addWidget( self.xnMaxSpin )
        self.horizontalLayout_xAxis.setStretchFactor(self.xnMaxSpin,2)
        self.xTypeCombo = QtWidgets.QComboBox(self.tab)
        self.xTypeCombo.setObjectName(_fromUtf8("xTypeCombo"))
        self.xTypeCombo.addItems( ['int','float','str','datetime'] )
        self.xTypeCombo.currentIndexChanged.connect(self.ChangeXDataType)
        self.horizontalLayout_xAxis.addWidget(self.xTypeCombo)
        self.horizontalLayout_xAxis.setStretchFactor(self.xTypeCombo,2)
        self.verticalLayout_2.addLayout(self.horizontalLayout_xAxis )
        
        # y axis options
        self.horizontalLayout_yAxis = QtWidgets.QHBoxLayout()
        self.horizontalLayout_yAxis.setObjectName(_fromUtf8("horizontalLayout_yAxis"))
        self.yColSelect = QtWidgets.QComboBox(self.tab)
        self.yColSelect.setObjectName(_fromUtf8("yColSelect"))
        self.yColSelect.currentIndexChanged.connect(self.ResetUserSelections)
        self.horizontalLayout_yAxis.addWidget(self.yColSelect)
        self.horizontalLayout_yAxis.setStretchFactor(self.yColSelect,2)
        self.ybinsLabel = QtWidgets.QLabel(self.tab)
        self.ybinsLabel.setText("Y Bins:")
        self.horizontalLayout_yAxis.addWidget( self.ybinsLabel )
        self.ynBinsSpin = QtWidgets.QSpinBox(self.tab)
        self.ynBinsSpin.setObjectName(_fromUtf8("ynBinsSpin"))
        self.ynBinsSpin.valueChanged.connect(self.YChangeBinning)
        self.horizontalLayout_yAxis.addWidget( self.ynBinsSpin )
        self.horizontalLayout_yAxis.setStretchFactor(self.ynBinsSpin,2)
        self.yminLabel = QtWidgets.QLabel(self.tab)
        self.yminLabel.setText("Y Min:")
        self.horizontalLayout_yAxis.addWidget( self.yminLabel )
        self.ynMinSpin = QtWidgets.QDoubleSpinBox(self.tab)
        self.ynMinSpin.setObjectName(_fromUtf8("ynMinSpin"))
        self.ynMinSpin.setRange( -1e20, 1e20 )
        self.ynMinSpin.valueChanged.connect(self.YChangeMin)
        self.horizontalLayout_yAxis.addWidget( self.ynMinSpin )
        self.horizontalLayout_yAxis.setStretchFactor(self.ynMinSpin,2)
        self.ymaxLabel = QtWidgets.QLabel(self.tab)
        self.ymaxLabel.setText("Y Max:")
        self.horizontalLayout_yAxis.addWidget( self.ymaxLabel )
        self.ynMaxSpin = QtWidgets.QDoubleSpinBox(self.tab)
        self.ynMaxSpin.setObjectName(_fromUtf8("ynMaxSpin"))
        self.ynMaxSpin.setRange( -1e20, 1e20 )
        self.ynMaxSpin.valueChanged.connect(self.YChangeMax)
        self.horizontalLayout_yAxis.addWidget( self.ynMaxSpin )
        self.horizontalLayout_yAxis.setStretchFactor(self.ynMaxSpin,2)
        self.yTypeCombo = QtWidgets.QComboBox(self.tab)
        self.yTypeCombo.setObjectName(_fromUtf8("yTypeCombo"))
        self.yTypeCombo.addItems( ['int','float','str','datetime'] )
        self.yTypeCombo.currentIndexChanged.connect(self.ChangeYDataType)
        self.horizontalLayout_yAxis.addWidget(self.yTypeCombo)
        self.horizontalLayout_yAxis.setStretchFactor(self.yTypeCombo,2)
        #self.verticalLayout_2.addLayout(self.horizontalLayout_yAxis )
        self.yAxisItems = [ self.yColSelect, self.ybinsLabel, self.ynBinsSpin, self.yminLabel, self.ynMinSpin,
                            self.ymaxLabel, self.ynMaxSpin, self.yTypeCombo ]

        self.binningChoices = [ self.ybinsLabel, self.ynBinsSpin, self.xbinsLabel, self.xnBinsSpin ]
        
        # Data tab
        self.tabWidget.addTab(self.tab, _fromUtf8(""))
        self.tab_2 = QtWidgets.QWidget()
        self.tab_2.setObjectName(_fromUtf8("tab_2"))
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.tab_2)
        self.verticalLayout_3.setObjectName(_fromUtf8("verticalLayout_3"))
        self.tableView = QtWidgets.QTableView(self.tab_2)
        self.tableView.setObjectName(_fromUtf8("tableView"))
        self.verticalLayout_3.addWidget(self.tableView)
        
        # Filter text entry
        self.filterHorLayout = QtWidgets.QHBoxLayout()
        self.filterHorLayout.setObjectName(_fromUtf8("filterHorLayout"))
        self.filterBox = QtWidgets.QLineEdit(self.centralwidget)
        self.filterBox.setObjectName(_fromUtf8("filterBox"))
        self.btnFilter = QtWidgets.QPushButton(self.centralwidget)
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
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName(_fromUtf8("statusbar"))
        MainWindow.setStatusBar(self.statusbar)

        # Set the default picture
        import matplotlib.image as mpimg
        img=mpimg.imread(r'H:\stash_projects\DataView\PandaViz.jpg')
        plt.imshow(img)

        self.hdfStore = None
        self.plotTypeCombo.addItems( ['Scatter','Line','Hist','Hist2d'] )
        self.userxBinning = False
        self.userxMax = False
        self.userxMin = False
        self.useryBinning = False
        self.useryMax = False
        self.useryMin = False        
        self.fileName = ""
        self.df = None
        self.orig_df = None
        self.filterStr = None
        self.lastFilterStr = None
        
        self.retranslateUi(MainWindow)
        self.tabWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
       
        if self.currentFile is not None:

            if len(self.currentFile.split( r':' )) > 1:
                self.currentFile = self.currentFile.split( r':' )[1][-1] + r':' + self.currentFile.split( r':' )[2] 
            
            self.treeView.setCurrentIndex( self.fileSystemModel.index( self.currentFile ) )
            self.recursive_expand( index, self.treeView )
            #self.on_treeView_doubleClicked(  self.fileSystemModel.index( self.currentFile ) )
            self.on_treeView_doubleClicked(self.fileSystemModel.index( self.currentFile ) ,self.currentFile )
        
    def setupCsv(self):
        self.data()
        self.columns = self.df.columns.tolist()
        self.xColSelect.clear()
        self.xColSelect.addItems( self.columns )
        self.yColSelect.clear()
        self.yColSelect.addItems( self.columns )
        self.xTypeCombo.Text = str(self.df[ self.columns[0] ].dtype)
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

    def plotLine(self):
        if self.data() is None: return
        plt.clf()
        xCol = str( self.xColSelect.currentText() )
        yCol = str( self.yColSelect.currentText() )
        ax = plt.gca()
        ax.plot( self.df[ xCol ].tolist(), self.df[ yCol ].tolist(), label=xCol + ' v ' + yCol )
        if self.userxMin or self.userxMax or self.useryMin or self.useryMax:
            ax.set_xlim( self.xnMinSpin.value(), self.xnMaxSpin.value() )
            ax.set_ylim( self.ynMinSpin.value(), self.ynMaxSpin.value() )
        else:
            self.xnMinSpin.setValue( ax.get_xlim()[0] )
            self.xnMaxSpin.setValue( ax.get_xlim()[1] )
            self.ynMinSpin.setValue( ax.get_ylim()[0] )
            self.ynMaxSpin.setValue( ax.get_ylim()[1] )            
        ax.set_xlabel( xCol )
        ax.set_ylabel( yCol )
        self.canvas.draw()
        
    def plotHist(self):
        if self.data() is None: return
        plt.clf()
        col = str( self.xColSelect.currentText() )
        if self.userxBinning: bins = self.xnBinsSpin.value()
        else: bins = 10

        if not self.userxBinning: self.xnBinsSpin.setValue( bins )

        if self.userxMin:
            Min = self.xnMinSpin.value()
        else:
            Min = self.df[col].min()
            try: self.xnMinSpin.setValue( Min )
            except: self.xnMinSpin.setValue( 0. )
        if self.userxMax:
            Max = self.xnMaxSpin.value()
        else:
            Max = self.df[col].max()
            try: self.xnMaxSpin.setValue( Max )
            except: self.xnMaxSpin.setValue( 0. )
                    
        plt.hist( sorted(self.df[ col ].tolist()), bins=bins, range=(Min,Max) )
        plt.xlabel( col )
        self.canvas.draw()
        
    def plotScatter(self):
        if self.data() is None: return
        plt.clf()
        xCol = str( self.xColSelect.currentText() )
        yCol = str( self.yColSelect.currentText() )
        ax = plt.gca()
        ax.scatter( self.df[ xCol ].tolist(), self.df[ yCol ].tolist(), label=xCol + ' v ' + yCol )
        if self.userxMin or self.userxMax or self.useryMin or self.useryMax:
            ax.set_xlim( self.xnMinSpin.value(), self.xnMaxSpin.value() )
            ax.set_ylim( self.ynMinSpin.value(), self.ynMaxSpin.value() )
        else:
            self.xnMinSpin.setValue( ax.get_xlim()[0] )
            self.xnMaxSpin.setValue( ax.get_xlim()[1] )
            self.ynMinSpin.setValue( ax.get_ylim()[0] )
            self.ynMaxSpin.setValue( ax.get_ylim()[1] )            
        ax.set_xlabel( xCol )
        ax.set_ylabel( yCol )
        self.canvas.draw()

    def plotHist2d(self):
        if self.data() is None: return
        plt.clf()
        xCol = str( self.xColSelect.currentText() )
        yCol = str( self.yColSelect.currentText() )
        ax = plt.gca()
        if self.userxBinning: bins = self.xnBinsSpin.value()
        else: bins = 10
        ax.hist2d( self.df[xCol].tolist(), self.df[yCol].tolist(), bins=bins )
        if not self.userxBinning: self.xnBinsSpin.setValue( bins )
        if not self.userxMin:
            self.xnMinSpin.setValue( ax.get_xlim()[0] )
        else:
            ax.set_xlim([self.xnMinSpin.value(), ax.get_xlim()[1] ] )
        if not self.userxMax:
            self.xnMaxSpin.setValue( ax.get_xlim()[1] )
        else:
            ax.set_xlim([ax.get_xlim()[0], self.xnMaxSpin.value() ] )
        if not self.useryMin:
            self.ynMinSpin.setValue( ax.get_ylim()[0] )
        else:
            ax.set_ylim([self.ynMinSpin.value(), ax.get_ylim()[1] ] )
        if not self.useryMax:
            self.ynMaxSpin.setValue( ax.get_ylim()[1] )
        else:
            ax.set_ylim([ax.get_ylim()[0], self.ynMaxSpin.value() ] )
        plt.xlabel( xCol )
        plt.ylabel( yCol )
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
        #self.tableView.sortByColumn(0);
        tm.sort( 0,  Qt.AscendingOrder )
        
    def plotZoom(self): self.toolbar.zoom()
    def plotPan(self): self.toolbar.pan()
    def plotHome(self): self.toolbar.home()
        
    def on_treeView_doubleClicked(self, index, fileName = '' ):
        if fileName == '':
            fileName = str(index.model().filePath(index))
            
        if self.fileName == fileName: return

        if self.hdfStore is not None:
            self.hdfStore.close()
            
        if fileName.endswith( ".csv" ):
            self.hdfStore = None
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
        MainWindow.setWindowTitle(_translate("MainWindow", "PandaViz", None))
        import os.path as osp
        path = osp.join(osp.dirname(sys.modules[__name__].__file__), 'PandaViz.jpg')
        MainWindow.setWindowIcon(QIcon(path))
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
        elif pType == 'Hist2d': self.plotHist2d()
        elif pType == 'Line': self.plotLine()

    def ChangeXDataType(self):
        if self.data() is None: return
        col = str( self.xColSelect.currentText() )
        changeType = str( self.xTypeCombo.currentText() )
        try:
            if changeType == 'datetime':
                self.df[ col ] = pd.to_datetime( self.df[ col ])
            else:
                exec("self.df[ col ] = self.df[ col ].astype("+ changeType + ")")
        except Exception as e:
            msg = QMessageBox()
            msg.setIcon(QMessageBox.Warning)
            msg.setText("Type Conversion Failed")
            msg.setWindowTitle("Error")
            msg.setDetailedText( str(e) )
            msg.setStandardButtons(QMessageBox.Ok)
            msg.exec_()
            pass
        pass

    def ChangeYDataType(self):
        if self.data() is None: return
        col = str( self.yColSelect.currentText() )
        changeType = str( self.yTypeCombo.currentText() )
        try:
            if changeType == 'datetime':
                self.df[ col ] = pd.to_datetime( self.df[ col ])
            else:
                exec("self.df[ col ] = self.df[ col ].astype("+ changeType + ")")
        except Exception as e:
            msg = QMessageBox()
            msg.setIcon(QMessageBox.Warning)
            msg.setText("Type Conversion Failed")
            msg.setWindowTitle("Error")
            msg.setDetailedText( str(e) )
            msg.setStandardButtons(QMessageBox.Ok)
            msg.exec_()
            pass
        pass
    
    def ChangePlotType(self):
        self.userBinning = False
        pType = self.plotTypeCombo.currentText()
        if pType == 'Scatter' or pType == 'Line' or pType == 'Hist2d':
            [ x.show() for x in self.yAxisItems ]
            found = False
            for i in range( self.verticalLayout_2.count() ):
                if self.verticalLayout_2.itemAt(i) == self.horizontalLayout_yAxis: found=True
            if not found: self.verticalLayout_2.addLayout( self.horizontalLayout_yAxis )
            if pType == 'Scatter' or pType == 'Line':
                [ x.hide() for x in self.binningChoices ]
            else:
                [ x.show() for x in self.binningChoices ]
        else:
            [ x.show() for x in self.binningChoices ]
            [ x.hide() for x in self.yAxisItems ]
            for i in range( self.verticalLayout_2.count() ):
                if self.verticalLayout_2.itemAt(i) == self.horizontalLayout_yAxis:
                    self.verticalLayout_2.removeItem( self.horizontalLayout_yAxis )
        self.verticalLayout_2.update()


    def XChangeBinning(self): self.userxBinning = True
    def YChangeBinning(self): self.useryBinning = True
    def XChangeMax(self): self.userxMax = True
    def YChangeMax(self): self.useryMax = True
    def XChangeMin(self): self.userxMin = True
    def YChangeMin(self): self.useryMin = True

    def ResetUserSelections(self):
        self.userxMin = False
        self.useryMin = False
        self.userxMax = False
        self.useryMax = False
        self.userxBinning = False
        self.useryBinning = False
