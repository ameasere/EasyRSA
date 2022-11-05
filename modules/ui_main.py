# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'newMain.ui'
##
## Created by: Qt User Interface Compiler version 6.4.0
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
        MainWindow.resize(1276, 685)
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
"	background-color: rgba(35,35,38, 180);\n"
"	border: 1px solid rgb(35,35,38);\n"
"	background-image: none;\n"
"	background-position: left center;\n"
"    background-repeat: no-repeat;\n"
"	border: none;\n"
"	border-left: 2px solid rgb(0,94,217);\n"
"	text-align: left;\n"
"	padding-left: 8px;\n"
"	margin: 0px;\n"
"}\n"
"\n"
"/* /////////////////////////////////////////////////////////////////////////////////////////////////\n"
"Bg App */\n"
"#bgApp {\n"
"	background-color: rgb(11,11,11);\n"
"	border: 1px solid rgb(35,35,38);\n"
"}\n"
"\n"
"/* /////////////////////////////////////////////////////////////////////////////////////////////////\n"
"Left Menu */\n"
"#leftMenuBg {\n"
"	background-color: rgb(35,35,38);\n"
"}\n"
"#topLogo {\n"
"	ba"
                        "ckground-color: rgb(35,35,38);\n"
"	background-image: url(:/images/images/images/RSA30x30.png);\n"
"	background-position: center;\n"
"	background-repeat: no-repeat;\n"
"}\n"
"#titleLeftApp { font: 63 12pt \"Segoe UI Semibold\"; }\n"
"#titleLeftDescription { font: 8pt \"Segoe UI\"; color: rgb(32, 124, 245); }\n"
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
"	background-color: rgb(11,11,11);\n"
"}\n"
"#topMenu .QPushButton:pressed {\n"
"	background-color: rgb(32, 124, 245);\n"
"	color: rgb(255, 255, 255);\n"
"}\n"
"#bottomMenu .QPushButton {\n"
"	background-position: left center;\n"
"    background-repeat: no-repeat;\n"
"	border: none;\n"
"	border-left: 20px solid transparent;\n"
"	background-color:transparent;\n"
"	text-align: left;\n"
"	padding-left"
                        ": 44px;\n"
"}\n"
"#bottomMenu .QPushButton:hover {\n"
"	background-color: rgb(11,11,11);\n"
"}\n"
"#bottomMenu .QPushButton:pressed {\n"
"	background-color: rgb(32, 124, 245);\n"
"	color: rgb(255, 255, 255);\n"
"}\n"
"#leftMenuFrame{\n"
"	border-top: 3px solid rgb(35,35,38);\n"
"}\n"
"\n"
"/* Toggle Button */\n"
"#toggleButton {\n"
"	background-position: left center;\n"
"    background-repeat: no-repeat;\n"
"	border: none;\n"
"	border-left: 20px solid transparent;\n"
"	background-color: rgb(37, 41, 48);\n"
"	text-align: left;\n"
"	padding-left: 44px;\n"
"	color: rgb(113, 126, 149);\n"
"}\n"
"#toggleButton:hover {\n"
"	background-color: rgb(11,11,11);\n"
"}\n"
"#toggleButton:pressed {\n"
"	background-color: rgb(32, 124, 245);\n"
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
"}\n"
"#extraTopBg {\n"
""
                        "	background-color: rgb(32, 124, 245);\n"
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
"#extraCloseColumnBtn:hover { background-color: rgb(87, 156, 247); border-style: solid; border-radius: 4px; }\n"
"#extraCloseColumnBtn:pressed { background-color: rgb(46, 130, 240); border-style: solid; border-radius: 4px; }\n"
"\n"
"/* Extra Content */\n"
"#extraContent{\n"
"	border-top: 3px solid rgb(11,11,11);\n"
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
"	background-color: rgb(11,11,11);\n"
"}\n"
"#extraTopMenu .QPushButton:pressed {\n"
"	background-color: rgb(32, 124, 245);\n"
"	color: rgb(255, 255, 255);\n"
"}\n"
"\n"
"/* /////////////////////////////////////////////////////////////////////////////////////////////////\n"
"Content App */\n"
"#contentTopBg{\n"
"	background-color: rgb(35,35,38);\n"
"}\n"
"#contentBottom{\n"
"	border-top: 3px solid rgb(35,35,38);\n"
"}\n"
"\n"
"/* Top Buttons */\n"
"#rightButtons .QPushButton { background-color: rgba(255, 255, 255, 0); border: none;  border-radius: 5px; }\n"
"#rightButtons .QPushButton:hover { background-color: rgb(44, 49, 57); border-style: solid; border-radius: 4px; }\n"
"#rightButtons .QPushButton:pressed { background-color: rgb(23, 26, 30); border-style: solid; border-radius: 4px; }\n"
"\n"
"/* Theme Settings */\n"
"#extraRightBox { background-color: rgb(35,35,38); }\n"
"#themeSettingsTopDetail { background-color: rgb(32, 124, 245); }\n"
"\n"
"/* Bottom "
                        "Bar */\n"
"#bottomBar { background-color: rgb(35,35,38); }\n"
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
"	background-color: rgb(11,11,11);\n"
"}\n"
"#contentSettings .QPushButton:pressed {\n"
"	background-color: rgb(32, 124, 245);\n"
"	color: rgb(255, 255, 255);\n"
"}\n"
"\n"
"/* /////////////////////////////////////////////////////////////////////////////////////////////////\n"
"QTableWidget */\n"
"QTableWidget {\n"
"	background-color: transparent;\n"
"	padding: 10px;\n"
"	border-radius: 5px;\n"
"	gridline-color: rgb(35,35,38);\n"
"	border-bottom: 1px solid rgb(44, 49, 60);\n"
""
                        "}\n"
"QTableWidget::item{\n"
"	border-color: rgb(44, 49, 60);\n"
"	padding-left: 5px;\n"
"	padding-right: 5px;\n"
"	gridline-color: rgb(44, 49, 60);\n"
"}\n"
"QTableWidget::item:selected{\n"
"	background-color: rgb(32, 124, 245);\n"
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
"}\n"
"\n"
"/* /////////////////////////////////////////////////////////////////////////////////////////////////\n"
"LineEdit */\n"
"QLineEdit {\n"
"	"
                        "background-color: rgb(35,35,38);\n"
"	border-radius: 5px;\n"
"	border: 2px solid rgb(35,35,38);\n"
"	padding-left: 10px;\n"
"	selection-color: rgb(255, 255, 255);\n"
"	selection-background-color: rgb(0,94,217);\n"
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
"	border: 2px solid rgb(64, 71, 88);\n"
"}\n"
"QPlainTextEdit:focus {\n"
"	border: 2px solid rgb(91, 101, 124);\n"
"}\n"
"\n"
"/* ////////////////////////////////////"
                        "/////////////////////////////////////////////////////////////\n"
"ScrollBars */\n"
"QScrollBar:horizontal {\n"
"    border: none;\n"
"    background: rgb(52, 59, 72);\n"
"    height: 8px;\n"
"    margin: 0px 21px 0 21px;\n"
"	border-radius: 0px;\n"
"}\n"
"QScrollBar::handle:horizontal {\n"
"    background: rgb(32, 124, 245);\n"
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
"    subcontrol-origin: margin;\n"
"}\n"
"QScrollBar::up-arrow:horizontal, QScrollBar::down-arrow:horizontal\n"
"{\n"
"     background: none;"
                        "\n"
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
"	background: rgb(32, 124, 245);\n"
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
"     subcontrol-position: top;\n"
"     subcontrol-origin: margin;\n"
" }\n"
" QScrollBar::up-arrow:vertical, QScrollBar::down-arrow:vertical {\n"
""
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
"    border: 3px solid rgb(52, 59, 72);\n"
"	width: 15px;\n"
"	height: 15px;\n"
"	border-radius: 10px;\n"
"    background: rgb(44, 49, 60);\n"
"}\n"
""
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
"	background-image: url(:/icons/images/icons/cil-arrow-bottom.png);\n"
"	background-position: center;\n"
"	background-repeat: no-repeat;\n"
" }\n"
"QCom"
                        "boBox QAbstractItemView {\n"
"	color: rgb(0,94,217);\n"
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
"    background-color: rgb(32, 124, 245);\n"
"    border: none;\n"
"    height: 10px;\n"
"    width: 10px;\n"
"    margin: 0px;\n"
"	border-radius: 5px;\n"
"}\n"
"QSlider::handle:horizontal:hover {\n"
"    background-color: rgb(255, 212, 155);\n"
"}\n"
"QSlider::handle:horizontal:pressed {\n"
"    background-color: rgb(0,94,217);\n"
"}\n"
"\n"
"QSlider::groove:vertical {\n"
"    border-radius: 5px;\n"
"    width: 10px;\n"
"    margin: 0px;\n"
"	background-color"
                        ": rgb(52, 59, 72);\n"
"}\n"
"QSlider::groove:vertical:hover {\n"
"	background-color: rgb(55, 62, 76);\n"
"}\n"
"QSlider::handle:vertical {\n"
"    background-color: rgb(32, 124, 245);\n"
"	border: none;\n"
"    height: 10px;\n"
"    width: 10px;\n"
"    margin: 0px;\n"
"	border-radius: 5px;\n"
"}\n"
"QSlider::handle:vertical:hover {\n"
"    background-color: rgb(255, 212, 155);\n"
"}\n"
"QSlider::handle:vertical:pressed {\n"
"    background-color: rgb(0,94,217);\n"
"}\n"
"\n"
"/* /////////////////////////////////////////////////////////////////////////////////////////////////\n"
"CommandLinkButton */\n"
"QCommandLinkButton {\n"
"	color: rgb(0,94,217);\n"
"	border-radius: 5px;\n"
"	padding: 5px;\n"
"}\n"
"QCommandLinkButton:hover {\n"
"	color: rgb(255, 170, 255);\n"
"	background-color: rgb(44, 49, 60);\n"
"}\n"
"QCommandLinkButton:pressed {\n"
"	color: rgb(32, 124, 245);\n"
"	background-color: rgb(52, 58, 71);\n"
"}\n"
"\n"
"/* ////////////////////////////////////////////////////////////////////////////////////"
                        "/////////////\n"
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
        self.toggleBox = QFrame(self.leftMenuFrame)
        self.toggleBox.setObjectName(u"toggleBox")
        self.toggleBox.setMaximumSize(QSize(16777215, 45))
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
"background-color: rgb(35, 35, 38);")

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
        self.leftBox.setFrameShape(QFrame.NoFrame)
        self.leftBox.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_3 = QHBoxLayout(self.leftBox)
        self.horizontalLayout_3.setSpacing(0)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.topLogo = QFrame(self.leftBox)
        self.topLogo.setObjectName(u"topLogo")
        self.topLogo.setMinimumSize(QSize(42, 42))
        self.topLogo.setMaximumSize(QSize(42, 42))
        self.topLogo.setSizeIncrement(QSize(0, 0))
        self.topLogo.setAutoFillBackground(False)
        self.topLogo.setStyleSheet(u"background-image: url(:/images/images/images/RSA30x30.png);\n"
"background-position: center;")
        self.topLogo.setFrameShape(QFrame.NoFrame)
        self.topLogo.setFrameShadow(QFrame.Raised)

        self.horizontalLayout_3.addWidget(self.topLogo)

        self.titleRightInfo = QLabel(self.leftBox)
        self.titleRightInfo.setObjectName(u"titleRightInfo")
        sizePolicy2 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Expanding)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.titleRightInfo.sizePolicy().hasHeightForWidth())
        self.titleRightInfo.setSizePolicy(sizePolicy2)
        self.titleRightInfo.setMinimumSize(QSize(10000, 0))
        self.titleRightInfo.setMaximumSize(QSize(16777215, 45))
        self.titleRightInfo.setFont(font)
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
        font1 = QFont()
        font1.setFamilies([u"Segoe UI"])
        font1.setPointSize(10)
        font1.setBold(False)
        font1.setItalic(False)
        font1.setStyleStrategy(QFont.PreferDefault)
        self.maximizeRestoreAppBtn.setFont(font1)
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
        self.dashboardTitle.setGeometry(QRect(0, 40, 1171, 31))
        self.dashboardTitle.setStyleSheet(u"color: rgb(0,94,217);\n"
"font: 18pt \"Segoe UI\" bold;")
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
"color: rgb(203, 203, 203);")
        self.publicKeyDisplay.setReadOnly(True)
        self.privateKeyDisplay = QPlainTextEdit(self.home)
        self.privateKeyDisplay.setObjectName(u"privateKeyDisplay")
        self.privateKeyDisplay.setGeometry(QRect(650, 149, 381, 231))
        self.privateKeyDisplay.setMinimumSize(QSize(200, 200))
        self.privateKeyDisplay.setStyleSheet(u"background-color: rgb(33, 37, 43);\n"
"color: rgb(203, 203, 203);")
        self.privateKeyDisplay.setReadOnly(True)
        self.warningMessage = QLabel(self.home)
        self.warningMessage.setObjectName(u"warningMessage")
        self.warningMessage.setGeometry(QRect(640, 430, 401, 51))
        sizePolicy2.setHeightForWidth(self.warningMessage.sizePolicy().hasHeightForWidth())
        self.warningMessage.setSizePolicy(sizePolicy2)
        self.warningMessage.setMaximumSize(QSize(16777215, 100))
        self.warningMessage.setFont(font)
        self.warningMessage.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignTop)
        self.warningMessage.setWordWrap(True)
        self.privateKeyCheckbox = QCheckBox(self.home)
        self.privateKeyCheckbox.setObjectName(u"privateKeyCheckbox")
        self.privateKeyCheckbox.setGeometry(QRect(900, 380, 131, 31))
        self.privateKeyCheckbox.setAutoFillBackground(False)
        self.privateKeyCheckbox.setStyleSheet(u"")
        self.privateKeyCheckbox.setChecked(False)
        self.privateKeyCheckbox.setTristate(False)
        self.copyPrivateKeyButton = QPushButton(self.home)
        self.copyPrivateKeyButton.setObjectName(u"copyPrivateKeyButton")
        self.copyPrivateKeyButton.setGeometry(QRect(650, 380, 241, 30))
        self.copyPrivateKeyButton.setMinimumSize(QSize(150, 30))
        self.copyPrivateKeyButton.setFont(font)
        self.copyPrivateKeyButton.setCursor(QCursor(Qt.PointingHandCursor))
        self.copyPrivateKeyButton.setStyleSheet(u"background-color: rgb(52, 59, 72);")
        icon5 = QIcon()
        icon5.addFile(u":/icons/images/icons/cil-clone.png", QSize(), QIcon.Normal, QIcon.Off)
        self.copyPrivateKeyButton.setIcon(icon5)
        self.dashboardTitle_2 = QLabel(self.home)
        self.dashboardTitle_2.setObjectName(u"dashboardTitle_2")
        self.dashboardTitle_2.setGeometry(QRect(140, 120, 381, 21))
        self.dashboardTitle_2.setStyleSheet(u"color: rgb(0,60,240);\n"
"font: 18pt \"Segoe UI\" bold;")
        self.dashboardTitle_2.setLineWidth(1)
        self.dashboardTitle_2.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignTop)
        self.dashboardTitle_3 = QLabel(self.home)
        self.dashboardTitle_3.setObjectName(u"dashboardTitle_3")
        self.dashboardTitle_3.setGeometry(QRect(650, 120, 381, 21))
        self.dashboardTitle_3.setStyleSheet(u"color: rgb(0,60,240);\n"
"font: 18pt \"Segoe UI\" bold;")
        self.dashboardTitle_3.setLineWidth(1)
        self.dashboardTitle_3.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignTop)
        self.copyPublicKeyButton = QPushButton(self.home)
        self.copyPublicKeyButton.setObjectName(u"copyPublicKeyButton")
        self.copyPublicKeyButton.setGeometry(QRect(140, 380, 381, 30))
        self.copyPublicKeyButton.setMinimumSize(QSize(150, 30))
        self.copyPublicKeyButton.setFont(font)
        self.copyPublicKeyButton.setCursor(QCursor(Qt.PointingHandCursor))
        self.copyPublicKeyButton.setStyleSheet(u"background-color: rgb(52, 59, 72);")
        self.copyPublicKeyButton.setIcon(icon5)
        self.topLogoInfo = QFrame(self.home)
        self.topLogoInfo.setObjectName(u"topLogoInfo")
        self.topLogoInfo.setGeometry(QRect(70, 50, 60, 50))
        self.topLogoInfo.setMinimumSize(QSize(0, 50))
        self.topLogoInfo.setMaximumSize(QSize(16777215, 50))
        self.topLogoInfo.setFrameShape(QFrame.NoFrame)
        self.topLogoInfo.setFrameShadow(QFrame.Raised)
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
        font2 = QFont()
        font2.setFamilies([u"Segoe UI"])
        __qtablewidgetitem4 = QTableWidgetItem()
        __qtablewidgetitem4.setFont(font2);
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
        self.filespaceTitle.setGeometry(QRect(0, 40, 1171, 31))
        self.filespaceTitle.setStyleSheet(u"color: rgb(0,94,217);\n"
"font: 18pt \"Segoe UI\" bold;")
        self.filespaceTitle.setLineWidth(1)
        self.filespaceTitle.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignTop)
        self.filepathBox_2 = QLineEdit(self.filespace)
        self.filepathBox_2.setObjectName(u"filepathBox_2")
        self.filepathBox_2.setGeometry(QRect(360, 190, 461, 30))
        self.filepathBox_2.setMinimumSize(QSize(0, 30))
        self.filepathBox_2.setStyleSheet(u"background-color: rgb(33, 37, 43);\n"
"border-bottom-left-radius :0px;\n"
"border-bottom-right-radius :0px;\n"
"border: none;")
        self.encryptButton_2 = QPushButton(self.filespace)
        self.encryptButton_2.setObjectName(u"encryptButton_2")
        self.encryptButton_2.setGeometry(QRect(370, 260, 221, 30))
        self.encryptButton_2.setMinimumSize(QSize(150, 30))
        self.encryptButton_2.setFont(font)
        self.encryptButton_2.setCursor(QCursor(Qt.PointingHandCursor))
        self.encryptButton_2.setStyleSheet(u"background-color: rgb(35, 35, 38);\n"
"border-top-right-radius :0px;\n"
"border-bottom-right-radius :0px;\n"
"border-top-left-radius :14px;\n"
"border-bottom-left-radius :14px;")
        icon8 = QIcon()
        icon8.addFile(u":/icons/images/icons/cil-lock-locked.png", QSize(), QIcon.Normal, QIcon.Off)
        self.encryptButton_2.setIcon(icon8)
        self.decryptButton_2 = QPushButton(self.filespace)
        self.decryptButton_2.setObjectName(u"decryptButton_2")
        self.decryptButton_2.setGeometry(QRect(590, 260, 221, 30))
        self.decryptButton_2.setMinimumSize(QSize(150, 30))
        self.decryptButton_2.setFont(font)
        self.decryptButton_2.setCursor(QCursor(Qt.PointingHandCursor))
        self.decryptButton_2.setStyleSheet(u"background-color: rgb(35, 35, 38);\n"
"border-top-left-radius :0px;\n"
"border-bottom-left-radius :0px;\n"
"border-top-right-radius :14px;\n"
"border-bottom-right-radius :14px;")
        icon9 = QIcon()
        icon9.addFile(u":/icons/images/icons/cil-lock-unlocked.png", QSize(), QIcon.Normal, QIcon.Off)
        self.decryptButton_2.setIcon(icon9)
        self.openFilepathButton_2 = QPushButton(self.filespace)
        self.openFilepathButton_2.setObjectName(u"openFilepathButton_2")
        self.openFilepathButton_2.setGeometry(QRect(360, 220, 461, 30))
        self.openFilepathButton_2.setMinimumSize(QSize(150, 30))
        self.openFilepathButton_2.setFont(font)
        self.openFilepathButton_2.setCursor(QCursor(Qt.PointingHandCursor))
        self.openFilepathButton_2.setStyleSheet(u"background-color: rgb(35, 35, 38);\n"
"border-top-left-radius :0px;\n"
"border-top-right-radius :0px;\n"
"border: none;")
        self.openFilepathButton_2.setIcon(icon6)
        self.selectFileToEncryptText = QLabel(self.filespace)
        self.selectFileToEncryptText.setObjectName(u"selectFileToEncryptText")
        self.selectFileToEncryptText.setGeometry(QRect(360, 160, 411, 21))
        sizePolicy2.setHeightForWidth(self.selectFileToEncryptText.sizePolicy().hasHeightForWidth())
        self.selectFileToEncryptText.setSizePolicy(sizePolicy2)
        self.selectFileToEncryptText.setMaximumSize(QSize(16777215, 45))
        self.selectFileToEncryptText.setFont(font)
        self.selectFileToEncryptText.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)
        self.multiviewCheckbox_1 = QCheckBox(self.filespace)
        self.multiviewCheckbox_1.setObjectName(u"multiviewCheckbox_1")
        self.multiviewCheckbox_1.setGeometry(QRect(960, 150, 131, 31))
        self.multiviewCheckbox_1.setAutoFillBackground(False)
        self.multiviewCheckbox_1.setStyleSheet(u"")
        self.multiviewCheckbox_1.setChecked(False)
        self.multiviewCheckbox_1.setTristate(False)
        self.currentDirectory_2 = QLabel(self.filespace)
        self.currentDirectory_2.setObjectName(u"currentDirectory_2")
        self.currentDirectory_2.setGeometry(QRect(280, 110, 591, 41))
        self.currentDirectory_2.setStyleSheet(u"color: rgb(220, 220, 220);")
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
        self.selectFileToEncryptText_2.setGeometry(QRect(910, 130, 231, 21))
        sizePolicy2.setHeightForWidth(self.selectFileToEncryptText_2.sizePolicy().hasHeightForWidth())
        self.selectFileToEncryptText_2.setSizePolicy(sizePolicy2)
        self.selectFileToEncryptText_2.setMaximumSize(QSize(16777215, 45))
        self.selectFileToEncryptText_2.setFont(font)
        self.selectFileToEncryptText_2.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)
        self.parentDriveTitle_2 = QLabel(self.filespace)
        self.parentDriveTitle_2.setObjectName(u"parentDriveTitle_2")
        self.parentDriveTitle_2.setGeometry(QRect(920, 200, 211, 21))
        self.parentDriveTitle_2.setStyleSheet(u"color: rgb(220, 220, 220);\n"
"")
        self.parentDriveTitle_2.setLineWidth(1)
        self.parentDriveTitle_2.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)
        self.driveInfoTitle_2 = QLabel(self.filespace)
        self.driveInfoTitle_2.setObjectName(u"driveInfoTitle_2")
        self.driveInfoTitle_2.setGeometry(QRect(920, 260, 211, 19))
        self.driveInfoTitle_2.setStyleSheet(u"color: rgb(220, 220, 220);")
        self.driveInfoTitle_2.setLineWidth(1)
        self.driveInfoTitle_2.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)
        self.driveInfo_2 = QLabel(self.filespace)
        self.driveInfo_2.setObjectName(u"driveInfo_2")
        self.driveInfo_2.setGeometry(QRect(920, 310, 211, 161))
        self.driveInfo_2.setStyleSheet(u"color: rgb(220, 220, 220);")
        self.driveInfo_2.setLineWidth(1)
        self.driveInfo_2.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignTop)
        self.driveInfo_2.setWordWrap(False)
        self.parentDriveSpace_2 = QProgressBar(self.filespace)
        self.parentDriveSpace_2.setObjectName(u"parentDriveSpace_2")
        self.parentDriveSpace_2.setGeometry(QRect(920, 230, 211, 16))
        self.parentDriveSpace_2.setStyleSheet(u"QProgressBar {\n"
"background-color: rgb(98, 114, 164);\n"
"color: rgb(220, 220, 220);\n"
"border-style: none;\n"
"border-radius: 10px;\n"
"text-align: center;\n"
"}\n"
"QProgressBar::chunk{\n"
"border-radius: 10px;\n"
"background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(0,94,217, 255), stop:1 rgba(6,51,110, 255));\n"
"}")
        self.parentDriveSpace_2.setValue(0)
        self.parentDrive_2 = QLabel(self.filespace)
        self.parentDrive_2.setObjectName(u"parentDrive_2")
        self.parentDrive_2.setGeometry(QRect(920, 290, 131, 21))
        self.parentDrive_2.setStyleSheet(u"color: rgb(220, 220, 220);")
        self.parentDrive_2.setLineWidth(1)
        self.parentDrive_2.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)
        self.openDirectory_2 = QPushButton(self.filespace)
        self.openDirectory_2.setObjectName(u"openDirectory_2")
        self.openDirectory_2.setGeometry(QRect(140, 110, 131, 41))
        self.openDirectory_2.setMinimumSize(QSize(10, 10))
        self.openDirectory_2.setMaximumSize(QSize(16777215, 50))
        self.openDirectory_2.setFont(font)
        self.openDirectory_2.setCursor(QCursor(Qt.PointingHandCursor))
        self.openDirectory_2.setStyleSheet(u"color: rgb(220, 220, 220);\n"
"background-color: rgb(35, 35, 38);\n"
"border: none;")
        self.openDirectory_2.setIcon(icon6)
        self.goToDefault_2 = QPushButton(self.filespace)
        self.goToDefault_2.setObjectName(u"goToDefault_2")
        self.goToDefault_2.setGeometry(QRect(30, 450, 171, 30))
        self.goToDefault_2.setMinimumSize(QSize(150, 30))
        self.goToDefault_2.setFont(font)
        self.goToDefault_2.setCursor(QCursor(Qt.PointingHandCursor))
        self.goToDefault_2.setStyleSheet(u"background-color: rgb(35, 35, 38);\n"
"border-bottom-left-radius :14px;\n"
"border-top-left-radius :14px;\n"
"border-top-right-radius :14px;\n"
"border-bottom-right-radius :14px;")
        icon10 = QIcon()
        icon10.addFile(u":/icons/images/icons/cil-house.png", QSize(), QIcon.Normal, QIcon.Off)
        self.goToDefault_2.setIcon(icon10)
        self.defaultLocation_2 = QPushButton(self.filespace)
        self.defaultLocation_2.setObjectName(u"defaultLocation_2")
        self.defaultLocation_2.setGeometry(QRect(230, 450, 201, 30))
        self.defaultLocation_2.setMinimumSize(QSize(150, 30))
        self.defaultLocation_2.setFont(font)
        self.defaultLocation_2.setCursor(QCursor(Qt.PointingHandCursor))
        self.defaultLocation_2.setStyleSheet(u"background-color: rgb(35, 35, 38);\n"
"border-top-left-radius :14px;\n"
"border-bottom-left-radius :14px;\n"
"border-top-right-radius :14px;\n"
"border-bottom-right-radius :14px;")
        icon11 = QIcon()
        icon11.addFile(u":/icons/images/icons/cil-star.png", QSize(), QIcon.Normal, QIcon.Off)
        self.defaultLocation_2.setIcon(icon11)
        self.goBackButton_2 = QPushButton(self.filespace)
        self.goBackButton_2.setObjectName(u"goBackButton_2")
        self.goBackButton_2.setGeometry(QRect(30, 110, 111, 41))
        self.goBackButton_2.setMinimumSize(QSize(10, 10))
        self.goBackButton_2.setMaximumSize(QSize(16777215, 50))
        self.goBackButton_2.setFont(font)
        self.goBackButton_2.setCursor(QCursor(Qt.PointingHandCursor))
        self.goBackButton_2.setStyleSheet(u"color: rgb(220, 220, 220);\n"
"background-color: rgb(35, 35, 38);\n"
"border: none;")
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
        self.announceBox.setStyleSheet(u"background-color: rgb(206, 55, 8);border-top-left-radius :10px;border-top-right-radius :10px;border-bottom-left-radius :10px;border-bottom-right-radius :10px;")
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
        self.encryptButton_3.setGeometry(QRect(460, 450, 201, 30))
        self.encryptButton_3.setMinimumSize(QSize(150, 30))
        self.encryptButton_3.setFont(font)
        self.encryptButton_3.setCursor(QCursor(Qt.PointingHandCursor))
        self.encryptButton_3.setStyleSheet(u"background-color: rgb(35, 35, 38);\n"
"border-bottom-left-radius :14px;\n"
"border-top-left-radius :14px;\n"
"border-top-right-radius :14px;\n"
"border-bottom-right-radius :14px;")
        self.encryptButton_3.setIcon(icon8)
        self.decryptButton_3 = QPushButton(self.filespace)
        self.decryptButton_3.setObjectName(u"decryptButton_3")
        self.decryptButton_3.setGeometry(QRect(690, 450, 201, 30))
        self.decryptButton_3.setMinimumSize(QSize(150, 30))
        self.decryptButton_3.setFont(font)
        self.decryptButton_3.setCursor(QCursor(Qt.PointingHandCursor))
        self.decryptButton_3.setStyleSheet(u"background-color: rgb(35, 35, 38);\n"
"border-bottom-left-radius :14px;\n"
"border-top-left-radius :14px;\n"
"border-top-right-radius :14px;\n"
"border-bottom-right-radius :14px;")
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
        self.border1_3.setGeometry(QRect(270, 110, 1, 41))
        sizePolicy2.setHeightForWidth(self.border1_3.sizePolicy().hasHeightForWidth())
        self.border1_3.setSizePolicy(sizePolicy2)
        self.border1_3.setMinimumSize(QSize(0, 20))
        self.border1_3.setMaximumSize(QSize(1, 100000))
        self.border1_3.setFont(font)
        self.border1_3.setStyleSheet(u"background-color: rgb(52, 59, 72);\n"
"\n"
"")
        self.border1_3.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)
        self.stackedWidget.addWidget(self.filespace)
        self.fileBrowserTree_2.raise_()
        self.border2.raise_()
        self.border1.raise_()
        self.currentDirectoryText.raise_()
        self.currentDirectory_2.raise_()
        self.multiviewDetailsBox.raise_()
        self.decryptButton_2.raise_()
        self.openFilepathButton_2.raise_()
        self.selectFileToEncryptText.raise_()
        self.filepathBox_2.raise_()
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
        self.Security = QWidget()
        self.Security.setObjectName(u"Security")
        self.dashboardTitle_10 = QLabel(self.Security)
        self.dashboardTitle_10.setObjectName(u"dashboardTitle_10")
        self.dashboardTitle_10.setGeometry(QRect(0, 0, 1171, 51))
        self.dashboardTitle_10.setStyleSheet(u"color: rgb(0,94,217);\n"
"font: 18pt \"Segoe UI\" bold;")
        self.dashboardTitle_10.setLineWidth(1)
        self.dashboardTitle_10.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignTop)
        self.dashboardTitle_11 = QLabel(self.Security)
        self.dashboardTitle_11.setObjectName(u"dashboardTitle_11")
        self.dashboardTitle_11.setGeometry(QRect(690, 460, 111, 31))
        self.dashboardTitle_11.setStyleSheet(u"font: 14pt \"Segoe UI\" bold;\n"
"color: rgb(255, 0, 0);")
        self.dashboardTitle_11.setLineWidth(1)
        self.dashboardTitle_11.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignTop)
        self.dangerBorder = QLabel(self.Security)
        self.dangerBorder.setObjectName(u"dangerBorder")
        self.dangerBorder.setGeometry(QRect(680, 450, 491, 121))
        self.dangerBorder.setStyleSheet(u"border: 2px double;\n"
"border-color: qradialgradient(spread:repeat, cx:0.5, cy:0.5, radius:0.077, fx:0.5, fy:0.5, stop:0.420455 rgba(255, 0, 0, 200), stop:0.497326 rgba(0, 0, 0, 147), stop:0.795455 rgba(0, 0, 0, 200))")
        self.dangerBorder.setLineWidth(1)
        self.dangerBorder.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignTop)
        self.regenkeysWidget = QWidget(self.Security)
        self.regenkeysWidget.setObjectName(u"regenkeysWidget")
        self.regenkeysWidget.setGeometry(QRect(690, 500, 151, 21))
        self.changeBitLength = QWidget(self.Security)
        self.changeBitLength.setObjectName(u"changeBitLength")
        self.changeBitLength.setGeometry(QRect(690, 530, 151, 21))
        self.stackedWidget.addWidget(self.Security)
        self.dangerBorder.raise_()
        self.dashboardTitle_10.raise_()
        self.dashboardTitle_11.raise_()
        self.regenkeysWidget.raise_()
        self.changeBitLength.raise_()
        self.Account = QWidget()
        self.Account.setObjectName(u"Account")
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
        font3 = QFont()
        font3.setFamilies([u"Segoe UI"])
        font3.setBold(False)
        font3.setItalic(False)
        self.creditsLabel.setFont(font3)
        self.creditsLabel.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.horizontalLayout_5.addWidget(self.creditsLabel)

        self.version = QLabel(self.bottomBar)
        self.version.setObjectName(u"version")
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

        self.stackedWidget.setCurrentIndex(2)
        self.closePopup.setDefault(False)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"EasyRSA", None))
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
        self.dashboardTitle.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\">Welcome to your EasyRSA Dashboard</p></body></html>", None))
#if QT_CONFIG(whatsthis)
        self.warningMessage.setWhatsThis("")
#endif // QT_CONFIG(whatsthis)
        self.warningMessage.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><span style=\" color:#ff0000;\">DANGER: Your private key is not to be shared. Doing so will allow </span><span style=\" font-weight:600; text-decoration: underline; color:#ff0000;\">anybody</span><span style=\" color:#ff0000;\"> to decrypt your data. Use this feature is at your own risk.</span></p></body></html>", None))
        self.privateKeyCheckbox.setText(QCoreApplication.translate("MainWindow", u"Show Private Key", None))
        self.copyPrivateKeyButton.setText(QCoreApplication.translate("MainWindow", u"Copy Private Key", None))
        self.dashboardTitle_2.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><span style=\" font-size:12pt;\">Your Public Key</span></p></body></html>", None))
        self.dashboardTitle_3.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><span style=\" font-size:12pt;\">Your Private Key</span></p></body></html>", None))
        self.copyPublicKeyButton.setText(QCoreApplication.translate("MainWindow", u"Copy Public Key", None))
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

        self.filespaceTitle.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\">EasyRSA Filespace</p></body></html>", None))
        self.filepathBox_2.setText("")
        self.filepathBox_2.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Type here", None))
        self.encryptButton_2.setText(QCoreApplication.translate("MainWindow", u"Encrypt", None))
        self.decryptButton_2.setText(QCoreApplication.translate("MainWindow", u"Decrypt", None))
        self.openFilepathButton_2.setText(QCoreApplication.translate("MainWindow", u"Select File", None))
        self.selectFileToEncryptText.setText(QCoreApplication.translate("MainWindow", u"Select file to encrypt:", None))
        self.multiviewCheckbox_1.setText(QCoreApplication.translate("MainWindow", u" Enable Multiview", None))
        self.currentDirectory_2.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p>aaaaa</p></body></html>", None))
        self.selectFileToEncryptText_2.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\">Want a more advanced view?</p></body></html>", None))
        self.parentDriveTitle_2.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\">Drive Usage</p></body></html>", None))
        self.driveInfoTitle_2.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\">Drive Information</p></body></html>", None))
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
        self.dashboardTitle_10.setText(QCoreApplication.translate("MainWindow", u"Security Centre", None))
        self.dashboardTitle_11.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:14pt;\">Danger Zone</span></p></body></html>", None))
        self.dangerBorder.setText("")
        self.btn_help.setText(QCoreApplication.translate("MainWindow", u"Help", None))
        self.btn_report.setText(QCoreApplication.translate("MainWindow", u"Report Issue", None))
        self.btn_logout.setText(QCoreApplication.translate("MainWindow", u"Logout", None))
        self.creditsLabel.setText(QCoreApplication.translate("MainWindow", u"Group 1", None))
        self.version.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-weight:600;\">Version</span> 0.0.4</p></body></html>", None))
    # retranslateUi

