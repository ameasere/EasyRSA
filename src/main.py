# ///////////////////////////////////////////////////////////////
#
# BY: WANDERSON M.PIMENTA
# PROJECT MADE WITH: Qt Designer and PySide6
# V: 1.0.0
#
# This project can be used freely for all uses, as long as they maintain the
# respective credits only in the Python scripts, any information in the visual
# interface (GUI) can be modified without any implication.
#
# There are limitations on Qt licenses if you want to use your products
# commercially, I recommend reading them on the official website:
# https://doc.qt.io/qtforpython/licenses.html
#
# ///////////////////////////////////////////////////////////////
import os
import platform
import sys

# Import QMainWindow
from PySide6.QtWidgets import QApplication, QMainWindow

from modules import *

# warnings.filterwarnings('ignore')
# os.environ['QT_DEBUG_PLUGINS'] = "1"
os.environ["QT_FONT_DPI"] = "96"  # FIX Problem for High DPI and Scale above 100%
title = "EasyRSA"
description = "RSA made simple."


class MainWindow(QMainWindow):
    """
    Dashboard
    """

    def __init__(self):
        QMainWindow.__init__(self)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        widgets = self.ui
        Settings.ENABLE_CUSTOM_TITLE_BAR = titleBarFlag
        # APPLY TEXTS
        self.setWindowTitle(title)
        # widgets.titleRightInfo.setText(description)

        # TOGGLE MENU
        widgets.toggleButton.clicked.connect(lambda: UIFunctions.toggleMenu(self, True))

        # SET UI DEFINITIONS
        UIFunctions.uiDefinitions(self)

        # QTableWidget PARAMETERS
        widgets.tableWidget.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)

        # BUTTONS CLICK
        widgets.btn_home.clicked.connect(self.buttonClick)
        widgets.btn_drive.clicked.connect(self.buttonClick)
        widgets.btn_passwords.clicked.connect(self.buttonClick)
        widgets.btn_account.clicked.connect(self.buttonClick)
        widgets.btn_exit.clicked.connect(self.buttonClick)
        widgets.extraLabel.setText("Bartosz/Leighton")

        # EXTRA LEFT BOX
        def openCloseLeftBox():
            UIFunctions.toggleLeftBox(self, True)

        widgets.toggleLeftBox.clicked.connect(openCloseLeftBox)
        widgets.extraCloseColumnBtn.clicked.connect(openCloseLeftBox)

        # EXTRA RIGHT BOX
        def openCloseRightBox():
            UIFunctions.toggleRightBox(self, True)

        widgets.settingsTopBtn.clicked.connect(openCloseRightBox)
        widgets.btn_logout.clicked.connect(self.buttonClick)
        widgets.btn_help.clicked.connect(self.buttonClick)
        widgets.btn_donate.clicked.connect(self.buttonClick)
        # SHOW APP
        self.show()
        widgets.btn_more.clicked.connect(self.buttonClick)

        # SET HOME PAGE AND SELECT MENU
        widgets.stackedWidget.setCurrentWidget(widgets.home)
        widgets.btn_home.setStyleSheet(UIFunctions.selectMenu(widgets.btn_home.styleSheet()))
        # Home Screen
        """
        
        Insert here
        
        """

    # BUTTONS CLICK
    def buttonClick(self):
        # GET BUTTON CLICKED
        btn = self.sender()
        btnName = btn.objectName()

        # SHOW HOME PAGE
        if btnName == "btn_home":
            self.ui.titleLeftDescription.setText("Dashboard")
            self.ui.stackedWidget.setCurrentWidget(self.ui.home)
            UIFunctions.resetStyle(self, btnName)
            btn.setStyleSheet(UIFunctions.selectMenu(btn.styleSheet()))

        # SHOW WIDGETS PAGE
        if btnName == "btn_drive":
            self.ui.titleLeftDescription.setText("Page 2")
            self.ui.stackedWidget.setCurrentWidget(self.ui.page2)
            UIFunctions.resetStyle(self, btnName)
            btn.setStyleSheet(UIFunctions.selectMenu(btn.styleSheet()))

        # SHOW NEW PAGE
        if btnName == "btn_passwords":
            self.ui.titleLeftDescription.setText("Page 3")
            self.ui.stackedWidget.setCurrentWidget(self.ui.page3)  # SET PAGE
            UIFunctions.resetStyle(self, btnName)  # RESET ANOTHERS BUTTONS SELECTED
            btn.setStyleSheet(UIFunctions.selectMenu(btn.styleSheet()))  # SELECT MENU

        if btnName == "btn_account":
            self.ui.titleLeftDescription.setText("Page 4")
            self.ui.stackedWidget.setCurrentWidget(self.ui.page4)  # SET PAGE
            UIFunctions.resetStyle(self, btnName)  # RESET ANOTHERS BUTTONS SELECTED
            btn.setStyleSheet(UIFunctions.selectMenu(btn.styleSheet()))  # SELECT MENU
        if btnName == "btn_exit":
            self.close()

    # RESIZE EVENTS
    def resizeEvent(self, event):
        # Update Size Grips
        UIFunctions.resize_grips(self)

    # MOUSE CLICK EVENTS
    def mousePressEvent(self, event):
        # SET DRAG POS WINDOW
        self.dragPos = event.globalPos()


if __name__ == "__main__":
    match platform.system():
        case "Windows":
            import ctypes
            myappid = 'theenigmaproject.crypto.easyRSA.001'  # arbitrary string
            ctypes.windll.shell32.SetCurrentProcessExplicitAppUserModelID(myappid)
            titleBarFlag = True
        case other:
            titleBarFlag = False
    app = QApplication(sys.argv)
    # app.setWindowIcon(QIcon('icon.png'))
    window = MainWindow()
    sys.exit(app.exec())
