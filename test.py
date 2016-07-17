'''
20160516: in v3, try to read in the csv file through menu rather than do this in the code, but v3 does not work

20160516: in v2, try to use dropdown menu to select data

20160515 in this v1, we can input the rating and year_quarter in the first and second cell of the table and then plot the result.
'''

from PyQt4 import QtGui
import os, sys
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from matplotlib import style
from matplotlib.backends.backend_qt4agg import FigureCanvasQTAgg as FigureCanvas

style.use('ggplot')


class PrettyWidget(QtGui.QWidget):


    def __init__(self):
        super(PrettyWidget, self).__init__()
        self.initUI()

    def initUI(self):
        self.setGeometry(600,300, 1000, 600)
        self.center()
        self.setWindowTitle('Revision on Plots, Tables and File Browser')     

        #Grid Layout
        grid = QtGui.QGridLayout()
        self.setLayout(grid)

        #Canvas and Toolbar
        self.figure = plt.figure(figsize=(15,5))    
        self.canvas = FigureCanvas(self.figure)     
        grid.addWidget(self.canvas, 2,0,1,2)


        #Import CSV Button
        btn1 = QtGui.QPushButton('Import CSV', self)
        btn1.resize(btn1.sizeHint())
        btn1.clicked.connect(self.getCSV)
        grid.addWidget(btn1, 1, 0)

        #DropDown mean / comboBox

        self.df = pd.DataFrame()
        self.column_list = []

        self.comboBox = QtGui.QComboBox(self)
        grid.addWidget(self.comboBox, 0, 0)

        self.comboBox2 = QtGui.QComboBox(self)
        grid.addWidget(self.comboBox2, 0, 1)

        #Plot Button
        btn2 = QtGui.QPushButton('Plot', self)
        btn2.resize(btn2.sizeHint())    
        btn2.clicked.connect(self.plot)
        grid.addWidget(btn2, 1, 1)

        self.show()


    def getCSV(self):
        filePath = QtGui.QFileDialog.getOpenFileName(self, 'CSV File', '~', '*.csv')
        print filePath
        self.df = pd.read_csv(str(filePath))
        self.column_list = self.df.columns.tolist()
        self.comboBox.addItems(self.column_list)
        self.comboBox2.addItems(self.column_list)

    def plot(self):
        plt.cla()
        plt.scatter( self.df[ str(self.comboBox.currentText()) ].values, self.df[ str(self.comboBox2.currentText()) ].values )
        ax = self.figure.add_subplot(111)
        ax.legend(loc = 0)
        self.canvas.draw()


    def center(self):
        qr = self.frameGeometry()
        cp = QtGui.QDesktopWidget().availableGeometry().center()
        qr.moveCenter(cp)
        self.move(qr.topLeft())



def main():
    app = QtGui.QApplication(sys.argv)
    w = PrettyWidget()
    app.exec_()


if __name__ == '__main__':
    main()
