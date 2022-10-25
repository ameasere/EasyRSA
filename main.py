"""
Main Driver Code for EasyRSA
"""
# ///////////////////////////////////////////////////////////////
#
# BY: WANDERSON M.PIMENTA
# PROJECT MADE WITH: Qt Designer and PySide6
# V: 0.0.2
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
# Made by Bartosz Rzepka (DevPanada), Leighton Brooks (enigmapr0ject)
# 21477187 / 21472005
# Theme by Zeno Rocha: https://zenorocha.com/
# noinspection PyUnresolvedReferences
import json
# noinspection PyUnresolvedReferences
import os
# noinspection PyUnresolvedReferences
import platform
# noinspection PyUnresolvedReferences
import sys
# noinspection PyUnresolvedReferences
import webbrowser
from msilib.schema import DuplicateFile
import shutil

# noinspection PyUnresolvedReferences
import pyperclip
import requests
# noinspection PyUnresolvedReferences
import rsa
# noinspection PyUnresolvedReferences
import time
# noinspection PyUnresolvedReferences
import ntpath
# noinspection PyUnresolvedReferences
from threading import *
# noinspection PyUnresolvedReferences
from PySide6 import QtGui, QtWidgets, QtCore
# noinspection PyUnresolvedReferences
from PySide6.QtWidgets import QMainWindow
# noinspection PyUnresolvedReferences
from modules import *

# warnings.filterwarnings('ignore')
# os.environ['QT_DEBUG_PLUGINS'] = "1"
# FIX Problem for High DPI and Scale above 100%
os.environ["QT_FONT_DPI"] = "96"
title = "EasyRSA"
description = "RSA made simple."


class MainWindow(QMainWindow):
    """
    Dashboard
    """

    def __init__(self, anonymous=False, publicKey=None, privateKey=None, newUser=False):
        QMainWindow.__init__(self)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        widgets = self.ui
        self.rt: RepeatedTimer | None = None
        self.model: QtWidgets.QFileSystemModel | None = None
        self.dragPos = None
        self.filepath: str | None = None
        self.anonymous = anonymous
        if publicKey and privateKey:
            self.__publicKey = publicKey
            self.__privateKey = privateKey
        elif newUser:
            pass
        else:
            # Check if the directory exists
            if not os.path.exists(os.getcwd() + "/.keys") or len(os.listdir(os.getcwd() + "/.keys")) == 0:
                (self.__publicKey, self.__privateKey) = rsa.newkeys(2048, poolsize=psutil.cpu_count())
                os.mkdir(os.getcwd() + "/.keys")
                # Export the keys to files and place them in ".keys" folder
                with open(".keys/public.pem", "wb") as f:
                    f.write(self.__publicKey.save_pkcs1())
                    f.close()
                with open(".keys/private.pem", "wb") as f:
                    f.write(self.__privateKey.save_pkcs1())
                    f.close()
            else:
                # Read the keys
                with open(".keys/public.pem", "rb") as f:
                    self.__publicKey = rsa.PublicKey.load_pkcs1(f.read())
                    f.close()
                with open(".keys/private.pem", "rb") as f:
                    self.__privateKey = rsa.PrivateKey.load_pkcs1(f.read())
                    f.close()
        Settings.ENABLE_CUSTOM_TITLE_BAR = titleBarFlag
        # APPLY TEXTS
        self.setWindowTitle(title)
        # widgets.titleRightInfo.setText(description)

        # TOGGLE MENU
        widgets.toggleButton.clicked.connect(
            lambda: UIFunctions.toggleMenu(self, True))

        # SET UI DEFINITIONS
        UIFunctions.uiDefinitions(self)

        # QTableWidget PARAMETERS
        widgets.tableWidget.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)

        # BUTTONS CLICK
        widgets.btn_home.clicked.connect(self.buttonClick)
        widgets.btn_filespace.clicked.connect(self.buttonClick)
        widgets.btn_passwords.clicked.connect(self.buttonClick)
        widgets.btn_account.clicked.connect(self.buttonClick)
        widgets.btn_exit.clicked.connect(self.buttonClick)
        widgets.closeAppBtn.clicked.connect(self.buttonClick)
        if self.anonymous:
            widgets.extraLabel.setText("Anonymous")
        else:
            pass

        # EXTRA LEFT BOX
        def openCloseLeftBox():
            """
            Open/Close Extra Left Box
            :return:
            """
            UIFunctions.toggleLeftBox(self, True)

        widgets.toggleLeftBox.clicked.connect(openCloseLeftBox)
        widgets.extraCloseColumnBtn.clicked.connect(openCloseLeftBox)

        # EXTRA RIGHT BOX
        def openCloseRightBox():
            """
            Open/Close Extra Right Box
            :return:
            """
            UIFunctions.toggleRightBox(self, True)

        widgets.settingsTopBtn.clicked.connect(openCloseRightBox)
        widgets.btn_logout.clicked.connect(self.buttonClick)
        widgets.btn_help.clicked.connect(self.buttonClick)
        widgets.btn_report.clicked.connect(self.buttonClick)
        widgets.btn_credits.clicked.connect(self.buttonClick)
        # SHOW APP
        self.show()
        widgets.btn_more.clicked.connect(self.buttonClick)

        """
        themeFile = "themes\\Hookmark.qss"

        # SET THEME AND HACKS
        UIFunctions.theme(self, themeFile, True)
        AppFunctions.setThemeHack(self)
        """
        # Search for config file
        stem = os.getcwd()
        stem += "\\config\\config.json"
        if not os.path.exists(stem):
            # Create JSON object
            data = {"defaultSDLocation": os.getcwd()}
            with open(stem, "w") as f:
                json.dump(data, f)
                f.close()
        else:
            with open(stem, "r") as f:
                self.configArray = json.load(f)
                f.close()

        # SET HOME PAGE AND SELECT MENU
        widgets.stackedWidget.setCurrentWidget(widgets.home)
        widgets.btn_home.setStyleSheet(
            UIFunctions.selectMenu(
                widgets.btn_home.styleSheet()))
        # Home Screen
        self.ui.credits.hide()
        self.ui.openFilepathButton.clicked.connect(self.buttonClick)
        self.ui.filepathBox.returnPressed.connect(self.buttonClick)
        self.ui.encryptButton.clicked.connect(self.buttonClick)
        self.ui.decryptButton.clicked.connect(self.buttonClick)
        # Main Page functionality

        self.ui.publicKeyDisplay.setPlainText(str(self.__publicKey))
        self.ui.privateKeyDisplay.setPlainText("PrivateKey(***********)")

        # Private Key Checkbox Tick
        self.ui.privateKeyCheckbox.stateChanged.connect(
            self.privateKeyCheckboxTick)

        # Copy Private Key
        self.ui.copyPrivateKeyButton.clicked.connect(self.buttonClick)

        # Filespace Page functionality

        # Multiview Checkbox Tick
        self.ui.multiviewCheckbox.stateChanged.connect(self.buttonClick)
        self.ui.openDirectory.clicked.connect(self.buttonClick)
        self.ui.defaultLocation.clicked.connect(self.buttonClick)
        self.ui.goToDefault.clicked.connect(self.buttonClick)
        self.ui.goBackButton.clicked.connect(self.buttonClick)

        # Multiview disabled by default
        self.ui.defaultLocation.hide()
        self.ui.driveInfo.hide()
        self.ui.driveInfoTitle.hide()
        self.ui.fileBrowserTree.hide()
        self.ui.goToDefault.hide()
        self.ui.openDirectory.hide()
        self.ui.parentDrive.hide()
        self.ui.parentDriveSpace.hide()
        self.ui.parentDriveTitle.hide()
        self.ui.goBackButton.hide()
        self.ui.filepathBox.show()
        self.ui.openFilepathButton.show()

    def openFile(self, index):
        item = index.model().filePath(self.ui.fileBrowserTree.currentIndex())
        if not os.path.isfile(item):
            return
        if platform.system() == "Windows":
            os.startfile(item)
        else:
            import subprocess
            opener = "open" if platform.system() == "Darwin" else "xdg-open"
            subprocess.call([opener, item])

    def encrypt(self, index):
        if isinstance(index, str):
            self.filepath = index
        else:
            if not index.isValid():
                self.ui.cryptoFeedbackTitle.setText("Encryption failed: No file selected")
                return
            self.filepath = index.model().filePath(index)
        if index is None:
            self.ui.cryptoFeedbackTitle.setText("Encryption failed: No file selected")
            return
        if not os.path.isfile(self.filepath):
            self.ui.cryptoFeedbackTitle.setText("Encryption failed: Not a file")
            return
        if os.stat(self.filepath).st_size == 0:
            self.ui.cryptoFeedbackTitle.setText("Encryption failed: File is empty")
            return
        self.ui.cryptoWarningTitle.setText("Warning: This can take a while depending on a number of factors.")
        self.ui.cryptoFeedbackTitle.setText("Encrypting...")
        with open(self.filepath, 'rb') as f:
            # Get the file name
            filename = os.path.basename(self.filepath)
            # Get the file extension
            file_extension = os.path.splitext(filename)[1]
            # New filename
            new_filename = filename.replace(file_extension, ".enc" + file_extension)
            # Add this to the path of the original file
            new_filepath = os.path.join(os.path.dirname(self.filepath), new_filename)
            # Read file in 2048 bit chunks, encrypt them and print them
            start = time.perf_counter()
            for chunk in iter(lambda: f.read(round((2048 / 8) - 11)), b''):
                # Encrypt chunk
                rsa.encrypt(chunk, self.__publicKey)
                with open(new_filepath, 'ab') as e:
                    e.write(rsa.encrypt(chunk, self.__publicKey))
                    e.close()
            end = time.perf_counter()
            f.close()
        self.ui.cryptoFeedbackTitle.setText("Encryption Complete!")
        self.ui.processingTime.setText("Time taken: " + str(round(end - start, 2)) + " seconds")
        self.ui.processingSize.setText("Filesize: " + str(round(os.path.getsize(self.filepath) / 1000000, 2)) + " MB")
        self.ui.cryptoWarningTitle.setText("")
        return True

    def decrypt(self, index):
        # If index is a string
        if isinstance(index, str):
            self.filepath = index
        else:
            if not index.isValid():
                self.ui.cryptoFeedbackTitle.setText("Decryption failed: No file selected")
                return
            self.filepath = index.model().filePath(index)
        if index is None:
            self.ui.cryptoFeedbackTitle.setText("Decryption failed: No file selected")
            return
        if not os.path.isfile(self.filepath):
            self.ui.cryptoFeedbackTitle.setText("Decryption failed: Not a file")
            return
        if os.stat(self.filepath).st_size == 0:
            self.ui.cryptoFeedbackTitle.setText("Decryption failed: File is empty")
            return
        self.ui.cryptoWarningTitle.setText("Warning: This can take a while depending on a number of factors.")
        self.ui.cryptoFeedbackTitle.setText("Decrypting...")
        with open(self.filepath, 'rb') as f:
            # Get the file name
            filename = os.path.basename(self.filepath)
            # Get the file extension
            file_extension = os.path.splitext(filename)[1]
            # New filename
            new_filename = filename.replace(file_extension, ".dec" + file_extension).replace(".enc", "")
            # Add this to the path of the original file
            new_filepath = os.path.join(os.path.dirname(self.filepath), new_filename)
            # Read file in 2048 bit chunks, encrypt them and print them
            start = time.perf_counter()
            # Account for padding
            for chunk in iter(lambda: f.read(round(2048 / 8)), b''):
                # Encrypt chunk
                try:
                    with open(new_filepath, 'ab') as d:
                        d.write(rsa.decrypt(chunk, self.__privateKey))
                        d.close()
                except rsa.pkcs1.DecryptionError as e:
                    self.ui.cryptoFeedbackTitle.setText("Decryption failed!")
                    # Set the error message into the warning label
                    self.ui.cryptoWarningTitle.setText(str(e))
                    os.remove(new_filepath)
                    return False
            end = time.perf_counter()
            f.close()
        self.ui.cryptoFeedbackTitle.setText("Decryption Complete!")
        self.ui.processingTime.setText("Time taken: " + str(round(end - start, 2)) + " seconds")
        self.ui.processingSize.setText("Filesize: " + str(round(os.path.getsize(self.filepath) / 1000000, 2)) + " MB")
        self.ui.cryptoWarningTitle.setText("")
        return True

    # BUTTON CLICK
    def buttonClick(self):
        """
        Button Click event handler
        :return:
        """
        # GET BUTTON CLICKED
        btn = self.sender()
        btnName = btn.objectName()
        match btnName:
            # SHOW NEW PAGE
            case "closeAppBtn":
                try:
                    self.rt.stop()
                    self.close()
                    sys.exit(0)
                except AttributeError:
                    self.close()
                    sys.exit(0)
                except Exception as e:
                    print(repr(e))
            case "btn_home":
                self.ui.titleLeftDescription.setText("Dashboard")  # SET PAGE
                self.ui.stackedWidget.setCurrentWidget(
                    self.ui.home)  # RESET ANOTHERS BUTTONS SELECTED
                UIFunctions.resetStyle(self, btnName)
                btn.setStyleSheet(
                    UIFunctions.selectMenu(
                        btn.styleSheet()))  # SELECT MENU
            case "btn_filespace":
                self.ui.titleLeftDescription.setText("Filespace")
                self.ui.stackedWidget.setCurrentWidget(self.ui.filespace)
                UIFunctions.resetStyle(self, btnName)
                btn.setStyleSheet(UIFunctions.selectMenu(btn.styleSheet()))
            case "btn_passwords":
                self.ui.titleLeftDescription.setText("Page 3")
                self.ui.stackedWidget.setCurrentWidget(self.ui.page3)
                UIFunctions.resetStyle(self, btnName)
                btn.setStyleSheet(UIFunctions.selectMenu(btn.styleSheet()))
            case "btn_account":
                self.ui.titleLeftDescription.setText("Page 4")
                self.ui.stackedWidget.setCurrentWidget(self.ui.page4)
                UIFunctions.resetStyle(self, btnName)
                btn.setStyleSheet(UIFunctions.selectMenu(btn.styleSheet()))
            case "btn_exit":
                self.close()
            case "btn_logout":
                self.close()
            case "btn_credits":
                # Check if the credits are already showing
                if self.ui.credits.isHidden():
                    self.ui.credits.show()
                else:
                    self.ui.credits.hide()
            case "btn_help":
                webbrowser.get().open("https://github.com/enigmapr0ject/EasyRSA")
            case "btn_report":
                webbrowser.get().open("https://github.com/enigmapr0ject/EasyRSA/issues")
            case "btn_more":
                webbrowser.get().open("https://github.com/enigmapr0ject")
            case "copyPrivateKeyButton":
                pyperclip.copy(self.ui.privateKeyDisplay.toPlainText())
            case "multiviewCheckbox":
                if self.ui.multiviewCheckbox.isChecked():
                    self.ui.filepathBox.hide()
                    self.ui.openFilepathButton.hide()
                    self.ui.encryptButton.hide()
                    self.ui.decryptButton.hide()
                    self.ui.defaultLocation.show()
                    self.ui.driveInfo.show()
                    self.ui.driveInfoTitle.show()
                    self.ui.fileBrowserTree.show()
                    self.ui.goToDefault.show()
                    self.ui.openDirectory.show()
                    self.ui.parentDrive.show()
                    self.ui.parentDriveSpace.show()
                    self.ui.parentDriveTitle.show()
                    self.ui.goBackButton.show()
                    self.model = QFileSystemModel()
                    self.model.setRootPath(os.getcwd())
                    self.ui.fileBrowserTree.setModel(
                        self.model)  # Set the model
                    if os.path.exists(self.configArray["defaultSDLocation"]):
                        self.ui.fileBrowserTree.setRootIndex(
                            self.model.index(self.configArray['defaultSDLocation']) if self.configArray[
                                                                                           'defaultSDLocation'] != "" else
                            self.model.index(
                                os.getcwd()))  # Set the first displaying directory
                    # If directory in defaultSDLocation doesn't exist on the
                    # current machine, use current directory
                    else:
                        self.ui.fileBrowserTree.setRootIndex(
                            self.model.index(os.getcwd()))
                        self.model.index(os.getcwd())
                    self.ui.fileBrowserTree.doubleClicked.connect(
                        self.openFile)
                    self.ui.fileBrowserTree.setAlternatingRowColors(
                        False)  # Set the alternating row colors
                    self.ui.fileBrowserTree.setSortingEnabled(
                        True)  # Set the sorting
                    # Default sort by name
                    self.ui.fileBrowserTree.sortByColumn(0, Qt.AscendingOrder)
                    self.ui.fileBrowserTree.setColumnWidth(0, 200)
                    self.ui.fileBrowserTree.setColumnWidth(1, 150)
                    self.ui.fileBrowserTree.setColumnWidth(2, 200)
                    self.ui.fileBrowserTree.setColumnWidth(3, 200)
                    # Set the context menu
                    self.ui.fileBrowserTree.setContextMenuPolicy(
                        QtCore.Qt.ContextMenuPolicy.CustomContextMenu)
                    # (right clicking)
                    self.ui.fileBrowserTree.customContextMenuRequested.connect(
                        self.contextMenu)  # Custom right click
                    # menu
                    # self.ui.fileBrowserTree.doubleClicked.connect() #
                    # Double-clicking on a file has a special effect
                    drivestats = DriveStatistics()
                    self.ui.parentDrive.setText(
                        "Parent Drive: %s" % drivestats.parentDrive)
                    self.ui.parentDriveSpace.setValue(
                        drivestats.parentDriveSpace)
                    self.ui.driveInfo.setText(drivestats.driveInformation)
                    if not self.rt:
                        self.rt = RepeatedTimer(5, self.driveStatistics)
                        self.rt.start()
                    else:
                        self.rt.start()
                else:
                    self.rt.stop()
                    self.ui.defaultLocation.hide()
                    self.ui.driveInfo.hide()
                    self.ui.driveInfoTitle.hide()
                    self.ui.fileBrowserTree.hide()
                    self.ui.goToDefault.hide()
                    self.ui.openDirectory.hide()
                    self.ui.parentDrive.hide()
                    self.ui.goBackButton.hide()
                    self.ui.parentDriveSpace.hide()
                    self.ui.parentDriveTitle.hide()
                    self.ui.filepathBox.show()
                    self.ui.openFilepathButton.show()
                    self.ui.encryptButton.show()
                    self.ui.decryptButton.show()
            case "openFilepathButton":
                self.filepath = QFileDialog.getOpenFileName(
                    self, "Select File", os.getcwd(), "All Files (*)")[0]
                if self.filepath == "":
                    return
                self.ui.filepathBox.setText(self.filepath)
            case "openDirectory":
                self.filepath = QFileDialog.getExistingDirectory(
                    self, "Select Directory", os.getcwd())
                if self.filepath == "":
                    return
                self.ui.fileBrowserTree.setRootIndex(
                    self.model.index(self.filepath))
            case "defaultLocation":
                self.filepath = QFileDialog.getExistingDirectory(
                    self, "Select Directory", os.getcwd())
                if self.filepath == "":
                    return
                self.ui.fileBrowserTree.setRootIndex(
                    self.model.index(self.filepath))
                self.configArray["defaultSDLocation"] = self.filepath
                with open("config\\config.json", "w") as f:
                    json.dump(self.configArray, f)
                    f.close()
            case "goToDefault":
                self.ui.fileBrowserTree.setRootIndex(
                    self.model.index(self.configArray['defaultSDLocation']))
            case "encryptButton":
                self.filepath = self.ui.filepathBox.text()
                if self.filepath == "":
                    self.ui.cryptoWarningTitle.setText("No file selected")
                    return
                p1 = Thread(target=self.encrypt, args=(self.filepath,))
                p1.start()
            case "filepathBox":
                self.filepath = self.ui.filepathBox.text()
                if self.filepath == "":
                    self.ui.cryptoWarningTitle.setText("No file selected")
                    return
                p1 = Thread(target=self.encrypt, args=(self.filepath,))
                p1.start()
            case "decryptButton":
                self.filepath = self.ui.filepathBox.text()
                if self.filepath == "":
                    self.ui.cryptoWarningTitle.setText("No file selected")
                    return
                p1 = Thread(target=self.decrypt, args=(self.filepath,))
                p1.start()
            case "goBackButton":
                self.filepath = self.model.filePath(
                    self.ui.fileBrowserTree.rootIndex())
                self.filepath = os.path.dirname(self.filepath)
                self.ui.fileBrowserTree.setRootIndex(
                    self.model.index(self.filepath))

    # Multiview drive statistics

    def driveStatistics(self):
        """
        Drive statistics for multiview, in realtime
        """
        drivestats = DriveStatistics()
        self.ui.parentDrive.setText(
            "Parent Drive: %s" %
            drivestats.parentDrive)
        self.ui.parentDriveSpace.setValue(drivestats.parentDriveSpace)
        self.ui.driveInfo.setText(drivestats.driveInformation)

    # Private Key Checkbox Tick
    def privateKeyCheckboxTick(self):
        """
        Private Key Checkbox Tick event
        :return:
        """
        if self.ui.privateKeyCheckbox.isChecked():
            self.ui.privateKeyDisplay.setPlainText(str(self.__privateKey))
        else:
            self.ui.privateKeyDisplay.setPlainText("PrivateKey(***********)")

    # Custom Context Menu
    def contextMenu(self):
        def renameFile():
            # Check if the file is a directory
            if self.ui.fileBrowserTree.currentIndex().isValid() and not self.model.isDir(
                    self.ui.fileBrowserTree.currentIndex()):
                index = self.ui.fileBrowserTree.currentIndex()
                file_path = self.model.filePath(index)
                self.rename = RenameFileWindow(file_path)
                self.rename.show()
            else:
                # Set the window title
                self.setWindowTitle("EasyRSA - No file selected")

        def deleteFile():
            # Check if the file is a directory
            if self.ui.fileBrowserTree.currentIndex().isValid() and not self.model.isDir(
                    self.ui.fileBrowserTree.currentIndex()):
                index = self.ui.fileBrowserTree.currentIndex()
                file_path = self.model.filePath(index)
                self.delete = DeleteConfirm(file_path)
                self.delete.show()
            else:
                # Set the window title
                self.setWindowTitle("EasyRSA - No file selected")

        def moveFile():
            if self.ui.fileBrowserTree.currentIndex().isValid() and not self.model.isDir(
                    self.ui.fileBrowserTree.currentIndex()):
                index = self.ui.fileBrowserTree.currentIndex()
                file_path = self.model.filePath(index)
                self.move = MoveFile(file_path)
                self.move.show()
            else:
                # Set the window title
                self.setWindowTitle("EasyRSA - No file selected")

        def duplicateFile():
            if self.ui.fileBrowserTree.currentIndex().isValid() and not self.model.isDir(
                    self.ui.fileBrowserTree.currentIndex()):
                index = self.ui.fileBrowserTree.currentIndex()
                file_path = self.model.filePath(index)
                ext = "." + file_path.split(".")[len(file_path.split(".")) - 1]
                duplicate_file_path = file_path.replace(ext, "(copy)" + ext)
                while os.path.exists(duplicate_file_path):
                    duplicate_file_path = file_path.replace(ext, "(copy)" + ext)
                shutil.copy(file_path, duplicate_file_path)
            else:
                # Set the window title
                self.setWindowTitle("EasyRSA - No file selected")

        """
        Custom Context Menu
        :return:
        """
        menu = QtWidgets.QMenu()
        menu.setStyleSheet(
            "QMenu {background-color: rgb(33, 37, 43); font: 8pt \"Segoe UI\"; color: rgb(189, 147, 249);}"
            "QMenu::item:selected {color: rgb(255, 255, 255); background-color: rgb(254, 120, 198); border-style: "
            "solid; border-radius: 4px;} "
            "QMenu::item {color: rgb(254, 120, 198); background-color: rgb(40, 44, 52; border-style: solid; "
            "border-radius: 4px;}")
        renameAction = QAction("Rename File")
        deleteAction = QAction("Delete File")
        moveAction = QAction("Move File")
        duplicateAction = QAction("Duplicate File")
        encryptAction = QAction("Encrypt File")
        decryptAction = QAction("Decrypt File")
        menu.addAction(encryptAction)
        menu.addAction(decryptAction)
        menu.addAction(duplicateAction)
        menu.addAction(renameAction)
        menu.addAction(moveAction)
        menu.addAction(deleteAction)
        # Connect context menu buttons to functions
        renameAction.triggered.connect(renameFile)
        deleteAction.triggered.connect(deleteFile)
        duplicateAction.triggered.connect(duplicateFile)
        moveAction.triggered.connect(moveFile)
        # Include file path of the selected item in the context menu
        encryptAction.triggered.connect(
            lambda: Thread(target=self.encrypt, args=(self.ui.fileBrowserTree.currentIndex(),)).start())
        decryptAction.triggered.connect(
            lambda: Thread(target=self.decrypt, args=(self.ui.fileBrowserTree.currentIndex(),)).start())
        cursor = QtGui.QCursor()
        menu.exec_(cursor.pos())

    # RESIZE EVENTS
    def resizeEvent(self, event):
        """
        Resize event
        :param event:
        :return:
        """
        UIFunctions.resize_grips(self)

    # MOUSE CLICK EVENTS
    def mousePressEvent(self, event):
        """
        Mouse press event
        :param event:
        :return:
        """
        # SET DRAG POS WINDOW
        self.dragPos = event.globalPos()


class LoginWindow(QMainWindow):
    def __init__(self):
        QMainWindow.__init__(self)
        # SET AS GLOBAL WIDGETS
        # ///////////////////////////////////////////////////////////////
        self.ui = Ui_LoginWindow()
        self.ui.setupUi(self)
        widgets = self.ui
        widgets.passbox.setEchoMode(QtWidgets.QLineEdit.Password)
        widgets.showpassword.stateChanged.connect(self.showPassword)
        widgets.loginButton.clicked.connect(self.login)
        widgets.registerButton.clicked.connect(self.register)
        widgets.cancelbutton.clicked.connect(self.register)
        widgets.submitbutton.clicked.connect(self.login)
        widgets.anonMode.clicked.connect(self.anonymousMode)
        widgets.closeAppBtn.clicked.connect(self.close)
        # USE CUSTOM TITLE BAR | USE AS "False" FOR MAC OR LINUX
        # ///////////////////////////////////////////////////////////////
        Settings.ENABLE_CUSTOM_TITLE_BAR = titleBarFlag

        widgets.supportButton.clicked.connect(self.supportButton)
        widgets.supportButton_2.clicked.connect(self.supportButton)
        # TOGGLE MENU
        # ///////////////////////////////////////////////////////////////
        # widgets.toggleButton.clicked.connect(lambda: UIFunctions.toggleMenu(self, True))
        # SET UI DEFINITIONS
        # ///////////////////////////////////////////////////////////////
        UIFunctions.uiDefinitions(self)
        # SHOW APP
        # ///////////////////////////////////////////////////////////////
        self.show()

        # SET CUSTOM THEME
        # ///////////////////////////////////////////////////////////////
        useCustomTheme = False
        themeFile = "themes\py_dracula_light.qss"

        # SET THEME AND HACKS
        if useCustomTheme:
            # LOAD AND APPLY STYLE
            UIFunctions.theme(self, themeFile, True)

            # SET HACKS
            AppFunctions.setThemeHack(self)

        # SET HOME PAGE AND SELECT MENU
        # ///////////////////////////////////////////////////////////////
        widgets.stackedWidget.setCurrentWidget(widgets.home)
        # widgets.btn_home.setStyleSheet(UIFunctions.selectMenu(widgets.btn_home.styleSheet()))

    def supportButton(self):
        webbrowser.get().open("https://github.com/enigmapr0ject/EasyRSA/issues")

    def showPassword(self):
        if self.ui.showpassword.isChecked():
            self.ui.passbox.setEchoMode(QtWidgets.QLineEdit.Normal)
        else:
            self.ui.passbox.setEchoMode(QtWidgets.QLineEdit.Password)

    def anonymousMode(self):
        # Check if the ".keys" folder exists and is populated
        if os.path.exists(os.path.join(os.getcwd(), ".keys")) and len(
                os.listdir(os.path.join(os.getcwd(), ".keys"))) > 0:
            self.close()
            self.main = MainWindow(anonymous=True)
            self.main.show()
        else:
            self.close()
            self.anonymous = AnonymousWindow()
            self.anonymous.show()

    def login(self):
        self.username = self.ui.userbox.text()
        self.password = self.ui.passbox.text()
        postData = {"Username": self.username, "Password": self.password}
        response = requests.post("https://enigmapr0ject.tech/api/easyrsa/login.php",
                                 data=postData).content.decode('utf-8')
        if response == "2":
            self.mainWindow = MainWindow()
            self.mainWindow.show()
        else:
            self.ui.responsetitle.setText(response)
            print(response)

    def register(self):
        self.fade()
        self.main = RegisterWindow()
        self.main.show()

    def fade(self):
        for i in range(10):
            i = i / 10
            self.setWindowOpacity(1 - i)
            time.sleep(0.02)
        self.close()

    def exitHandler(self):
        self.close()

    # RESIZE EVENTS
    # ///////////////////////////////////////////////////////////////
    def resizeEvent(self, event):
        # Update Size Grips
        UIFunctions.resize_grips(self)

    # MOUSE CLICK EVENTS
    # ///////////////////////////////////////////////////////////////
    def mousePressEvent(self, event):
        # SET DRAG POS WINDOW
        self.dragPos = event.globalPos()


class RegisterWindow(QMainWindow):
    def __init__(self):
        QMainWindow.__init__(self)

        # SET AS GLOBAL WIDGETS
        # ///////////////////////////////////////////////////////////////
        self.ui = Ui_RegisterWindow()
        self.ui.setupUi(self)
        widgets = self.ui
        widgets.loginButton.clicked.connect(self.login)
        widgets.registerButton.clicked.connect(self.register)
        widgets.closeAppBtn.clicked.connect(self.close)
        # USE CUSTOM TITLE BAR | USE AS "False" FOR MAC OR LINUX
        # ///////////////////////////////////////////////////////////////
        Settings.ENABLE_CUSTOM_TITLE_BAR = titleBarFlag

        # APP NAME
        # ///////////////////////////////////////////////////////////////
        widgets.supportButton.clicked.connect(self.supportButton)
        # TOGGLE MENU
        # ///////////////////////////////////////////////////////////////
        # widgets.toggleButton.clicked.connect(lambda: UIFunctions.toggleMenu(self, True))

        # SET UI DEFINITIONS
        # ///////////////////////////////////////////////////////////////
        UIFunctions.uiDefinitions(self)

        # SHOW APP
        # ///////////////////////////////////////////////////////////////
        self.show()

        # SET CUSTOM THEME
        # ///////////////////////////////////////////////////////////////
        useCustomTheme = False
        themeFile = "themes\py_dracula_light.qss"

        # SET THEME AND HACKS
        if useCustomTheme:
            # LOAD AND APPLY STYLE
            UIFunctions.theme(self, themeFile, True)

            # SET HACKS
            AppFunctions.setThemeHack(self)

        # SET HOME PAGE AND SELECT MENU
        # ///////////////////////////////////////////////////////////////
        widgets.stackedWidget.setCurrentWidget(widgets.home)
        # widgets.btn_home.setStyleSheet(UIFunctions.selectMenu(widgets.btn_home.styleSheet()))

    # BUTTONS CLICK
    # Post here your functions for clicked buttons
    def supportButton(self):
        webbrowser.get().open("https://github.com/enigmapr0ject/EasyRSA/issues")

    def login(self):
        self.fade()
        self.login = LoginWindow()
        self.login.show()

    def register(self):
        username = self.ui.userbox.text()
        emailaddress = self.ui.emailbox.text()
        postData = {"Username": username, "Email": emailaddress}
        response = requests.post("https://enigmapr0ject.tech/api/easyrsa/register.php", data=postData).content.decode(
            'utf-8')
        self.ui.responsetitle.setText(response)

    def fade(self):
        for i in range(10):
            i = i / 10
            self.setWindowOpacity(1 - i)
            time.sleep(0.02)
        self.close()

    def exitHandler(self):
        self.close()

    # RESIZE EVENTS
    # ///////////////////////////////////////////////////////////////
    def resizeEvent(self, event):
        # Update Size Grips
        UIFunctions.resize_grips(self)

    # MOUSE CLICK EVENTS
    # ///////////////////////////////////////////////////////////////
    def mousePressEvent(self, event):
        # SET DRAG POS WINDOW
        self.dragPos = event.globalPos()


class AnonymousWindow(QMainWindow):
    def __init__(self):
        QMainWindow.__init__(self)
        # SET AS GLOBAL WIDGETS
        # ///////////////////////////////////////////////////////////////
        self.ui = Ui_Anonymous()
        self.ui.setupUi(self)
        widgets = self.ui
        # USE CUSTOM TITLE BAR | USE AS "False" FOR MAC OR LINUX
        # ///////////////////////////////////////////////////////////////
        Settings.ENABLE_CUSTOM_TITLE_BAR = titleBarFlag

        # TOGGLE MENU
        # ///////////////////////////////////////////////////////////////
        # widgets.toggleButton.clicked.connect(lambda: UIFunctions.toggleMenu(self, True))
        # SET UI DEFINITIONS
        # ///////////////////////////////////////////////////////////////
        UIFunctions.uiDefinitions(self)
        # SHOW APP
        # ///////////////////////////////////////////////////////////////
        self.show()
        widgets.yesButton.clicked.connect(self.yes)
        widgets.noButton.clicked.connect(self.no)
        widgets.closeAppBtn.clicked.connect(self.close)
        # SET CUSTOM THEME
        # ///////////////////////////////////////////////////////////////
        useCustomTheme = False
        themeFile = "themes\\py_dracula_light.qss"

        # SET THEME AND HACKS
        if useCustomTheme:
            # LOAD AND APPLY STYLE
            UIFunctions.theme(self, themeFile, True)

            # SET HACKS
            AppFunctions.setThemeHack(self)

        # SET HOME PAGE AND SELECT MENU
        # ///////////////////////////////////////////////////////////////
        widgets.stackedWidget.setCurrentWidget(widgets.home)
        # widgets.btn_home.setStyleSheet(UIFunctions.selectMenu(widgets.btn_home.styleSheet()))

    def yes(self):
        # Check the tickbox is checked
        if self.ui.acceptBox.isChecked():
            self.ui.responsetitle.setText("Generating keys...")
            self.main = MainWindow(anonymous=True)
            self.main.show()
        else:
            self.ui.responsetitle.setText("You must tick the box above.")
            return
        self.fade()

    def no(self):
        self.close()
        self.main = LoginWindow()
        self.main.show()

    def fade(self):
        for i in range(10):
            i = i / 10
            self.setWindowOpacity(1 - i)
            time.sleep(0.02)
        self.close()

    # RESIZE EVENTS
    # ///////////////////////////////////////////////////////////////
    def resizeEvent(self, event):
        # Update Size Grips
        UIFunctions.resize_grips(self)

    # MOUSE CLICK EVENTS
    # ///////////////////////////////////////////////////////////////
    def mousePressEvent(self, event):
        # SET DRAG POS WINDOW
        self.dragPos = event.globalPos()

    def exitHandler(self):
        self.fade()


class RenameFileWindow(QMainWindow):
    def __init__(self, filepath):
        QMainWindow.__init__(self)
        # SET AS GLOBAL WIDGETS
        # ///////////////////////////////////////////////////////////////
        self.ui = Ui_RenameWindow()
        self.ui.setupUi(self)
        self.filepath = filepath
        self.newName: str | None = None
        widgets = self.ui
        # USE CUSTOM TITLE BAR | USE AS "False" FOR MAC OR LINUX
        # ///////////////////////////////////////////////////////////////
        match platform.system():
            case "Windows":
                titleBarFlag = True
            case _:
                titleBarFlag = False
        Settings.ENABLE_CUSTOM_TITLE_BAR = titleBarFlag

        # TOGGLE MENU
        # ///////////////////////////////////////////////////////////////
        # widgets.toggleButton.clicked.connect(lambda: UIFunctions.toggleMenu(self, True))
        # SET UI DEFINITIONS
        # ///////////////////////////////////////////////////////////////
        UIFunctions.uiDefinitions(self)
        # SHOW APP
        # ///////////////////////////////////////////////////////////////
        self.show()
        widgets.confirmButton.clicked.connect(self.confirm)
        widgets.cancelButton.clicked.connect(self.fade)
        widgets.closeAppBtn.clicked.connect(self.close)
        # SET CUSTOM THEME
        # ///////////////////////////////////////////////////////////////
        useCustomTheme = False
        themeFile = "themes\\py_dracula_light.qss"

        # SET THEME AND HACKS
        if useCustomTheme:
            # LOAD AND APPLY STYLE
            UIFunctions.theme(self, themeFile, True)

            # SET HACKS
            AppFunctions.setThemeHack(self)

        # SET HOME PAGE AND SELECT MENU
        # ///////////////////////////////////////////////////////////////
        widgets.stackedWidget.setCurrentWidget(widgets.home)
        # widgets.btn_home.setStyleSheet(UIFunctions.selectMenu(widgets.btn_home.styleSheet()))

    def confirm(self):
        """
        The function takes the filepath of the file to be renamed and renames it to the new name.

        """
        self.newName = self.ui.fileNameBox.text()

        def path_leaf(path):  # Splits path names into tails and heads
            head, tail = ntpath.split(path)
            return head

        stem = path_leaf(self.filepath)
        if systemLabel == "Darwin" or systemLabel == "Linux":
            self.newName = stem + "/" + self.newName
        else:
            self.newName = stem + "\\" + self.newName
        if len(self.newName) < 1:
            self.ui.responseTitle.setText("Blank file names don't exist!")
        else:
            try:
                os.rename(self.filepath, self.newName)
                self.fade()
            except Exception as e:
                self.ui.responseTitle.setText("Error: %s" % e)

    def fade(self):
        for i in range(10):
            i = i / 10
            self.setWindowOpacity(1 - i)
            time.sleep(0.02)
        self.close()

    # RESIZE EVENTS
    # ///////////////////////////////////////////////////////////////
    def resizeEvent(self, event):
        # Update Size Grips
        UIFunctions.resize_grips(self)

    # MOUSE CLICK EVENTS
    # ///////////////////////////////////////////////////////////////
    def mousePressEvent(self, event):
        # SET DRAG POS WINDOW
        self.dragPos = event.globalPos()

    def exitHandler(self):
        self.fade()


class DeleteConfirm(QMainWindow):
    def __init__(self, index):
        QMainWindow.__init__(self)
        # SET AS GLOBAL WIDGETS
        # ///////////////////////////////////////////////////////////////
        self.ui = Ui_ConfirmDeleteWindow()
        self.ui.setupUi(self)
        self.index = index
        widgets = self.ui
        # USE CUSTOM TITLE BAR | USE AS "False" FOR MAC OR LINUX
        # ///////////////////////////////////////////////////////////////
        Settings.ENABLE_CUSTOM_TITLE_BAR = titleBarFlag

        # TOGGLE MENU
        # ///////////////////////////////////////////////////////////////
        # widgets.toggleButton.clicked.connect(lambda: UIFunctions.toggleMenu(self, True))
        # SET UI DEFINITIONS
        # ///////////////////////////////////////////////////////////////
        UIFunctions.uiDefinitions(self)
        # SHOW APP
        # ///////////////////////////////////////////////////////////////
        self.show()
        widgets.yesButton.clicked.connect(self.yes)
        widgets.noButton.clicked.connect(self.fade)
        widgets.closeAppBtn.clicked.connect(self.close)
        # SET CUSTOM THEME
        # ///////////////////////////////////////////////////////////////
        useCustomTheme = False
        themeFile = "themes\\py_dracula_light.qss"

        # SET THEME AND HACKS
        if useCustomTheme:
            # LOAD AND APPLY STYLE
            UIFunctions.theme(self, themeFile, True)

            # SET HACKS
            AppFunctions.setThemeHack(self)

        # SET HOME PAGE AND SELECT MENU
        # ///////////////////////////////////////////////////////////////
        widgets.stackedWidget.setCurrentWidget(widgets.home)
        # widgets.btn_home.setStyleSheet(UIFunctions.selectMenu(widgets.btn_home.styleSheet()))

    def yes(self):
        try:
            os.remove(self.index)
        except Exception as e:
            self.close()
        self.fade()

    def fade(self):
        for i in range(10):
            i = i / 10
            self.setWindowOpacity(1 - i)
            time.sleep(0.02)
        self.close()

    # RESIZE EVENTS
    # ///////////////////////////////////////////////////////////////
    def resizeEvent(self, event):
        # Update Size Grips
        UIFunctions.resize_grips(self)

    # MOUSE CLICK EVENTS
    # ///////////////////////////////////////////////////////////////
    def mousePressEvent(self, event):
        # SET DRAG POS WINDOW
        self.dragPos = event.globalPos()

    def exitHandler(self):
        self.fade()


class MoveFile(QMainWindow):
    def __init__(self, index):
        QMainWindow.__init__(self)
        # SET AS GLOBAL WIDGETS
        # ///////////////////////////////////////////////////////////////
        self.ui = Ui_MoveWindow()
        self.ui.setupUi(self)
        self.index = index
        self.filepath = None
        self.newName: str | None = None
        widgets = self.ui
        # USE CUSTOM TITLE BAR | USE AS "False" FOR MAC OR LINUX
        # ///////////////////////////////////////////////////////////////
        Settings.ENABLE_CUSTOM_TITLE_BAR = titleBarFlag

        # TOGGLE MENU
        # ///////////////////////////////////////////////////////////////
        # widgets.toggleButton.clicked.connect(lambda: UIFunctions.toggleMenu(self, True))
        # SET UI DEFINITIONS
        # ///////////////////////////////////////////////////////////////
        UIFunctions.uiDefinitions(self)
        # SHOW APP
        # ///////////////////////////////////////////////////////////////
        self.show()
        widgets.confirmButton.clicked.connect(self.yes)
        widgets.cancelButton.clicked.connect(self.fade)
        widgets.openFilepathButton.clicked.connect(self.openFile)
        widgets.closeAppBtn.clicked.connect(self.close)
        # SET CUSTOM THEME
        # ///////////////////////////////////////////////////////////////
        useCustomTheme = False
        themeFile = "themes\\py_dracula_light.qss"

        # SET THEME AND HACKS
        if useCustomTheme:
            # LOAD AND APPLY STYLE
            UIFunctions.theme(self, themeFile, True)

            # SET HACKS
            AppFunctions.setThemeHack(self)

        # SET HOME PAGE AND SELECT MENU
        # ///////////////////////////////////////////////////////////////
        widgets.stackedWidget.setCurrentWidget(widgets.home)
        # widgets.btn_home.setStyleSheet(UIFunctions.selectMenu(widgets.btn_home.styleSheet()))

    def yes(self):
        self.newName = self.ui.fileNameBox.text()

        def path_leaf(path):  # Splits path names into tails and heads
            head, tail = ntpath.split(path)
            return tail or ntpath.basename(head)

        # Get file name from index
        stem = path_leaf(self.index)
        if systemLabel == "Darwin" or systemLabel == "Linux":
            self.newName = self.newName + "/" + stem
        else:
            self.newName = self.newName + "\\" + stem
        if len(self.newName) < 1:
            self.ui.responseTitle.setText("Blank file names don't exist!")
        else:
            try:
                os.rename(self.index, self.newName)
                self.fade()
            except Exception as e:
                self.ui.responseTitle.setText("Error: %s" % e)
                print(repr(e))
                print(self.newName)

    def openFile(self):
        # Open file selection window
        self.filepath = QFileDialog.getExistingDirectory(
            self, "Select Directory")
        self.ui.fileNameBox.setText(self.filepath)

    def fade(self):
        for i in range(10):
            i = i / 10
            self.setWindowOpacity(1 - i)
            time.sleep(0.02)
        self.close()

    # RESIZE EVENTS
    # ///////////////////////////////////////////////////////////////
    def resizeEvent(self, event):
        # Update Size Grips
        UIFunctions.resize_grips(self)

    # MOUSE CLICK EVENTS
    # ///////////////////////////////////////////////////////////////
    def mousePressEvent(self, event):
        # SET DRAG POS WINDOW
        self.dragPos = event.globalPos()

    def exitHandler(self):
        self.fade()


if __name__ == "__main__":
    match platform.system():  # Check the OS
        case "Windows":  # If Windows
            import ctypes  # Windows exclusive library

            # arbitrary string, can be anything
            myappid = 'theenigmaproject.crypto.easyRSA.003'
            ctypes.windll.shell32.SetCurrentProcessExplicitAppUserModelID(
                myappid)  # Set the AppID. Needed for
            # taskbar icon and window icons to work.
            # Variable holding the value for if we have a custom titlebar or
            # not. This is broken
            titleBarFlag = True
            # on any other OS.
        case other:
            titleBarFlag = False
    app = QApplication(sys.argv)
    window = LoginWindow()
    sys.exit(app.exec())
