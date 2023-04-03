# Form implementation generated from reading ui file 'ui/NhanDien.ui'
#
# Created by: PyQt6 UI code generator 6.4.2
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets
from PyQt6.QtCore import Qt
from PyQt6.QtGui import QPixmap
from datetime import datetime
import os
import cv2
import sys
SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
sys.path.append(os.path.dirname(SCRIPT_DIR))
from BUS.face_recognition import face_recognition
from BUS.BuoiHocBUS import BuoiHocBUS
from BUS.GiangVienBUS import GiangVienBUS
from BUS.SinhVienBUS import SinhVienBUS
from BUS.HinhAnhSVBUS import HinhAnhSVBUS
from BUS.DiemDanhBUS import DiemDanhBUS
from DAL.DiemDanh import DiemDanh
class UI_NhanDien(object):
        masinhvien = ''
        hinhanh = ''
        arr_masinhvien = []
        flagSetInfoSV = False
        
        def setupUi(self, MainWindow):
                MainWindow.setObjectName("MainWindow")
                MainWindow.resize(800, 590)
                self.centralwidget = QtWidgets.QWidget(parent=MainWindow)
                self.centralwidget.setObjectName("centralwidget")
                self.frmHeader = QtWidgets.QFrame(parent=self.centralwidget)
                self.frmHeader.setGeometry(QtCore.QRect(0, 30, 851, 51))
                self.frmHeader.setAccessibleName("")
                self.frmHeader.setLayoutDirection(QtCore.Qt.LayoutDirection.LeftToRight)
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
                font = QtGui.QFont()
                font.setPointSize(9)
                self.btnBack.setFont(font)
                self.btnBack.setCursor(QtGui.QCursor(QtCore.Qt.CursorShape.PointingHandCursor))
                self.btnBack.setStyleSheet("#btnLogout\n"
        "{\n"
        "    padding:3px;\n"
        "}")
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
                icon.addPixmap(QtGui.QPixmap("ui\\../image/icon/moon_symbol_50px.png"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
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
                icon1.addPixmap(QtGui.QPixmap("ui\\../image/icon/time_50px.png"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
                self.btnTime.setIcon(icon1)
                self.btnTime.setIconSize(QtCore.QSize(20, 20))
                self.btnTime.setObjectName("btnTime")
                self.label_3.raise_()
                self.btnBack.raise_()
                self.label_4.raise_()
                self.label_2.raise_()
                self.btnDark.raise_()
                self.btnTime.raise_()
                self.frame = QtWidgets.QFrame(parent=self.centralwidget)
                self.frame.setGeometry(QtCore.QRect(20, 100, 471, 421))
                self.frame.setStyleSheet("#frame\n"
        "{\n"
        "    border-width: 2;\n"
        "    border-radius: 5;\n"
        "     border-style: solid;\n"
        "      border-color: #457fca;\n"
        "}")
                self.frame.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
                self.frame.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
                self.frame.setObjectName("frame")
                self.label_6 = QtWidgets.QLabel(parent=self.frame)
                self.label_6.setGeometry(QtCore.QRect(20, 40, 101, 24))
                font = QtGui.QFont()
                font.setPointSize(10)
                self.label_6.setFont(font)
                self.label_6.setObjectName("label_6")
                self.cmbBuoiHoc = QtWidgets.QComboBox(parent=self.frame)
                self.cmbBuoiHoc.setGeometry(QtCore.QRect(120, 40, 101, 21))
                font = QtGui.QFont()
                font.setPointSize(10)
                self.cmbBuoiHoc.setFont(font)
                self.cmbBuoiHoc.setObjectName("cmbBuoiHoc")
                self.cmbBuoiHoc.currentIndexChanged.connect(self.ChangeBuoiHoc)
                self.cmbBuoiHoc.setStyleSheet("#cmbBuoiHoc{color:black}")
                self.label_7 = QtWidgets.QLabel(parent=self.frame)
                self.label_7.setGeometry(QtCore.QRect(260, 40, 131, 24))
                font = QtGui.QFont()
                font.setPointSize(10)
                self.label_7.setFont(font)
                self.label_7.setObjectName("label_7")
                self.cmbLoaiDiemDanh = QtWidgets.QComboBox(parent=self.frame)
                self.cmbLoaiDiemDanh.setGeometry(QtCore.QRect(400, 40, 51, 21))
                font = QtGui.QFont()
                font.setPointSize(10)
                self.cmbLoaiDiemDanh.setFont(font)
                self.cmbLoaiDiemDanh.setObjectName("cmbLoaiDiemDanh")
                self.cmbLoaiDiemDanh.addItem("")
                self.cmbLoaiDiemDanh.addItem("Vào")
                self.cmbLoaiDiemDanh.addItem("Ra")
                self.cmbLoaiDiemDanh.setStyleSheet("#cmbLoaiDiemDanh{color:black}")
                self.frame_5 = QtWidgets.QFrame(parent=self.frame)
                self.frame_5.setGeometry(QtCore.QRect(10, 380, 451, 31))
                self.frame_5.setFrameShape(QtWidgets.QFrame.Shape.Box)
                self.frame_5.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
                self.frame_5.setObjectName("frame_5")
                self.lblThongBao = QtWidgets.QLabel(parent=self.frame_5)
                self.lblThongBao.setGeometry(QtCore.QRect(10, 5, 420, 23))
                font = QtGui.QFont()
                font.setPointSize(10)
                self.lblThongBao.setFont(font)
                self.lblThongBao.setStyleSheet("#lblThongBao\n"
        "{\n"
        "color:red;\n"
        "}")
                self.lblThongBao.setObjectName("lblThongBao")
                self.label_20 = QtWidgets.QLabel(parent=self.frame)
                self.label_20.setGeometry(QtCore.QRect(20, 10, 171, 21))
                font = QtGui.QFont()
                font.setPointSize(12)
                font.setBold(True)
                font.setWeight(75)
                self.label_20.setFont(font)
                self.label_20.setStyleSheet("#label_20\n"
        "{\n"
        "font-weight:bold;\n"
        "}")
                self.label_20.setObjectName("label_20")
                self.camera = QtWidgets.QLabel(parent=self.frame)
                self.camera.setGeometry(QtCore.QRect(10, 80, 451, 291))
                self.camera.setStyleSheet("#camera\n"
        "{\n"
        "border:1px solid;\n"
        "}")
                self.camera.setText("")
                self.camera.setObjectName("camera")
                self.frame_2 = QtWidgets.QFrame(parent=self.centralwidget)
                self.frame_2.setGeometry(QtCore.QRect(510, 100, 271, 291))
                self.frame_2.setStyleSheet("#frame_2\n"
        "{\n"
        "    border-width: 2;\n"
        "    border-radius: 5;\n"
        "     border-style: solid;\n"
        "      border-color: #457fca;\n"
        "}")
                self.frame_2.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
                self.frame_2.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
                self.frame_2.setObjectName("frame_2")
                self.label_9 = QtWidgets.QLabel(parent=self.frame_2)
                self.label_9.setGeometry(QtCore.QRect(20, 10, 171, 21))
                font = QtGui.QFont()
                font.setPointSize(12)
                font.setBold(True)
                font.setWeight(75)
                self.label_9.setFont(font)
                self.label_9.setStyleSheet("#label_9\n"
        "{\n"
        "font-weight:bold;\n"
        "}")
                self.label_9.setObjectName("label_9")
                self.label_10 = QtWidgets.QLabel(parent=self.frame_2)
                self.label_10.setGeometry(QtCore.QRect(30, 190, 81, 21))
                font = QtGui.QFont()
                font.setPointSize(10)
                self.label_10.setFont(font)
                self.label_10.setObjectName("label_10")
                self.txtMaSV = QtWidgets.QLineEdit(parent=self.frame_2)
                self.txtMaSV.setGeometry(QtCore.QRect(110, 190, 141, 20))
                self.txtMaSV.setObjectName("txtMaSV")
                self.txtHoTen = QtWidgets.QLineEdit(parent=self.frame_2)
                self.txtHoTen.setGeometry(QtCore.QRect(110, 220, 141, 20))
                self.txtHoTen.setText("")
                self.txtHoTen.setObjectName("txtHoTen")
                self.label_11 = QtWidgets.QLabel(parent=self.frame_2)
                self.label_11.setGeometry(QtCore.QRect(30, 220, 71, 21))
                font = QtGui.QFont()
                font.setPointSize(10)
                self.label_11.setFont(font)
                self.label_11.setObjectName("label_11")
                self.label_12 = QtWidgets.QLabel(parent=self.frame_2)
                self.label_12.setGeometry(QtCore.QRect(30, 250, 81, 21))
                font = QtGui.QFont()
                font.setPointSize(10)
                self.label_12.setFont(font)
                self.label_12.setObjectName("label_12")
                self.timeThoiGian = QtWidgets.QTimeEdit(parent=self.frame_2)
                self.timeThoiGian.setGeometry(QtCore.QRect(110, 250, 141, 22))
                self.timeThoiGian.setObjectName("timeThoiGian")
                self.timeThoiGian.setDisplayFormat("HH:mm:ss")
                self.imageNhanDien = QtWidgets.QLabel(parent=self.frame_2)
                self.imageNhanDien.setGeometry(QtCore.QRect(81, 40, 131, 131))
                self.imageNhanDien.setStyleSheet("#imageNhanDien\n"
        "{\n"
        "border:1px solid;\n"
        "}")
                self.imageNhanDien.setText("")
                self.imageNhanDien.setObjectName("imageNhanDien")
                self.frame_3 = QtWidgets.QFrame(parent=self.centralwidget)
                self.frame_3.setGeometry(QtCore.QRect(510, 410, 271, 161))
                self.frame_3.setStyleSheet("#frame_3\n"
        "{\n"
        "    border-width: 2;\n"
        "    border-radius: 5;\n"
        "     border-style: solid;\n"
        "      border-color: #457fca;\n"
        "}")
                self.frame_3.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
                self.frame_3.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
                self.frame_3.setObjectName("frame_3")
                self.label_13 = QtWidgets.QLabel(parent=self.frame_3)
                self.label_13.setGeometry(QtCore.QRect(20, 10, 171, 21))
                font = QtGui.QFont()
                font.setPointSize(12)
                font.setBold(True)
                font.setWeight(75)
                self.label_13.setFont(font)
                self.label_13.setStyleSheet("#label_13\n"
        "{\n"
        "font-weight:bold;\n"
        "}")
                self.label_13.setObjectName("label_13")
                self.label_14 = QtWidgets.QLabel(parent=self.frame_3)
                self.label_14.setGeometry(QtCore.QRect(30, 70, 101, 16))
                font = QtGui.QFont()
                font.setPointSize(10)
                self.label_14.setFont(font)
                self.label_14.setObjectName("label_14")
                self.label_15 = QtWidgets.QLabel(parent=self.frame_3)
                self.label_15.setGeometry(QtCore.QRect(30, 100, 101, 16))
                font = QtGui.QFont()
                font.setPointSize(10)
                self.label_15.setFont(font)
                self.label_15.setObjectName("label_15")
                self.label_16 = QtWidgets.QLabel(parent=self.frame_3)
                self.label_16.setGeometry(QtCore.QRect(30, 40, 101, 16))
                font = QtGui.QFont()
                font.setPointSize(10)
                self.label_16.setFont(font)
                self.label_16.setObjectName("label_16")
                self.lblIDBuoiHoc = QtWidgets.QLabel(parent=self.frame_3)
                self.lblIDBuoiHoc.setGeometry(QtCore.QRect(130, 40, 138, 16))
                font = QtGui.QFont()
                font.setPointSize(10)
                self.lblIDBuoiHoc.setFont(font)
                self.lblIDBuoiHoc.setStyleSheet("#lblIDBuoiHoc\n"
        "{\n"
        "color:red;\n"
        "}")
                self.lblIDBuoiHoc.setObjectName("lblIDBuoiHoc")
                self.lblNgay = QtWidgets.QLabel(parent=self.frame_3)
                self.lblNgay.setGeometry(QtCore.QRect(130, 70, 138, 16))
                font = QtGui.QFont()
                font.setPointSize(10)
                self.lblNgay.setFont(font)
                self.lblNgay.setStyleSheet("#lblNgay{\n"
        "color:red;\n"
        "}")
                self.lblNgay.setObjectName("lblNgay")
                self.lblThoiGian = QtWidgets.QLabel(parent=self.frame_3)
                self.lblThoiGian.setGeometry(QtCore.QRect(130, 100, 138, 16))
                font = QtGui.QFont()
                font.setPointSize(10)
                self.lblThoiGian.setFont(font)
                self.lblThoiGian.setStyleSheet("#lblThoiGian\n"
        "{\n"
        "color:red;\n"
        "}")
                self.lblThoiGian.setObjectName("lblThoiGian")
                self.lblGiangVien = QtWidgets.QLabel(parent=self.frame_3)
                self.lblGiangVien.setGeometry(QtCore.QRect(130, 130, 138, 20))
                font = QtGui.QFont()
                font.setPointSize(10)
                self.lblGiangVien.setFont(font)
                self.lblGiangVien.setStyleSheet("#lblGiangVien\n"
        "{\n"
        "color:red;\n"
        "}")
                self.lblGiangVien.setObjectName("lblGiangVien")
                self.label_17 = QtWidgets.QLabel(parent=self.frame_3)
                self.label_17.setGeometry(QtCore.QRect(30, 130, 101, 20))
                font = QtGui.QFont()
                font.setPointSize(10)
                self.label_17.setFont(font)
                self.label_17.setObjectName("label_17")
                self.horizontalLayoutWidget = QtWidgets.QWidget(parent=self.centralwidget)
                self.horizontalLayoutWidget.setGeometry(QtCore.QRect(20, 530, 471, 41))
                self.horizontalLayoutWidget.setObjectName("horizontalLayoutWidget")
                self.horizontalLayout = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget)
                self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
                self.horizontalLayout.setSpacing(10)
                self.horizontalLayout.setObjectName("horizontalLayout")
                self.btnMoCam = QtWidgets.QPushButton(parent=self.horizontalLayoutWidget)
                font = QtGui.QFont()
                font.setPointSize(10)
                font.setBold(True)
                font.setWeight(75)
                self.btnMoCam.setFont(font)
                self.btnMoCam.setCursor(QtGui.QCursor(QtCore.Qt.CursorShape.PointingHandCursor))
                self.btnMoCam.setStyleSheet("#btnMoCam{\n"
        "background-color:qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(69, 127, 202, 255), stop:1 rgba(86, 145, 200, 255));\n"
        "color:white;\n"
        "font-weight:bold;\n"
        "border-radius:3px;\n"
        "padding: 7px;\n"
        "}\n"
        "#btnMoCam:hover{\n"
        "background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(107, 149, 202, 255), stop:1 rgba(86, 145, 200, 255));\n"
        "}")
                self.btnMoCam.setObjectName("btnMoCam")
                self.btnMoCam.clicked.connect(self.start_capture_video)
                self.horizontalLayout.addWidget(self.btnMoCam)
                self.btnDongCam = QtWidgets.QPushButton(parent=self.horizontalLayoutWidget)
                font = QtGui.QFont()
                font.setPointSize(10)
                font.setBold(True)
                font.setWeight(75)
                self.btnDongCam.setFont(font)
                self.btnDongCam.setCursor(QtGui.QCursor(QtCore.Qt.CursorShape.PointingHandCursor))
                self.btnDongCam.setStyleSheet("#btnDongCam{\n"
        "background-color:qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(69, 127, 202, 255), stop:1 rgba(86, 145, 200, 255));\n"
        "color:white;\n"
        "font-weight:bold;\n"
        "border-radius:3px;\n"
        "padding: 7px;\n"
        "}\n"
        "#btnDongCam:hover{\n"
        "background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(107, 149, 202, 255), stop:1 rgba(86, 145, 200, 255));\n"
        "}")
                self.btnDongCam.setObjectName("btnDongCam")
                self.btnDongCam.clicked.connect(self.stop_capture_video)

                self.thread = {}

                self.horizontalLayout.addWidget(self.btnDongCam)
                self.frame_7 = QtWidgets.QFrame(parent=self.centralwidget)
                self.frame_7.setGeometry(QtCore.QRect(0, 0, 801, 31))
                self.frame_7.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
                self.frame_7.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
                self.frame_7.setObjectName("frame_7")
                self.btnClose = QtWidgets.QPushButton(parent=self.frame_7)
                self.btnClose.setGeometry(QtCore.QRect(777, 4, 24, 24))
                self.btnClose.setCursor(QtGui.QCursor(QtCore.Qt.CursorShape.PointingHandCursor))
                self.btnClose.setText("")
                icon2 = QtGui.QIcon()
                icon2.addPixmap(QtGui.QPixmap("ui\\../image/icon/close_50px.png"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
                self.btnClose.setIcon(icon2)
                self.btnClose.setIconSize(QtCore.QSize(20, 20))
                self.btnClose.setObjectName("btnClose")
                self.btnMinimize = QtWidgets.QPushButton(parent=self.frame_7)
                self.btnMinimize.setGeometry(QtCore.QRect(752, 4, 24, 24))
                self.btnMinimize.setCursor(QtGui.QCursor(QtCore.Qt.CursorShape.PointingHandCursor))
                self.btnMinimize.setText("")
                icon3 = QtGui.QIcon()
                icon3.addPixmap(QtGui.QPixmap("ui\\../image/icon/subtract_50px.png"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
                self.btnMinimize.setIcon(icon3)
                self.btnMinimize.setIconSize(QtCore.QSize(20, 20))
                self.btnMinimize.setObjectName("btnMinimize")
                self.label_21 = QtWidgets.QLabel(parent=self.frame_7)
                self.label_21.setGeometry(QtCore.QRect(10, 2, 201, 26))
                font = QtGui.QFont()
                font.setPointSize(9)
                font.setStyleStrategy(QtGui.QFont.StyleStrategy.NoAntialias)
                self.label_21.setFont(font)
                self.label_21.setAcceptDrops(False)
                self.label_21.setToolTip("")
                self.label_21.setAutoFillBackground(False)
                self.label_21.setFrameShape(QtWidgets.QFrame.Shape.NoFrame)
                self.label_21.setFrameShadow(QtWidgets.QFrame.Shadow.Plain)
                self.label_21.setTextFormat(QtCore.Qt.TextFormat.AutoText)
                self.label_21.setScaledContents(False)
                self.label_21.setWordWrap(False)
                self.label_21.setIndent(-1)
                self.label_21.setTextInteractionFlags(QtCore.Qt.TextInteractionFlag.LinksAccessibleByMouse)
                self.label_21.setObjectName("label_21")
                MainWindow.setCentralWidget(self.centralwidget)

                self.retranslateUi(MainWindow)
                
                self.loadListBH()  

                # tạo timer
                self.timer = QtCore.QTimer()
                self.timer.timeout.connect(self.clock_number)
                # start and update every second
                self.timer.start(1000)
                self.clock_number()

                QtCore.QMetaObject.connectSlotsByName(MainWindow)
                
        def retranslateUi(self, MainWindow):
                _translate = QtCore.QCoreApplication.translate
                MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
                self.label_3.setText(_translate("MainWindow", "Nhận diện khuôn mặt"))
                self.btnBack.setText(_translate("MainWindow", "Trở về"))
                self.label_6.setText(_translate("MainWindow", "Chọn buổi học:"))
                self.label_7.setText(_translate("MainWindow", "Chọn loại điểm danh"))
                self.lblThongBao.setText(_translate("MainWindow", "Thông báo: Vui lòng chọn ID buổi học và loại điểm danh để mở camera!"))
                self.label_20.setText(_translate("MainWindow", "Màn hình nhận diện"))
                self.label_9.setText(_translate("MainWindow", "Thông tin điểm danh"))
                self.label_10.setText(_translate("MainWindow", "Mã SV:"))
                self.label_11.setText(_translate("MainWindow", "Họ tên:"))
                self.label_12.setText(_translate("MainWindow", "Thời gian:"))
                self.label_13.setText(_translate("MainWindow", "Thông tin buổi học"))
                self.label_14.setText(_translate("MainWindow", "Ngày"))
                self.label_15.setText(_translate("MainWindow", "Thời gian:"))
                self.label_16.setText(_translate("MainWindow", "ID buổi học"))
                self.label_17.setText(_translate("MainWindow", "Giảng viên"))
                self.btnMoCam.setText(_translate("MainWindow", "Mở Camera"))
                self.btnDongCam.setText(_translate("MainWindow", "Đóng Camera"))
                self.label_21.setText(_translate("MainWindow", "Phần mềm điểm danh sinh viên"))
         # LOAD COMBOBOX DANH SÁCH BUỔI HỌC
        def loadListBH(self):
                self.cmbBuoiHoc.addItem("")

                gvBUS = BuoiHocBUS()
                list = gvBUS.get()
                if list is not None:
                        for row in list:
                                self.cmbBuoiHoc.addItem(row[0])
        # THAY ĐỔI BUỔI HỌC
        def ChangeBuoiHoc(self):
                mabuoihoc = self.cmbBuoiHoc.currentText()
                bhBUS = BuoiHocBUS()
                value = mabuoihoc
                list = bhBUS.findMaBuoiHoc(value)
                if list is not None:
                        for row in list:
                                self.lblIDBuoiHoc.setText(mabuoihoc)
                                self.lblNgay.setText(row[3].strftime("%d/%m/%Y"))
                                self.lblThoiGian.setText("{} - {}".format(str(row[1]),str(row[2])))
                                # LẤY TÊN GV
                                tengv = ""
                                gvBUS = GiangVienBUS()
                                gv = gvBUS.getItem(row[5])
                                if gv is not None:
                                        tengv = gv._hoten
                                self.lblGiangVien.setText(tengv)
                                      
        def stop_capture_video(self):    
                self.flagSetInfoSV = False                                        
                self.thread[1].stop()
                self.camera.setPixmap(QtGui.QPixmap())  
                self.cmbBuoiHoc.setEnabled(True)
                self.cmbBuoiHoc.setCurrentIndex(0)
                self.cmbLoaiDiemDanh.setEnabled(True)
                self.cmbLoaiDiemDanh.setCurrentIndex(0)
                self.imageNhanDien.setPixmap(QtGui.QPixmap())  
                self.txtMaSV.clear()
                self.txtHoTen.clear()
                self.timeThoiGian.clear()
                self.lblIDBuoiHoc.clear()
                self.lblGiangVien.clear()
                self.lblNgay.clear()
                self.lblThoiGian.clear()
                self.lblThongBao.setText("Thông báo: Vui lòng chọn ID buổi học và loại điểm danh để mở camera!")

                
        def start_capture_video(self):
                if(self.cmbBuoiHoc.currentIndex()!=0 and self.cmbLoaiDiemDanh.currentIndex()!=0):
                        self.thread[1] = face_recognition(index=1)                
                        self.thread[1].start()
                        self.thread[1].signal.connect(self.show_wedcam)                        
                        self.lblThongBao.setText("Thông báo: Camera đang mở...")
                        self.cmbBuoiHoc.setEnabled(False)
                        self.cmbLoaiDiemDanh.setEnabled(False)
                else:
                        self.lblThongBao.setText("Thông báo: Vui lòng chọn ID buổi học và loại điểm danh để mở camera!")
                        QtWidgets.QMessageBox.information(self.centralwidget,"Thông báo","Vui lòng chọn ID buổi học và loại điểm danh để mở camera!" )

        def show_wedcam(self, cv_img):
                """Updates the image_label with a new opencv image"""    
                            
                self.masinhvien = self.thread[1].getIDSV()            
                if self.masinhvien not in self.arr_masinhvien:                    
                        self.arr_masinhvien.append(self.masinhvien)
                        self.flagSetInfoSV = False
                
                if (self.thread[1].getLink_Image()!='') and self.flagSetInfoSV == False:                        
                        # SET IMAGE NHẬN DIỆN
                        pixmap = self.convert_cv_qt(self.thread[1].getCv_Image_Cur(), 131, 131)    
                        self.imageNhanDien.setPixmap(pixmap)                
                        self.setInfoSV()       
                        self.hinhanh = self.thread[1].getLink_Image()
                        if self.cmbLoaiDiemDanh.currentIndex()==1:
                                self.addDiemDanh()
                        else:
                                self.updateGioRa()

                        self.flagSetInfoSV = True

                # SET CAMERA
                qt_img = self.convert_cv_qt(cv_img, 501, 341)                
                self.camera.setPixmap(qt_img)

        def convert_cv_qt(self, cv_img, width, height):
                """Convert from an opencv image to QPixmap"""
                rgb_image = cv2.cvtColor(cv_img, cv2.COLOR_BGR2RGB)
                h, w, ch = rgb_image.shape
                bytes_per_line = ch * w
                convert_to_Qt_format = QtGui.QImage(rgb_image.data, w, h, bytes_per_line, QtGui.QImage.Format.Format_RGB888)
                p = convert_to_Qt_format.scaled(width, height, Qt.AspectRatioMode.KeepAspectRatio)  
                return QPixmap.fromImage(p)
        
        
        def setInfoSV(self):
                if self.masinhvien!='' :
                        tensinhvien = ''
                        svBUS = SinhVienBUS()
                        list = svBUS.findMaSinhVien(self.masinhvien)
                        if list is not None:
                                for row in list:
                                        tensinhvien = row[1]                                
                
                        self.txtMaSV.setText(self.masinhvien)
                        self.txtHoTen.setText(tensinhvien)

                        # SET THỜI GIAN
                        time_str = self.label_2.text()
                        time_format =  "%H:%M:%S"                
                        time = datetime.strptime(time_str,time_format).time()
                        self.timeThoiGian.setTime(time)

        def addDiemDanh(self):
                ddBUS = DiemDanhBUS()
                madiemdanh = ddBUS.generateID()
                masinhvien = self.txtMaSV.text()
                giovao = self.timeThoiGian.text()                
                date_time_str = self.label_4.text()
                ngay = datetime.strptime(date_time_str, "%d/%m/%Y").strftime('%Y-%m-%d')
                mabuoihoc = self.lblIDBuoiHoc.text()
                hinhanh = self.hinhanh
                diemdanh = DiemDanh(madiemdanh, masinhvien, giovao,'', ngay, mabuoihoc,hinhanh)
                ddBUS.add(diemdanh)

        def updateGioRa(self):
                ddBUS = DiemDanhBUS()
                masinhvien = self.txtMaSV.text()
                giora = self.timeThoiGian.text()                
                mabuoihoc = self.lblIDBuoiHoc.text()  
                ddBUS.updateGioRa(masinhvien, mabuoihoc, giora)

        def clock_number(self):
                time = datetime.now()
                format_time = time.strftime("%H:%M:%S")
                self.label_2.setText(format_time)

                format_date = time.strftime("%d/%m/%Y")
                self.label_4.setText(format_date)





       
                


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = UI_NhanDien()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec())
