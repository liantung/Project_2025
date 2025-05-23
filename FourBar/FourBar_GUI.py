# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'FourBar_GUI.ui'
#
# Created by: PyQt5 UI code generator 5.15.7
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again. Do not edit this file unless you know what you are doing.

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(1723, 1408)
        self.verticalLayout = QtWidgets.QVBoxLayout(Form)
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.lbl_Zoom = QtWidgets.QLabel(Form)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lbl_Zoom.sizePolicy().hasHeightForWidth())
        self.lbl_Zoom.setSizePolicy(sizePolicy)
        self.lbl_Zoom.setMaximumSize(QtCore.QSize(50, 16777215))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.lbl_Zoom.setFont(font)
        self.lbl_Zoom.setObjectName("lbl_Zoom")
        self.horizontalLayout.addWidget(self.lbl_Zoom)
        self.spnd_Zoom = QtWidgets.QDoubleSpinBox(Form)
        self.spnd_Zoom.setMaximumSize(QtCore.QSize(75, 16777215))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.spnd_Zoom.setFont(font)
        self.spnd_Zoom.setProperty("value", 1.0)
        self.spnd_Zoom.setObjectName("spnd_Zoom")
        self.horizontalLayout.addWidget(self.spnd_Zoom)
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem)
        self.lbl_InputAngle = QtWidgets.QLabel(Form)
        self.lbl_InputAngle.setMaximumSize(QtCore.QSize(30, 16777215))
        font = QtGui.QFont()
        font.setFamily("Symbol")
        font.setPointSize(12)
        self.lbl_InputAngle.setFont(font)
        self.lbl_InputAngle.setObjectName("lbl_InputAngle")
        self.horizontalLayout.addWidget(self.lbl_InputAngle)
        self.nud_InputAngle = QtWidgets.QDoubleSpinBox(Form)
        self.nud_InputAngle.setMaximum(360.0)
        self.nud_InputAngle.setProperty("value", 90.0)
        self.nud_InputAngle.setObjectName("nud_InputAngle")
        self.horizontalLayout.addWidget(self.nud_InputAngle)
        self.lbl_OutputAngle = QtWidgets.QLabel(Form)
        self.lbl_OutputAngle.setMaximumSize(QtCore.QSize(30, 16777215))
        font = QtGui.QFont()
        font.setFamily("Symbol")
        font.setPointSize(12)
        self.lbl_OutputAngle.setFont(font)
        self.lbl_OutputAngle.setObjectName("lbl_OutputAngle")
        self.horizontalLayout.addWidget(self.lbl_OutputAngle)
        self.lbl_OutputAngle_Val = QtWidgets.QLabel(Form)
        self.lbl_OutputAngle_Val.setObjectName("lbl_OutputAngle_Val")
        self.horizontalLayout.addWidget(self.lbl_OutputAngle_Val)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.lbl_Link1Length = QtWidgets.QLabel(Form)
        self.lbl_Link1Length.setObjectName("lbl_Link1Length")
        self.horizontalLayout_4.addWidget(self.lbl_Link1Length)
        self.nud_Link1Length = QtWidgets.QDoubleSpinBox(Form)
        self.nud_Link1Length.setMaximum(5000.0)
        self.nud_Link1Length.setObjectName("nud_Link1Length")
        self.horizontalLayout_4.addWidget(self.nud_Link1Length)
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_4.addItem(spacerItem1)
        self.verticalLayout_2.addLayout(self.horizontalLayout_4)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.label_2 = QtWidgets.QLabel(Form)
        self.label_2.setFrameShadow(QtWidgets.QFrame.Plain)
        self.label_2.setObjectName("label_2")
        self.horizontalLayout_3.addWidget(self.label_2)
        self.nud_Link3Length = QtWidgets.QDoubleSpinBox(Form)
        self.nud_Link3Length.setMaximum(5000.0)
        self.nud_Link3Length.setObjectName("nud_Link3Length")
        self.horizontalLayout_3.addWidget(self.nud_Link3Length)
        spacerItem2 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem2)
        self.verticalLayout_2.addLayout(self.horizontalLayout_3)
        self.verticalLayout.addLayout(self.verticalLayout_2)
        self.gv_Main = QtWidgets.QGraphicsView(Form)
        self.gv_Main.setMouseTracking(True)
        self.gv_Main.setObjectName("gv_Main")
        self.verticalLayout.addWidget(self.gv_Main)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.lbl_Zoom.setText(_translate("Form", "Zoom"))
        self.lbl_InputAngle.setText(_translate("Form", "f1"))
        self.lbl_OutputAngle.setText(_translate("Form", "f3"))
        self.lbl_OutputAngle_Val.setText(_translate("Form", "0.00"))
        self.lbl_Link1Length.setText(_translate("Form", "Link 1 Length"))
        self.label_2.setText(_translate("Form", "Link 3 Length"))
