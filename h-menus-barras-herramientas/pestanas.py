# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'qt-designer\h-menus-barras-herramientas\pestanas.ui'
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

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName(_fromUtf8("Dialog"))
        Dialog.resize(228, 161)
        self.horizontalLayout = QtGui.QHBoxLayout(Dialog)
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.tabWidget = QtGui.QTabWidget(Dialog)
        self.tabWidget.setStyleSheet(_fromUtf8("background-color: rgb(170, 255, 127);\n"
"font: 10pt \"MS Shell Dlg 2\";"))
        self.tabWidget.setLocale(QtCore.QLocale(QtCore.QLocale.Spanish, QtCore.QLocale.Ecuador))
        self.tabWidget.setObjectName(_fromUtf8("tabWidget"))
        self.tab = QtGui.QWidget()
        self.tab.setObjectName(_fromUtf8("tab"))
        self.horizontalLayout_2 = QtGui.QHBoxLayout(self.tab)
        self.horizontalLayout_2.setObjectName(_fromUtf8("horizontalLayout_2"))
        self.gridLayout = QtGui.QGridLayout()
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.checkBox = QtGui.QCheckBox(self.tab)
        self.checkBox.setObjectName(_fromUtf8("checkBox"))
        self.gridLayout.addWidget(self.checkBox, 0, 0, 1, 1)
        self.checkBox_3 = QtGui.QCheckBox(self.tab)
        self.checkBox_3.setObjectName(_fromUtf8("checkBox_3"))
        self.gridLayout.addWidget(self.checkBox_3, 2, 0, 1, 1)
        self.checkBox_2 = QtGui.QCheckBox(self.tab)
        self.checkBox_2.setObjectName(_fromUtf8("checkBox_2"))
        self.gridLayout.addWidget(self.checkBox_2, 1, 0, 1, 1)
        self.horizontalLayout_2.addLayout(self.gridLayout)
        self.tabWidget.addTab(self.tab, _fromUtf8(""))
        self.tab_2 = QtGui.QWidget()
        self.tab_2.setObjectName(_fromUtf8("tab_2"))
        self.horizontalLayout_3 = QtGui.QHBoxLayout(self.tab_2)
        self.horizontalLayout_3.setObjectName(_fromUtf8("horizontalLayout_3"))
        self.gridLayout_4 = QtGui.QGridLayout()
        self.gridLayout_4.setObjectName(_fromUtf8("gridLayout_4"))
        self.checkBox_17 = QtGui.QCheckBox(self.tab_2)
        self.checkBox_17.setObjectName(_fromUtf8("checkBox_17"))
        self.gridLayout_4.addWidget(self.checkBox_17, 2, 0, 1, 1)
        self.checkBox_16 = QtGui.QCheckBox(self.tab_2)
        self.checkBox_16.setObjectName(_fromUtf8("checkBox_16"))
        self.gridLayout_4.addWidget(self.checkBox_16, 1, 0, 1, 1)
        self.checkBox_15 = QtGui.QCheckBox(self.tab_2)
        self.checkBox_15.setObjectName(_fromUtf8("checkBox_15"))
        self.gridLayout_4.addWidget(self.checkBox_15, 0, 0, 1, 1)
        self.horizontalLayout_3.addLayout(self.gridLayout_4)
        self.tabWidget.addTab(self.tab_2, _fromUtf8(""))
        self.tab_3 = QtGui.QWidget()
        self.tab_3.setObjectName(_fromUtf8("tab_3"))
        self.horizontalLayout_4 = QtGui.QHBoxLayout(self.tab_3)
        self.horizontalLayout_4.setObjectName(_fromUtf8("horizontalLayout_4"))
        self.gridLayout_3 = QtGui.QGridLayout()
        self.gridLayout_3.setObjectName(_fromUtf8("gridLayout_3"))
        self.checkBox_4 = QtGui.QCheckBox(self.tab_3)
        self.checkBox_4.setObjectName(_fromUtf8("checkBox_4"))
        self.gridLayout_3.addWidget(self.checkBox_4, 0, 0, 1, 1)
        self.checkBox_5 = QtGui.QCheckBox(self.tab_3)
        self.checkBox_5.setObjectName(_fromUtf8("checkBox_5"))
        self.gridLayout_3.addWidget(self.checkBox_5, 1, 0, 1, 1)
        self.checkBox_6 = QtGui.QCheckBox(self.tab_3)
        self.checkBox_6.setObjectName(_fromUtf8("checkBox_6"))
        self.gridLayout_3.addWidget(self.checkBox_6, 2, 0, 1, 1)
        self.checkBox_7 = QtGui.QCheckBox(self.tab_3)
        self.checkBox_7.setObjectName(_fromUtf8("checkBox_7"))
        self.gridLayout_3.addWidget(self.checkBox_7, 3, 0, 1, 1)
        self.horizontalLayout_4.addLayout(self.gridLayout_3)
        self.tabWidget.addTab(self.tab_3, _fromUtf8(""))
        self.horizontalLayout.addWidget(self.tabWidget)

        self.retranslateUi(Dialog)
        self.tabWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(_translate("Dialog", "Dialog", None))
        self.checkBox.setText(_translate("Dialog", "Pizza $22", None))
        self.checkBox_3.setText(_translate("Dialog", "Hamburguesa de Pollo $4", None))
        self.checkBox_2.setText(_translate("Dialog", "Hot-Dog $3.50", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), _translate("Dialog", "Comida", None))
        self.checkBox_17.setText(_translate("Dialog", "Cerveza $2.50", None))
        self.checkBox_16.setText(_translate("Dialog", "Gaseosas $2", None))
        self.checkBox_15.setText(_translate("Dialog", "Agua $1.50", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), _translate("Dialog", "Bebidas", None))
        self.checkBox_4.setText(_translate("Dialog", "Vainilla $2", None))
        self.checkBox_5.setText(_translate("Dialog", "Frutilla $2.50", None))
        self.checkBox_6.setText(_translate("Dialog", "Piña $2.75", None))
        self.checkBox_7.setText(_translate("Dialog", "Chocolate $2.25", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_3), _translate("Dialog", "Helados", None))
