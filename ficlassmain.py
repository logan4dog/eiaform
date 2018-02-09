from PyQt5 import QtWidgets
# contains UI from qt designer
from filelist import Ui_MainWindow
import os
import re
import sys


class MainWindow_Exec:
    """A main window execute class"""
    def __init__(self):
        # A qt window class

        #self.app = 0
        self.app = QtWidgets.QApplication(sys.argv)
        self.MainWindow = QtWidgets.QMainWindow()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self.MainWindow)

        self.update_textedit()
        self.MainWindow.show()
        sys.exit(self.app.exec_())

    def update_textedit(self):
        """Fill up TextEdit widget with curr dir file name"""
        #a = [x for x in os.listdir('.') if re.search('.py', x)]
        a = [x for x in os.listdir('.')]
        self.ui.textEdit.setText("+++++++++++++++++++++++")
        b = sorted(a)
        for f in b:
            self.ui.textEdit.append(f)
        self.ui.label.setText(os.getcwd())

    def getMainWindow(self):
        pass

if __name__ == "__main__":
    MainWindow_Exec()

