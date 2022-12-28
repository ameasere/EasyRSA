# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'newMain.ui'
##
## Created by: Qt User Interface Compiler version 6.4.1
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QAbstractItemView, QAbstractScrollArea, QApplication, QCheckBox,
    QComboBox, QCommandLinkButton, QFrame, QGridLayout,
    QHBoxLayout, QHeaderView, QLabel, QLineEdit,
    QMainWindow, QPlainTextEdit, QProgressBar, QPushButton,
    QRadioButton, QScrollArea, QScrollBar, QSizePolicy,
    QSlider, QStackedWidget, QTableWidget, QTableWidgetItem,
    QTextEdit, QTreeView, QVBoxLayout, QWidget)
from .resources_rc import *
class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1274, 693)
        MainWindow.setMinimumSize(QSize(940, 560))
        icon = QIcon()
        icon.addFile(u":/images/images/images/RSA.png", QSize(), QIcon.Normal, QIcon.Off)
        MainWindow.setWindowIcon(icon)
        self.styleSheet = QWidget(MainWindow)
        self.styleSheet.setObjectName(u"styleSheet")
        font = QFont()
        font.setFamilies([u"Segoe UI"])
        font.setPointSize(10)
        font.setBold(False)
        font.setItalic(False)
        self.styleSheet.setFont(font)
        self.styleSheet.setStyleSheet(u"/* Halloween Stylesheet */\n"
"\n"
"QWidget{\n"
"	color: rgb(221, 221, 221);\n"
"	font: 10pt \"Segoe UI\";\n"
"}\n"
"\n"
"/* /////////////////////////////////////////////////////////////////////////////////////////////////\n"
"Tooltip */\n"
"QToolTip {\n"
"	color: #ffffff;\n"
"	background-color: rgba(35, 36, 42, 180);\n"
"	border: 1px solid rgb(35,35,38);\n"
"	background-image: none;\n"
"	background-position: left center;\n"
"    background-repeat: no-repeat;\n"
"	border: none;\n"
"	border-left: 2px solid rgb(97, 67, 133);\n"
"	text-align: left;\n"
"	padding-left: 8px;\n"
"	margin: 0px;\n"
"}\n"
"\n"
"/* /////////////////////////////////////////////////////////////////////////////////////////////////\n"
"Bg App */\n"
"#bgApp {\n"
"	background-color: rgb(35, 36, 42);\n"
"	border: 1px solid rgb(35,35,38);\n"
"}\n"
"\n"
"/* /////////////////////////////////////////////////////////////////////////////////////////////////\n"
"Left Menu */\n"
"#leftMenuBg {\n"
"	background-color: qlineargradient(spread:pad, x1:0, y1"
                        ":0, x2:1, y2:1, stop:0 rgba(97, 67, 133, 255), stop:1 rgba(81, 99, 149, 255));\n"
"}\n"
"#topLogo {\n"
"	background-color: transparent;\n"
"	background-image: url(:/images/images/images/RSA30x30.png);\n"
"	background-position: center;\n"
"	background-repeat: no-repeat;\n"
"}\n"
"#titleLeftApp { font: 81 12pt \"Raleway ExtraBold\"; }\n"
"#titleLeftDescription { font: 8pt \"Segoe UI\"; color: #aa63ff; }\n"
"\n"
"/* MENUS */\n"
"#topMenu .QPushButton {\n"
"	background-position: left center;\n"
"    background-repeat: no-repeat;\n"
"	border: none;\n"
"	border-left: 22px solid transparent;\n"
"	background-color: transparent;\n"
"	text-align: left;\n"
"	padding-left: 44px;\n"
"}\n"
"#topMenu .QPushButton:hover {\n"
"	background-color: rgb(35,35,38);\n"
"}\n"
"#topMenu .QPushButton:pressed {\n"
"	background-color: #aa63ff;\n"
"	color: #fff;\n"
"}\n"
"#bottomMenu .QPushButton {\n"
"	background-position: left center;\n"
"    background-repeat: no-repeat;\n"
"	border: none;\n"
"	border-left: 20px solid transparent;\n"
""
                        "	background-color:transparent;\n"
"	text-align: left;\n"
"	padding-left: 44px;\n"
"}\n"
"#bottomMenu .QPushButton:hover {\n"
"	background-color: rgb(35,35,38);\n"
"}\n"
"#bottomMenu .QPushButton:pressed {\n"
"	background-color: #aa63ff;\n"
"	color: #fff;\n"
"}\n"
"#leftMenuFrame{\n"
"	border-top: solid rgb(35,35,38);\n"
"}\n"
"\n"
"/* Toggle Button */\n"
"#toggleButton {\n"
"	background-position: left center;\n"
"    background-repeat: no-repeat;\n"
"	border: none;\n"
"	border-left: 20px solid transparent;\n"
"	background-color: #23242a;\n"
"	text-align: left;\n"
"	padding-left: 44px;\n"
"	color: rgb(113, 126, 149);\n"
"}\n"
"#toggleButton:hover {\n"
"	background-color: rgb(11,11,11);\n"
"}\n"
"#toggleButton:pressed { \n"
"	background-color: #fff;\n"
"}\n"
"\n"
"/* Title Menu */\n"
"#titleRightInfo { padding-left: 10px; }\n"
"\n"
"\n"
"/* /////////////////////////////////////////////////////////////////////////////////////////////////\n"
"Extra Tab */\n"
"#extraLeftBox {\n"
"	background-color: rgb(35,35,38);\n"
""
                        "}\n"
"#extraTopBg {\n"
"	background-color: #aa63ff;\n"
"}\n"
"\n"
"/* Icon */\n"
"#extraIcon {\n"
"	background-position: center;\n"
"	background-repeat: no-repeat;\n"
"	background-image: url(:/icons/images/icons/icon_settings.png);\n"
"}\n"
"\n"
"/* Label */\n"
"#extraLabel { color: rgb(255, 255, 255); }\n"
"\n"
"/* Btn Close */\n"
"#extraCloseColumnBtn { background-color: rgba(255, 255, 255, 0); border: none;  border-radius: 5px; }\n"
"#extraCloseColumnBtn:hover { background-color: rgb(35,35,38); border-style: solid; border-radius: 4px; }\n"
"#extraCloseColumnBtn:pressed { background-color: #aa63ff; border-style: solid; border-radius: 4px; }\n"
"\n"
"/* Extra Content */\n"
"#extraContent{\n"
"	border-top: 3px solid rgb(35,35,38);\n"
"}\n"
"\n"
"/* Extra Top Menus */\n"
"#extraTopMenu .QPushButton {\n"
"background-position: left center;\n"
"    background-repeat: no-repeat;\n"
"	border: none;\n"
"	border-left: 22px solid transparent;\n"
"	background-color:transparent;\n"
"	text-align: left;\n"
"	padding-left: "
                        "44px;\n"
"}\n"
"#extraTopMenu .QPushButton:hover {\n"
"	background-color: rgb(35,35,38);\n"
"}\n"
"#extraTopMenu .QPushButton:pressed {\n"
"	background-color: #aa63ff;\n"
"	color: #fff;\n"
"}\n"
"\n"
"/* /////////////////////////////////////////////////////////////////////////////////////////////////\n"
"Content App */\n"
"#contentTopBg{\n"
"	background-color: qlineargradient(spread:pad, x1:1, y1:1, x2:0, y2:0, stop:0 rgba(97, 67, 133, 255), stop:1 rgba(81, 99, 149, 255));\n"
"}\n"
"#contentBottom{\n"
"	border-top: 3px solid rgb(35,35,38);\n"
"}\n"
"\n"
"/* Top Buttons */\n"
"#rightButtons .QPushButton { background-color: rgba(255, 255, 255, 0); border: none;  border-radius: 5px; }\n"
"#rightButtons .QPushButton:hover { background-color: rgb(44, 49, 57); border-style: solid; border-radius: 4px; }\n"
"#rightButtons .QPushButton:pressed { background-color: #aa63ff; border-style: solid; border-radius: 4px; }\n"
"\n"
"/* Theme Settings */\n"
"#extraRightBox { background-color: rgb(35,35,38); }\n"
"#themeSettingsTo"
                        "pDetail { background-color: #aa63ff; }\n"
"\n"
"/* Bottom Bar */\n"
"#bottomBar { background-color: qlineargradient(spread:pad, x1:1, y1:0.511, x2:0, y2:0.517, stop:0 rgba(97, 67, 133, 255), stop:1 rgba(81, 99, 149, 255)); }\n"
"#bottomBar QLabel { font-size: 11px; color: rgb(113, 126, 149); padding-left: 10px; padding-right: 10px; padding-bottom: 2px; }\n"
"\n"
"/* CONTENT SETTINGS */\n"
"/* MENUS */\n"
"#contentSettings .QPushButton {\n"
"	background-position: left center;\n"
"    background-repeat: no-repeat;\n"
"	border: none;\n"
"	border-left: 22px solid transparent;\n"
"	background-color:transparent;\n"
"	text-align: left;\n"
"	padding-left: 44px;\n"
"}\n"
"#contentSettings .QPushButton:hover {\n"
"	background-color: rgb(35,35,38);\n"
"}\n"
"#contentSettings .QPushButton:pressed {\n"
"	background-color: #aa63ff;\n"
"	color: rgb(255, 255, 255);\n"
"}\n"
"\n"
"/* /////////////////////////////////////////////////////////////////////////////////////////////////\n"
"QTableWidget */\n"
"QTableWidget {\n"
"	bac"
                        "kground-color: transparent;\n"
"	padding: 10px;\n"
"	border-radius: 5px;\n"
"	gridline-color: rgb(35,35,38);\n"
"	border-bottom: 1px solid rgb(44, 49, 60);\n"
"}\n"
"QTableWidget::item{\n"
"	border-color: rgb(44, 49, 60);\n"
"	padding-left: 5px;\n"
"	padding-right: 5px;\n"
"	gridline-color: rgb(44, 49, 60);\n"
"}\n"
"QTableWidget::item:selected{\n"
"	background-color: #aa63ff;\n"
"}\n"
"QHeaderView::section{\n"
"	background-color: rgb(35,35,38);\n"
"	max-width: 30px;\n"
"	border: 1px solid rgb(35,35,38);\n"
"	border-style: none;\n"
"    border-bottom: 1px solid rgb(44, 49, 60);\n"
"    border-right: 1px solid rgb(44, 49, 60);\n"
"}\n"
"QTableWidget::horizontalHeader {\n"
"	background-color: rgb(35,35,38);\n"
"}\n"
"QHeaderView::section:horizontal\n"
"{\n"
"    border: 1px solid rgb(35,35,38);\n"
"	background-color: rgb(35,35,38);\n"
"	padding: 3px;\n"
"	border-top-left-radius: 7px;\n"
"    border-top-right-radius: 7px;\n"
"}\n"
"QHeaderView::section:vertical\n"
"{\n"
"    border: 1px solid rgb(44, 49, 60);\n"
""
                        "}\n"
"\n"
"/* /////////////////////////////////////////////////////////////////////////////////////////////////\n"
"LineEdit */\n"
"QLineEdit {\n"
"	background-color: rgb(35,35,38);\n"
"	border-radius: 5px;\n"
"	border: 2px solid rgb(35,35,38);\n"
"	padding-left: 10px;\n"
"	selection-color: rgb(255, 255, 255);\n"
"	selection-background-color: #aa63ff;\n"
"}\n"
"QLineEdit:hover {\n"
"	border: 2px solid rgb(64, 71, 88);\n"
"}\n"
"QLineEdit:focus {\n"
"	border: 2px solid rgb(91, 101, 124);\n"
"}\n"
"\n"
"/* /////////////////////////////////////////////////////////////////////////////////////////////////\n"
"PlainTextEdit */\n"
"QPlainTextEdit {\n"
"	background-color: rgb(27, 29, 35);\n"
"	border-radius: 5px;\n"
"	padding: 10px;\n"
"	selection-color: rgb(255, 255, 255);\n"
"	selection-background-color: rgb(0,94,217);\n"
"}\n"
"QPlainTextEdit  QScrollBar:vertical {\n"
"    width: 8px;\n"
" }\n"
"QPlainTextEdit  QScrollBar:horizontal {\n"
"    height: 8px;\n"
" }\n"
"QPlainTextEdit:hover {\n"
"	border: 2px solid rgb"
                        "(64, 71, 88);\n"
"}\n"
"QPlainTextEdit:focus {\n"
"	border: 2px solid rgb(91, 101, 124);\n"
"}\n"
"\n"
"/* /////////////////////////////////////////////////////////////////////////////////////////////////\n"
"ScrollBars */\n"
"QScrollBar:horizontal {\n"
"    border: none;\n"
"    background: rgb(52, 59, 72);\n"
"    height: 8px;\n"
"    margin: 0px 21px 0 21px;\n"
"	border-radius: 0px;\n"
"}\n"
"QScrollBar::handle:horizontal {\n"
"    background: #aa63ff;\n"
"    min-width: 25px;\n"
"	border-radius: 4px;\n"
"}\n"
"QScrollBar::add-line:horizontal {\n"
"    border: none;\n"
"    background: rgb(55, 63, 77);\n"
"    width: 20px;\n"
"	border-top-right-radius: 4px;\n"
"    border-bottom-right-radius: 4px;\n"
"    subcontrol-position: right;\n"
"    subcontrol-origin: margin;\n"
"}\n"
"QScrollBar::sub-line:horizontal {\n"
"    border: none;\n"
"    background: rgb(55, 63, 77);\n"
"    width: 20px;\n"
"	border-top-left-radius: 4px;\n"
"    border-bottom-left-radius: 4px;\n"
"    subcontrol-position: left;\n"
"    sub"
                        "control-origin: margin;\n"
"}\n"
"QScrollBar::up-arrow:horizontal, QScrollBar::down-arrow:horizontal\n"
"{\n"
"     background: none;\n"
"}\n"
"QScrollBar::add-page:horizontal, QScrollBar::sub-page:horizontal\n"
"{\n"
"     background: none;\n"
"}\n"
" QScrollBar:vertical {\n"
"	border: none;\n"
"    background: rgb(52, 59, 72);\n"
"    width: 8px;\n"
"    margin: 21px 0 21px 0;\n"
"	border-radius: 0px;\n"
" }\n"
" QScrollBar::handle:vertical {\n"
"	background: #aa63ff;\n"
"    min-height: 25px;\n"
"	border-radius: 4px;\n"
" }\n"
" QScrollBar::add-line:vertical {\n"
"     border: none;\n"
"    background: rgb(55, 63, 77);\n"
"     height: 20px;\n"
"	border-bottom-left-radius: 4px;\n"
"    border-bottom-right-radius: 4px;\n"
"     subcontrol-position: bottom;\n"
"     subcontrol-origin: margin;\n"
" }\n"
" QScrollBar::sub-line:vertical {\n"
"	border: none;\n"
"    background: rgb(55, 63, 77);\n"
"     height: 20px;\n"
"	border-top-left-radius: 4px;\n"
"    border-top-right-radius: 4px;\n"
"     subcontrol-posit"
                        "ion: top;\n"
"     subcontrol-origin: margin;\n"
" }\n"
" QScrollBar::up-arrow:vertical, QScrollBar::down-arrow:vertical {\n"
"     background: none;\n"
" }\n"
"\n"
" QScrollBar::add-page:vertical, QScrollBar::sub-page:vertical {\n"
"     background: none;\n"
" }\n"
"\n"
"/* /////////////////////////////////////////////////////////////////////////////////////////////////\n"
"CheckBox */\n"
"QCheckBox::indicator {\n"
"    border: 3px solid rgb(52, 59, 72);\n"
"	width: 15px;\n"
"	height: 15px;\n"
"	border-radius: 10px;\n"
"    background: rgb(44, 49, 60);\n"
"}\n"
"QCheckBox::indicator:hover {\n"
"    border: 3px solid rgb(58, 66, 81);\n"
"}\n"
"QCheckBox::indicator:checked {\n"
"    background: 3px solid rgb(52, 59, 72);\n"
"	border: 3px solid rgb(52, 59, 72);\n"
"	background-image: url(:/icons/images/icons/cil-check-alt.png);\n"
"}\n"
"\n"
"/* /////////////////////////////////////////////////////////////////////////////////////////////////\n"
"RadioButton */\n"
"QRadioButton::indicator {\n"
"    border: 3px so"
                        "lid rgb(52, 59, 72);\n"
"	width: 15px;\n"
"	height: 15px;\n"
"	border-radius: 10px;\n"
"    background: rgb(44, 49, 60);\n"
"}\n"
"QRadioButton::indicator:hover {\n"
"    border: 3px solid rgb(58, 66, 81);\n"
"}\n"
"QRadioButton::indicator:checked {\n"
"    background: 3px solid rgb(94, 106, 130);\n"
"	border: 3px solid rgb(52, 59, 72);\n"
"}\n"
"\n"
"/* /////////////////////////////////////////////////////////////////////////////////////////////////\n"
"ComboBox */\n"
"QComboBox{\n"
"	background-color: rgb(27, 29, 35);\n"
"	border-radius: 5px;\n"
"	border: 2px solid rgb(35,35,38);\n"
"	padding: 5px;\n"
"	padding-left: 10px;\n"
"}\n"
"QComboBox:hover{\n"
"	border: 2px solid rgb(64, 71, 88);\n"
"}\n"
"QComboBox::drop-down {\n"
"	subcontrol-origin: padding;\n"
"	subcontrol-position: top right;\n"
"	width: 25px;\n"
"	border-left-width: 3px;\n"
"	border-left-color: rgba(39, 44, 54, 150);\n"
"	border-left-style: solid;\n"
"	border-top-right-radius: 3px;\n"
"	border-bottom-right-radius: 3px;\n"
"	background-image: u"
                        "rl(:/icons/images/icons/cil-arrow-bottom.png);\n"
"	background-position: center;\n"
"	background-repeat: no-repeat;\n"
" }\n"
"QComboBox QAbstractItemView {\n"
"	color: #aa63ff;\n"
"	background-color: rgb(35,35,38);\n"
"	padding: 10px;\n"
"	selection-background-color: rgb(39, 44, 54);\n"
"}\n"
"\n"
"/* /////////////////////////////////////////////////////////////////////////////////////////////////\n"
"Sliders */\n"
"QSlider::groove:horizontal {\n"
"    border-radius: 5px;\n"
"    height: 10px;\n"
"	margin: 0px;\n"
"	background-color: rgb(52, 59, 72);\n"
"}\n"
"QSlider::groove:horizontal:hover {\n"
"	background-color: rgb(55, 62, 76);\n"
"}\n"
"QSlider::handle:horizontal {\n"
"    background-color: #aa63ff;\n"
"    border: none;\n"
"    height: 10px;\n"
"    width: 10px;\n"
"    margin: 0px;\n"
"	border-radius: 5px;\n"
"}\n"
"QSlider::handle:horizontal:hover {\n"
"    background-color: #aa63ff;\n"
"}\n"
"QSlider::handle:horizontal:pressed {\n"
"    background-color: #aa63ff;\n"
"}\n"
"\n"
"QSlider::groove:vert"
                        "ical {\n"
"    border-radius: 5px;\n"
"    width: 10px;\n"
"    margin: 0px;\n"
"	background-color: rgb(52, 59, 72);\n"
"}\n"
"QSlider::groove:vertical:hover {\n"
"	background-color: rgb(55, 62, 76);\n"
"}\n"
"QSlider::handle:vertical {\n"
"    background-color: #aa63ff;\n"
"	border: none;\n"
"    height: 10px;\n"
"    width: 10px;\n"
"    margin: 0px;\n"
"	border-radius: 5px;\n"
"}\n"
"QSlider::handle:vertical:hover {\n"
"    background-color: #aa63ff;\n"
"}\n"
"QSlider::handle:vertical:pressed {\n"
"    background-color: #aa63ff;\n"
"}\n"
"\n"
"/* /////////////////////////////////////////////////////////////////////////////////////////////////\n"
"CommandLinkButton */\n"
"QCommandLinkButton {\n"
"	color: #aa63ff;\n"
"	border-radius: 5px;\n"
"	padding: 5px;\n"
"}\n"
"QCommandLinkButton:hover {\n"
"	color: #fff;\n"
"	background-color: rgb(44, 49, 60);\n"
"}\n"
"QCommandLinkButton:pressed {\n"
"	color: #aa63ff;\n"
"	background-color: rgb(52, 58, 71);\n"
"}\n"
"\n"
"/* ///////////////////////////////////////////"
                        "//////////////////////////////////////////////////////\n"
"Button */\n"
"#pagesContainer QPushButton {\n"
"	border: 2px solid rgb(52, 59, 72);\n"
"	border-radius: 5px;\n"
"	background-color: rgb(52, 59, 72);\n"
"}\n"
"#pagesContainer QPushButton:hover {\n"
"	background-color: rgb(57, 65, 80);\n"
"	border: 2px solid rgb(61, 70, 86);\n"
"}\n"
"#pagesContainer QPushButton:pressed {\n"
"	background-color: rgb(35, 40, 49);\n"
"	border: 2px solid rgb(43, 50, 61);\n"
"}")
        self.bgApp = QFrame(self.styleSheet)
        self.bgApp.setObjectName(u"bgApp")
        self.bgApp.setGeometry(QRect(10, 10, 1260, 668))
        self.bgApp.setStyleSheet(u"")
        self.bgApp.setFrameShape(QFrame.NoFrame)
        self.bgApp.setFrameShadow(QFrame.Raised)
        self.appLayout = QHBoxLayout(self.bgApp)
        self.appLayout.setSpacing(0)
        self.appLayout.setObjectName(u"appLayout")
        self.appLayout.setContentsMargins(0, 0, 0, 0)
        self.leftMenuBg = QFrame(self.bgApp)
        self.leftMenuBg.setObjectName(u"leftMenuBg")
        self.leftMenuBg.setMinimumSize(QSize(60, 0))
        self.leftMenuBg.setMaximumSize(QSize(60, 16777215))
        self.leftMenuBg.setFrameShape(QFrame.NoFrame)
        self.leftMenuBg.setFrameShadow(QFrame.Raised)
        self.verticalLayout_3 = QVBoxLayout(self.leftMenuBg)
        self.verticalLayout_3.setSpacing(0)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.leftMenuFrame = QFrame(self.leftMenuBg)
        self.leftMenuFrame.setObjectName(u"leftMenuFrame")
        self.leftMenuFrame.setFrameShape(QFrame.NoFrame)
        self.leftMenuFrame.setFrameShadow(QFrame.Raised)
        self.verticalMenuLayout = QVBoxLayout(self.leftMenuFrame)
        self.verticalMenuLayout.setSpacing(0)
        self.verticalMenuLayout.setObjectName(u"verticalMenuLayout")
        self.verticalMenuLayout.setContentsMargins(0, 0, 0, 0)
        self.topLogoInfo_2 = QFrame(self.leftMenuFrame)
        self.topLogoInfo_2.setObjectName(u"topLogoInfo_2")
        self.topLogoInfo_2.setMinimumSize(QSize(0, 50))
        self.topLogoInfo_2.setMaximumSize(QSize(16777215, 50))
        self.topLogoInfo_2.setFrameShape(QFrame.NoFrame)
        self.topLogoInfo_2.setFrameShadow(QFrame.Raised)
        self.topLogo_2 = QFrame(self.topLogoInfo_2)
        self.topLogo_2.setObjectName(u"topLogo_2")
        self.topLogo_2.setGeometry(QRect(10, 10, 42, 42))
        self.topLogo_2.setMinimumSize(QSize(42, 42))
        self.topLogo_2.setMaximumSize(QSize(42, 42))
        self.topLogo_2.setStyleSheet(u"background-image: url(:/images/images/images/icon40.png);\n"
"background-position: center;\n"
"background-repeat: no-repeat;")
        self.topLogo_2.setFrameShape(QFrame.NoFrame)
        self.topLogo_2.setFrameShadow(QFrame.Raised)
        self.topLogo = QFrame(self.topLogo_2)
        self.topLogo.setObjectName(u"topLogo")
        self.topLogo.setGeometry(QRect(0, 0, 42, 42))
        self.topLogo.setMinimumSize(QSize(42, 42))
        self.topLogo.setMaximumSize(QSize(42, 42))
        self.topLogo.setSizeIncrement(QSize(0, 0))
        self.topLogo.setAutoFillBackground(False)
        self.topLogo.setStyleSheet(u"background-image: url(:/images/images/images/RSA30x30.png);\n"
"background-position: center;\n"
"background-color: transparent;")
        self.topLogo.setFrameShape(QFrame.NoFrame)
        self.topLogo.setFrameShadow(QFrame.Raised)
        self.titleLeftApp = QLabel(self.topLogoInfo_2)
        self.titleLeftApp.setObjectName(u"titleLeftApp")
        self.titleLeftApp.setGeometry(QRect(70, 8, 160, 20))
        font1 = QFont()
        font1.setFamilies([u"Raleway ExtraBold"])
        font1.setPointSize(12)
        font1.setBold(False)
        font1.setItalic(False)
        self.titleLeftApp.setFont(font1)
        self.titleLeftApp.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignTop)
        self.titleLeftDescription = QLabel(self.topLogoInfo_2)
        self.titleLeftDescription.setObjectName(u"titleLeftDescription")
        self.titleLeftDescription.setGeometry(QRect(70, 27, 160, 16))
        self.titleLeftDescription.setMaximumSize(QSize(16777215, 16))
        font2 = QFont()
        font2.setFamilies([u"Raleway Medium"])
        font2.setPointSize(10)
        font2.setBold(False)
        font2.setItalic(False)
        self.titleLeftDescription.setFont(font2)
        self.titleLeftDescription.setStyleSheet(u"font: 57 10pt \"Raleway Medium\";")
        self.titleLeftDescription.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignTop)

        self.verticalMenuLayout.addWidget(self.topLogoInfo_2)

        self.toggleBox = QFrame(self.leftMenuFrame)
        self.toggleBox.setObjectName(u"toggleBox")
        self.toggleBox.setMaximumSize(QSize(16777215, 45))
        self.toggleBox.setStyleSheet(u"")
        self.toggleBox.setFrameShape(QFrame.NoFrame)
        self.toggleBox.setFrameShadow(QFrame.Raised)
        self.verticalLayout_4 = QVBoxLayout(self.toggleBox)
        self.verticalLayout_4.setSpacing(0)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.verticalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.toggleButton = QPushButton(self.toggleBox)
        self.toggleButton.setObjectName(u"toggleButton")
        sizePolicy = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.toggleButton.sizePolicy().hasHeightForWidth())
        self.toggleButton.setSizePolicy(sizePolicy)
        self.toggleButton.setMinimumSize(QSize(0, 50))
        self.toggleButton.setFont(font)
        self.toggleButton.setCursor(QCursor(Qt.PointingHandCursor))
        self.toggleButton.setLayoutDirection(Qt.LeftToRight)
        self.toggleButton.setStyleSheet(u"background-image: url(:/icons/images/icons/icon_menu.png);\n"
"background-color: transparent;")

        self.verticalLayout_4.addWidget(self.toggleButton)


        self.verticalMenuLayout.addWidget(self.toggleBox)

        self.topMenu = QFrame(self.leftMenuFrame)
        self.topMenu.setObjectName(u"topMenu")
        self.topMenu.setFrameShape(QFrame.NoFrame)
        self.topMenu.setFrameShadow(QFrame.Raised)
        self.verticalLayout_8 = QVBoxLayout(self.topMenu)
        self.verticalLayout_8.setSpacing(0)
        self.verticalLayout_8.setObjectName(u"verticalLayout_8")
        self.verticalLayout_8.setContentsMargins(0, 0, 0, 0)
        self.btn_home = QPushButton(self.topMenu)
        self.btn_home.setObjectName(u"btn_home")
        sizePolicy.setHeightForWidth(self.btn_home.sizePolicy().hasHeightForWidth())
        self.btn_home.setSizePolicy(sizePolicy)
        self.btn_home.setMinimumSize(QSize(0, 45))
        self.btn_home.setFont(font)
        self.btn_home.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_home.setLayoutDirection(Qt.LeftToRight)
        self.btn_home.setStyleSheet(u"background-image: url(:/icons/images/icons/cil-home.png);")

        self.verticalLayout_8.addWidget(self.btn_home)

        self.btn_filespace = QPushButton(self.topMenu)
        self.btn_filespace.setObjectName(u"btn_filespace")
        sizePolicy.setHeightForWidth(self.btn_filespace.sizePolicy().hasHeightForWidth())
        self.btn_filespace.setSizePolicy(sizePolicy)
        self.btn_filespace.setMinimumSize(QSize(0, 45))
        self.btn_filespace.setFont(font)
        self.btn_filespace.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_filespace.setLayoutDirection(Qt.LeftToRight)
        self.btn_filespace.setStyleSheet(u"background-image: url(:/icons/images/icons/cil-file.png);")

        self.verticalLayout_8.addWidget(self.btn_filespace)

        self.btn_security = QPushButton(self.topMenu)
        self.btn_security.setObjectName(u"btn_security")
        sizePolicy.setHeightForWidth(self.btn_security.sizePolicy().hasHeightForWidth())
        self.btn_security.setSizePolicy(sizePolicy)
        self.btn_security.setMinimumSize(QSize(0, 45))
        self.btn_security.setFont(font)
        self.btn_security.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_security.setLayoutDirection(Qt.LeftToRight)
        self.btn_security.setStyleSheet(u"background-image: url(:/icons/images/icons/cil-lock-locked.png);")

        self.verticalLayout_8.addWidget(self.btn_security)

        self.btn_account = QPushButton(self.topMenu)
        self.btn_account.setObjectName(u"btn_account")
        sizePolicy.setHeightForWidth(self.btn_account.sizePolicy().hasHeightForWidth())
        self.btn_account.setSizePolicy(sizePolicy)
        self.btn_account.setMinimumSize(QSize(0, 45))
        self.btn_account.setFont(font)
        self.btn_account.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_account.setLayoutDirection(Qt.LeftToRight)
        self.btn_account.setStyleSheet(u"background-image: url(:/icons/images/icons/cil-user.png);")

        self.verticalLayout_8.addWidget(self.btn_account)

        self.btn_exit = QPushButton(self.topMenu)
        self.btn_exit.setObjectName(u"btn_exit")
        sizePolicy.setHeightForWidth(self.btn_exit.sizePolicy().hasHeightForWidth())
        self.btn_exit.setSizePolicy(sizePolicy)
        self.btn_exit.setMinimumSize(QSize(0, 45))
        self.btn_exit.setFont(font)
        self.btn_exit.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_exit.setLayoutDirection(Qt.LeftToRight)
        self.btn_exit.setStyleSheet(u"background-image: url(:/icons/images/icons/cil-x.png);")

        self.verticalLayout_8.addWidget(self.btn_exit)


        self.verticalMenuLayout.addWidget(self.topMenu)

        self.bottomMenu = QFrame(self.leftMenuFrame)
        self.bottomMenu.setObjectName(u"bottomMenu")
        self.bottomMenu.setFrameShape(QFrame.NoFrame)
        self.bottomMenu.setFrameShadow(QFrame.Raised)
        self.verticalLayout_9 = QVBoxLayout(self.bottomMenu)
        self.verticalLayout_9.setSpacing(0)
        self.verticalLayout_9.setObjectName(u"verticalLayout_9")
        self.verticalLayout_9.setContentsMargins(0, 0, 0, 0)
        self.toggleLeftBox = QPushButton(self.bottomMenu)
        self.toggleLeftBox.setObjectName(u"toggleLeftBox")
        sizePolicy.setHeightForWidth(self.toggleLeftBox.sizePolicy().hasHeightForWidth())
        self.toggleLeftBox.setSizePolicy(sizePolicy)
        self.toggleLeftBox.setMinimumSize(QSize(0, 45))
        self.toggleLeftBox.setFont(font)
        self.toggleLeftBox.setCursor(QCursor(Qt.PointingHandCursor))
        self.toggleLeftBox.setLayoutDirection(Qt.LeftToRight)
        self.toggleLeftBox.setStyleSheet(u"background-image: url(:/icons/images/icons/icon_settings.png);")

        self.verticalLayout_9.addWidget(self.toggleLeftBox)


        self.verticalMenuLayout.addWidget(self.bottomMenu, 0, Qt.AlignBottom)


        self.verticalLayout_3.addWidget(self.leftMenuFrame)


        self.appLayout.addWidget(self.leftMenuBg)

        self.extraLeftBox = QFrame(self.bgApp)
        self.extraLeftBox.setObjectName(u"extraLeftBox")
        self.extraLeftBox.setMinimumSize(QSize(0, 0))
        self.extraLeftBox.setMaximumSize(QSize(0, 16777215))
        self.extraLeftBox.setFrameShape(QFrame.NoFrame)
        self.extraLeftBox.setFrameShadow(QFrame.Raised)
        self.extraColumLayout = QVBoxLayout(self.extraLeftBox)
        self.extraColumLayout.setSpacing(0)
        self.extraColumLayout.setObjectName(u"extraColumLayout")
        self.extraColumLayout.setContentsMargins(0, 0, 0, 0)
        self.extraTopBg = QFrame(self.extraLeftBox)
        self.extraTopBg.setObjectName(u"extraTopBg")
        self.extraTopBg.setMinimumSize(QSize(0, 50))
        self.extraTopBg.setMaximumSize(QSize(16777215, 50))
        self.extraTopBg.setFrameShape(QFrame.NoFrame)
        self.extraTopBg.setFrameShadow(QFrame.Raised)
        self.verticalLayout_5 = QVBoxLayout(self.extraTopBg)
        self.verticalLayout_5.setSpacing(0)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.verticalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.extraTopLayout = QGridLayout()
        self.extraTopLayout.setObjectName(u"extraTopLayout")
        self.extraTopLayout.setHorizontalSpacing(10)
        self.extraTopLayout.setVerticalSpacing(0)
        self.extraTopLayout.setContentsMargins(10, -1, 10, -1)
        self.extraIcon = QFrame(self.extraTopBg)
        self.extraIcon.setObjectName(u"extraIcon")
        self.extraIcon.setMinimumSize(QSize(20, 0))
        self.extraIcon.setMaximumSize(QSize(20, 20))
        self.extraIcon.setStyleSheet(u"background-image: url(:/icons/images/icons/cil-user.png);")
        self.extraIcon.setFrameShape(QFrame.NoFrame)
        self.extraIcon.setFrameShadow(QFrame.Raised)

        self.extraTopLayout.addWidget(self.extraIcon, 0, 0, 1, 1)

        self.extraLabel = QLabel(self.extraTopBg)
        self.extraLabel.setObjectName(u"extraLabel")
        self.extraLabel.setMinimumSize(QSize(150, 0))

        self.extraTopLayout.addWidget(self.extraLabel, 0, 1, 1, 1)

        self.extraCloseColumnBtn = QPushButton(self.extraTopBg)
        self.extraCloseColumnBtn.setObjectName(u"extraCloseColumnBtn")
        self.extraCloseColumnBtn.setMinimumSize(QSize(28, 28))
        self.extraCloseColumnBtn.setMaximumSize(QSize(28, 28))
        self.extraCloseColumnBtn.setCursor(QCursor(Qt.PointingHandCursor))
        icon1 = QIcon()
        icon1.addFile(u":/icons/images/icons/icon_close.png", QSize(), QIcon.Normal, QIcon.Off)
        self.extraCloseColumnBtn.setIcon(icon1)
        self.extraCloseColumnBtn.setIconSize(QSize(20, 20))

        self.extraTopLayout.addWidget(self.extraCloseColumnBtn, 0, 2, 1, 1)


        self.verticalLayout_5.addLayout(self.extraTopLayout)


        self.extraColumLayout.addWidget(self.extraTopBg)

        self.extraContent = QFrame(self.extraLeftBox)
        self.extraContent.setObjectName(u"extraContent")
        self.extraContent.setFrameShape(QFrame.NoFrame)
        self.extraContent.setFrameShadow(QFrame.Raised)
        self.verticalLayout_12 = QVBoxLayout(self.extraContent)
        self.verticalLayout_12.setSpacing(0)
        self.verticalLayout_12.setObjectName(u"verticalLayout_12")
        self.verticalLayout_12.setContentsMargins(0, 0, 0, 0)
        self.extraTopMenu = QFrame(self.extraContent)
        self.extraTopMenu.setObjectName(u"extraTopMenu")
        self.extraTopMenu.setFrameShape(QFrame.NoFrame)
        self.extraTopMenu.setFrameShadow(QFrame.Raised)
        self.verticalLayout_11 = QVBoxLayout(self.extraTopMenu)
        self.verticalLayout_11.setSpacing(0)
        self.verticalLayout_11.setObjectName(u"verticalLayout_11")
        self.verticalLayout_11.setContentsMargins(0, 0, 0, 0)
        self.btn_share = QPushButton(self.extraTopMenu)
        self.btn_share.setObjectName(u"btn_share")
        sizePolicy.setHeightForWidth(self.btn_share.sizePolicy().hasHeightForWidth())
        self.btn_share.setSizePolicy(sizePolicy)
        self.btn_share.setMinimumSize(QSize(0, 45))
        self.btn_share.setFont(font)
        self.btn_share.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_share.setLayoutDirection(Qt.LeftToRight)
        self.btn_share.setStyleSheet(u"background-image: url(:/icons/images/icons/cil-share-boxed.png);")

        self.verticalLayout_11.addWidget(self.btn_share)

        self.btn_credits = QPushButton(self.extraTopMenu)
        self.btn_credits.setObjectName(u"btn_credits")
        sizePolicy.setHeightForWidth(self.btn_credits.sizePolicy().hasHeightForWidth())
        self.btn_credits.setSizePolicy(sizePolicy)
        self.btn_credits.setMinimumSize(QSize(0, 45))
        self.btn_credits.setFont(font)
        self.btn_credits.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_credits.setLayoutDirection(Qt.LeftToRight)
        self.btn_credits.setStyleSheet(u"background-image: url(:/icons/images/icons/cil-equalizer.png);")

        self.verticalLayout_11.addWidget(self.btn_credits)

        self.btn_more = QPushButton(self.extraTopMenu)
        self.btn_more.setObjectName(u"btn_more")
        sizePolicy.setHeightForWidth(self.btn_more.sizePolicy().hasHeightForWidth())
        self.btn_more.setSizePolicy(sizePolicy)
        self.btn_more.setMinimumSize(QSize(0, 45))
        self.btn_more.setFont(font)
        self.btn_more.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_more.setLayoutDirection(Qt.LeftToRight)
        self.btn_more.setStyleSheet(u"background-image: url(:/icons/images/icons/cil-layers.png);")

        self.verticalLayout_11.addWidget(self.btn_more)


        self.verticalLayout_12.addWidget(self.extraTopMenu, 0, Qt.AlignTop)

        self.extraCenter = QFrame(self.extraContent)
        self.extraCenter.setObjectName(u"extraCenter")
        self.extraCenter.setFrameShape(QFrame.NoFrame)
        self.extraCenter.setFrameShadow(QFrame.Raised)
        self.verticalLayout_10 = QVBoxLayout(self.extraCenter)
        self.verticalLayout_10.setObjectName(u"verticalLayout_10")
        self.credits = QTextEdit(self.extraCenter)
        self.credits.setObjectName(u"credits")
        self.credits.setMinimumSize(QSize(222, 0))
        self.credits.setStyleSheet(u"background: transparent;")
        self.credits.setFrameShape(QFrame.NoFrame)
        self.credits.setReadOnly(True)

        self.verticalLayout_10.addWidget(self.credits)


        self.verticalLayout_12.addWidget(self.extraCenter)

        self.extraBottom = QFrame(self.extraContent)
        self.extraBottom.setObjectName(u"extraBottom")
        self.extraBottom.setFrameShape(QFrame.NoFrame)
        self.extraBottom.setFrameShadow(QFrame.Raised)

        self.verticalLayout_12.addWidget(self.extraBottom)


        self.extraColumLayout.addWidget(self.extraContent)


        self.appLayout.addWidget(self.extraLeftBox)

        self.contentBox = QFrame(self.bgApp)
        self.contentBox.setObjectName(u"contentBox")
        self.contentBox.setFrameShape(QFrame.NoFrame)
        self.contentBox.setFrameShadow(QFrame.Raised)
        self.verticalLayout_2 = QVBoxLayout(self.contentBox)
        self.verticalLayout_2.setSpacing(0)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.contentTopBg = QFrame(self.contentBox)
        self.contentTopBg.setObjectName(u"contentTopBg")
        self.contentTopBg.setMinimumSize(QSize(0, 50))
        self.contentTopBg.setMaximumSize(QSize(16777215, 50))
        self.contentTopBg.setStyleSheet(u"")
        self.contentTopBg.setFrameShape(QFrame.NoFrame)
        self.contentTopBg.setFrameShadow(QFrame.Raised)
        self.horizontalLayout = QHBoxLayout(self.contentTopBg)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 10, 0)
        self.leftBox = QFrame(self.contentTopBg)
        self.leftBox.setObjectName(u"leftBox")
        sizePolicy1 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Preferred)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.leftBox.sizePolicy().hasHeightForWidth())
        self.leftBox.setSizePolicy(sizePolicy1)
        self.leftBox.setStyleSheet(u"")
        self.leftBox.setFrameShape(QFrame.NoFrame)
        self.leftBox.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_3 = QHBoxLayout(self.leftBox)
        self.horizontalLayout_3.setSpacing(0)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.titleRightInfo = QLabel(self.leftBox)
        self.titleRightInfo.setObjectName(u"titleRightInfo")
        sizePolicy2 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Expanding)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.titleRightInfo.sizePolicy().hasHeightForWidth())
        self.titleRightInfo.setSizePolicy(sizePolicy2)
        self.titleRightInfo.setMinimumSize(QSize(10000, 0))
        self.titleRightInfo.setMaximumSize(QSize(16777215, 45))
        font3 = QFont()
        font3.setFamilies([u"Raleway ExtraBold"])
        font3.setPointSize(10)
        font3.setBold(False)
        font3.setItalic(False)
        self.titleRightInfo.setFont(font3)
        self.titleRightInfo.setStyleSheet(u"font: 81 10pt \"Raleway ExtraBold\";")
        self.titleRightInfo.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.horizontalLayout_3.addWidget(self.titleRightInfo)


        self.horizontalLayout.addWidget(self.leftBox)

        self.rightButtons = QFrame(self.contentTopBg)
        self.rightButtons.setObjectName(u"rightButtons")
        self.rightButtons.setMinimumSize(QSize(0, 28))
        self.rightButtons.setFrameShape(QFrame.NoFrame)
        self.rightButtons.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_2 = QHBoxLayout(self.rightButtons)
        self.horizontalLayout_2.setSpacing(5)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.settingsTopBtn = QPushButton(self.rightButtons)
        self.settingsTopBtn.setObjectName(u"settingsTopBtn")
        self.settingsTopBtn.setMinimumSize(QSize(28, 28))
        self.settingsTopBtn.setMaximumSize(QSize(28, 28))
        self.settingsTopBtn.setCursor(QCursor(Qt.PointingHandCursor))
        icon2 = QIcon()
        icon2.addFile(u":/icons/images/icons/icon_settings.png", QSize(), QIcon.Normal, QIcon.Off)
        self.settingsTopBtn.setIcon(icon2)
        self.settingsTopBtn.setIconSize(QSize(20, 20))

        self.horizontalLayout_2.addWidget(self.settingsTopBtn)

        self.minimizeAppBtn = QPushButton(self.rightButtons)
        self.minimizeAppBtn.setObjectName(u"minimizeAppBtn")
        self.minimizeAppBtn.setMinimumSize(QSize(28, 28))
        self.minimizeAppBtn.setMaximumSize(QSize(28, 28))
        self.minimizeAppBtn.setCursor(QCursor(Qt.PointingHandCursor))
        icon3 = QIcon()
        icon3.addFile(u":/icons/images/icons/icon_minimize.png", QSize(), QIcon.Normal, QIcon.Off)
        self.minimizeAppBtn.setIcon(icon3)
        self.minimizeAppBtn.setIconSize(QSize(20, 20))

        self.horizontalLayout_2.addWidget(self.minimizeAppBtn)

        self.maximizeRestoreAppBtn = QPushButton(self.rightButtons)
        self.maximizeRestoreAppBtn.setObjectName(u"maximizeRestoreAppBtn")
        self.maximizeRestoreAppBtn.setMinimumSize(QSize(28, 28))
        self.maximizeRestoreAppBtn.setMaximumSize(QSize(28, 28))
        font4 = QFont()
        font4.setFamilies([u"Segoe UI"])
        font4.setPointSize(10)
        font4.setBold(False)
        font4.setItalic(False)
        font4.setStyleStrategy(QFont.PreferDefault)
        self.maximizeRestoreAppBtn.setFont(font4)
        self.maximizeRestoreAppBtn.setCursor(QCursor(Qt.PointingHandCursor))
        icon4 = QIcon()
        icon4.addFile(u":/icons/images/icons/icon_maximize.png", QSize(), QIcon.Normal, QIcon.Off)
        self.maximizeRestoreAppBtn.setIcon(icon4)
        self.maximizeRestoreAppBtn.setIconSize(QSize(20, 20))

        self.horizontalLayout_2.addWidget(self.maximizeRestoreAppBtn)

        self.closeAppBtn = QPushButton(self.rightButtons)
        self.closeAppBtn.setObjectName(u"closeAppBtn")
        self.closeAppBtn.setMinimumSize(QSize(28, 28))
        self.closeAppBtn.setMaximumSize(QSize(28, 28))
        self.closeAppBtn.setCursor(QCursor(Qt.PointingHandCursor))
        self.closeAppBtn.setIcon(icon1)
        self.closeAppBtn.setIconSize(QSize(20, 20))

        self.horizontalLayout_2.addWidget(self.closeAppBtn)


        self.horizontalLayout.addWidget(self.rightButtons, 0, Qt.AlignRight)


        self.verticalLayout_2.addWidget(self.contentTopBg)

        self.contentBottom = QFrame(self.contentBox)
        self.contentBottom.setObjectName(u"contentBottom")
        self.contentBottom.setFrameShape(QFrame.NoFrame)
        self.contentBottom.setFrameShadow(QFrame.Raised)
        self.verticalLayout_6 = QVBoxLayout(self.contentBottom)
        self.verticalLayout_6.setSpacing(0)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.verticalLayout_6.setContentsMargins(0, 0, 0, 0)
        self.content = QFrame(self.contentBottom)
        self.content.setObjectName(u"content")
        self.content.setFrameShape(QFrame.NoFrame)
        self.content.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_4 = QHBoxLayout(self.content)
        self.horizontalLayout_4.setSpacing(0)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.horizontalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.pagesContainer = QFrame(self.content)
        self.pagesContainer.setObjectName(u"pagesContainer")
        self.pagesContainer.setStyleSheet(u"")
        self.pagesContainer.setFrameShape(QFrame.NoFrame)
        self.pagesContainer.setFrameShadow(QFrame.Raised)
        self.verticalLayout_15 = QVBoxLayout(self.pagesContainer)
        self.verticalLayout_15.setSpacing(0)
        self.verticalLayout_15.setObjectName(u"verticalLayout_15")
        self.verticalLayout_15.setContentsMargins(10, 10, 10, 10)
        self.stackedWidget = QStackedWidget(self.pagesContainer)
        self.stackedWidget.setObjectName(u"stackedWidget")
        self.stackedWidget.setStyleSheet(u"background: transparent;")
        self.home = QWidget()
        self.home.setObjectName(u"home")
        self.home.setStyleSheet(u"/*background-image: url(:/images/images/images/salvation_inverted.png);*/\n"
"background-position: center;\n"
"background-repeat: no-repeat;")
        self.dashboardTitle = QLabel(self.home)
        self.dashboardTitle.setObjectName(u"dashboardTitle")
        self.dashboardTitle.setGeometry(QRect(0, 40, 1171, 41))
        self.dashboardTitle.setStyleSheet(u"color: rgb(255, 255, 255);\n"
"font: 57 18pt \"Raleway Medium\";")
        self.dashboardTitle.setLineWidth(1)
        self.dashboardTitle.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignTop)
        self.publicKeySA = QScrollArea(self.home)
        self.publicKeySA.setObjectName(u"publicKeySA")
        self.publicKeySA.setGeometry(QRect(180, 180, 341, 201))
        self.publicKeySA.setStyleSheet(u" QScrollBar:vertical {\n"
"    background: rgb(52, 59, 72);\n"
" }\n"
" QScrollBar:horizontal {\n"
"    background: rgb(52, 59, 72);\n"
" }")
        self.publicKeySA.setFrameShape(QFrame.NoFrame)
        self.publicKeySA.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.publicKeySA.setHorizontalScrollBarPolicy(Qt.ScrollBarAsNeeded)
        self.publicKeySA.setWidgetResizable(True)
        self.scrollAreaWidgetContents_2 = QWidget()
        self.scrollAreaWidgetContents_2.setObjectName(u"scrollAreaWidgetContents_2")
        self.scrollAreaWidgetContents_2.setGeometry(QRect(0, 0, 341, 201))
        self.scrollAreaWidgetContents_2.setStyleSheet(u" QScrollBar:vertical {\n"
"	border: none;\n"
"    background: rgb(52, 59, 72);\n"
"    width: 14px;\n"
"    margin: 21px 0 21px 0;\n"
"	border-radius: 0px;\n"
" }")
        self.horizontalLayout_13 = QHBoxLayout(self.scrollAreaWidgetContents_2)
        self.horizontalLayout_13.setObjectName(u"horizontalLayout_13")
        self.publicKeySA.setWidget(self.scrollAreaWidgetContents_2)
        self.privateKeySA = QScrollArea(self.home)
        self.privateKeySA.setObjectName(u"privateKeySA")
        self.privateKeySA.setGeometry(QRect(650, 180, 341, 201))
        self.privateKeySA.setStyleSheet(u" QScrollBar:vertical {\n"
"    background: rgb(52, 59, 72);\n"
" }\n"
" QScrollBar:horizontal {\n"
"    background: rgb(52, 59, 72);\n"
" }")
        self.privateKeySA.setFrameShape(QFrame.NoFrame)
        self.privateKeySA.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.privateKeySA.setHorizontalScrollBarPolicy(Qt.ScrollBarAsNeeded)
        self.privateKeySA.setWidgetResizable(True)
        self.scrollAreaWidgetContents_3 = QWidget()
        self.scrollAreaWidgetContents_3.setObjectName(u"scrollAreaWidgetContents_3")
        self.scrollAreaWidgetContents_3.setGeometry(QRect(0, 0, 341, 201))
        self.scrollAreaWidgetContents_3.setStyleSheet(u" QScrollBar:vertical {\n"
"	border: none;\n"
"    background: rgb(52, 59, 72);\n"
"    width: 14px;\n"
"    margin: 21px 0 21px 0;\n"
"	border-radius: 0px;\n"
" }")
        self.horizontalLayout_14 = QHBoxLayout(self.scrollAreaWidgetContents_3)
        self.horizontalLayout_14.setObjectName(u"horizontalLayout_14")
        self.privateKeySA.setWidget(self.scrollAreaWidgetContents_3)
        self.publicKeyDisplay = QPlainTextEdit(self.home)
        self.publicKeyDisplay.setObjectName(u"publicKeyDisplay")
        self.publicKeyDisplay.setGeometry(QRect(140, 149, 381, 231))
        self.publicKeyDisplay.setMinimumSize(QSize(200, 200))
        self.publicKeyDisplay.setStyleSheet(u"background-color: rgb(33, 37, 43);\n"
"color: rgb(203, 203, 203);\n"
"border-bottom-left-radius :0px;\n"
"border-bottom-right-radius :0px;")
        self.publicKeyDisplay.setReadOnly(True)
        self.privateKeyDisplay = QPlainTextEdit(self.home)
        self.privateKeyDisplay.setObjectName(u"privateKeyDisplay")
        self.privateKeyDisplay.setGeometry(QRect(650, 149, 381, 231))
        self.privateKeyDisplay.setMinimumSize(QSize(200, 200))
        self.privateKeyDisplay.setStyleSheet(u"background-color: rgb(33, 37, 43);\n"
"color: rgb(203, 203, 203);\n"
"border-bottom-left-radius :0px;")
        self.privateKeyDisplay.setReadOnly(True)
        self.privateKeyCheckbox = QCheckBox(self.home)
        self.privateKeyCheckbox.setObjectName(u"privateKeyCheckbox")
        self.privateKeyCheckbox.setGeometry(QRect(900, 380, 141, 31))
        self.privateKeyCheckbox.setAutoFillBackground(False)
        self.privateKeyCheckbox.setStyleSheet(u"font: 57 10pt \"Raleway Medium\";")
        self.privateKeyCheckbox.setChecked(False)
        self.privateKeyCheckbox.setTristate(False)
        self.copyPrivateKeyButton = QPushButton(self.home)
        self.copyPrivateKeyButton.setObjectName(u"copyPrivateKeyButton")
        self.copyPrivateKeyButton.setGeometry(QRect(650, 380, 241, 30))
        self.copyPrivateKeyButton.setMinimumSize(QSize(150, 30))
        font5 = QFont()
        font5.setFamilies([u"Raleway SemiBold"])
        font5.setPointSize(10)
        font5.setBold(False)
        font5.setItalic(False)
        self.copyPrivateKeyButton.setFont(font5)
        self.copyPrivateKeyButton.setCursor(QCursor(Qt.PointingHandCursor))
        self.copyPrivateKeyButton.setStyleSheet(u"background-color: rgb(52, 59, 72);\n"
"border-top-left-radius :0px;\n"
"border-top-right-radius :0px;\n"
"font: 63 10pt \"Raleway SemiBold\";")
        icon5 = QIcon()
        icon5.addFile(u":/icons/images/icons/cil-clone.png", QSize(), QIcon.Normal, QIcon.Off)
        self.copyPrivateKeyButton.setIcon(icon5)
        self.dashboardTitle_2 = QLabel(self.home)
        self.dashboardTitle_2.setObjectName(u"dashboardTitle_2")
        self.dashboardTitle_2.setGeometry(QRect(140, 120, 381, 21))
        self.dashboardTitle_2.setStyleSheet(u"font: 57 18pt \"Raleway Bold\";")
        self.dashboardTitle_2.setLineWidth(1)
        self.dashboardTitle_2.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignTop)
        self.dashboardTitle_3 = QLabel(self.home)
        self.dashboardTitle_3.setObjectName(u"dashboardTitle_3")
        self.dashboardTitle_3.setGeometry(QRect(650, 120, 381, 21))
        self.dashboardTitle_3.setStyleSheet(u"font: 57 18pt \"Raleway Bold\";")
        self.dashboardTitle_3.setLineWidth(1)
        self.dashboardTitle_3.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignTop)
        self.copyPublicKeyButton = QPushButton(self.home)
        self.copyPublicKeyButton.setObjectName(u"copyPublicKeyButton")
        self.copyPublicKeyButton.setGeometry(QRect(140, 380, 381, 30))
        self.copyPublicKeyButton.setMinimumSize(QSize(150, 30))
        self.copyPublicKeyButton.setFont(font5)
        self.copyPublicKeyButton.setCursor(QCursor(Qt.PointingHandCursor))
        self.copyPublicKeyButton.setStyleSheet(u"background-color: rgb(52, 59, 72);\n"
"border-top-left-radius :0px;\n"
"border-top-right-radius :0px;\n"
"font: 63 10pt \"Raleway SemiBold\";")
        self.copyPublicKeyButton.setIcon(icon5)
        self.topLogoInfo = QFrame(self.home)
        self.topLogoInfo.setObjectName(u"topLogoInfo")
        self.topLogoInfo.setGeometry(QRect(70, 50, 60, 50))
        self.topLogoInfo.setMinimumSize(QSize(0, 50))
        self.topLogoInfo.setMaximumSize(QSize(16777215, 50))
        self.topLogoInfo.setFrameShape(QFrame.NoFrame)
        self.topLogoInfo.setFrameShadow(QFrame.Raised)
        self.backer1_3 = QLabel(self.home)
        self.backer1_3.setObjectName(u"backer1_3")
        self.backer1_3.setGeometry(QRect(140, 440, 901, 31))
        sizePolicy2.setHeightForWidth(self.backer1_3.sizePolicy().hasHeightForWidth())
        self.backer1_3.setSizePolicy(sizePolicy2)
        self.backer1_3.setMaximumSize(QSize(16777215, 1000))
        self.backer1_3.setFont(font3)
        self.backer1_3.setStyleSheet(u"color: rgb(255, 255, 255);\n"
"background-color: rgb(255, 0, 0);\n"
"border-top-left-radius :14px;\n"
"border-bottom-left-radius :14px;\n"
"border-top-right-radius :14px;\n"
"border-bottom-right-radius :14px;\n"
"font: 81 10pt \"Raleway ExtraBold\";")
        self.backer1_3.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)
        self.backer1_3.setWordWrap(True)
        self.stackedWidget.addWidget(self.home)
        self.widgets = QWidget()
        self.widgets.setObjectName(u"widgets")
        self.widgets.setStyleSheet(u"b")
        self.verticalLayout = QVBoxLayout(self.widgets)
        self.verticalLayout.setSpacing(10)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(10, 10, 10, 10)
        self.row_1 = QFrame(self.widgets)
        self.row_1.setObjectName(u"row_1")
        self.row_1.setFrameShape(QFrame.StyledPanel)
        self.row_1.setFrameShadow(QFrame.Raised)
        self.verticalLayout_16 = QVBoxLayout(self.row_1)
        self.verticalLayout_16.setSpacing(0)
        self.verticalLayout_16.setObjectName(u"verticalLayout_16")
        self.verticalLayout_16.setContentsMargins(0, 0, 0, 0)
        self.frame_div_content_1 = QFrame(self.row_1)
        self.frame_div_content_1.setObjectName(u"frame_div_content_1")
        self.frame_div_content_1.setMinimumSize(QSize(0, 110))
        self.frame_div_content_1.setMaximumSize(QSize(16777215, 110))
        self.frame_div_content_1.setFrameShape(QFrame.NoFrame)
        self.frame_div_content_1.setFrameShadow(QFrame.Raised)
        self.verticalLayout_17 = QVBoxLayout(self.frame_div_content_1)
        self.verticalLayout_17.setSpacing(0)
        self.verticalLayout_17.setObjectName(u"verticalLayout_17")
        self.verticalLayout_17.setContentsMargins(0, 0, 0, 0)
        self.frame_title_wid_1 = QFrame(self.frame_div_content_1)
        self.frame_title_wid_1.setObjectName(u"frame_title_wid_1")
        self.frame_title_wid_1.setMaximumSize(QSize(16777215, 35))
        self.frame_title_wid_1.setFrameShape(QFrame.StyledPanel)
        self.frame_title_wid_1.setFrameShadow(QFrame.Raised)
        self.verticalLayout_18 = QVBoxLayout(self.frame_title_wid_1)
        self.verticalLayout_18.setObjectName(u"verticalLayout_18")
        self.labelBoxBlenderInstalation = QLabel(self.frame_title_wid_1)
        self.labelBoxBlenderInstalation.setObjectName(u"labelBoxBlenderInstalation")
        self.labelBoxBlenderInstalation.setFont(font)
        self.labelBoxBlenderInstalation.setStyleSheet(u"")

        self.verticalLayout_18.addWidget(self.labelBoxBlenderInstalation)


        self.verticalLayout_17.addWidget(self.frame_title_wid_1)

        self.frame_content_wid_1 = QFrame(self.frame_div_content_1)
        self.frame_content_wid_1.setObjectName(u"frame_content_wid_1")
        self.frame_content_wid_1.setFrameShape(QFrame.NoFrame)
        self.frame_content_wid_1.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_9 = QHBoxLayout(self.frame_content_wid_1)
        self.horizontalLayout_9.setObjectName(u"horizontalLayout_9")
        self.gridLayout = QGridLayout()
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setContentsMargins(-1, -1, -1, 0)
        self.pushButton = QPushButton(self.frame_content_wid_1)
        self.pushButton.setObjectName(u"pushButton")
        self.pushButton.setMinimumSize(QSize(150, 30))
        self.pushButton.setFont(font)
        self.pushButton.setCursor(QCursor(Qt.PointingHandCursor))
        self.pushButton.setStyleSheet(u"background-color: rgb(52, 59, 72);")
        icon6 = QIcon()
        icon6.addFile(u":/icons/images/icons/cil-folder-open.png", QSize(), QIcon.Normal, QIcon.Off)
        self.pushButton.setIcon(icon6)

        self.gridLayout.addWidget(self.pushButton, 0, 1, 1, 1)

        self.labelVersion_3 = QLabel(self.frame_content_wid_1)
        self.labelVersion_3.setObjectName(u"labelVersion_3")
        self.labelVersion_3.setStyleSheet(u"color: rgb(113, 126, 149);")
        self.labelVersion_3.setLineWidth(1)
        self.labelVersion_3.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.gridLayout.addWidget(self.labelVersion_3, 1, 0, 1, 2)

        self.lineEdit = QLineEdit(self.frame_content_wid_1)
        self.lineEdit.setObjectName(u"lineEdit")
        self.lineEdit.setMinimumSize(QSize(0, 30))
        self.lineEdit.setStyleSheet(u"background-color: rgb(33, 37, 43);")

        self.gridLayout.addWidget(self.lineEdit, 0, 0, 1, 1)


        self.horizontalLayout_9.addLayout(self.gridLayout)


        self.verticalLayout_17.addWidget(self.frame_content_wid_1)


        self.verticalLayout_16.addWidget(self.frame_div_content_1)


        self.verticalLayout.addWidget(self.row_1)

        self.row_2 = QFrame(self.widgets)
        self.row_2.setObjectName(u"row_2")
        self.row_2.setMinimumSize(QSize(0, 150))
        self.row_2.setFrameShape(QFrame.StyledPanel)
        self.row_2.setFrameShadow(QFrame.Raised)
        self.verticalLayout_19 = QVBoxLayout(self.row_2)
        self.verticalLayout_19.setObjectName(u"verticalLayout_19")
        self.gridLayout_2 = QGridLayout()
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.checkBox = QCheckBox(self.row_2)
        self.checkBox.setObjectName(u"checkBox")
        self.checkBox.setAutoFillBackground(False)
        self.checkBox.setStyleSheet(u"")

        self.gridLayout_2.addWidget(self.checkBox, 0, 0, 1, 1)

        self.radioButton = QRadioButton(self.row_2)
        self.radioButton.setObjectName(u"radioButton")
        self.radioButton.setStyleSheet(u"")

        self.gridLayout_2.addWidget(self.radioButton, 0, 1, 1, 1)

        self.verticalSlider = QSlider(self.row_2)
        self.verticalSlider.setObjectName(u"verticalSlider")
        self.verticalSlider.setStyleSheet(u"")
        self.verticalSlider.setOrientation(Qt.Vertical)

        self.gridLayout_2.addWidget(self.verticalSlider, 0, 2, 3, 1)

        self.verticalScrollBar = QScrollBar(self.row_2)
        self.verticalScrollBar.setObjectName(u"verticalScrollBar")
        self.verticalScrollBar.setStyleSheet(u" QScrollBar:vertical { background: rgb(52, 59, 72); }\n"
" QScrollBar:horizontal { background: rgb(52, 59, 72); }")
        self.verticalScrollBar.setOrientation(Qt.Vertical)

        self.gridLayout_2.addWidget(self.verticalScrollBar, 0, 4, 3, 1)

        self.scrollArea = QScrollArea(self.row_2)
        self.scrollArea.setObjectName(u"scrollArea")
        self.scrollArea.setStyleSheet(u" QScrollBar:vertical {\n"
"    background: rgb(52, 59, 72);\n"
" }\n"
" QScrollBar:horizontal {\n"
"    background: rgb(52, 59, 72);\n"
" }")
        self.scrollArea.setFrameShape(QFrame.NoFrame)
        self.scrollArea.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOn)
        self.scrollArea.setHorizontalScrollBarPolicy(Qt.ScrollBarAsNeeded)
        self.scrollArea.setWidgetResizable(True)
        self.scrollAreaWidgetContents = QWidget()
        self.scrollAreaWidgetContents.setObjectName(u"scrollAreaWidgetContents")
        self.scrollAreaWidgetContents.setGeometry(QRect(0, 0, 218, 218))
        self.scrollAreaWidgetContents.setStyleSheet(u" QScrollBar:vertical {\n"
"	border: none;\n"
"    background: rgb(52, 59, 72);\n"
"    width: 14px;\n"
"    margin: 21px 0 21px 0;\n"
"	border-radius: 0px;\n"
" }")
        self.horizontalLayout_11 = QHBoxLayout(self.scrollAreaWidgetContents)
        self.horizontalLayout_11.setObjectName(u"horizontalLayout_11")
        self.plainTextEdit = QPlainTextEdit(self.scrollAreaWidgetContents)
        self.plainTextEdit.setObjectName(u"plainTextEdit")
        self.plainTextEdit.setMinimumSize(QSize(200, 200))
        self.plainTextEdit.setStyleSheet(u"background-color: rgb(33, 37, 43);")

        self.horizontalLayout_11.addWidget(self.plainTextEdit)

        self.scrollArea.setWidget(self.scrollAreaWidgetContents)

        self.gridLayout_2.addWidget(self.scrollArea, 0, 5, 3, 1)

        self.comboBox = QComboBox(self.row_2)
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.setObjectName(u"comboBox")
        self.comboBox.setFont(font)
        self.comboBox.setAutoFillBackground(False)
        self.comboBox.setStyleSheet(u"background-color: rgb(33, 37, 43);")
        self.comboBox.setIconSize(QSize(16, 16))
        self.comboBox.setFrame(True)

        self.gridLayout_2.addWidget(self.comboBox, 1, 0, 1, 2)

        self.horizontalScrollBar = QScrollBar(self.row_2)
        self.horizontalScrollBar.setObjectName(u"horizontalScrollBar")
        sizePolicy.setHeightForWidth(self.horizontalScrollBar.sizePolicy().hasHeightForWidth())
        self.horizontalScrollBar.setSizePolicy(sizePolicy)
        self.horizontalScrollBar.setStyleSheet(u" QScrollBar:vertical { background: rgb(52, 59, 72); }\n"
" QScrollBar:horizontal { background: rgb(52, 59, 72); }")
        self.horizontalScrollBar.setOrientation(Qt.Horizontal)

        self.gridLayout_2.addWidget(self.horizontalScrollBar, 1, 3, 1, 1)

        self.commandLinkButton = QCommandLinkButton(self.row_2)
        self.commandLinkButton.setObjectName(u"commandLinkButton")
        self.commandLinkButton.setCursor(QCursor(Qt.PointingHandCursor))
        self.commandLinkButton.setStyleSheet(u"")
        icon7 = QIcon()
        icon7.addFile(u":/icons/images/icons/cil-link.png", QSize(), QIcon.Normal, QIcon.Off)
        self.commandLinkButton.setIcon(icon7)

        self.gridLayout_2.addWidget(self.commandLinkButton, 1, 6, 1, 1)

        self.horizontalSlider = QSlider(self.row_2)
        self.horizontalSlider.setObjectName(u"horizontalSlider")
        self.horizontalSlider.setStyleSheet(u"")
        self.horizontalSlider.setOrientation(Qt.Horizontal)

        self.gridLayout_2.addWidget(self.horizontalSlider, 2, 0, 1, 2)


        self.verticalLayout_19.addLayout(self.gridLayout_2)


        self.verticalLayout.addWidget(self.row_2)

        self.row_3 = QFrame(self.widgets)
        self.row_3.setObjectName(u"row_3")
        self.row_3.setMinimumSize(QSize(0, 150))
        self.row_3.setFrameShape(QFrame.StyledPanel)
        self.row_3.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_12 = QHBoxLayout(self.row_3)
        self.horizontalLayout_12.setSpacing(0)
        self.horizontalLayout_12.setObjectName(u"horizontalLayout_12")
        self.horizontalLayout_12.setContentsMargins(0, 0, 0, 0)
        self.tableWidget = QTableWidget(self.row_3)
        if (self.tableWidget.columnCount() < 4):
            self.tableWidget.setColumnCount(4)
        __qtablewidgetitem = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(0, __qtablewidgetitem)
        __qtablewidgetitem1 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(1, __qtablewidgetitem1)
        __qtablewidgetitem2 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(2, __qtablewidgetitem2)
        __qtablewidgetitem3 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(3, __qtablewidgetitem3)
        if (self.tableWidget.rowCount() < 16):
            self.tableWidget.setRowCount(16)
        font6 = QFont()
        font6.setFamilies([u"Segoe UI"])
        __qtablewidgetitem4 = QTableWidgetItem()
        __qtablewidgetitem4.setFont(font6);
        self.tableWidget.setVerticalHeaderItem(0, __qtablewidgetitem4)
        __qtablewidgetitem5 = QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(1, __qtablewidgetitem5)
        __qtablewidgetitem6 = QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(2, __qtablewidgetitem6)
        __qtablewidgetitem7 = QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(3, __qtablewidgetitem7)
        __qtablewidgetitem8 = QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(4, __qtablewidgetitem8)
        __qtablewidgetitem9 = QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(5, __qtablewidgetitem9)
        __qtablewidgetitem10 = QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(6, __qtablewidgetitem10)
        __qtablewidgetitem11 = QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(7, __qtablewidgetitem11)
        __qtablewidgetitem12 = QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(8, __qtablewidgetitem12)
        __qtablewidgetitem13 = QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(9, __qtablewidgetitem13)
        __qtablewidgetitem14 = QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(10, __qtablewidgetitem14)
        __qtablewidgetitem15 = QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(11, __qtablewidgetitem15)
        __qtablewidgetitem16 = QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(12, __qtablewidgetitem16)
        __qtablewidgetitem17 = QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(13, __qtablewidgetitem17)
        __qtablewidgetitem18 = QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(14, __qtablewidgetitem18)
        __qtablewidgetitem19 = QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(15, __qtablewidgetitem19)
        __qtablewidgetitem20 = QTableWidgetItem()
        self.tableWidget.setItem(0, 0, __qtablewidgetitem20)
        __qtablewidgetitem21 = QTableWidgetItem()
        self.tableWidget.setItem(0, 1, __qtablewidgetitem21)
        __qtablewidgetitem22 = QTableWidgetItem()
        self.tableWidget.setItem(0, 2, __qtablewidgetitem22)
        __qtablewidgetitem23 = QTableWidgetItem()
        self.tableWidget.setItem(0, 3, __qtablewidgetitem23)
        self.tableWidget.setObjectName(u"tableWidget")
        sizePolicy3 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        sizePolicy3.setHorizontalStretch(0)
        sizePolicy3.setVerticalStretch(0)
        sizePolicy3.setHeightForWidth(self.tableWidget.sizePolicy().hasHeightForWidth())
        self.tableWidget.setSizePolicy(sizePolicy3)
        palette = QPalette()
        brush = QBrush(QColor(221, 221, 221, 255))
        brush.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Active, QPalette.WindowText, brush)
        brush1 = QBrush(QColor(0, 0, 0, 0))
        brush1.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Active, QPalette.Button, brush1)
        palette.setBrush(QPalette.Active, QPalette.Text, brush)
        palette.setBrush(QPalette.Active, QPalette.ButtonText, brush)
        brush2 = QBrush(QColor(0, 0, 0, 255))
        brush2.setStyle(Qt.NoBrush)
        palette.setBrush(QPalette.Active, QPalette.Base, brush2)
        palette.setBrush(QPalette.Active, QPalette.Window, brush1)
        palette.setBrush(QPalette.Inactive, QPalette.WindowText, brush)
        palette.setBrush(QPalette.Inactive, QPalette.Button, brush1)
        palette.setBrush(QPalette.Inactive, QPalette.Text, brush)
        palette.setBrush(QPalette.Inactive, QPalette.ButtonText, brush)
        brush3 = QBrush(QColor(0, 0, 0, 255))
        brush3.setStyle(Qt.NoBrush)
        palette.setBrush(QPalette.Inactive, QPalette.Base, brush3)
        palette.setBrush(QPalette.Inactive, QPalette.Window, brush1)
        palette.setBrush(QPalette.Disabled, QPalette.WindowText, brush)
        palette.setBrush(QPalette.Disabled, QPalette.Button, brush1)
        palette.setBrush(QPalette.Disabled, QPalette.Text, brush)
        palette.setBrush(QPalette.Disabled, QPalette.ButtonText, brush)
        brush4 = QBrush(QColor(0, 0, 0, 255))
        brush4.setStyle(Qt.NoBrush)
        palette.setBrush(QPalette.Disabled, QPalette.Base, brush4)
        palette.setBrush(QPalette.Disabled, QPalette.Window, brush1)
        self.tableWidget.setPalette(palette)
        self.tableWidget.setFrameShape(QFrame.NoFrame)
        self.tableWidget.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOn)
        self.tableWidget.setSizeAdjustPolicy(QAbstractScrollArea.AdjustToContents)
        self.tableWidget.setEditTriggers(QAbstractItemView.NoEditTriggers)
        self.tableWidget.setSelectionMode(QAbstractItemView.SingleSelection)
        self.tableWidget.setSelectionBehavior(QAbstractItemView.SelectRows)
        self.tableWidget.setShowGrid(True)
        self.tableWidget.setGridStyle(Qt.SolidLine)
        self.tableWidget.setSortingEnabled(False)
        self.tableWidget.horizontalHeader().setVisible(False)
        self.tableWidget.horizontalHeader().setCascadingSectionResizes(True)
        self.tableWidget.horizontalHeader().setDefaultSectionSize(200)
        self.tableWidget.horizontalHeader().setStretchLastSection(True)
        self.tableWidget.verticalHeader().setVisible(False)
        self.tableWidget.verticalHeader().setCascadingSectionResizes(False)
        self.tableWidget.verticalHeader().setHighlightSections(False)
        self.tableWidget.verticalHeader().setStretchLastSection(True)

        self.horizontalLayout_12.addWidget(self.tableWidget)


        self.verticalLayout.addWidget(self.row_3)

        self.stackedWidget.addWidget(self.widgets)
        self.filespace = QWidget()
        self.filespace.setObjectName(u"filespace")
        self.filespaceTitle = QLabel(self.filespace)
        self.filespaceTitle.setObjectName(u"filespaceTitle")
        self.filespaceTitle.setGeometry(QRect(0, 40, 1171, 51))
        self.filespaceTitle.setStyleSheet(u"color: rgb(255, 255, 255);\n"
"font: 57 18pt \"Raleway Medium\";")
        self.filespaceTitle.setLineWidth(1)
        self.filespaceTitle.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignTop)
        self.filepathBox_2 = QLineEdit(self.filespace)
        self.filepathBox_2.setObjectName(u"filepathBox_2")
        self.filepathBox_2.setGeometry(QRect(360, 190, 461, 30))
        self.filepathBox_2.setMinimumSize(QSize(0, 30))
        self.filepathBox_2.setStyleSheet(u"background-color: rgb(33, 37, 43);\n"
"border-bottom-left-radius :0px;\n"
"border-bottom-right-radius :0px;\n"
"border-color :rgb(51, 51, 56);\n"
"border-bottom:none;\n"
"font: 57 10pt \"Raleway Medium\";")
        self.encryptButton_2 = QPushButton(self.filespace)
        self.encryptButton_2.setObjectName(u"encryptButton_2")
        self.encryptButton_2.setGeometry(QRect(370, 280, 221, 30))
        self.encryptButton_2.setMinimumSize(QSize(150, 30))
        self.encryptButton_2.setFont(font2)
        self.encryptButton_2.setCursor(QCursor(Qt.PointingHandCursor))
        self.encryptButton_2.setStyleSheet(u"background-color: rgb(35, 35, 38);\n"
"border-top-right-radius :0px;\n"
"border-bottom-right-radius :0px;\n"
"border-top-left-radius :14px;\n"
"border-bottom-left-radius :14px;\n"
"border-color :rgb(51, 51, 56);\n"
"font: 57 10pt \"Raleway Medium\";")
        icon8 = QIcon()
        icon8.addFile(u":/icons/images/icons/cil-lock-locked.png", QSize(), QIcon.Normal, QIcon.Off)
        self.encryptButton_2.setIcon(icon8)
        self.decryptButton_2 = QPushButton(self.filespace)
        self.decryptButton_2.setObjectName(u"decryptButton_2")
        self.decryptButton_2.setGeometry(QRect(590, 280, 221, 30))
        self.decryptButton_2.setMinimumSize(QSize(150, 30))
        self.decryptButton_2.setFont(font2)
        self.decryptButton_2.setCursor(QCursor(Qt.PointingHandCursor))
        self.decryptButton_2.setStyleSheet(u"background-color: rgb(35, 35, 38);\n"
"border-top-left-radius :0px;\n"
"border-bottom-left-radius :0px;\n"
"border-top-right-radius :14px;\n"
"border-bottom-right-radius :14px;\n"
"border-color :rgb(51, 51, 56);\n"
"font: 57 10pt \"Raleway Medium\";")
        icon9 = QIcon()
        icon9.addFile(u":/icons/images/icons/cil-lock-unlocked.png", QSize(), QIcon.Normal, QIcon.Off)
        self.decryptButton_2.setIcon(icon9)
        self.openFilepathButton_2 = QPushButton(self.filespace)
        self.openFilepathButton_2.setObjectName(u"openFilepathButton_2")
        self.openFilepathButton_2.setGeometry(QRect(360, 220, 461, 41))
        self.openFilepathButton_2.setMinimumSize(QSize(150, 30))
        self.openFilepathButton_2.setFont(font2)
        self.openFilepathButton_2.setCursor(QCursor(Qt.PointingHandCursor))
        self.openFilepathButton_2.setStyleSheet(u"background-color: rgb(35, 35, 38);\n"
"border-top-left-radius :0px;\n"
"border-top-right-radius :0px;\n"
"border-color :rgb(51, 51, 56);\n"
"font: 57 10pt \"Raleway Medium\";")
        self.openFilepathButton_2.setIcon(icon6)
        self.selectFileToEncryptText = QLabel(self.filespace)
        self.selectFileToEncryptText.setObjectName(u"selectFileToEncryptText")
        self.selectFileToEncryptText.setGeometry(QRect(290, 150, 601, 21))
        sizePolicy2.setHeightForWidth(self.selectFileToEncryptText.sizePolicy().hasHeightForWidth())
        self.selectFileToEncryptText.setSizePolicy(sizePolicy2)
        self.selectFileToEncryptText.setMaximumSize(QSize(16777215, 45))
        self.selectFileToEncryptText.setFont(font)
        self.selectFileToEncryptText.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)
        self.multiviewCheckbox_1 = QCheckBox(self.filespace)
        self.multiviewCheckbox_1.setObjectName(u"multiviewCheckbox_1")
        self.multiviewCheckbox_1.setGeometry(QRect(960, 140, 141, 31))
        self.multiviewCheckbox_1.setAutoFillBackground(False)
        self.multiviewCheckbox_1.setStyleSheet(u"font: 57 10pt \"Raleway Medium\";")
        self.multiviewCheckbox_1.setChecked(False)
        self.multiviewCheckbox_1.setTristate(False)
        self.currentDirectory_2 = QLabel(self.filespace)
        self.currentDirectory_2.setObjectName(u"currentDirectory_2")
        self.currentDirectory_2.setGeometry(QRect(290, 110, 581, 41))
        self.currentDirectory_2.setStyleSheet(u"color: rgb(220, 220, 220);\n"
"font: 57 10pt \"Raleway Medium\";")
        self.currentDirectory_2.setFrameShape(QFrame.NoFrame)
        self.currentDirectory_2.setLineWidth(1)
        self.currentDirectory_2.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)
        self.fileBrowserTree_2 = QTreeView(self.filespace)
        self.fileBrowserTree_2.setObjectName(u"fileBrowserTree_2")
        self.fileBrowserTree_2.setGeometry(QRect(40, 150, 851, 271))
        self.fileBrowserTree_2.setStyleSheet(u"background-color: rgb(35, 35, 38);\n"
"")
        self.fileBrowserTree_2.setFrameShape(QFrame.NoFrame)
        self.selectFileToEncryptText_2 = QLabel(self.filespace)
        self.selectFileToEncryptText_2.setObjectName(u"selectFileToEncryptText_2")
        self.selectFileToEncryptText_2.setGeometry(QRect(910, 120, 231, 21))
        sizePolicy2.setHeightForWidth(self.selectFileToEncryptText_2.sizePolicy().hasHeightForWidth())
        self.selectFileToEncryptText_2.setSizePolicy(sizePolicy2)
        self.selectFileToEncryptText_2.setMaximumSize(QSize(16777215, 45))
        self.selectFileToEncryptText_2.setFont(font)
        self.selectFileToEncryptText_2.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)
        self.parentDriveTitle_2 = QLabel(self.filespace)
        self.parentDriveTitle_2.setObjectName(u"parentDriveTitle_2")
        self.parentDriveTitle_2.setGeometry(QRect(920, 200, 211, 21))
        self.parentDriveTitle_2.setStyleSheet(u"")
        self.parentDriveTitle_2.setLineWidth(1)
        self.parentDriveTitle_2.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)
        self.driveInfoTitle_2 = QLabel(self.filespace)
        self.driveInfoTitle_2.setObjectName(u"driveInfoTitle_2")
        self.driveInfoTitle_2.setGeometry(QRect(920, 260, 211, 19))
        self.driveInfoTitle_2.setStyleSheet(u"")
        self.driveInfoTitle_2.setLineWidth(1)
        self.driveInfoTitle_2.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)
        self.driveInfo_2 = QLabel(self.filespace)
        self.driveInfo_2.setObjectName(u"driveInfo_2")
        self.driveInfo_2.setGeometry(QRect(920, 310, 211, 161))
        self.driveInfo_2.setStyleSheet(u"color: rgb(220, 220, 220);\n"
"font: 57 10pt \"Raleway Medium\";")
        self.driveInfo_2.setLineWidth(1)
        self.driveInfo_2.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignTop)
        self.driveInfo_2.setWordWrap(False)
        self.parentDriveSpace_2 = QProgressBar(self.filespace)
        self.parentDriveSpace_2.setObjectName(u"parentDriveSpace_2")
        self.parentDriveSpace_2.setGeometry(QRect(920, 230, 211, 16))
        self.parentDriveSpace_2.setStyleSheet(u"QProgressBar {\n"
"background-color: rgb(98, 114, 164);\n"
"	color: rgb(170, 99, 255);\n"
"border-style: none;\n"
"border-radius: 10px;\n"
"text-align: center;\n"
"	font: 57 10pt \"Raleway Medium\";\n"
"}\n"
"QProgressBar::chunk{\n"
"border-radius: 10px;\n"
"background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(81, 99, 149, 255), stop:1 rgba(255, 255, 255, 255));\n"
"}")
        self.parentDriveSpace_2.setValue(0)
        self.parentDrive_2 = QLabel(self.filespace)
        self.parentDrive_2.setObjectName(u"parentDrive_2")
        self.parentDrive_2.setGeometry(QRect(920, 290, 131, 21))
        self.parentDrive_2.setStyleSheet(u"color: rgb(220, 220, 220);\n"
"font: 57 10pt \"Raleway Medium\";")
        self.parentDrive_2.setLineWidth(1)
        self.parentDrive_2.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)
        self.openDirectory_2 = QPushButton(self.filespace)
        self.openDirectory_2.setObjectName(u"openDirectory_2")
        self.openDirectory_2.setGeometry(QRect(140, 110, 131, 41))
        self.openDirectory_2.setMinimumSize(QSize(10, 10))
        self.openDirectory_2.setMaximumSize(QSize(16777215, 50))
        self.openDirectory_2.setFont(font2)
        self.openDirectory_2.setCursor(QCursor(Qt.PointingHandCursor))
        self.openDirectory_2.setStyleSheet(u"color: rgb(220, 220, 220);\n"
"background-color: rgb(35, 35, 38);\n"
"border: none;\n"
"font: 57 10pt \"Raleway Medium\";")
        self.openDirectory_2.setIcon(icon6)
        self.goToDefault_2 = QPushButton(self.filespace)
        self.goToDefault_2.setObjectName(u"goToDefault_2")
        self.goToDefault_2.setGeometry(QRect(50, 450, 191, 30))
        self.goToDefault_2.setMinimumSize(QSize(150, 30))
        self.goToDefault_2.setFont(font2)
        self.goToDefault_2.setCursor(QCursor(Qt.PointingHandCursor))
        self.goToDefault_2.setStyleSheet(u"background-color: rgb(35, 35, 38);\n"
"border-bottom-left-radius :14px;\n"
"border-top-left-radius :14px;\n"
"border-top-right-radius :14px;\n"
"border-bottom-right-radius :14px;\n"
"border-color :rgb(51, 51, 56);\n"
"font: 57 10pt \"Raleway Medium\";")
        icon10 = QIcon()
        icon10.addFile(u":/icons/images/icons/cil-house.png", QSize(), QIcon.Normal, QIcon.Off)
        self.goToDefault_2.setIcon(icon10)
        self.defaultLocation_2 = QPushButton(self.filespace)
        self.defaultLocation_2.setObjectName(u"defaultLocation_2")
        self.defaultLocation_2.setGeometry(QRect(260, 450, 191, 30))
        self.defaultLocation_2.setMinimumSize(QSize(150, 30))
        self.defaultLocation_2.setFont(font2)
        self.defaultLocation_2.setCursor(QCursor(Qt.PointingHandCursor))
        self.defaultLocation_2.setStyleSheet(u"background-color: rgb(35, 35, 38);\n"
"border-top-left-radius :14px;\n"
"border-bottom-left-radius :14px;\n"
"border-top-right-radius :14px;\n"
"border-bottom-right-radius :14px;\n"
"border-color :rgb(51, 51, 56);\n"
"font: 57 10pt \"Raleway Medium\";")
        icon11 = QIcon()
        icon11.addFile(u":/icons/images/icons/cil-star.png", QSize(), QIcon.Normal, QIcon.Off)
        self.defaultLocation_2.setIcon(icon11)
        self.goBackButton_2 = QPushButton(self.filespace)
        self.goBackButton_2.setObjectName(u"goBackButton_2")
        self.goBackButton_2.setGeometry(QRect(30, 110, 111, 41))
        self.goBackButton_2.setMinimumSize(QSize(10, 10))
        self.goBackButton_2.setMaximumSize(QSize(16777215, 50))
        self.goBackButton_2.setFont(font2)
        self.goBackButton_2.setCursor(QCursor(Qt.PointingHandCursor))
        self.goBackButton_2.setStyleSheet(u"color: rgb(220, 220, 220);\n"
"background-color: rgb(35, 35, 38);\n"
"border: none;\n"
"font: 57 10pt \"Raleway Medium\";")
        icon12 = QIcon()
        icon12.addFile(u":/icons/images/icons/cil-arrow-circle-left.png", QSize(), QIcon.Normal, QIcon.Off)
        self.goBackButton_2.setIcon(icon12)
        self.multiviewDetailsBox = QLabel(self.filespace)
        self.multiviewDetailsBox.setObjectName(u"multiviewDetailsBox")
        self.multiviewDetailsBox.setGeometry(QRect(910, 190, 231, 251))
        self.multiviewDetailsBox.setStyleSheet(u"color: rgb(113, 126, 149);\n"
"background-color: rgb(35, 35, 38);\n"
"border-top-left-radius :7px;\n"
"border-top-right-radius :7px;\n"
"border-bottom-left-radius :7px;\n"
"border-bottom-right-radius :7px;")
        self.multiviewDetailsBox.setFrameShape(QFrame.NoFrame)
        self.multiviewDetailsBox.setLineWidth(1)
        self.multiviewDetailsBox.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)
        self.currentDirectoryText = QLabel(self.filespace)
        self.currentDirectoryText.setObjectName(u"currentDirectoryText")
        self.currentDirectoryText.setGeometry(QRect(40, 110, 851, 41))
        sizePolicy2.setHeightForWidth(self.currentDirectoryText.sizePolicy().hasHeightForWidth())
        self.currentDirectoryText.setSizePolicy(sizePolicy2)
        self.currentDirectoryText.setMinimumSize(QSize(0, 30))
        self.currentDirectoryText.setMaximumSize(QSize(16777215, 45))
        self.currentDirectoryText.setFont(font)
        self.currentDirectoryText.setStyleSheet(u"color: rgb(113, 126, 149);\n"
"background-color: rgb(35, 35, 38);\n"
"border-top-left-radius :7px;\n"
"border-top-right-radius :7px;")
        self.currentDirectoryText.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)
        self.announceBox = QLabel(self.filespace)
        self.announceBox.setObjectName(u"announceBox")
        self.announceBox.setGeometry(QRect(70, 540, 1031, 31))
        self.announceBox.setStyleSheet(u"background-color: rgb(206, 55, 8);border-top-left-radius :15px;border-top-right-radius :15px;border-bottom-left-radius :15px;border-bottom-right-radius :15px;\n"
"font: 81 10pt \"Raleway ExtraBold\";")
        self.announceBox.setFrameShape(QFrame.Panel)
        self.announceBox.setFrameShadow(QFrame.Raised)
        self.announceBox.setLineWidth(0)
        self.announceBox.setTextFormat(Qt.RichText)
        self.announceBox.setScaledContents(False)
        self.announceBox.setAlignment(Qt.AlignCenter)
        self.announceBox.setWordWrap(False)
        self.border1 = QLabel(self.filespace)
        self.border1.setObjectName(u"border1")
        self.border1.setGeometry(QRect(40, 420, 851, 21))
        sizePolicy2.setHeightForWidth(self.border1.sizePolicy().hasHeightForWidth())
        self.border1.setSizePolicy(sizePolicy2)
        self.border1.setMaximumSize(QSize(16777215, 45))
        self.border1.setFont(font)
        self.border1.setStyleSheet(u"color: rgb(113, 126, 149);\n"
"background-color: rgb(35, 35, 38);\n"
"border-bottom-left-radius :7px;\n"
"border-bottom-right-radius :7px;")
        self.border1.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)
        self.border2 = QLabel(self.filespace)
        self.border2.setObjectName(u"border2")
        self.border2.setGeometry(QRect(30, 110, 20, 331))
        sizePolicy2.setHeightForWidth(self.border2.sizePolicy().hasHeightForWidth())
        self.border2.setSizePolicy(sizePolicy2)
        self.border2.setMaximumSize(QSize(16777215, 1000))
        self.border2.setFont(font)
        self.border2.setStyleSheet(u"color: rgb(113, 126, 149);\n"
"background-color: rgb(35, 35, 38);\n"
"border-bottom-left-radius :7px;\n"
"border-top-left-radius :7px;")
        self.border2.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)
        self.encryptButton_3 = QPushButton(self.filespace)
        self.encryptButton_3.setObjectName(u"encryptButton_3")
        self.encryptButton_3.setGeometry(QRect(470, 450, 191, 30))
        self.encryptButton_3.setMinimumSize(QSize(150, 30))
        self.encryptButton_3.setFont(font2)
        self.encryptButton_3.setCursor(QCursor(Qt.PointingHandCursor))
        self.encryptButton_3.setStyleSheet(u"background-color: rgb(35, 35, 38);\n"
"border-bottom-left-radius :14px;\n"
"border-top-left-radius :14px;\n"
"border-top-right-radius :14px;\n"
"border-bottom-right-radius :14px;\n"
"border-color :rgb(51, 51, 56);\n"
"font: 57 10pt \"Raleway Medium\";")
        self.encryptButton_3.setIcon(icon8)
        self.decryptButton_3 = QPushButton(self.filespace)
        self.decryptButton_3.setObjectName(u"decryptButton_3")
        self.decryptButton_3.setGeometry(QRect(680, 450, 191, 30))
        self.decryptButton_3.setMinimumSize(QSize(150, 30))
        self.decryptButton_3.setFont(font2)
        self.decryptButton_3.setCursor(QCursor(Qt.PointingHandCursor))
        self.decryptButton_3.setStyleSheet(u"background-color: rgb(35, 35, 38);\n"
"border-bottom-left-radius :14px;\n"
"border-top-left-radius :14px;\n"
"border-top-right-radius :14px;\n"
"border-bottom-right-radius :14px;\n"
"border-color :rgb(51, 51, 56);\n"
"font: 57 10pt \"Raleway Medium\";")
        self.decryptButton_3.setIcon(icon9)
        self.closePopup = QPushButton(self.filespace)
        self.closePopup.setObjectName(u"closePopup")
        self.closePopup.setGeometry(QRect(1070, 540, 31, 31))
        self.closePopup.setMinimumSize(QSize(30, 30))
        self.closePopup.setFont(font)
        self.closePopup.setCursor(QCursor(Qt.PointingHandCursor))
        self.closePopup.setStyleSheet(u"border: none;")
        icon13 = QIcon()
        icon13.addFile(u":/icons/images/icons/cil-x-circle.png", QSize(), QIcon.Normal, QIcon.Off)
        self.closePopup.setIcon(icon13)
        self.closePopup.setFlat(False)
        self.border1_2 = QLabel(self.filespace)
        self.border1_2.setObjectName(u"border1_2")
        self.border1_2.setGeometry(QRect(30, 150, 861, 1))
        sizePolicy2.setHeightForWidth(self.border1_2.sizePolicy().hasHeightForWidth())
        self.border1_2.setSizePolicy(sizePolicy2)
        self.border1_2.setMaximumSize(QSize(16777215, 1))
        self.border1_2.setFont(font)
        self.border1_2.setStyleSheet(u"background-color: rgb(52, 59, 72);\n"
"\n"
"")
        self.border1_2.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)
        self.border1_3 = QLabel(self.filespace)
        self.border1_3.setObjectName(u"border1_3")
        self.border1_3.setGeometry(QRect(280, 110, 1, 41))
        sizePolicy2.setHeightForWidth(self.border1_3.sizePolicy().hasHeightForWidth())
        self.border1_3.setSizePolicy(sizePolicy2)
        self.border1_3.setMinimumSize(QSize(0, 20))
        self.border1_3.setMaximumSize(QSize(1, 100000))
        self.border1_3.setFont(font)
        self.border1_3.setStyleSheet(u"background-color: rgb(52, 59, 72);\n"
"\n"
"")
        self.border1_3.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)
        self.backer1 = QLabel(self.filespace)
        self.backer1.setObjectName(u"backer1")
        self.backer1.setGeometry(QRect(290, 110, 601, 251))
        sizePolicy2.setHeightForWidth(self.backer1.sizePolicy().hasHeightForWidth())
        self.backer1.setSizePolicy(sizePolicy2)
        self.backer1.setMaximumSize(QSize(16777215, 1000))
        self.backer1.setFont(font)
        self.backer1.setStyleSheet(u"color: rgb(113, 126, 149);\n"
"background-color: rgb(35, 35, 38);\n"
"border-top-left-radius :14px;\n"
"border-bottom-left-radius :14px;\n"
"border-top-right-radius :14px;\n"
"border-bottom-right-radius :14px;")
        self.backer1.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)
        self.multiviewDetailsBox_2 = QLabel(self.filespace)
        self.multiviewDetailsBox_2.setObjectName(u"multiviewDetailsBox_2")
        self.multiviewDetailsBox_2.setGeometry(QRect(910, 110, 231, 71))
        self.multiviewDetailsBox_2.setStyleSheet(u"color: rgb(113, 126, 149);\n"
"background-color: rgb(35, 35, 38);\n"
"border-top-left-radius :7px;\n"
"border-top-right-radius :7px;\n"
"border-bottom-left-radius :7px;\n"
"border-bottom-right-radius :7px;")
        self.multiviewDetailsBox_2.setFrameShape(QFrame.NoFrame)
        self.multiviewDetailsBox_2.setLineWidth(1)
        self.multiviewDetailsBox_2.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)
        self.stackedWidget.addWidget(self.filespace)
        self.backer1.raise_()
        self.multiviewDetailsBox_2.raise_()
        self.fileBrowserTree_2.raise_()
        self.border2.raise_()
        self.border1.raise_()
        self.currentDirectoryText.raise_()
        self.currentDirectory_2.raise_()
        self.multiviewDetailsBox.raise_()
        self.filespaceTitle.raise_()
        self.multiviewCheckbox_1.raise_()
        self.selectFileToEncryptText_2.raise_()
        self.parentDriveTitle_2.raise_()
        self.driveInfoTitle_2.raise_()
        self.driveInfo_2.raise_()
        self.parentDriveSpace_2.raise_()
        self.parentDrive_2.raise_()
        self.openDirectory_2.raise_()
        self.goToDefault_2.raise_()
        self.defaultLocation_2.raise_()
        self.goBackButton_2.raise_()
        self.announceBox.raise_()
        self.encryptButton_3.raise_()
        self.decryptButton_3.raise_()
        self.closePopup.raise_()
        self.border1_2.raise_()
        self.border1_3.raise_()
        self.encryptButton_2.raise_()
        self.filepathBox_2.raise_()
        self.decryptButton_2.raise_()
        self.openFilepathButton_2.raise_()
        self.selectFileToEncryptText.raise_()
        self.Security = QWidget()
        self.Security.setObjectName(u"Security")
        self.dashboardTitle_10 = QLabel(self.Security)
        self.dashboardTitle_10.setObjectName(u"dashboardTitle_10")
        self.dashboardTitle_10.setGeometry(QRect(0, 40, 1171, 41))
        self.dashboardTitle_10.setStyleSheet(u"font: 57 18pt \"Raleway Medium\";")
        self.dashboardTitle_10.setLineWidth(1)
        self.dashboardTitle_10.setAlignment(Qt.AlignHCenter|Qt.AlignTop)
        self.dashboardTitle_11 = QLabel(self.Security)
        self.dashboardTitle_11.setObjectName(u"dashboardTitle_11")
        self.dashboardTitle_11.setGeometry(QRect(680, 120, 121, 41))
        self.dashboardTitle_11.setStyleSheet(u"font: 81 14pt \"Raleway ExtraBold\";")
        self.dashboardTitle_11.setLineWidth(1)
        self.dashboardTitle_11.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignTop)
        self.dangerBorder = QLabel(self.Security)
        self.dangerBorder.setObjectName(u"dangerBorder")
        self.dangerBorder.setGeometry(QRect(670, 120, 491, 121))
        self.dangerBorder.setStyleSheet(u"border: 1px double;\n"
"border-color: rgb(255, 0, 0);")
        self.dangerBorder.setLineWidth(1)
        self.dangerBorder.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignTop)
        self.regenkeysWidget = QWidget(self.Security)
        self.regenkeysWidget.setObjectName(u"regenkeysWidget")
        self.regenkeysWidget.setGeometry(QRect(680, 150, 151, 21))
        self.changeBitLength = QWidget(self.Security)
        self.changeBitLength.setObjectName(u"changeBitLength")
        self.changeBitLength.setGeometry(QRect(680, 180, 151, 21))
        self.signAndVerify = QPushButton(self.Security)
        self.signAndVerify.setObjectName(u"signAndVerify")
        self.signAndVerify.setGeometry(QRect(20, 120, 191, 30))
        self.signAndVerify.setMinimumSize(QSize(150, 30))
        self.signAndVerify.setFont(font2)
        self.signAndVerify.setCursor(QCursor(Qt.PointingHandCursor))
        self.signAndVerify.setStyleSheet(u"background-color: rgb(35, 35, 38);\n"
"border-bottom-left-radius :14px;\n"
"border-top-left-radius :14px;\n"
"border-top-right-radius :14px;\n"
"border-bottom-right-radius :14px;\n"
"border-color :rgb(51, 51, 56);\n"
"font: 57 10pt \"Raleway Medium\";")
        icon14 = QIcon()
        icon14.addFile(u":/icons/images/icons/cil-fingerprint.png", QSize(), QIcon.Normal, QIcon.Off)
        self.signAndVerify.setIcon(icon14)
        self.signFile = QPushButton(self.Security)
        self.signFile.setObjectName(u"signFile")
        self.signFile.setGeometry(QRect(60, 160, 150, 30))
        self.signFile.setMinimumSize(QSize(150, 30))
        self.signFile.setFont(font2)
        self.signFile.setCursor(QCursor(Qt.PointingHandCursor))
        self.signFile.setStyleSheet(u"background-color: rgb(35, 35, 38);\n"
"border-bottom-left-radius :14px;\n"
"border-top-left-radius :14px;\n"
"border-top-right-radius :14px;\n"
"border-bottom-right-radius :14px;\n"
"border-color :rgb(51, 51, 56);\n"
"font: 57 10pt \"Raleway Medium\";")
        self.signFile.setIcon(icon14)
        self.verifySignature = QPushButton(self.Security)
        self.verifySignature.setObjectName(u"verifySignature")
        self.verifySignature.setGeometry(QRect(60, 200, 150, 30))
        self.verifySignature.setMinimumSize(QSize(150, 30))
        self.verifySignature.setFont(font2)
        self.verifySignature.setCursor(QCursor(Qt.PointingHandCursor))
        self.verifySignature.setStyleSheet(u"background-color: rgb(35, 35, 38);\n"
"border-bottom-left-radius :14px;\n"
"border-top-left-radius :14px;\n"
"border-top-right-radius :14px;\n"
"border-bottom-right-radius :14px;\n"
"border-color :rgb(51, 51, 56);\n"
"font: 57 10pt \"Raleway Medium\";")
        icon15 = QIcon()
        icon15.addFile(u":/icons/images/icons/cil-check-circle.png", QSize(), QIcon.Normal, QIcon.Off)
        self.verifySignature.setIcon(icon15)
        self.line = QFrame(self.Security)
        self.line.setObjectName(u"line")
        self.line.setGeometry(QRect(30, 150, 16, 31))
        self.line.setStyleSheet(u"color: rgb(170, 99, 255);")
        self.line.setFrameShadow(QFrame.Plain)
        self.line.setLineWidth(5)
        self.line.setFrameShape(QFrame.VLine)
        self.line_2 = QFrame(self.Security)
        self.line_2.setObjectName(u"line_2")
        self.line_2.setGeometry(QRect(40, 170, 21, 16))
        self.line_2.setStyleSheet(u"color: rgb(170, 99, 255);")
        self.line_2.setFrameShadow(QFrame.Plain)
        self.line_2.setLineWidth(5)
        self.line_2.setFrameShape(QFrame.HLine)
        self.line_3 = QFrame(self.Security)
        self.line_3.setObjectName(u"line_3")
        self.line_3.setGeometry(QRect(30, 180, 16, 41))
        self.line_3.setStyleSheet(u"color: rgb(170, 99, 255);")
        self.line_3.setFrameShadow(QFrame.Plain)
        self.line_3.setLineWidth(5)
        self.line_3.setFrameShape(QFrame.VLine)
        self.line_4 = QFrame(self.Security)
        self.line_4.setObjectName(u"line_4")
        self.line_4.setGeometry(QRect(40, 210, 21, 16))
        self.line_4.setStyleSheet(u"color: rgb(170, 99, 255);")
        self.line_4.setFrameShadow(QFrame.Plain)
        self.line_4.setLineWidth(5)
        self.line_4.setFrameShape(QFrame.HLine)
        self.dangerZone3Widget = QWidget(self.Security)
        self.dangerZone3Widget.setObjectName(u"dangerZone3Widget")
        self.dangerZone3Widget.setGeometry(QRect(680, 210, 151, 21))
        self.generateChecksum = QPushButton(self.Security)
        self.generateChecksum.setObjectName(u"generateChecksum")
        self.generateChecksum.setGeometry(QRect(240, 120, 191, 30))
        self.generateChecksum.setMinimumSize(QSize(150, 30))
        self.generateChecksum.setFont(font2)
        self.generateChecksum.setCursor(QCursor(Qt.PointingHandCursor))
        self.generateChecksum.setStyleSheet(u"background-color: rgb(35, 35, 38);\n"
"border-bottom-left-radius :14px;\n"
"border-top-left-radius :14px;\n"
"border-top-right-radius :14px;\n"
"border-bottom-right-radius :14px;\n"
"border-color :rgb(51, 51, 56);\n"
"font: 57 10pt \"Raleway Medium\";")
        icon16 = QIcon()
        icon16.addFile(u":/icons/images/icons/cil-tags.png", QSize(), QIcon.Normal, QIcon.Off)
        self.generateChecksum.setIcon(icon16)
        self.line_5 = QFrame(self.Security)
        self.line_5.setObjectName(u"line_5")
        self.line_5.setGeometry(QRect(250, 180, 16, 41))
        self.line_5.setStyleSheet(u"color: rgb(4, 239, 188)")
        self.line_5.setFrameShadow(QFrame.Plain)
        self.line_5.setLineWidth(5)
        self.line_5.setFrameShape(QFrame.VLine)
        self.line_6 = QFrame(self.Security)
        self.line_6.setObjectName(u"line_6")
        self.line_6.setGeometry(QRect(260, 210, 21, 16))
        self.line_6.setStyleSheet(u"color: rgb(4, 239, 188)")
        self.line_6.setFrameShadow(QFrame.Plain)
        self.line_6.setLineWidth(5)
        self.line_6.setFrameShape(QFrame.HLine)
        self.line_7 = QFrame(self.Security)
        self.line_7.setObjectName(u"line_7")
        self.line_7.setGeometry(QRect(250, 150, 16, 31))
        self.line_7.setStyleSheet(u"color: rgb(4, 239, 188)")
        self.line_7.setFrameShadow(QFrame.Plain)
        self.line_7.setLineWidth(5)
        self.line_7.setFrameShape(QFrame.VLine)
        self.line_8 = QFrame(self.Security)
        self.line_8.setObjectName(u"line_8")
        self.line_8.setGeometry(QRect(260, 170, 21, 16))
        self.line_8.setStyleSheet(u"color: rgb(4, 239, 188)")
        self.line_8.setFrameShadow(QFrame.Plain)
        self.line_8.setLineWidth(5)
        self.line_8.setFrameShape(QFrame.HLine)
        self.sha256 = QPushButton(self.Security)
        self.sha256.setObjectName(u"sha256")
        self.sha256.setGeometry(QRect(280, 160, 150, 30))
        self.sha256.setMinimumSize(QSize(150, 30))
        self.sha256.setFont(font2)
        self.sha256.setCursor(QCursor(Qt.PointingHandCursor))
        self.sha256.setStyleSheet(u"background-color: rgb(35, 35, 38);\n"
"border-bottom-left-radius :14px;\n"
"border-top-left-radius :14px;\n"
"border-top-right-radius :14px;\n"
"border-bottom-right-radius :14px;\n"
"border-color :rgb(51, 51, 56);\n"
"font: 57 10pt \"Raleway Medium\";")
        icon17 = QIcon()
        icon17.addFile(u":/icons/images/icons/cil-file.png", QSize(), QIcon.Normal, QIcon.Off)
        self.sha256.setIcon(icon17)
        self.sha384 = QPushButton(self.Security)
        self.sha384.setObjectName(u"sha384")
        self.sha384.setGeometry(QRect(280, 200, 150, 30))
        self.sha384.setMinimumSize(QSize(150, 30))
        self.sha384.setFont(font2)
        self.sha384.setCursor(QCursor(Qt.PointingHandCursor))
        self.sha384.setStyleSheet(u"background-color: rgb(35, 35, 38);\n"
"border-bottom-left-radius :14px;\n"
"border-top-left-radius :14px;\n"
"border-top-right-radius :14px;\n"
"border-bottom-right-radius :14px;\n"
"border-color :rgb(51, 51, 56);\n"
"font: 57 10pt \"Raleway Medium\";")
        self.sha384.setIcon(icon17)
        self.sha512 = QPushButton(self.Security)
        self.sha512.setObjectName(u"sha512")
        self.sha512.setGeometry(QRect(280, 240, 150, 30))
        self.sha512.setMinimumSize(QSize(150, 30))
        self.sha512.setFont(font2)
        self.sha512.setCursor(QCursor(Qt.PointingHandCursor))
        self.sha512.setStyleSheet(u"background-color: rgb(35, 35, 38);\n"
"border-bottom-left-radius :14px;\n"
"border-top-left-radius :14px;\n"
"border-top-right-radius :14px;\n"
"border-bottom-right-radius :14px;\n"
"border-color :rgb(51, 51, 56);\n"
"font: 57 10pt \"Raleway Medium\";")
        self.sha512.setIcon(icon17)
        self.line_9 = QFrame(self.Security)
        self.line_9.setObjectName(u"line_9")
        self.line_9.setGeometry(QRect(250, 220, 16, 41))
        self.line_9.setStyleSheet(u"color: rgb(4, 239, 188)")
        self.line_9.setFrameShadow(QFrame.Plain)
        self.line_9.setLineWidth(5)
        self.line_9.setFrameShape(QFrame.VLine)
        self.line_10 = QFrame(self.Security)
        self.line_10.setObjectName(u"line_10")
        self.line_10.setGeometry(QRect(260, 250, 21, 16))
        self.line_10.setStyleSheet(u"color: rgb(4, 239, 188)")
        self.line_10.setFrameShadow(QFrame.Plain)
        self.line_10.setLineWidth(5)
        self.line_10.setFrameShape(QFrame.HLine)
        self.announceBox2 = QLabel(self.Security)
        self.announceBox2.setObjectName(u"announceBox2")
        self.announceBox2.setGeometry(QRect(70, 540, 1031, 31))
        self.announceBox2.setStyleSheet(u"background-color: rgb(206, 55, 8);border-top-left-radius :15px;border-top-right-radius :15px;border-bottom-left-radius :15px;border-bottom-right-radius :15px;\n"
"font: 81 10pt \"Raleway ExtraBold\";")
        self.announceBox2.setFrameShape(QFrame.Panel)
        self.announceBox2.setFrameShadow(QFrame.Raised)
        self.announceBox2.setLineWidth(0)
        self.announceBox2.setTextFormat(Qt.RichText)
        self.announceBox2.setScaledContents(False)
        self.announceBox2.setAlignment(Qt.AlignCenter)
        self.announceBox2.setWordWrap(True)
        self.stackedWidget.addWidget(self.Security)
        self.dangerBorder.raise_()
        self.dashboardTitle_10.raise_()
        self.dashboardTitle_11.raise_()
        self.regenkeysWidget.raise_()
        self.changeBitLength.raise_()
        self.signAndVerify.raise_()
        self.signFile.raise_()
        self.verifySignature.raise_()
        self.line.raise_()
        self.line_2.raise_()
        self.line_3.raise_()
        self.line_4.raise_()
        self.dangerZone3Widget.raise_()
        self.generateChecksum.raise_()
        self.line_5.raise_()
        self.line_6.raise_()
        self.line_7.raise_()
        self.line_8.raise_()
        self.sha256.raise_()
        self.sha384.raise_()
        self.sha512.raise_()
        self.line_9.raise_()
        self.line_10.raise_()
        self.announceBox2.raise_()
        self.Account = QWidget()
        self.Account.setObjectName(u"Account")
        self.dashboardTitle_12 = QLabel(self.Account)
        self.dashboardTitle_12.setObjectName(u"dashboardTitle_12")
        self.dashboardTitle_12.setGeometry(QRect(0, 40, 1171, 41))
        self.dashboardTitle_12.setStyleSheet(u"font: 57 18pt \"Raleway Medium\";")
        self.dashboardTitle_12.setLineWidth(1)
        self.dashboardTitle_12.setAlignment(Qt.AlignHCenter|Qt.AlignTop)
        self.enable2fa = QPushButton(self.Account)
        self.enable2fa.setObjectName(u"enable2fa")
        self.enable2fa.setGeometry(QRect(20, 120, 191, 31))
        self.enable2fa.setMinimumSize(QSize(150, 30))
        self.enable2fa.setFont(font5)
        self.enable2fa.setCursor(QCursor(Qt.PointingHandCursor))
        self.enable2fa.setStyleSheet(u"background-color: #aa63ff;\n"
"font: 63 10pt \"Raleway SemiBold\";\n"
"")
        icon18 = QIcon()
        icon18.addFile(u"images/icons/cil-mobile.png", QSize(), QIcon.Normal, QIcon.Off)
        self.enable2fa.setIcon(icon18)
        self.enable2fa.setFlat(False)
        self.tooltip1 = QLabel(self.Account)
        self.tooltip1.setObjectName(u"tooltip1")
        self.tooltip1.setGeometry(QRect(220, 130, 16, 16))
        self.tooltip1.setStyleSheet(u"font: 57 18pt \"Raleway Medium\";")
        self.tooltip1.setLineWidth(1)
        self.tooltip1.setPixmap(QPixmap(u":/icons/images/icons/information.png"))
        self.tooltip1.setScaledContents(True)
        self.tooltip1.setAlignment(Qt.AlignHCenter|Qt.AlignTop)
        self.disabledText1 = QLabel(self.Account)
        self.disabledText1.setObjectName(u"disabledText1")
        self.disabledText1.setGeometry(QRect(20, 160, 221, 21))
        self.disabledText1.setStyleSheet(u"font: 57 10pt \"Raleway Medium\";")
        self.disabledText1.setLineWidth(1)
        self.disabledText1.setPixmap(QPixmap(u":/icons/images/icons/information.png"))
        self.disabledText1.setScaledContents(True)
        self.disabledText1.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignTop)
        self.stackedWidget.addWidget(self.Account)

        self.verticalLayout_15.addWidget(self.stackedWidget)


        self.horizontalLayout_4.addWidget(self.pagesContainer)

        self.extraRightBox = QFrame(self.content)
        self.extraRightBox.setObjectName(u"extraRightBox")
        self.extraRightBox.setMinimumSize(QSize(0, 0))
        self.extraRightBox.setMaximumSize(QSize(0, 16777215))
        self.extraRightBox.setFrameShape(QFrame.NoFrame)
        self.extraRightBox.setFrameShadow(QFrame.Raised)
        self.verticalLayout_7 = QVBoxLayout(self.extraRightBox)
        self.verticalLayout_7.setSpacing(0)
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.verticalLayout_7.setContentsMargins(0, 0, 0, 0)
        self.themeSettingsTopDetail = QFrame(self.extraRightBox)
        self.themeSettingsTopDetail.setObjectName(u"themeSettingsTopDetail")
        self.themeSettingsTopDetail.setMaximumSize(QSize(16777215, 3))
        self.themeSettingsTopDetail.setFrameShape(QFrame.NoFrame)
        self.themeSettingsTopDetail.setFrameShadow(QFrame.Raised)

        self.verticalLayout_7.addWidget(self.themeSettingsTopDetail)

        self.contentSettings = QFrame(self.extraRightBox)
        self.contentSettings.setObjectName(u"contentSettings")
        self.contentSettings.setFrameShape(QFrame.NoFrame)
        self.contentSettings.setFrameShadow(QFrame.Raised)
        self.verticalLayout_13 = QVBoxLayout(self.contentSettings)
        self.verticalLayout_13.setSpacing(0)
        self.verticalLayout_13.setObjectName(u"verticalLayout_13")
        self.verticalLayout_13.setContentsMargins(0, 0, 0, 0)
        self.topMenus = QFrame(self.contentSettings)
        self.topMenus.setObjectName(u"topMenus")
        self.topMenus.setFrameShape(QFrame.NoFrame)
        self.topMenus.setFrameShadow(QFrame.Raised)
        self.verticalLayout_14 = QVBoxLayout(self.topMenus)
        self.verticalLayout_14.setSpacing(0)
        self.verticalLayout_14.setObjectName(u"verticalLayout_14")
        self.verticalLayout_14.setContentsMargins(0, 0, 0, 0)
        self.btn_help = QPushButton(self.topMenus)
        self.btn_help.setObjectName(u"btn_help")
        sizePolicy.setHeightForWidth(self.btn_help.sizePolicy().hasHeightForWidth())
        self.btn_help.setSizePolicy(sizePolicy)
        self.btn_help.setMinimumSize(QSize(0, 45))
        self.btn_help.setFont(font)
        self.btn_help.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_help.setLayoutDirection(Qt.LeftToRight)
        self.btn_help.setStyleSheet(u"background-image: url(:/icons/images/icons/cil-external-link.png);")

        self.verticalLayout_14.addWidget(self.btn_help)

        self.btn_report = QPushButton(self.topMenus)
        self.btn_report.setObjectName(u"btn_report")
        sizePolicy.setHeightForWidth(self.btn_report.sizePolicy().hasHeightForWidth())
        self.btn_report.setSizePolicy(sizePolicy)
        self.btn_report.setMinimumSize(QSize(0, 45))
        self.btn_report.setFont(font)
        self.btn_report.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_report.setLayoutDirection(Qt.LeftToRight)
        self.btn_report.setStyleSheet(u"background-image: url(:/icons/images/icons/cil-speech.png);")

        self.verticalLayout_14.addWidget(self.btn_report)

        self.btn_logout = QPushButton(self.topMenus)
        self.btn_logout.setObjectName(u"btn_logout")
        sizePolicy.setHeightForWidth(self.btn_logout.sizePolicy().hasHeightForWidth())
        self.btn_logout.setSizePolicy(sizePolicy)
        self.btn_logout.setMinimumSize(QSize(0, 45))
        self.btn_logout.setFont(font)
        self.btn_logout.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_logout.setLayoutDirection(Qt.LeftToRight)
        self.btn_logout.setStyleSheet(u"background-image: url(:/icons/images/icons/cil-account-logout.png);")

        self.verticalLayout_14.addWidget(self.btn_logout)


        self.verticalLayout_13.addWidget(self.topMenus, 0, Qt.AlignTop)


        self.verticalLayout_7.addWidget(self.contentSettings)


        self.horizontalLayout_4.addWidget(self.extraRightBox)


        self.verticalLayout_6.addWidget(self.content)

        self.bottomBar = QFrame(self.contentBottom)
        self.bottomBar.setObjectName(u"bottomBar")
        self.bottomBar.setMinimumSize(QSize(0, 22))
        self.bottomBar.setMaximumSize(QSize(16777215, 22))
        self.bottomBar.setFrameShape(QFrame.NoFrame)
        self.bottomBar.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_5 = QHBoxLayout(self.bottomBar)
        self.horizontalLayout_5.setSpacing(0)
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.horizontalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.creditsLabel = QLabel(self.bottomBar)
        self.creditsLabel.setObjectName(u"creditsLabel")
        self.creditsLabel.setMaximumSize(QSize(16777215, 16))
        font7 = QFont()
        font7.setFamilies([u"Raleway SemiBold"])
        font7.setPointSize(8)
        font7.setBold(False)
        font7.setItalic(False)
        self.creditsLabel.setFont(font7)
        self.creditsLabel.setStyleSheet(u"font: 63 8pt \"Raleway SemiBold\";")
        self.creditsLabel.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.horizontalLayout_5.addWidget(self.creditsLabel)

        self.version = QLabel(self.bottomBar)
        self.version.setObjectName(u"version")
        self.version.setStyleSheet(u"font: 63 8pt \"Raleway SemiBold\";")
        self.version.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.horizontalLayout_5.addWidget(self.version)

        self.frame_size_grip = QFrame(self.bottomBar)
        self.frame_size_grip.setObjectName(u"frame_size_grip")
        self.frame_size_grip.setMinimumSize(QSize(20, 0))
        self.frame_size_grip.setMaximumSize(QSize(20, 16777215))
        self.frame_size_grip.setFrameShape(QFrame.NoFrame)
        self.frame_size_grip.setFrameShadow(QFrame.Raised)

        self.horizontalLayout_5.addWidget(self.frame_size_grip)


        self.verticalLayout_6.addWidget(self.bottomBar)


        self.verticalLayout_2.addWidget(self.contentBottom)


        self.appLayout.addWidget(self.contentBox)

        MainWindow.setCentralWidget(self.styleSheet)

        self.retranslateUi(MainWindow)

        self.stackedWidget.setCurrentIndex(4)
        self.closePopup.setDefault(False)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"EasyRSA", None))
        self.titleLeftApp.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" color:#ffffff;\">EasyRSA</span></p></body></html>", None))
        self.titleLeftDescription.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" color:#aa63ff;\">RSA D.M.E.</span></p></body></html>", None))
        self.toggleButton.setText(QCoreApplication.translate("MainWindow", u"Hide", None))
        self.btn_home.setText(QCoreApplication.translate("MainWindow", u"Home", None))
        self.btn_filespace.setText(QCoreApplication.translate("MainWindow", u"Drive", None))
        self.btn_security.setText(QCoreApplication.translate("MainWindow", u"Passwords", None))
        self.btn_account.setText(QCoreApplication.translate("MainWindow", u"Account", None))
        self.btn_exit.setText(QCoreApplication.translate("MainWindow", u"Log out", None))
        self.toggleLeftBox.setText(QCoreApplication.translate("MainWindow", u"Settings", None))
        self.extraLabel.setText("")
#if QT_CONFIG(tooltip)
        self.extraCloseColumnBtn.setToolTip(QCoreApplication.translate("MainWindow", u"Hide", None))
#endif // QT_CONFIG(tooltip)
        self.extraCloseColumnBtn.setText("")
        self.btn_share.setText(QCoreApplication.translate("MainWindow", u"Share", None))
        self.btn_credits.setText(QCoreApplication.translate("MainWindow", u"Show Credits", None))
        self.btn_more.setText(QCoreApplication.translate("MainWindow", u"More", None))
        self.credits.setHtml(QCoreApplication.translate("MainWindow", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:'Segoe UI'; font-size:10pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"center\" style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:12pt; font-weight:600; color:#ffd579;\">Credit</span></p>\n"
"<p align=\"center\" style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" color:#ffb379;\">Theme by: Zeno Rocha</span></p>\n"
"<p align=\"center\" style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" color:#ffb379;\">UI framework by: Wanderson M. Pimenta</span></p>\n"
"<p align=\"center\" style=\" "
                        "margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:12pt; font-weight:600; color:#ffd579;\">Developers</span></p>\n"
"<p align=\"center\" style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:9pt; color:#ffffff;\">Leigh | Developer</span></p>\n"
"<p align=\"center\" style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:9pt; color:#ffffff;\">Bartosz | Developer</span></p></body></html>", None))
        self.titleRightInfo.setText(QCoreApplication.translate("MainWindow", u"EasyRSA", None))
#if QT_CONFIG(tooltip)
        self.settingsTopBtn.setToolTip(QCoreApplication.translate("MainWindow", u"Settings", None))
#endif // QT_CONFIG(tooltip)
        self.settingsTopBtn.setText("")
#if QT_CONFIG(tooltip)
        self.minimizeAppBtn.setToolTip(QCoreApplication.translate("MainWindow", u"Minimize", None))
#endif // QT_CONFIG(tooltip)
        self.minimizeAppBtn.setText("")
#if QT_CONFIG(tooltip)
        self.maximizeRestoreAppBtn.setToolTip(QCoreApplication.translate("MainWindow", u"Maximize", None))
#endif // QT_CONFIG(tooltip)
        self.maximizeRestoreAppBtn.setText("")
#if QT_CONFIG(tooltip)
        self.closeAppBtn.setToolTip(QCoreApplication.translate("MainWindow", u"Close", None))
#endif // QT_CONFIG(tooltip)
        self.closeAppBtn.setText("")
        self.dashboardTitle.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><span style=\" font-weight:600;\">Welcome to your EasyRSA Dashboard</span></p></body></html>", None))
        self.privateKeyCheckbox.setText(QCoreApplication.translate("MainWindow", u"Show Private Key", None))
        self.copyPrivateKeyButton.setText(QCoreApplication.translate("MainWindow", u"Copy Private Key", None))
        self.dashboardTitle_2.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><span style=\" font-size:12pt; font-weight:600; color:#aa63ff;\">Your Public Key</span></p></body></html>", None))
        self.dashboardTitle_3.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><span style=\" font-size:12pt; font-weight:600; color:#aa63ff;\">Your Private Key</span></p></body></html>", None))
        self.copyPublicKeyButton.setText(QCoreApplication.translate("MainWindow", u"Copy Public Key", None))
        self.backer1_3.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><span style=\" font-weight:600; color:#ffffff;\">DANGER:</span><span style=\" color:#ffffff;\"> Your private key is not to be shared. Doing so will allow anybody to decrypt your data. Use this feature is at your own risk.</span></p></body></html>", None))
        self.labelBoxBlenderInstalation.setText(QCoreApplication.translate("MainWindow", u"FILE BOX", None))
        self.pushButton.setText(QCoreApplication.translate("MainWindow", u"Open", None))
        self.labelVersion_3.setText(QCoreApplication.translate("MainWindow", u"Label description", None))
        self.lineEdit.setText("")
        self.lineEdit.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Type here", None))
        self.checkBox.setText(QCoreApplication.translate("MainWindow", u"CheckBox", None))
        self.radioButton.setText(QCoreApplication.translate("MainWindow", u"RadioButton", None))
        self.comboBox.setItemText(0, QCoreApplication.translate("MainWindow", u"Test 1", None))
        self.comboBox.setItemText(1, QCoreApplication.translate("MainWindow", u"Test 2", None))
        self.comboBox.setItemText(2, QCoreApplication.translate("MainWindow", u"Test 3", None))

        self.commandLinkButton.setText(QCoreApplication.translate("MainWindow", u"Link Button", None))
        self.commandLinkButton.setDescription(QCoreApplication.translate("MainWindow", u"Link description", None))
        ___qtablewidgetitem = self.tableWidget.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("MainWindow", u"0", None));
        ___qtablewidgetitem1 = self.tableWidget.horizontalHeaderItem(1)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("MainWindow", u"1", None));
        ___qtablewidgetitem2 = self.tableWidget.horizontalHeaderItem(2)
        ___qtablewidgetitem2.setText(QCoreApplication.translate("MainWindow", u"2", None));
        ___qtablewidgetitem3 = self.tableWidget.horizontalHeaderItem(3)
        ___qtablewidgetitem3.setText(QCoreApplication.translate("MainWindow", u"3", None));
        ___qtablewidgetitem4 = self.tableWidget.verticalHeaderItem(0)
        ___qtablewidgetitem4.setText(QCoreApplication.translate("MainWindow", u"New Row", None));
        ___qtablewidgetitem5 = self.tableWidget.verticalHeaderItem(1)
        ___qtablewidgetitem5.setText(QCoreApplication.translate("MainWindow", u"New Row", None));
        ___qtablewidgetitem6 = self.tableWidget.verticalHeaderItem(2)
        ___qtablewidgetitem6.setText(QCoreApplication.translate("MainWindow", u"New Row", None));
        ___qtablewidgetitem7 = self.tableWidget.verticalHeaderItem(3)
        ___qtablewidgetitem7.setText(QCoreApplication.translate("MainWindow", u"New Row", None));
        ___qtablewidgetitem8 = self.tableWidget.verticalHeaderItem(4)
        ___qtablewidgetitem8.setText(QCoreApplication.translate("MainWindow", u"New Row", None));
        ___qtablewidgetitem9 = self.tableWidget.verticalHeaderItem(5)
        ___qtablewidgetitem9.setText(QCoreApplication.translate("MainWindow", u"New Row", None));
        ___qtablewidgetitem10 = self.tableWidget.verticalHeaderItem(6)
        ___qtablewidgetitem10.setText(QCoreApplication.translate("MainWindow", u"New Row", None));
        ___qtablewidgetitem11 = self.tableWidget.verticalHeaderItem(7)
        ___qtablewidgetitem11.setText(QCoreApplication.translate("MainWindow", u"New Row", None));
        ___qtablewidgetitem12 = self.tableWidget.verticalHeaderItem(8)
        ___qtablewidgetitem12.setText(QCoreApplication.translate("MainWindow", u"New Row", None));
        ___qtablewidgetitem13 = self.tableWidget.verticalHeaderItem(9)
        ___qtablewidgetitem13.setText(QCoreApplication.translate("MainWindow", u"New Row", None));
        ___qtablewidgetitem14 = self.tableWidget.verticalHeaderItem(10)
        ___qtablewidgetitem14.setText(QCoreApplication.translate("MainWindow", u"New Row", None));
        ___qtablewidgetitem15 = self.tableWidget.verticalHeaderItem(11)
        ___qtablewidgetitem15.setText(QCoreApplication.translate("MainWindow", u"New Row", None));
        ___qtablewidgetitem16 = self.tableWidget.verticalHeaderItem(12)
        ___qtablewidgetitem16.setText(QCoreApplication.translate("MainWindow", u"New Row", None));
        ___qtablewidgetitem17 = self.tableWidget.verticalHeaderItem(13)
        ___qtablewidgetitem17.setText(QCoreApplication.translate("MainWindow", u"New Row", None));
        ___qtablewidgetitem18 = self.tableWidget.verticalHeaderItem(14)
        ___qtablewidgetitem18.setText(QCoreApplication.translate("MainWindow", u"New Row", None));
        ___qtablewidgetitem19 = self.tableWidget.verticalHeaderItem(15)
        ___qtablewidgetitem19.setText(QCoreApplication.translate("MainWindow", u"New Row", None));

        __sortingEnabled = self.tableWidget.isSortingEnabled()
        self.tableWidget.setSortingEnabled(False)
        ___qtablewidgetitem20 = self.tableWidget.item(0, 0)
        ___qtablewidgetitem20.setText(QCoreApplication.translate("MainWindow", u"Test", None));
        ___qtablewidgetitem21 = self.tableWidget.item(0, 1)
        ___qtablewidgetitem21.setText(QCoreApplication.translate("MainWindow", u"Text", None));
        ___qtablewidgetitem22 = self.tableWidget.item(0, 2)
        ___qtablewidgetitem22.setText(QCoreApplication.translate("MainWindow", u"Cell", None));
        ___qtablewidgetitem23 = self.tableWidget.item(0, 3)
        ___qtablewidgetitem23.setText(QCoreApplication.translate("MainWindow", u"Line", None));
        self.tableWidget.setSortingEnabled(__sortingEnabled)

        self.filespaceTitle.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><span style=\" font-weight:600;\">EasyRSA Filespace</span></p></body></html>", None))
        self.filepathBox_2.setText("")
        self.filepathBox_2.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Type here", None))
        self.encryptButton_2.setText(QCoreApplication.translate("MainWindow", u"Encrypt File", None))
        self.decryptButton_2.setText(QCoreApplication.translate("MainWindow", u"Decrypt File", None))
        self.openFilepathButton_2.setText(QCoreApplication.translate("MainWindow", u"Browse Files", None))
        self.selectFileToEncryptText.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><span style=\" font-weight:600; color:#aa63ff;\">Select file to encrypt</span></p></body></html>", None))
        self.multiviewCheckbox_1.setText(QCoreApplication.translate("MainWindow", u" Enable Multiview", None))
        self.currentDirectory_2.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p>aaaaa</p></body></html>", None))
        self.selectFileToEncryptText_2.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><span style=\" font-weight:600; color:#aa63ff;\">Want a more advanced view?</span></p></body></html>", None))
        self.parentDriveTitle_2.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><span style=\" font-weight:600; color:#aa63ff;\">Drive Usage</span></p></body></html>", None))
        self.driveInfoTitle_2.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><span style=\" font-weight:600; color:#aa63ff;\">Drive Information</span></p></body></html>", None))
        self.driveInfo_2.setText("")
        self.parentDrive_2.setText(QCoreApplication.translate("MainWindow", u"Parent Drive:", None))
        self.openDirectory_2.setText(QCoreApplication.translate("MainWindow", u" Open Directory", None))
        self.goToDefault_2.setText(QCoreApplication.translate("MainWindow", u"Go To Default Location", None))
        self.defaultLocation_2.setText(QCoreApplication.translate("MainWindow", u"Change Default Location", None))
        self.goBackButton_2.setText(QCoreApplication.translate("MainWindow", u" Go Back..", None))
        self.multiviewDetailsBox.setText("")
        self.currentDirectoryText.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><br/></p></body></html>", None))
        self.announceBox.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><span style=\" color:#d80a14;\">ErrorBox</span></p></body></html>", None))
        self.border1.setText("")
        self.border2.setText("")
        self.encryptButton_3.setText(QCoreApplication.translate("MainWindow", u"Encrypt Selected File", None))
        self.decryptButton_3.setText(QCoreApplication.translate("MainWindow", u"Decrypt Selected File", None))
        self.closePopup.setText("")
        self.border1_2.setText("")
        self.border1_3.setText("")
        self.backer1.setText("")
        self.multiviewDetailsBox_2.setText("")
        self.dashboardTitle_10.setText(QCoreApplication.translate("MainWindow", u"Security Centre", None))
        self.dashboardTitle_11.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" color:#ff0000;\">Danger Zone</span></p></body></html>", None))
        self.dangerBorder.setText("")
        self.signAndVerify.setText(QCoreApplication.translate("MainWindow", u"Sign and Verify file", None))
        self.signFile.setText(QCoreApplication.translate("MainWindow", u"Sign File", None))
        self.verifySignature.setText(QCoreApplication.translate("MainWindow", u"Verify Signature", None))
        self.generateChecksum.setText(QCoreApplication.translate("MainWindow", u"Generate Checksum", None))
        self.sha256.setText(QCoreApplication.translate("MainWindow", u"SHA256", None))
        self.sha384.setText(QCoreApplication.translate("MainWindow", u"SHA384", None))
        self.sha512.setText(QCoreApplication.translate("MainWindow", u"SHA512", None))
        self.announceBox2.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><span style=\" color:#d80a14;\">ErrorBox</span></p></body></html>", None))
        self.dashboardTitle_12.setText(QCoreApplication.translate("MainWindow", u"Account Settings", None))
        self.enable2fa.setText(QCoreApplication.translate("MainWindow", u"Enable 2 Factor/Get Seed", None))
#if QT_CONFIG(tooltip)
        self.tooltip1.setToolTip(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:11pt; color:#ffffff;\">This will send a code to you every time you log in. <br>Click this if you have also lost the seed you require to add this account to your Authenticator app.</span></p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.tooltip1.setText("")
#if QT_CONFIG(tooltip)
        self.disabledText1.setToolTip(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:11pt; color:#ffffff;\">This will send a code to you every time you log in. <br>Click this if you have also lost the seed you require to add this account to your Authenticator app.</span></p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.disabledText1.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-family:'Medium'; font-size:11pt; font-weight:400; font-style:italic;\">2 Factor Authentication Disabled</span></p></body></html>", None))
        self.btn_help.setText(QCoreApplication.translate("MainWindow", u"Help", None))
        self.btn_report.setText(QCoreApplication.translate("MainWindow", u"Report Issue", None))
        self.btn_logout.setText(QCoreApplication.translate("MainWindow", u"Logout", None))
        self.creditsLabel.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:8pt; color:#ffffff;\">Group 1</span></p></body></html>", None))
        self.version.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-weight:600; color:#ffffff;\">Version</span><span style=\" color:#ffffff;\"> 0.0.4</span></p></body></html>", None))
    # retranslateUi

