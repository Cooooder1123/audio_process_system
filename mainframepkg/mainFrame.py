# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'mainFrame.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.setEnabled(True)
        MainWindow.resize(1275, 818)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.progressBar = QtWidgets.QProgressBar(self.centralwidget)
        self.progressBar.setGeometry(QtCore.QRect(30, 340, 361, 23))
        self.progressBar.setProperty("value", 0)
        self.progressBar.setObjectName("progressBar")
        self.line = QtWidgets.QFrame(self.centralwidget)
        self.line.setGeometry(QtCore.QRect(420, -40, 20, 411))
        self.line.setFrameShape(QtWidgets.QFrame.VLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.plainTextEdit = QtWidgets.QPlainTextEdit(self.centralwidget)
        self.plainTextEdit.setEnabled(True)
        self.plainTextEdit.setGeometry(QtCore.QRect(30, 440, 871, 301))
        self.plainTextEdit.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOn)
        self.plainTextEdit.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOn)
        self.plainTextEdit.setReadOnly(True)
        self.plainTextEdit.setObjectName("plainTextEdit")
        self.label_13 = QtWidgets.QLabel(self.centralwidget)
        self.label_13.setGeometry(QtCore.QRect(450, 10, 81, 41))
        font = QtGui.QFont()
        font.setFamily("Adobe Devanagari")
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.label_13.setFont(font)
        self.label_13.setObjectName("label_13")
        self.label_15 = QtWidgets.QLabel(self.centralwidget)
        self.label_15.setGeometry(QtCore.QRect(950, 10, 81, 31))
        font = QtGui.QFont()
        font.setFamily("Adobe Devanagari")
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.label_15.setFont(font)
        self.label_15.setObjectName("label_15")
        self.label_14 = QtWidgets.QLabel(self.centralwidget)
        self.label_14.setGeometry(QtCore.QRect(30, 390, 81, 41))
        font = QtGui.QFont()
        font.setFamily("Adobe Devanagari")
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.label_14.setFont(font)
        self.label_14.setObjectName("label_14")
        self.layoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.layoutWidget.setGeometry(QtCore.QRect(30, 20, 361, 301))
        self.layoutWidget.setObjectName("layoutWidget")
        self.gridLayout = QtWidgets.QGridLayout(self.layoutWidget)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setObjectName("gridLayout")
        self.lineEdit_2 = QtWidgets.QLineEdit(self.layoutWidget)
        self.lineEdit_2.setEnabled(False)
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.gridLayout.addWidget(self.lineEdit_2, 1, 1, 1, 1)
        self.label_5 = QtWidgets.QLabel(self.layoutWidget)
        self.label_5.setObjectName("label_5")
        self.gridLayout.addWidget(self.label_5, 4, 0, 1, 1)
        self.lineEdit_5 = QtWidgets.QLineEdit(self.layoutWidget)
        self.lineEdit_5.setEnabled(False)
        self.lineEdit_5.setObjectName("lineEdit_5")
        self.gridLayout.addWidget(self.lineEdit_5, 4, 1, 1, 1)
        self.label_2 = QtWidgets.QLabel(self.layoutWidget)
        self.label_2.setObjectName("label_2")
        self.gridLayout.addWidget(self.label_2, 1, 0, 1, 1)
        self.label_4 = QtWidgets.QLabel(self.layoutWidget)
        self.label_4.setObjectName("label_4")
        self.gridLayout.addWidget(self.label_4, 3, 0, 1, 1)
        self.lineEdit_3 = QtWidgets.QLineEdit(self.layoutWidget)
        self.lineEdit_3.setEnabled(False)
        self.lineEdit_3.setObjectName("lineEdit_3")
        self.gridLayout.addWidget(self.lineEdit_3, 2, 1, 1, 1)
        self.lineEdit_4 = QtWidgets.QLineEdit(self.layoutWidget)
        self.lineEdit_4.setEnabled(False)
        self.lineEdit_4.setObjectName("lineEdit_4")
        self.gridLayout.addWidget(self.lineEdit_4, 3, 1, 1, 1)
        self.lineEdit = QtWidgets.QLineEdit(self.layoutWidget)
        self.lineEdit.setEnabled(False)
        self.lineEdit.setObjectName("lineEdit")
        self.gridLayout.addWidget(self.lineEdit, 0, 1, 1, 1)
        self.label_3 = QtWidgets.QLabel(self.layoutWidget)
        self.label_3.setObjectName("label_3")
        self.gridLayout.addWidget(self.label_3, 2, 0, 1, 1)
        self.label = QtWidgets.QLabel(self.layoutWidget)
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 0, 0, 1, 1)
        self.layoutWidget1 = QtWidgets.QWidget(self.centralwidget)
        self.layoutWidget1.setGeometry(QtCore.QRect(450, 50, 451, 321))
        self.layoutWidget1.setObjectName("layoutWidget1")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.layoutWidget1)
        self.gridLayout_2.setSizeConstraint(QtWidgets.QLayout.SetDefaultConstraint)
        self.gridLayout_2.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_2.setSpacing(7)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.textEdit_2 = QtWidgets.QTextEdit(self.layoutWidget1)
        self.textEdit_2.setEnabled(True)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.textEdit_2.sizePolicy().hasHeightForWidth())
        self.textEdit_2.setSizePolicy(sizePolicy)
        self.textEdit_2.setMaximumSize(QtCore.QSize(500, 70))
        self.textEdit_2.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOn)
        self.textEdit_2.setReadOnly(True)
        self.textEdit_2.setObjectName("textEdit_2")
        self.gridLayout_2.addWidget(self.textEdit_2, 5, 1, 1, 1)
        self.label_8 = QtWidgets.QLabel(self.layoutWidget1)
        self.label_8.setObjectName("label_8")
        self.gridLayout_2.addWidget(self.label_8, 4, 0, 1, 1)
        self.label_6 = QtWidgets.QLabel(self.layoutWidget1)
        self.label_6.setObjectName("label_6")
        self.gridLayout_2.addWidget(self.label_6, 1, 0, 1, 1)
        self.label_9 = QtWidgets.QLabel(self.layoutWidget1)
        self.label_9.setObjectName("label_9")
        self.gridLayout_2.addWidget(self.label_9, 3, 0, 1, 1)
        self.lineEdit_6 = QtWidgets.QLineEdit(self.layoutWidget1)
        self.lineEdit_6.setEnabled(False)
        self.lineEdit_6.setObjectName("lineEdit_6")
        self.gridLayout_2.addWidget(self.lineEdit_6, 1, 1, 1, 1)
        self.label_7 = QtWidgets.QLabel(self.layoutWidget1)
        self.label_7.setObjectName("label_7")
        self.gridLayout_2.addWidget(self.label_7, 6, 0, 1, 1)
        self.lineEdit_9 = QtWidgets.QLineEdit(self.layoutWidget1)
        self.lineEdit_9.setEnabled(False)
        self.lineEdit_9.setObjectName("lineEdit_9")
        self.gridLayout_2.addWidget(self.lineEdit_9, 3, 1, 1, 1)
        self.label_16 = QtWidgets.QLabel(self.layoutWidget1)
        self.label_16.setObjectName("label_16")
        self.gridLayout_2.addWidget(self.label_16, 5, 0, 1, 1)
        self.label_17 = QtWidgets.QLabel(self.layoutWidget1)
        self.label_17.setObjectName("label_17")
        self.gridLayout_2.addWidget(self.label_17, 0, 0, 1, 1)
        self.lineEdit_11 = QtWidgets.QLineEdit(self.layoutWidget1)
        self.lineEdit_11.setEnabled(False)
        self.lineEdit_11.setObjectName("lineEdit_11")
        self.gridLayout_2.addWidget(self.lineEdit_11, 0, 1, 1, 1)
        self.textEdit = QtWidgets.QTextEdit(self.layoutWidget1)
        self.textEdit.setEnabled(True)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.textEdit.sizePolicy().hasHeightForWidth())
        self.textEdit.setSizePolicy(sizePolicy)
        self.textEdit.setMaximumSize(QtCore.QSize(500, 70))
        self.textEdit.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOn)
        self.textEdit.setReadOnly(True)
        self.textEdit.setObjectName("textEdit")
        self.gridLayout_2.addWidget(self.textEdit, 6, 1, 1, 1)
        self.textEdit_3 = QtWidgets.QTextEdit(self.layoutWidget1)
        self.textEdit_3.setEnabled(False)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.textEdit_3.sizePolicy().hasHeightForWidth())
        self.textEdit_3.setSizePolicy(sizePolicy)
        self.textEdit_3.setMaximumSize(QtCore.QSize(500, 50))
        self.textEdit_3.setObjectName("textEdit_3")
        self.gridLayout_2.addWidget(self.textEdit_3, 4, 1, 1, 1)
        self.layoutWidget2 = QtWidgets.QWidget(self.centralwidget)
        self.layoutWidget2.setGeometry(QtCore.QRect(950, 50, 291, 301))
        self.layoutWidget2.setObjectName("layoutWidget2")
        self.gridLayout_3 = QtWidgets.QGridLayout(self.layoutWidget2)
        self.gridLayout_3.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.textEdit_5 = QtWidgets.QTextEdit(self.layoutWidget2)
        self.textEdit_5.setEnabled(False)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.textEdit_5.sizePolicy().hasHeightForWidth())
        self.textEdit_5.setSizePolicy(sizePolicy)
        self.textEdit_5.setMaximumSize(QtCore.QSize(100, 50))
        self.textEdit_5.setObjectName("textEdit_5")
        self.gridLayout_3.addWidget(self.textEdit_5, 1, 1, 1, 1)
        self.label_11 = QtWidgets.QLabel(self.layoutWidget2)
        self.label_11.setObjectName("label_11")
        self.gridLayout_3.addWidget(self.label_11, 1, 0, 1, 1)
        self.label_12 = QtWidgets.QLabel(self.layoutWidget2)
        self.label_12.setObjectName("label_12")
        self.gridLayout_3.addWidget(self.label_12, 2, 0, 1, 1)
        self.label_10 = QtWidgets.QLabel(self.layoutWidget2)
        self.label_10.setObjectName("label_10")
        self.gridLayout_3.addWidget(self.label_10, 0, 0, 1, 1)
        self.textEdit_8 = QtWidgets.QTextEdit(self.layoutWidget2)
        self.textEdit_8.setEnabled(False)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.textEdit_8.sizePolicy().hasHeightForWidth())
        self.textEdit_8.setSizePolicy(sizePolicy)
        self.textEdit_8.setMaximumSize(QtCore.QSize(300, 50))
        self.textEdit_8.setObjectName("textEdit_8")
        self.gridLayout_3.addWidget(self.textEdit_8, 1, 2, 1, 1)
        self.textEdit_6 = QtWidgets.QTextEdit(self.layoutWidget2)
        self.textEdit_6.setEnabled(False)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.textEdit_6.sizePolicy().hasHeightForWidth())
        self.textEdit_6.setSizePolicy(sizePolicy)
        self.textEdit_6.setMaximumSize(QtCore.QSize(100, 50))
        self.textEdit_6.setObjectName("textEdit_6")
        self.gridLayout_3.addWidget(self.textEdit_6, 2, 1, 1, 1)
        self.textEdit_9 = QtWidgets.QTextEdit(self.layoutWidget2)
        self.textEdit_9.setEnabled(False)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.textEdit_9.sizePolicy().hasHeightForWidth())
        self.textEdit_9.setSizePolicy(sizePolicy)
        self.textEdit_9.setMaximumSize(QtCore.QSize(300, 50))
        self.textEdit_9.setObjectName("textEdit_9")
        self.gridLayout_3.addWidget(self.textEdit_9, 2, 2, 1, 1)
        self.textEdit_7 = QtWidgets.QTextEdit(self.layoutWidget2)
        self.textEdit_7.setEnabled(False)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.textEdit_7.sizePolicy().hasHeightForWidth())
        self.textEdit_7.setSizePolicy(sizePolicy)
        self.textEdit_7.setMaximumSize(QtCore.QSize(300, 50))
        self.textEdit_7.setObjectName("textEdit_7")
        self.gridLayout_3.addWidget(self.textEdit_7, 0, 2, 1, 1)
        self.textEdit_4 = QtWidgets.QTextEdit(self.layoutWidget2)
        self.textEdit_4.setEnabled(False)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.textEdit_4.sizePolicy().hasHeightForWidth())
        self.textEdit_4.setSizePolicy(sizePolicy)
        self.textEdit_4.setMaximumSize(QtCore.QSize(100, 50))
        self.textEdit_4.setObjectName("textEdit_4")
        self.gridLayout_3.addWidget(self.textEdit_4, 0, 1, 1, 1)
        self.label_18 = QtWidgets.QLabel(self.layoutWidget2)
        self.label_18.setObjectName("label_18")
        self.gridLayout_3.addWidget(self.label_18, 3, 0, 1, 1)
        self.textEdit_10 = QtWidgets.QTextEdit(self.layoutWidget2)
        self.textEdit_10.setEnabled(False)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.textEdit_10.sizePolicy().hasHeightForWidth())
        self.textEdit_10.setSizePolicy(sizePolicy)
        self.textEdit_10.setMaximumSize(QtCore.QSize(300, 50))
        self.textEdit_10.setObjectName("textEdit_10")
        self.gridLayout_3.addWidget(self.textEdit_10, 3, 2, 1, 1)
        self.textEdit_11 = QtWidgets.QTextEdit(self.layoutWidget2)
        self.textEdit_11.setEnabled(False)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.textEdit_11.sizePolicy().hasHeightForWidth())
        self.textEdit_11.setSizePolicy(sizePolicy)
        self.textEdit_11.setMaximumSize(QtCore.QSize(100, 50))
        self.textEdit_11.setObjectName("textEdit_11")
        self.gridLayout_3.addWidget(self.textEdit_11, 3, 1, 1, 1)
        self.label_19 = QtWidgets.QLabel(self.layoutWidget2)
        self.label_19.setObjectName("label_19")
        self.gridLayout_3.addWidget(self.label_19, 4, 0, 1, 1)
        self.textEdit_13 = QtWidgets.QTextEdit(self.layoutWidget2)
        self.textEdit_13.setEnabled(False)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.textEdit_13.sizePolicy().hasHeightForWidth())
        self.textEdit_13.setSizePolicy(sizePolicy)
        self.textEdit_13.setMaximumSize(QtCore.QSize(100, 50))
        self.textEdit_13.setObjectName("textEdit_13")
        self.gridLayout_3.addWidget(self.textEdit_13, 4, 1, 1, 1)
        self.textEdit_12 = QtWidgets.QTextEdit(self.layoutWidget2)
        self.textEdit_12.setEnabled(False)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.textEdit_12.sizePolicy().hasHeightForWidth())
        self.textEdit_12.setSizePolicy(sizePolicy)
        self.textEdit_12.setMaximumSize(QtCore.QSize(300, 50))
        self.textEdit_12.setObjectName("textEdit_12")
        self.gridLayout_3.addWidget(self.textEdit_12, 4, 2, 1, 1)
        self.layoutWidget_2 = QtWidgets.QWidget(self.centralwidget)
        self.layoutWidget_2.setGeometry(QtCore.QRect(950, 370, 291, 301))
        self.layoutWidget_2.setObjectName("layoutWidget_2")
        self.gridLayout_4 = QtWidgets.QGridLayout(self.layoutWidget_2)
        self.gridLayout_4.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_4.setObjectName("gridLayout_4")
        self.textEdit_14 = QtWidgets.QTextEdit(self.layoutWidget_2)
        self.textEdit_14.setEnabled(False)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.textEdit_14.sizePolicy().hasHeightForWidth())
        self.textEdit_14.setSizePolicy(sizePolicy)
        self.textEdit_14.setMaximumSize(QtCore.QSize(100, 50))
        self.textEdit_14.setObjectName("textEdit_14")
        self.gridLayout_4.addWidget(self.textEdit_14, 1, 1, 1, 1)
        self.label_20 = QtWidgets.QLabel(self.layoutWidget_2)
        self.label_20.setObjectName("label_20")
        self.gridLayout_4.addWidget(self.label_20, 1, 0, 1, 1)
        self.label_21 = QtWidgets.QLabel(self.layoutWidget_2)
        self.label_21.setObjectName("label_21")
        self.gridLayout_4.addWidget(self.label_21, 2, 0, 1, 1)
        self.label_22 = QtWidgets.QLabel(self.layoutWidget_2)
        self.label_22.setObjectName("label_22")
        self.gridLayout_4.addWidget(self.label_22, 0, 0, 1, 1)
        self.textEdit_15 = QtWidgets.QTextEdit(self.layoutWidget_2)
        self.textEdit_15.setEnabled(False)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.textEdit_15.sizePolicy().hasHeightForWidth())
        self.textEdit_15.setSizePolicy(sizePolicy)
        self.textEdit_15.setMaximumSize(QtCore.QSize(300, 50))
        self.textEdit_15.setObjectName("textEdit_15")
        self.gridLayout_4.addWidget(self.textEdit_15, 1, 2, 1, 1)
        self.textEdit_16 = QtWidgets.QTextEdit(self.layoutWidget_2)
        self.textEdit_16.setEnabled(False)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.textEdit_16.sizePolicy().hasHeightForWidth())
        self.textEdit_16.setSizePolicy(sizePolicy)
        self.textEdit_16.setMaximumSize(QtCore.QSize(100, 50))
        self.textEdit_16.setObjectName("textEdit_16")
        self.gridLayout_4.addWidget(self.textEdit_16, 2, 1, 1, 1)
        self.textEdit_17 = QtWidgets.QTextEdit(self.layoutWidget_2)
        self.textEdit_17.setEnabled(False)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.textEdit_17.sizePolicy().hasHeightForWidth())
        self.textEdit_17.setSizePolicy(sizePolicy)
        self.textEdit_17.setMaximumSize(QtCore.QSize(300, 50))
        self.textEdit_17.setObjectName("textEdit_17")
        self.gridLayout_4.addWidget(self.textEdit_17, 2, 2, 1, 1)
        self.textEdit_18 = QtWidgets.QTextEdit(self.layoutWidget_2)
        self.textEdit_18.setEnabled(False)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.textEdit_18.sizePolicy().hasHeightForWidth())
        self.textEdit_18.setSizePolicy(sizePolicy)
        self.textEdit_18.setMaximumSize(QtCore.QSize(300, 50))
        self.textEdit_18.setObjectName("textEdit_18")
        self.gridLayout_4.addWidget(self.textEdit_18, 0, 2, 1, 1)
        self.textEdit_19 = QtWidgets.QTextEdit(self.layoutWidget_2)
        self.textEdit_19.setEnabled(False)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.textEdit_19.sizePolicy().hasHeightForWidth())
        self.textEdit_19.setSizePolicy(sizePolicy)
        self.textEdit_19.setMaximumSize(QtCore.QSize(100, 50))
        self.textEdit_19.setObjectName("textEdit_19")
        self.gridLayout_4.addWidget(self.textEdit_19, 0, 1, 1, 1)
        self.label_23 = QtWidgets.QLabel(self.layoutWidget_2)
        self.label_23.setObjectName("label_23")
        self.gridLayout_4.addWidget(self.label_23, 3, 0, 1, 1)
        self.textEdit_20 = QtWidgets.QTextEdit(self.layoutWidget_2)
        self.textEdit_20.setEnabled(False)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.textEdit_20.sizePolicy().hasHeightForWidth())
        self.textEdit_20.setSizePolicy(sizePolicy)
        self.textEdit_20.setMaximumSize(QtCore.QSize(300, 50))
        self.textEdit_20.setObjectName("textEdit_20")
        self.gridLayout_4.addWidget(self.textEdit_20, 3, 2, 1, 1)
        self.textEdit_21 = QtWidgets.QTextEdit(self.layoutWidget_2)
        self.textEdit_21.setEnabled(False)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.textEdit_21.sizePolicy().hasHeightForWidth())
        self.textEdit_21.setSizePolicy(sizePolicy)
        self.textEdit_21.setMaximumSize(QtCore.QSize(100, 50))
        self.textEdit_21.setObjectName("textEdit_21")
        self.gridLayout_4.addWidget(self.textEdit_21, 3, 1, 1, 1)
        self.label_24 = QtWidgets.QLabel(self.layoutWidget_2)
        self.label_24.setObjectName("label_24")
        self.gridLayout_4.addWidget(self.label_24, 4, 0, 1, 1)
        self.textEdit_22 = QtWidgets.QTextEdit(self.layoutWidget_2)
        self.textEdit_22.setEnabled(False)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.textEdit_22.sizePolicy().hasHeightForWidth())
        self.textEdit_22.setSizePolicy(sizePolicy)
        self.textEdit_22.setMaximumSize(QtCore.QSize(100, 50))
        self.textEdit_22.setObjectName("textEdit_22")
        self.gridLayout_4.addWidget(self.textEdit_22, 4, 1, 1, 1)
        self.textEdit_23 = QtWidgets.QTextEdit(self.layoutWidget_2)
        self.textEdit_23.setEnabled(False)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.textEdit_23.sizePolicy().hasHeightForWidth())
        self.textEdit_23.setSizePolicy(sizePolicy)
        self.textEdit_23.setMaximumSize(QtCore.QSize(300, 50))
        self.textEdit_23.setObjectName("textEdit_23")
        self.gridLayout_4.addWidget(self.textEdit_23, 4, 2, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1275, 26))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label_13.setText(_translate("MainWindow", "系统监控"))
        self.label_15.setText(_translate("MainWindow", "线程监控"))
        self.label_14.setText(_translate("MainWindow", "系统监控"))
        self.label_5.setText(_translate("MainWindow", "剩余时长："))
        self.label_2.setText(_translate("MainWindow", "音频文件个数："))
        self.label_4.setText(_translate("MainWindow", "处理效率："))
        self.label_3.setText(_translate("MainWindow", "已处理数量："))
        self.label.setText(_translate("MainWindow", "当前打开文件："))
        self.label_8.setText(_translate("MainWindow", "磁盘使用情况:"))
        self.label_6.setText(_translate("MainWindow", "CPU使用情况:"))
        self.label_9.setText(_translate("MainWindow", "网络情况:"))
        self.label_7.setText(_translate("MainWindow", "GPU使用情况:"))
        self.label_16.setText(_translate("MainWindow", "温度:"))
        self.label_17.setText(_translate("MainWindow", "当前时间:"))
        self.label_11.setText(_translate("MainWindow", "线程二:"))
        self.label_12.setText(_translate("MainWindow", "线程三:"))
        self.label_10.setText(_translate("MainWindow", "线程一:"))
        self.label_18.setText(_translate("MainWindow", "线程四:"))
        self.label_19.setText(_translate("MainWindow", "线程五:"))
        self.label_20.setText(_translate("MainWindow", "线程七:"))
        self.label_21.setText(_translate("MainWindow", "线程八:"))
        self.label_22.setText(_translate("MainWindow", "线程六:"))
        self.label_23.setText(_translate("MainWindow", "线程九:"))
        self.label_24.setText(_translate("MainWindow", "线程十:"))

