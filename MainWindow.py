# Form implementation generated from reading ui file 'D:\KTLT_NGUYENVONHUNGOC_EXERCISE\MODULE2\Exercise33\MainWindow.ui'
#
# Created by: PyQt6 UI code generator 6.7.1
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(425, 366)
        self.centralwidget = QtWidgets.QWidget(parent=MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(parent=self.centralwidget)
        self.label.setGeometry(QtCore.QRect(10, 0, 311, 31))
        font = QtGui.QFont()
        font.setPointSize(13)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.lineEditOriginialArray = QtWidgets.QLineEdit(parent=self.centralwidget)
        self.lineEditOriginialArray.setGeometry(QtCore.QRect(10, 40, 401, 21))
        self.lineEditOriginialArray.setObjectName("lineEditOriginialArray")
        self.label_2 = QtWidgets.QLabel(parent=self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(10, 80, 311, 31))
        font = QtGui.QFont()
        font.setPointSize(13)
        font.setBold(True)
        font.setWeight(75)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.lineEditResult = QtWidgets.QLineEdit(parent=self.centralwidget)
        self.lineEditResult.setGeometry(QtCore.QRect(10, 120, 401, 21))
        self.lineEditResult.setObjectName("lineEditResult")
        self.pushButtonRandomArray = QtWidgets.QPushButton(parent=self.centralwidget)
        self.pushButtonRandomArray.setGeometry(QtCore.QRect(20, 160, 181, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.pushButtonRandomArray.setFont(font)
        self.pushButtonRandomArray.setStyleSheet("background-color: rgb(221, 221, 221);")
        self.pushButtonRandomArray.setObjectName("pushButtonRandomArray")
        self.pushButtonSumofArray = QtWidgets.QPushButton(parent=self.centralwidget)
        self.pushButtonSumofArray.setGeometry(QtCore.QRect(20, 200, 181, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.pushButtonSumofArray.setFont(font)
        self.pushButtonSumofArray.setStyleSheet("background-color: rgb(221, 221, 221);")
        self.pushButtonSumofArray.setObjectName("pushButtonSumofArray")
        self.pushButtonCountoddelement = QtWidgets.QPushButton(parent=self.centralwidget)
        self.pushButtonCountoddelement.setGeometry(QtCore.QRect(20, 240, 181, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.pushButtonCountoddelement.setFont(font)
        self.pushButtonCountoddelement.setStyleSheet("background-color: rgb(221, 221, 221);")
        self.pushButtonCountoddelement.setObjectName("pushButtonCountoddelement")
        self.pushButtonSumofelement = QtWidgets.QPushButton(parent=self.centralwidget)
        self.pushButtonSumofelement.setGeometry(QtCore.QRect(20, 280, 181, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.pushButtonSumofelement.setFont(font)
        self.pushButtonSumofelement.setStyleSheet("background-color: rgb(221, 221, 221);")
        self.pushButtonSumofelement.setObjectName("pushButtonSumofelement")
        self.pushButtonSortDescending = QtWidgets.QPushButton(parent=self.centralwidget)
        self.pushButtonSortDescending.setGeometry(QtCore.QRect(220, 280, 181, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.pushButtonSortDescending.setFont(font)
        self.pushButtonSortDescending.setStyleSheet("background-color: rgb(221, 221, 221);")
        self.pushButtonSortDescending.setObjectName("pushButtonSortDescending")
        self.pushButtonSortAscending = QtWidgets.QPushButton(parent=self.centralwidget)
        self.pushButtonSortAscending.setGeometry(QtCore.QRect(220, 240, 181, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.pushButtonSortAscending.setFont(font)
        self.pushButtonSortAscending.setStyleSheet("background-color: rgb(221, 221, 221);")
        self.pushButtonSortAscending.setObjectName("pushButtonSortAscending")
        self.pushButtonFindsmallestelement = QtWidgets.QPushButton(parent=self.centralwidget)
        self.pushButtonFindsmallestelement.setGeometry(QtCore.QRect(220, 160, 181, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.pushButtonFindsmallestelement.setFont(font)
        self.pushButtonFindsmallestelement.setStyleSheet("background-color: rgb(221, 221, 221);")
        self.pushButtonFindsmallestelement.setObjectName("pushButtonFindsmallestelement")
        self.pushButtonIncrementdoublevalue = QtWidgets.QPushButton(parent=self.centralwidget)
        self.pushButtonIncrementdoublevalue.setGeometry(QtCore.QRect(220, 200, 181, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.pushButtonIncrementdoublevalue.setFont(font)
        self.pushButtonIncrementdoublevalue.setStyleSheet("background-color: rgb(221, 221, 221);")
        self.pushButtonIncrementdoublevalue.setObjectName("pushButtonIncrementdoublevalue")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(parent=MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 425, 18))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(parent=MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label.setText(_translate("MainWindow", "Originial Array:"))
        self.label_2.setText(_translate("MainWindow", "Result:"))
        self.pushButtonRandomArray.setText(_translate("MainWindow", "Random Array"))
        self.pushButtonSumofArray.setText(_translate("MainWindow", "Sum of Array"))
        self.pushButtonCountoddelement.setText(_translate("MainWindow", "Count odd element"))
        self.pushButtonSumofelement.setText(_translate("MainWindow", "Sum of odd element"))
        self.pushButtonSortDescending.setText(_translate("MainWindow", "Sort - Descending"))
        self.pushButtonSortAscending.setText(_translate("MainWindow", "Sort - Ascending"))
        self.pushButtonFindsmallestelement.setText(_translate("MainWindow", "Find smallest element"))
        self.pushButtonIncrementdoublevalue.setText(_translate("MainWindow", "Increment double value"))
