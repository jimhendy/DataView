from PyQt4 import QtGui
from PyQt4 import QtCore
import sys
import design
import os, time

class ExampleApp(QtGui.QMainWindow, design.Ui_MainWindow):
    def __init__(self):
        super(self.__class__, self).__init__()
        self.setupUi(self) 

def main():
    app = QtGui.QApplication(sys.argv)
    form = ExampleApp()                
    form.show()
    app.exec_()                        
    
    
if __name__ == '__main__':
    main()                             
