from PyQt5 import QtWidgets, QtCore
# contains UI from qt designer
from eia_ui import Ui_MainWindow
import os
import re
import sys
import urllib.request
import pprint
import json


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


    def getMainWindow(self):
        pass

    def eiaf(self,pay):
        URL = 'http://api.eia.gov/category/?&api_key='+'E74A9A9CEE9CED02E0AD1992BB74CE33&category_id=711275&'+pay
        response =urllib.request.urlopen(URL)
        str_response = response.read()
        obj = json.loads(str_response.decode('utf-8'))
        return obj

    def eiaf_str(self,pay):
        URL = 'http://api.eia.gov/category/?&api_key='+'E74A9A9CEE9CED02E0AD1992BB74CE33&category_id=711275&'+pay
        response =urllib.request.urlopen(URL)
        str_response = response.read()
        #obj = json.loads(str_response.decode('utf-8'))
        pp = pprint.PrettyPrinter(indent=4)
        return str_response.decode("utf-8")

    def eiaf_header(self):
        return "++++++++++++++++++++++++++++++"

    def te_help(self,s):
        self.ui.textEdit.append(s)

    def series_dict_out(self,ds):
        m = QtCore.QStringListModel()
        for x in ds.keys():
            self.te_help(x+":" + ds[x])
        m.setStringList(['One','Two','Three'])
        self.ui.listView



    def update_textedit(self):
        """Fill up TextEdit widget with curr dir file name"""
        obj = self.eiaf("category_id=41134")
        self.ui.textEdit.setText("eia data")
        self.ui.textEdit.append(self.eiaf_header())
        s = "parent category:"+ obj["category"]["parent_category_id"]
        self.te_help(s)
        for key in obj.keys():
            self.ui.textEdit.append("obj key:"+key)
        s = "category name:"+obj["category"]["name"]
        self.te_help(s)
        self.ui.label.setText("Category ID: "+obj["category"]["category_id"])
        self.te_help(s)
        self.series_dict_out(obj["category"]["childseries"][0])
        for n in range(len(obj["category"]["childseries"])):
            self.series_dict_out(obj["category"]["childseries"][n])
        self.series_dict_out(obj["category"]["childseries"][0])
        self.ui.textEdit.append(self.eiaf_header())

        s = self.eiaf_str("category_id=41134")
        self.ui.textEdit.append(s)

if __name__ == "__main__":
    MainWindow_Exec()

