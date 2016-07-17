# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'DataView.ui'
#
# Created by: PyQt4 UI code generator 4.11.4
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

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
        MainWindow.setObjectName(_fromUtf8("MainWindow"))
        MainWindow.resize(539, 600)
        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.verticalLayout = QtGui.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.splitter = QtGui.QSplitter(self.centralwidget)
        self.splitter.setOrientation(QtCore.Qt.Horizontal)
        self.splitter.setObjectName(_fromUtf8("splitter"))        
        self.fileSystemModel = QtGui.QDirModel(self.splitter)
        self.fileSystemModel.setObjectName(_fromUtf8("fileSystemModel"))
        index = self.fileSystemModel.index(QtCore.QDir.currentPath())
        self.treeView = QtGui.QTreeView(self.splitter)
        self.treeView.setObjectName(_fromUtf8("treeView"))
        self.treeView.setModel(self.fileSystemModel)
        self.recursive_expand( index, self.treeView )
        tVheader = self.treeView.header()
        for i in range(1,4): tVheader.hideSection(i)
        self.tabWidget = QtGui.QTabWidget(self.splitter)
        self.tabWidget.setObjectName(_fromUtf8("tabWidget"))
        self.tab = QtGui.QWidget()
        self.tab.setObjectName(_fromUtf8("tab"))
        self.verticalLayout_2 = QtGui.QVBoxLayout(self.tab)
        self.verticalLayout_2.setObjectName(_fromUtf8("verticalLayout_2"))
        self.graphicsView = QtGui.QGraphicsView(self.tab)
        self.graphicsView.setObjectName(_fromUtf8("graphicsView"))
        self.verticalLayout_2.addWidget(self.graphicsView)
        self.horizontalLayout = QtGui.QHBoxLayout()
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.btnScatter = QtGui.QPushButton(self.tab)
        self.btnScatter.setObjectName(_fromUtf8("btnScatter"))
        self.horizontalLayout.addWidget(self.btnScatter)
        self.btnHist = QtGui.QPushButton(self.tab)
        self.btnHist.setObjectName(_fromUtf8("btnHist"))
        self.horizontalLayout.addWidget(self.btnHist)
        self.verticalLayout_2.addLayout(self.horizontalLayout)
        self.tabWidget.addTab(self.tab, _fromUtf8(""))
        self.tab_2 = QtGui.QWidget()
        self.tab_2.setObjectName(_fromUtf8("tab_2"))
        self.treeView.raise_()
        self.tabWidget.addTab(self.tab_2, _fromUtf8(""))
        self.verticalLayout.addWidget(self.splitter)
        self.splitter.setStretchFactor(1, 3)
        self.splitter.setStretchFactor(0, 1)
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtGui.QStatusBar(MainWindow)
        self.statusbar.setObjectName(_fromUtf8("statusbar"))
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        self.tabWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    
        
    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow", None))
        self.btnScatter.setText(_translate("MainWindow", "Scatter", None))
        self.btnHist.setText(_translate("MainWindow", "Hist", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), _translate("MainWindow", "Plot", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), _translate("MainWindow", "Data", None))

    def recursive_expand(self, index, treeView):
        treeView.expand( index )
        parent = index.parent()
        if parent != index:
            self.recursive_expand( parent, treeView )
