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
        index = self.fileSystemModel.index(QtCore.QDir.currentPath())
        self.treeView = QtGui.QTreeView(self.splitter)
        self.treeView.setObjectName(_fromUtf8("treeView"))
        self.treeView.setModel(self.fileSystemModel)
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
        self.btnScatter = QtGui.QPushButton(self.tab)
        self.btnScatter.setObjectName(_fromUtf8("btnScatter"))
        self.btnScatter.clicked.connect(self.plotScatter)
        self.horizontalLayout.addWidget(self.btnScatter)
        self.btnHist = QtGui.QPushButton(self.tab)
        self.btnHist.setObjectName(_fromUtf8("btnHist"))
        self.btnHist.clicked.connect(self.plotHist)
        self.horizontalLayout.addWidget(self.btnHist)
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

        # Column Selectors
        self.horizontalLayout_columnSelectors = QtGui.QHBoxLayout()
        self.horizontalLayout_columnSelectors.setObjectName(_fromUtf8("horizontalLayout_columnSelectors"))
        self.xColSelect = QtGui.QComboBox(self.tab)
        self.xColSelect.setObjectName(_fromUtf8("xColSelect"))
        self.horizontalLayout_columnSelectors.addWidget(self.xColSelect)
        self.yColSelect = QtGui.QComboBox(self.tab)
        self.yColSelect.setObjectName(_fromUtf8("yColSelect"))
        self.horizontalLayout_columnSelectors.addWidget(self.yColSelect)
        self.verticalLayout_2.addLayout(self.horizontalLayout_columnSelectors)
        
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

        self.fileName = ""
        self.df = None
        self.orig_df = None
        self.filterStr = None
        self.lastFilterStr = None
        
        self.retranslateUi(MainWindow)
        self.tabWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

        #if len(sys.argv) > 2:
            
        
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
        self.chosen_h5key = str( SelectDialog.SelectDialog.getOptions( self.h5keys ) )
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
        self.btnScatter.setText(_translate("MainWindow", "Scatter", None))
        self.btnHist.setText(_translate("MainWindow", "Hist", None))
        self.btnZoom.setText(_translate("MainWindow", "Zoom", None))
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

