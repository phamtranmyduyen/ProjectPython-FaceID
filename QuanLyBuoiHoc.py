# Form implementation generated from reading ui file 'QuanLyBuoiHoc.ui'
#
# Created by: PyQt6 UI code generator 6.4.2
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 530)
        self.centralwidget = QtWidgets.QWidget(parent=MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.frmHeader = QtWidgets.QFrame(parent=self.centralwidget)
        self.frmHeader.setGeometry(QtCore.QRect(1, 31, 851, 51))
        self.frmHeader.setAccessibleName("")
        self.frmHeader.setLayoutDirection(QtCore.Qt.LayoutDirection.LeftToRight)
        self.frmHeader.setStyleSheet("#frmHeader{background-color:qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(69, 127, 202, 255), stop:1 rgba(86, 145, 200, 255))}\n"
"")
        self.frmHeader.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.frmHeader.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.frmHeader.setLineWidth(1)
        self.frmHeader.setObjectName("frmHeader")
        self.label_3 = QtWidgets.QLabel(parent=self.frmHeader)
        self.label_3.setGeometry(QtCore.QRect(0, 0, 801, 51))
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.label_3.setFont(font)
        self.label_3.setStyleSheet("#label_3\n"
"{\n"
"    font-weight:bold;\n"
"}")
        self.label_3.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.label_3.setObjectName("label_3")
        self.btnBack = QtWidgets.QPushButton(parent=self.frmHeader)
        self.btnBack.setGeometry(QtCore.QRect(730, 12, 61, 23))
        self.btnBack.setCursor(QtGui.QCursor(QtCore.Qt.CursorShape.PointingHandCursor))
        self.btnBack.setObjectName("btnBack")
        self.label_2 = QtWidgets.QLabel(parent=self.frmHeader)
        self.label_2.setGeometry(QtCore.QRect(50, 10, 91, 16))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setStyleStrategy(QtGui.QFont.StyleStrategy.NoAntialias)
        self.label_2.setFont(font)
        self.label_2.setAcceptDrops(False)
        self.label_2.setToolTip("")
        self.label_2.setAutoFillBackground(False)
        self.label_2.setFrameShape(QtWidgets.QFrame.Shape.NoFrame)
        self.label_2.setFrameShadow(QtWidgets.QFrame.Shadow.Plain)
        self.label_2.setTextFormat(QtCore.Qt.TextFormat.AutoText)
        self.label_2.setScaledContents(False)
        self.label_2.setWordWrap(False)
        self.label_2.setIndent(-1)
        self.label_2.setTextInteractionFlags(QtCore.Qt.TextInteractionFlag.LinksAccessibleByMouse)
        self.label_2.setObjectName("label_2")
        self.label_4 = QtWidgets.QLabel(parent=self.frmHeader)
        self.label_4.setGeometry(QtCore.QRect(50, 30, 91, 16))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        self.btnDark = QtWidgets.QPushButton(parent=self.frmHeader)
        self.btnDark.setGeometry(QtCore.QRect(680, 8, 31, 31))
        self.btnDark.setCursor(QtGui.QCursor(QtCore.Qt.CursorShape.PointingHandCursor))
        self.btnDark.setText("")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("image/icon/moon_symbol_50px.png"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        self.btnDark.setIcon(icon)
        self.btnDark.setIconSize(QtCore.QSize(20, 20))
        self.btnDark.setObjectName("btnDark")
        self.btnTime = QtWidgets.QPushButton(parent=self.frmHeader)
        self.btnTime.setGeometry(QtCore.QRect(10, 10, 31, 31))
        self.btnTime.setCursor(QtGui.QCursor(QtCore.Qt.CursorShape.PointingHandCursor))
        self.btnTime.setStyleSheet("#btnTime\n"
"{\n"
"background-color: transparent;\n"
"}")
        self.btnTime.setText("")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("image/icon/time_50px.png"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        self.btnTime.setIcon(icon1)
        self.btnTime.setIconSize(QtCore.QSize(20, 20))
        self.btnTime.setObjectName("btnTime")
        self.label_3.raise_()
        self.btnBack.raise_()
        self.label_4.raise_()
        self.label_2.raise_()
        self.btnDark.raise_()
        self.btnTime.raise_()
        self.frmChangeBuoiHoc = QtWidgets.QFrame(parent=self.centralwidget)
        self.frmChangeBuoiHoc.setGeometry(QtCore.QRect(20, 100, 231, 411))
        self.frmChangeBuoiHoc.setStyleSheet("#frmChangeBuoiHoc\n"
"{\n"
"    border-width: 2;\n"
"    border-radius: 5;\n"
"     border-style: solid;\n"
"      border-color: #457fca;\n"
"}")
        self.frmChangeBuoiHoc.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.frmChangeBuoiHoc.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.frmChangeBuoiHoc.setObjectName("frmChangeBuoiHoc")
        self.label_5 = QtWidgets.QLabel(parent=self.frmChangeBuoiHoc)
        self.label_5.setGeometry(QtCore.QRect(0, 10, 231, 21))
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.label_5.setFont(font)
        self.label_5.setStyleSheet("#label_5\n"
"{\n"
"    font-weight:bold;\n"
"}")
        self.label_5.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.label_5.setObjectName("label_5")
        self.label_10 = QtWidgets.QLabel(parent=self.frmChangeBuoiHoc)
        self.label_10.setGeometry(QtCore.QRect(20, 60, 71, 21))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.label_10.setFont(font)
        self.label_10.setAlignment(QtCore.Qt.AlignmentFlag.AlignBottom|QtCore.Qt.AlignmentFlag.AlignLeading|QtCore.Qt.AlignmentFlag.AlignLeft)
        self.label_10.setObjectName("label_10")
        self.lineEdit_2 = QtWidgets.QLineEdit(parent=self.frmChangeBuoiHoc)
        self.lineEdit_2.setGeometry(QtCore.QRect(90, 60, 121, 21))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.lineEdit_2.setFont(font)
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.label_11 = QtWidgets.QLabel(parent=self.frmChangeBuoiHoc)
        self.label_11.setGeometry(QtCore.QRect(20, 100, 71, 21))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.label_11.setFont(font)
        self.label_11.setAlignment(QtCore.Qt.AlignmentFlag.AlignBottom|QtCore.Qt.AlignmentFlag.AlignLeading|QtCore.Qt.AlignmentFlag.AlignLeft)
        self.label_11.setObjectName("label_11")
        self.timeEdit = QtWidgets.QTimeEdit(parent=self.frmChangeBuoiHoc)
        self.timeEdit.setGeometry(QtCore.QRect(90, 100, 121, 22))
        self.timeEdit.setObjectName("timeEdit")
        self.label_12 = QtWidgets.QLabel(parent=self.frmChangeBuoiHoc)
        self.label_12.setGeometry(QtCore.QRect(20, 140, 71, 16))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.label_12.setFont(font)
        self.label_12.setAlignment(QtCore.Qt.AlignmentFlag.AlignBottom|QtCore.Qt.AlignmentFlag.AlignLeading|QtCore.Qt.AlignmentFlag.AlignLeft)
        self.label_12.setObjectName("label_12")
        self.timeEdit_2 = QtWidgets.QTimeEdit(parent=self.frmChangeBuoiHoc)
        self.timeEdit_2.setGeometry(QtCore.QRect(90, 140, 121, 22))
        self.timeEdit_2.setObjectName("timeEdit_2")
        self.label_13 = QtWidgets.QLabel(parent=self.frmChangeBuoiHoc)
        self.label_13.setGeometry(QtCore.QRect(20, 180, 71, 21))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.label_13.setFont(font)
        self.label_13.setAlignment(QtCore.Qt.AlignmentFlag.AlignBottom|QtCore.Qt.AlignmentFlag.AlignLeading|QtCore.Qt.AlignmentFlag.AlignLeft)
        self.label_13.setObjectName("label_13")
        self.dateEdit = QtWidgets.QDateEdit(parent=self.frmChangeBuoiHoc)
        self.dateEdit.setGeometry(QtCore.QRect(90, 180, 121, 22))
        self.dateEdit.setObjectName("dateEdit")
        self.label_14 = QtWidgets.QLabel(parent=self.frmChangeBuoiHoc)
        self.label_14.setGeometry(QtCore.QRect(20, 220, 71, 21))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.label_14.setFont(font)
        self.label_14.setAlignment(QtCore.Qt.AlignmentFlag.AlignBottom|QtCore.Qt.AlignmentFlag.AlignLeading|QtCore.Qt.AlignmentFlag.AlignLeft)
        self.label_14.setObjectName("label_14")
        self.comboBox = QtWidgets.QComboBox(parent=self.frmChangeBuoiHoc)
        self.comboBox.setGeometry(QtCore.QRect(90, 220, 121, 22))
        self.comboBox.setObjectName("comboBox")
        self.comboBox.addItem("")
        self.horizontalLayoutWidget = QtWidgets.QWidget(parent=self.frmChangeBuoiHoc)
        self.horizontalLayoutWidget.setGeometry(QtCore.QRect(29, 280, 171, 51))
        self.horizontalLayoutWidget.setObjectName("horizontalLayoutWidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setSpacing(10)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.pushButton_2 = QtWidgets.QPushButton(parent=self.horizontalLayoutWidget)
        self.pushButton_2.setCursor(QtGui.QCursor(QtCore.Qt.CursorShape.PointingHandCursor))
        self.pushButton_2.setStyleSheet("#pushButton_2{\n"
"background-color:qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(69, 127, 202, 255), stop:1 rgba(86, 145, 200, 255));\n"
"color:white;\n"
"font-weight:bold;\n"
"border-radius:3px;\n"
"padding: 5px;\n"
"}\n"
"#pushButton_2:hover{\n"
"background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(107, 149, 202, 255), stop:1 rgba(86, 145, 200, 255));\n"
"}")
        self.pushButton_2.setObjectName("pushButton_2")
        self.horizontalLayout.addWidget(self.pushButton_2)
        self.pushButton = QtWidgets.QPushButton(parent=self.horizontalLayoutWidget)
        self.pushButton.setCursor(QtGui.QCursor(QtCore.Qt.CursorShape.PointingHandCursor))
        self.pushButton.setStyleSheet("#pushButton{\n"
"background-color:qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(69, 127, 202, 255), stop:1 rgba(86, 145, 200, 255));\n"
"color:white;\n"
"font-weight:bold;\n"
"border-radius:3px;\n"
"padding: 5px;\n"
"}\n"
"#pushButton:hover{\n"
"background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(107, 149, 202, 255), stop:1 rgba(86, 145, 200, 255));\n"
"}")
        self.pushButton.setObjectName("pushButton")
        self.horizontalLayout.addWidget(self.pushButton)
        self.horizontalLayoutWidget_2 = QtWidgets.QWidget(parent=self.frmChangeBuoiHoc)
        self.horizontalLayoutWidget_2.setGeometry(QtCore.QRect(29, 330, 171, 51))
        self.horizontalLayoutWidget_2.setObjectName("horizontalLayoutWidget_2")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget_2)
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_2.setSpacing(10)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.pushButton_3 = QtWidgets.QPushButton(parent=self.horizontalLayoutWidget_2)
        self.pushButton_3.setCursor(QtGui.QCursor(QtCore.Qt.CursorShape.PointingHandCursor))
        self.pushButton_3.setStyleSheet("#pushButton_3{\n"
"background-color:qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(69, 127, 202, 255), stop:1 rgba(86, 145, 200, 255));\n"
"color:white;\n"
"font-weight:bold;\n"
"border-radius:3px;\n"
"padding: 5px;\n"
"}\n"
"#pushButton_3:hover{\n"
"background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(107, 149, 202, 255), stop:1 rgba(86, 145, 200, 255));\n"
"}")
        self.pushButton_3.setObjectName("pushButton_3")
        self.horizontalLayout_2.addWidget(self.pushButton_3)
        self.pushButton_4 = QtWidgets.QPushButton(parent=self.horizontalLayoutWidget_2)
        self.pushButton_4.setCursor(QtGui.QCursor(QtCore.Qt.CursorShape.PointingHandCursor))
        self.pushButton_4.setStyleSheet("#pushButton_4{\n"
"background-color:qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(69, 127, 202, 255), stop:1 rgba(86, 145, 200, 255));\n"
"color:white;\n"
"font-weight:bold;\n"
"border-radius:3px;\n"
"padding: 5px;\n"
"}\n"
"#pushButton_4:hover{\n"
"background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(107, 149, 202, 255), stop:1 rgba(86, 145, 200, 255));\n"
"}")
        self.pushButton_4.setObjectName("pushButton_4")
        self.horizontalLayout_2.addWidget(self.pushButton_4)
        self.frmInfoBuoiHoc = QtWidgets.QFrame(parent=self.centralwidget)
        self.frmInfoBuoiHoc.setGeometry(QtCore.QRect(271, 101, 511, 411))
        self.frmInfoBuoiHoc.setStyleSheet("#frmInfoBuoiHoc\n"
"{\n"
"    border-width: 2;\n"
"    border-radius: 5;\n"
"     border-style: solid;\n"
"      border-color: #457fca;\n"
"}")
        self.frmInfoBuoiHoc.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.frmInfoBuoiHoc.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.frmInfoBuoiHoc.setObjectName("frmInfoBuoiHoc")
        self.frame_3 = QtWidgets.QFrame(parent=self.frmInfoBuoiHoc)
        self.frame_3.setGeometry(QtCore.QRect(20, 10, 471, 61))
        self.frame_3.setFrameShape(QtWidgets.QFrame.Shape.Box)
        self.frame_3.setFrameShadow(QtWidgets.QFrame.Shadow.Sunken)
        self.frame_3.setObjectName("frame_3")
        self.label_17 = QtWidgets.QLabel(parent=self.frame_3)
        self.label_17.setGeometry(QtCore.QRect(10, 10, 131, 21))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.label_17.setFont(font)
        self.label_17.setObjectName("label_17")
        self.label_18 = QtWidgets.QLabel(parent=self.frame_3)
        self.label_18.setGeometry(QtCore.QRect(10, 30, 101, 21))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.label_18.setFont(font)
        self.label_18.setAlignment(QtCore.Qt.AlignmentFlag.AlignBottom|QtCore.Qt.AlignmentFlag.AlignLeading|QtCore.Qt.AlignmentFlag.AlignLeft)
        self.label_18.setObjectName("label_18")
        self.comboBox_5 = QtWidgets.QComboBox(parent=self.frame_3)
        self.comboBox_5.setGeometry(QtCore.QRect(110, 30, 101, 21))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.comboBox_5.setFont(font)
        self.comboBox_5.setObjectName("comboBox_5")
        self.comboBox_5.addItem("")
        self.lineEdit_6 = QtWidgets.QLineEdit(parent=self.frame_3)
        self.lineEdit_6.setGeometry(QtCore.QRect(220, 30, 231, 21))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.lineEdit_6.setFont(font)
        self.lineEdit_6.setText("")
        self.lineEdit_6.setObjectName("lineEdit_6")
        self.tableWidget = QtWidgets.QTableWidget(parent=self.frmInfoBuoiHoc)
        self.tableWidget.setGeometry(QtCore.QRect(20, 90, 471, 301))
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(5)
        self.tableWidget.setRowCount(3)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(4, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setItem(0, 0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setItem(0, 1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setItem(0, 2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setItem(0, 3, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setItem(0, 4, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setItem(1, 0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setItem(1, 1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setItem(1, 2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setItem(1, 3, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setItem(1, 4, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setItem(2, 0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setItem(2, 1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setItem(2, 2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setItem(2, 3, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setItem(2, 4, item)
        self.frame = QtWidgets.QFrame(parent=self.centralwidget)
        self.frame.setGeometry(QtCore.QRect(0, 0, 801, 31))
        self.frame.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.frame.setObjectName("frame")
        self.btnClose = QtWidgets.QPushButton(parent=self.frame)
        self.btnClose.setGeometry(QtCore.QRect(777, 4, 24, 24))
        self.btnClose.setCursor(QtGui.QCursor(QtCore.Qt.CursorShape.PointingHandCursor))
        self.btnClose.setText("")
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap("image/icon/close_50px.png"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        self.btnClose.setIcon(icon2)
        self.btnClose.setIconSize(QtCore.QSize(20, 20))
        self.btnClose.setObjectName("btnClose")
        self.btnMinimize = QtWidgets.QPushButton(parent=self.frame)
        self.btnMinimize.setGeometry(QtCore.QRect(752, 4, 24, 24))
        self.btnMinimize.setCursor(QtGui.QCursor(QtCore.Qt.CursorShape.PointingHandCursor))
        self.btnMinimize.setText("")
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap("image/icon/subtract_50px.png"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        self.btnMinimize.setIcon(icon3)
        self.btnMinimize.setIconSize(QtCore.QSize(20, 20))
        self.btnMinimize.setObjectName("btnMinimize")
        self.label_15 = QtWidgets.QLabel(parent=self.frame)
        self.label_15.setGeometry(QtCore.QRect(10, 2, 201, 26))
        font = QtGui.QFont()
        font.setPointSize(9)
        font.setStyleStrategy(QtGui.QFont.StyleStrategy.NoAntialias)
        self.label_15.setFont(font)
        self.label_15.setAcceptDrops(False)
        self.label_15.setToolTip("")
        self.label_15.setAutoFillBackground(False)
        self.label_15.setFrameShape(QtWidgets.QFrame.Shape.NoFrame)
        self.label_15.setFrameShadow(QtWidgets.QFrame.Shadow.Plain)
        self.label_15.setTextFormat(QtCore.Qt.TextFormat.AutoText)
        self.label_15.setScaledContents(False)
        self.label_15.setWordWrap(False)
        self.label_15.setIndent(-1)
        self.label_15.setTextInteractionFlags(QtCore.Qt.TextInteractionFlag.LinksAccessibleByMouse)
        self.label_15.setObjectName("label_15")
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label_3.setText(_translate("MainWindow", "Quản lý buổi học"))
        self.btnBack.setText(_translate("MainWindow", "Trở về"))
        self.label_2.setText(_translate("MainWindow", "09:15:00"))
        self.label_4.setText(_translate("MainWindow", "02/02/2022"))
        self.label_5.setText(_translate("MainWindow", "THÔNG TIN BUỔI HỌC"))
        self.label_10.setText(_translate("MainWindow", "ID buổi học"))
        self.lineEdit_2.setText(_translate("MainWindow", "1"))
        self.label_11.setText(_translate("MainWindow", "Giờ bắt đầu"))
        self.label_12.setText(_translate("MainWindow", "Giờ kết thúc"))
        self.label_13.setText(_translate("MainWindow", "Ngày"))
        self.label_14.setText(_translate("MainWindow", "Lớp học"))
        self.comboBox.setItemText(0, _translate("MainWindow", "DCT1205"))
        self.pushButton_2.setText(_translate("MainWindow", "Thêm"))
        self.pushButton.setText(_translate("MainWindow", "Sửa"))
        self.pushButton_3.setText(_translate("MainWindow", "Xóa"))
        self.pushButton_4.setText(_translate("MainWindow", "Làm mới"))
        self.label_17.setText(_translate("MainWindow", "Hệ thống tìm kiếm:"))
        self.label_18.setText(_translate("MainWindow", "Tìm kiếm theo:"))
        self.comboBox_5.setItemText(0, _translate("MainWindow", "ID buổi học"))
        item = self.tableWidget.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "ID buổi học"))
        item = self.tableWidget.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "Giờ bắt đầu"))
        item = self.tableWidget.horizontalHeaderItem(2)
        item.setText(_translate("MainWindow", "Giờ kết thúc"))
        item = self.tableWidget.horizontalHeaderItem(3)
        item.setText(_translate("MainWindow", "Ngày"))
        item = self.tableWidget.horizontalHeaderItem(4)
        item.setText(_translate("MainWindow", "Lớp học"))
        __sortingEnabled = self.tableWidget.isSortingEnabled()
        self.tableWidget.setSortingEnabled(False)
        item = self.tableWidget.item(0, 0)
        item.setText(_translate("MainWindow", "1"))
        item = self.tableWidget.item(0, 1)
        item.setText(_translate("MainWindow", "7:00:00"))
        item = self.tableWidget.item(0, 2)
        item.setText(_translate("MainWindow", "12:00:00"))
        item = self.tableWidget.item(0, 3)
        item.setText(_translate("MainWindow", "1/1/2022"))
        item = self.tableWidget.item(0, 4)
        item.setText(_translate("MainWindow", "DCT1200"))
        item = self.tableWidget.item(1, 0)
        item.setText(_translate("MainWindow", "2"))
        item = self.tableWidget.item(1, 1)
        item.setText(_translate("MainWindow", "8:00:00"))
        item = self.tableWidget.item(1, 2)
        item.setText(_translate("MainWindow", "11:00:00"))
        item = self.tableWidget.item(1, 3)
        item.setText(_translate("MainWindow", "2/2/2022"))
        item = self.tableWidget.item(1, 4)
        item.setText(_translate("MainWindow", "DCT1201"))
        item = self.tableWidget.item(2, 0)
        item.setText(_translate("MainWindow", "3"))
        item = self.tableWidget.item(2, 1)
        item.setText(_translate("MainWindow", "13:00:00"))
        item = self.tableWidget.item(2, 2)
        item.setText(_translate("MainWindow", "17:00:00"))
        item = self.tableWidget.item(2, 3)
        item.setText(_translate("MainWindow", "3/2/2022"))
        item = self.tableWidget.item(2, 4)
        item.setText(_translate("MainWindow", "DCT1203"))
        self.tableWidget.setSortingEnabled(__sortingEnabled)
        self.label_15.setText(_translate("MainWindow", "Phần mềm điểm danh sinh viên"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec())
