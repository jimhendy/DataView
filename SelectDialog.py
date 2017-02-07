from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *

class SelectDialog(QDialog):
    
    def __init__(self, options, parent = None):
        super(SelectDialog, self).__init__(parent)

        layout = QVBoxLayout(self)

        self.combo = QComboBox()
        self.combo.addItems( options )
        
        layout.addWidget( self.combo )

        # OK and Cancel buttons
        buttons = QDialogButtonBox(
            QDialogButtonBox.Ok | QDialogButtonBox.Cancel,
            Qt.Horizontal, self)
        buttons.accepted.connect(self.select)
        buttons.rejected.connect(self.reject)
        layout.addWidget(buttons)

    def select(self):
        self.chosenOption = self.combo.currentText()
        self.accept()

    def run(self):
        self.chosenOption = ""
        if self.exec_():
            return self.chosenOption
        else:
            return ""
        
    # static method to create the dialog and return (date, time, accepted)
    @staticmethod
    def getOptions(options, parent = None):
        dialog = SelectDialog(options,parent)
        result = dialog.run()
        return result
