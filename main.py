"""
Main Driver Code for EasyRSA
"""
# noinspection PyUnresolvedReferences
import base64
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
import random
# noinspection PyUnresolvedReferences
import string
# noinspection PyUnresolvedReferences
import sys
# noinspection PyUnresolvedReferences
import webbrowser
# noinspection PyUnresolvedReferences
import shutil
# noinspection PyUnresolvedReferences
import winreg
# noinspection PyUnresolvedReferences
from Cryptodome.Cipher import AES
# noinspection PyUnresolvedReferences
import pyperclip
# noinspection PyUnresolvedReferences
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

from Custom_Widgets.Widgets import *

# warnings.filterwarnings('ignore')
# os.environ['QT_DEBUG_PLUGINS'] = "1"
# FIX Problem for High DPI and Scale above 100%
os.environ["QT_FONT_DPI"] = "96"
title = "EasyRSA"
description = "RSA made simple."


# Check Windows registry for a key to see if there is an encryption key stored
# If there is, use it, if not, generate a new one and store it in the registry
def check_key_nonce() -> bool:
    """
    Check Windows registry for a key to see if there is an encryption key stored
    :return:
    """
    try:
        regkey = winreg.OpenKey(winreg.HKEY_CURRENT_USER, "Software\\" + title, 0, winreg.KEY_READ)
        winreg.QueryValueEx(regkey, "key")
        winreg.QueryValueEx(regkey, "nonce")
        return True
    except FileNotFoundError:
        # Generate random 16 character string
        aes_key = ''.join(random.choices(string.ascii_uppercase + string.digits, k=16))
        aes_nonce = ''.join(random.choices(string.ascii_uppercase + string.digits, k=16))
        # Store key in registry
        regkey = winreg.CreateKey(winreg.HKEY_CURRENT_USER, "Software\\" + title)
        winreg.SetValueEx(regkey, "key", 0, winreg.REG_SZ, aes_key)
        winreg.SetValueEx(regkey, "nonce", 0, winreg.REG_SZ, aes_nonce)
        return False


def support():
    """
    Open support page
    :return:
    """
    webbrowser.get().open("https://github.com/enigmapr0ject/EasyRSA/issues")


class MainWindow(QMainWindow):
    """
    Dashboard
    """

    def __init__(self, anonymous=False, publickey=None, privatekey=None, sessionToken=None, username=None):
        # Call to QMainWindow as super
        super(MainWindow, self).__init__()
        self.regenKeysWindow = None
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        widgets = self.ui
        self.rt: RepeatedTimer | None = None
        self.model: QtWidgets.QFileSystemModel | None = None
        self.dragPos = None
        self.filepath: str | None = None
        self.anonymous = anonymous
        if publickey and privatekey and sessionToken and username:
            self.__publicKey = publickey
            self.__privateKey = privatekey
            self.__sessionToken = sessionToken
            self.__username = username
        else:
            self.__sessionToken = None
            self.__username = None
            # Check if the directory exists
            if not os.path.exists(os.getcwd() + "/.keys") or len(os.listdir(os.getcwd() + "/.keys")) == 0:
                (self.__publicKey, self.__privateKey) = rsa.newkeys(2048, poolsize=psutil.cpu_count())
                if not os.path.exists(os.getcwd() + "/.keys"):
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
        widgets.btn_security.clicked.connect(self.buttonClick)
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

        themeFile = "themes\\dracula_halloween.qss"

        # SET THEME AND HACKS
        UIFunctions.theme(self, themeFile, True)

        # Search for config file
        stem = os.getcwd()
        stem += "\\config\\config.json"
        if not os.path.exists(stem):
            # Create JSON object
            data = {"defaultSDLocation": os.getcwd(), "defaultBitLength": 2048}
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

        # Add custom buttons in the danger zone label
        self.regenerateKeys = QCustomQPushButton(self.ui.regenkeysWidget)
        self.regenerateKeys.setText("Regenerate Keys")
        self.regenerateKeys.clicked.connect(self.dangerZone_regenKeys)
        self.regenerateKeys.resize(150, 20)
        self.regenerateKeys.setObjectAnimateOn("hover")
        applyAnimationThemeStyle(self.regenerateKeys, 12)

        self.changeBitLength = QCustomQPushButton(self.ui.changeBitLength)
        self.changeBitLength.setText("Change Bit Length")
        self.changeBitLength.clicked.connect(self.dangerZone_changeBitLength)
        self.changeBitLength.resize(150, 20)
        self.changeBitLength.setObjectAnimateOn("hover")
        applyAnimationThemeStyle(self.changeBitLength, 12)

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
        self.ui.currentDirectory.hide()
        self.ui.filepathBox.show()
        self.ui.openFilepathButton.show()

    def dangerZone_changeBitLength(self):
        self.DZ_changeBitLength = BitLengthWindow()
        self.DZ_changeBitLength.show()

    def dangerZone_regenKeys(self):
        self.regenKeysWindow = RegenerateKeysWindow(self.anonymous, self, self.__sessionToken, self.__username)
        self.regenKeysWindow.show()

    def openFile(self, index):
        """
        Open file in default application
        :param index:
        :return:
        """
        item = index.model().filePath(self.ui.fileBrowserTree.currentIndex())
        if not os.path.isfile(item):
            self.filepath = index.model().filePath(self.ui.fileBrowserTree.currentIndex())
            self.ui.fileBrowserTree.setRootIndex(
                self.model.index(self.filepath))
            self.ui.currentDirectory.setText(self.filepath)
            return
        if platform.system() == "Windows":
            os.startfile(item)
        else:
            import subprocess
            opener = "open" if platform.system() == "Darwin" else "xdg-open"
            subprocess.call([opener, item])

    def encrypt(self, index):
        """
        Encrypt file
        :param index:
        :return:
        """
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
        """
        Decrypt file
        :param index:
        :return:
        """
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
            case "btn_security":
                self.ui.titleLeftDescription.setText("Security")
                self.ui.stackedWidget.setCurrentWidget(self.ui.Security)
                UIFunctions.resetStyle(self, btnName)
                btn.setStyleSheet(UIFunctions.selectMenu(btn.styleSheet()))
            case "btn_account":
                self.ui.titleLeftDescription.setText("Account")
                self.ui.stackedWidget.setCurrentWidget(self.ui.Account)
                UIFunctions.resetStyle(self, btnName)
                btn.setStyleSheet(UIFunctions.selectMenu(btn.styleSheet()))
            case "btn_exit":
                self.__privateKey = None
                self.__publicKey = None
                self.__username = None
                self.__sessionToken = None
                self.filepath = None
                self.anonymous = None
                try:
                    self.rt.stop()
                except AttributeError:
                    pass
                self.close()
                self.loginWindow = LoginWindow()
                self.loginWindow.show()
            case "btn_logout":
                # Nullify every sensitive variable
                self.__privateKey = None
                self.__publicKey = None
                self.__username = None
                self.__sessionToken = None
                self.filepath = None
                self.anonymous = None
                try:
                    self.rt.stop()
                except AttributeError:
                    pass
                self.close()
                self.loginWindow = LoginWindow()
                self.loginWindow.show()
            case "btn_credits":
                # Check if the credits are already showing
                if self.ui.credits.isHidden():
                    self.ui.credits.show()
                else:
                    self.ui.credits.hide()
            case "btn_help":
                webbrowser.get().open("https://github.com/enigmapr0ject/EasyRSA")
            case "btn_report":
                support()
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
                    self.ui.currentDirectory.show()
                    self.model = QFileSystemModel()
                    self.model.setRootPath(os.getcwd())
                    self.ui.fileBrowserTree.setModel(
                        self.model)  # Set the model
                    if os.path.exists(self.configArray["defaultSDLocation"]):
                        self.ui.fileBrowserTree.setRootIndex(
                            self.model.index(self.configArray['defaultSDLocation']) if self.configArray[
                                                                                           'defaultSDLocation'] != ""
                            else
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
                    self.filepath = self.model.filePath(
                        self.ui.fileBrowserTree.rootIndex())
                    self.ui.currentDirectory.setText(self.filepath)
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
                    self.ui.currentDirectory.hide()
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
                self.ui.currentDirectory.setText(self.filepath)
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
                self.ui.currentDirectory.setText(self.filepath)
            case "goToDefault":
                self.ui.fileBrowserTree.setRootIndex(
                    self.model.index(self.configArray['defaultSDLocation']))
                self.ui.currentDirectory.setText(self.configArray['defaultSDLocation'])
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
                self.ui.currentDirectory.setText(self.filepath)
            case _:
                print(btnName)

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
        """
        Custom Context Menu
        """

        def renameFile():
            """
            Rename file
            """
            # Check if the file is a directory
            if self.ui.fileBrowserTree.currentIndex().isValid() and not self.model.isDir(
                    self.ui.fileBrowserTree.currentIndex()):
                index = self.ui.fileBrowserTree.currentIndex()
                file_path = self.model.filePath(index)
                self.rename = RenameFileWindow(file_path)
                self.rename.show()
            else:
                # Set the window title
                self.ui.cryptoWarningTitle.setText("Select a file.")
                self.setWindowTitle("EasyRSA - No file selected")

        def deleteFile():
            """
            Delete file
            """
            # Check if the file is a directory
            if self.ui.fileBrowserTree.currentIndex().isValid() and not self.model.isDir(
                    self.ui.fileBrowserTree.currentIndex()):
                index = self.ui.fileBrowserTree.currentIndex()
                file_path = self.model.filePath(index)
                self.delete = DeleteConfirm(file_path)
                self.delete.show()
            else:
                # Set the window title
                self.ui.cryptoWarningTitle.setText("Select a file.")
                self.setWindowTitle("EasyRSA - No file selected")

        def moveFile():
            """
            Move file
            """
            if self.ui.fileBrowserTree.currentIndex().isValid() and not self.model.isDir(
                    self.ui.fileBrowserTree.currentIndex()):
                index = self.ui.fileBrowserTree.currentIndex()
                file_path = self.model.filePath(index)
                self.move = MoveFile(file_path)
                self.move.show()
            else:
                # Set the window title
                self.ui.cryptoWarningTitle.setText("Select a file.")
                self.setWindowTitle("EasyRSA - No file selected")

        def duplicateFile():
            """
            Duplicate file
            """
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
                self.ui.cryptoWarningTitle.setText("Select a file.")
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
        menu.exec(cursor.pos())

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
        self.dragPos = event.globalPosition().toPoint()


class LoginWindow(QMainWindow):
    """
    Login Screen
    """

    def __init__(self):
        # SET AS GLOBAL WIDGETS
        # ///////////////////////////////////////////////////////////////
        super().__init__()
        self.__sessionToken = None
        self.dragPos = None
        self.ui = Ui_LoginWindow()
        self.ui.setupUi(self)
        widgets = self.ui
        self.main: MainWindow | None = None
        self.anonymous: AnonymousWindow | None = None
        self.username: str | None = None
        self.password: str | None = None
        self.mainWindow: MainWindow | None = None
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

        widgets.supportButton.clicked.connect(lambda: support())
        widgets.supportButton_2.clicked.connect(lambda: support())
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
        themeFile = "themes\\dracula_halloween.qss"

        # SET THEME AND HACKS
        UIFunctions.theme(self, themeFile, True)

        # SET HOME PAGE AND SELECT MENU
        # ///////////////////////////////////////////////////////////////
        widgets.stackedWidget.setCurrentWidget(widgets.home)
        # widgets.btn_home.setStyleSheet(UIFunctions.selectMenu(widgets.btn_home.styleSheet()))

    def showPassword(self):
        """
        Show password
        """
        if self.ui.showpassword.isChecked():
            self.ui.passbox.setEchoMode(QtWidgets.QLineEdit.Normal)
        else:
            self.ui.passbox.setEchoMode(QtWidgets.QLineEdit.Password)

    def anonymousMode(self):
        """
        Anonymous mode
        """
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
        """
        Login
        """
        self.username = self.ui.userbox.text()
        self.password = self.ui.passbox.text()
        postData = {"Email": self.username, "Password": self.password}
        response = requests.post("https://enigmapr0ject.tech/api/easyrsa/login.php",
                                 data=postData).content.decode('utf-8')
        if len(response) > 0:
            self.__sessionToken = response
            request = requests.post("https://enigmapr0ject.tech/api/easyrsa/keys.php", data=postData)
            response = request.content.decode('utf-8')
            publickey = base64.b64decode(response.split("\n")[0])
            privatekey = base64.b64decode(response.split("\n")[1])
            cipher = AES.new(aeskey, AES.MODE_EAX, nonce=nonce)
            # Decrypt public key
            publickey = cipher.decrypt(publickey)
            cipher2 = AES.new(aeskey, AES.MODE_EAX, nonce=nonce)
            # Decrypt private key
            privatekey = cipher2.decrypt(privatekey)
            # Decode from base 64
            publickey = base64.b64decode(publickey)
            privatekey = base64.b64decode(privatekey)
            publickey = rsa.PublicKey.load_pkcs1(publickey)
            privatekey = rsa.PrivateKey.load_pkcs1(privatekey)
            self.close()
            self.mainWindow = MainWindow(publickey=publickey, privatekey=privatekey, sessionToken=self.__sessionToken,
                                         username=self.username)
            self.mainWindow.ui.extraLabel.setText(self.username)
            self.mainWindow.show()
        else:
            self.ui.responsetitle.setText(response)

    def register(self):
        """
        Register
        """
        self.fade()
        self.main = RegisterWindow()
        self.main.show()

    def fade(self):
        """
        Fade window out slowly
        """
        for i in range(10):
            i /= 10
            self.setWindowOpacity(1 - i)
            time.sleep(0.02)
        self.close()

    def exitHandler(self):
        """
        Exit handler
        """
        self.close()

    # RESIZE EVENTS
    # ///////////////////////////////////////////////////////////////
    def resizeEvent(self, event):
        """
        Resize event
        :param event:
        """
        # Update Size Grips
        UIFunctions.resize_grips(self)

    # MOUSE CLICK EVENTS
    # ///////////////////////////////////////////////////////////////
    def mousePressEvent(self, event):
        """
        Mouse press event
        :param event:
        """
        # SET DRAG POS WINDOW
        self.dragPos = event.globalPosition().toPoint()


class RegisterWindow(QMainWindow):
    """
    Register Screen
    """

    def __init__(self):
        super().__init__()

        # SET AS GLOBAL WIDGETS
        # ///////////////////////////////////////////////////////////////
        self.dragPos = None
        self.login = None
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
        widgets.supportButton.clicked.connect(lambda: support())
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
        themeFile = "themes\\dracula_halloween.qss"

        # SET THEME AND HACKS
        UIFunctions.theme(self, themeFile, True)

        # SET HOME PAGE AND SELECT MENU
        # ///////////////////////////////////////////////////////////////
        widgets.stackedWidget.setCurrentWidget(widgets.home)
        # widgets.btn_home.setStyleSheet(UIFunctions.selectMenu(widgets.btn_home.styleSheet()))

    # BUTTONS CLICK
    # Post here your functions for clicked buttons

    def login(self):
        """
        Login
        """
        self.fade()
        self.login = LoginWindow()
        self.login.show()

    def register(self):
        """
        Register
        """
        emailaddress = self.ui.emailbox.text()
        publicKey, privateKey = rsa.newkeys(2048, poolsize=psutil.cpu_count())
        # Encrypt the public key
        cipher = AES.new(aeskey, AES.MODE_EAX, nonce=nonce)
        ciphertext = cipher.encrypt(base64.b64encode(publicKey.save_pkcs1()))
        # Encrypt the private key
        cipher2 = AES.new(aeskey, AES.MODE_EAX, nonce=nonce)
        ciphertext2 = cipher2.encrypt(base64.b64encode(privateKey.save_pkcs1()))
        postData = {"Email": emailaddress, "pub": base64.b64encode(ciphertext), "prv": base64.b64encode(ciphertext2)}
        response = requests.post("https://enigmapr0ject.tech/api/easyrsa/register.php", data=postData).content.decode(
            'utf-8')
        self.ui.responsetitle.setText(response)

    def fade(self):
        """
        Fade window out slowly
        """
        for i in range(10):
            i /= 10
            self.setWindowOpacity(1 - i)
            time.sleep(0.02)
        self.close()

    def exitHandler(self):
        """
        Exit handler
        """
        self.close()

    # RESIZE EVENTS
    # ///////////////////////////////////////////////////////////////
    def resizeEvent(self, event):
        """
        Resize event
        :param event:
        """
        # Update Size Grips
        UIFunctions.resize_grips(self)

    # MOUSE CLICK EVENTS
    # ///////////////////////////////////////////////////////////////
    def mousePressEvent(self, event):
        """
        Mouse press event
        :param event:
        """
        # SET DRAG POS WINDOW
        self.dragPos = event.globalPosition().toPoint()


class AnonymousWindow(QMainWindow):
    """
    Anonymous Screen
    """

    def __init__(self):
        super().__init__()
        # SET AS GLOBAL WIDGETS
        # ///////////////////////////////////////////////////////////////
        self.dragPos = None
        self.main = None
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
        themeFile = "themes\\dracula_halloween.qss"

        # SET THEME AND HACKS
        UIFunctions.theme(self, themeFile, True)

        # SET HOME PAGE AND SELECT MENU
        # ///////////////////////////////////////////////////////////////
        widgets.stackedWidget.setCurrentWidget(widgets.home)
        # widgets.btn_home.setStyleSheet(UIFunctions.selectMenu(widgets.btn_home.styleSheet()))

    def yes(self):
        """
        Yes
        :return:
        """
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
        """
        No
        """
        self.close()
        self.main = LoginWindow()
        self.main.show()

    def fade(self):
        """
        Fade window out slowly
        """
        for i in range(10):
            i /= 10
            self.setWindowOpacity(1 - i)
            time.sleep(0.02)
        self.close()

    # RESIZE EVENTS
    # ///////////////////////////////////////////////////////////////
    def resizeEvent(self, event):
        """
        Resize event
        :param event:
        """
        # Update Size Grips
        UIFunctions.resize_grips(self)

    # MOUSE CLICK EVENTS
    # ///////////////////////////////////////////////////////////////
    def mousePressEvent(self, event):
        """
        Mouse press event
        :param event:
        """
        # SET DRAG POS WINDOW
        self.dragPos = event.globalPosition().toPoint()

    def exitHandler(self):
        """
        Exit handler
        """
        self.fade()


"""
Danger Zone Windows
"""


class RegenerateKeysWindow(QMainWindow):
    """
    Regenerate Keys Window
    """

    def __init__(self, anonymousFlag, mainWindow, sessionToken, username):
        super().__init__()
        # SET AS GLOBAL WIDGETS
        # ///////////////////////////////////////////////////////////////
        self.dragPos = None
        self.ui = Ui_RegenerateKeysWindow()
        self.ui.setupUi(self)
        self.parentWindow = mainWindow
        self.anonymous = anonymousFlag
        self.__sessionToken = sessionToken
        self.__username = username
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
        themeFile = "themes\\dracula_halloween.qss"

        # SET THEME AND HACKS
        UIFunctions.theme(self, themeFile, True)

        # SET HOME PAGE AND SELECT MENU
        # ///////////////////////////////////////////////////////////////
        widgets.stackedWidget.setCurrentWidget(widgets.home)
        # widgets.btn_home.setStyleSheet(UIFunctions.selectMenu(widgets.btn_home.styleSheet()))

    def yes(self):
        def regenerateKeys(defaultBitLength):
            """
            Regenerate keys
            """
            (self.__publicKey, self.__privateKey) = rsa.newkeys(int(defaultBitLength), poolsize=psutil.cpu_count())
            if self.anonymous:
                # Delete the keys
                os.remove(".keys\\public.pem")
                os.remove(".keys\\private.pem")
                if not os.path.exists(os.getcwd() + "/.keys"):
                    os.mkdir(os.getcwd() + "/.keys")
                # Export the keys to files and place them in ".keys" folder
                with open(".keys/public.pem", "wb") as f:
                    f.write(self.__publicKey.save_pkcs1())
                    f.close()
                with open(".keys/private.pem", "wb") as f:
                    f.write(self.__privateKey.save_pkcs1())
                    f.close()
                self.parentWindow.ui.publicKeyDisplay.setPlainText(str(self.__publicKey))
                if self.parentWindow.ui.privateKeyCheckbox.isChecked():
                    self.parentWindow.ui.privateKeyDisplay.setPlainText(str(self.__privateKey))
                self.parentWindow.__publicKey = self.__publicKey
                self.parentWindow.__privateKey = self.__privateKey
            else:
                cipher = AES.new(aeskey, AES.MODE_EAX, nonce=nonce)
                ciphertext = cipher.encrypt(base64.b64encode(self.__publicKey.save_pkcs1()))
                # Encrypt the private key
                cipher2 = AES.new(aeskey, AES.MODE_EAX, nonce=nonce)
                ciphertext2 = cipher2.encrypt(base64.b64encode(self.__privateKey.save_pkcs1()))
                ciphertext = base64.b64encode(ciphertext)
                ciphertext2 = base64.b64encode(ciphertext2)
                data = {"Email": self.__username, "SessionToken": self.__sessionToken, "pub": ciphertext,
                        "prv": ciphertext2}
                # Send to server
                r = requests.post("https://enigmapr0ject.tech/api/easyrsa/updateKeys.php", data=data)
                # Check if the request was successful
                print(r.text)
                if r.text == "200":
                    self.parentWindow.ui.publicKeyDisplay.setPlainText(str(self.__publicKey))
                    if self.parentWindow.ui.privateKeyCheckbox.isChecked():
                        self.parentWindow.ui.privateKeyDisplay.setPlainText(str(self.__privateKey))
                    self.parentWindow.__publicKey = self.__publicKey
                    self.parentWindow.__privateKey = self.__privateKey
                elif r.text == "403":
                    self.ui.usertitle_2.setText("Invalid session token")
                    return
                else:
                    self.ui.usertitle_2.setText("An error occurred")
                    return
            self.ui.usertitle_2.hide()
            self.ui.usertitle.setText("Keys regenerated successfully. You can now close this window.")
        try:
            self.ui.yesButton.hide()
            self.ui.noButton.hide()
            self.ui.usertitle_2.setText("Generating keys...")
            with open("config\\config.json", "r") as f:
                config = json.load(f)
                defaultBitLength = config["defaultBitLength"]
                f.close()
            p1 = Thread(target=regenerateKeys, args=(defaultBitLength,))
            p1.start()
        except Exception as e:
            self.usertitle_2.setText("An error occurred")

    def fade(self):
        """
        Fade window out slowly
        """
        for i in range(10):
            i /= 10
            self.setWindowOpacity(1 - i)
            time.sleep(0.02)
        self.close()

    # RESIZE EVENTS
    # ///////////////////////////////////////////////////////////////
    def resizeEvent(self, event):
        """
        Resize event
        :param event:
        """
        # Update Size Grips
        UIFunctions.resize_grips(self)

    # MOUSE CLICK EVENTS
    # ///////////////////////////////////////////////////////////////
    def mousePressEvent(self, event):
        """
        Mouse press event
        :param event:
        """
        # SET DRAG POS WINDOW, without deprecation
        self.dragPos = event.globalPosition().toPoint()

    def exitHandler(self):
        """
        Exit handler
        """
        self.fade()

class BitLengthWindow(QMainWindow):
    """
    Regenerate Keys Window
    """

    def __init__(self):
        super().__init__()
        # SET AS GLOBAL WIDGETS
        # ///////////////////////////////////////////////////////////////
        self.dragPos = None
        self.ui = Ui_BitLengthWindow()
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
        widgets.noButton.clicked.connect(self.fade)
        widgets.closeAppBtn.clicked.connect(self.close)
        widgets.bitLengthBox.currentTextChanged.connect(self.comboBoxChange)
        # SET CUSTOM THEME
        # ///////////////////////////////////////////////////////////////
        themeFile = "themes\\dracula_halloween.qss"

        # SET THEME AND HACKS
        UIFunctions.theme(self, themeFile, True)

        # SET HOME PAGE AND SELECT MENU
        # ///////////////////////////////////////////////////////////////
        widgets.stackedWidget.setCurrentWidget(widgets.home)
        # widgets.btn_home.setStyleSheet(UIFunctions.selectMenu(widgets.btn_home.styleSheet()))

    def comboBoxChange(self, s):
        if s == "512":
            self.ui.warningIcon.show()
            self.ui.warningLabel.show()
        else:
            self.ui.warningIcon.hide()
            self.ui.warningLabel.hide()

    def yes(self):
        self.ui.yesButton.hide()
        self.ui.noButton.hide()
        self.ui.bitLengthBox.hide()
        self.ui.usertitle.hide()
        # Get the bit length from the combobox
        bitLength = self.ui.bitLengthBox.currentText()
        # Save the bit length to the config file
        with open("config\\config.json", "r") as f:
            config = json.load(f)
            f.close()
        config["defaultBitLength"] = bitLength
        with open("config\\config.json", "w") as f:
            json.dump(config, f, indent=4)
            f.close()
        # Update the UI
        self.ui.warningLabel.setText("Bit length updated successfully. To use this new length, you will have to regenerate your keys.")
        # Check if the label is hidden
        if self.ui.warningLabel.isHidden():
            self.ui.warningLabel.show()

    def fade(self):
        """
        Fade window out slowly
        """
        for i in range(10):
            i /= 10
            self.setWindowOpacity(1 - i)
            time.sleep(0.02)
        self.close()

    # RESIZE EVENTS
    # ///////////////////////////////////////////////////////////////
    def resizeEvent(self, event):
        """
        Resize event
        :param event:
        """
        # Update Size Grips
        UIFunctions.resize_grips(self)

    # MOUSE CLICK EVENTS
    # ///////////////////////////////////////////////////////////////
    def mousePressEvent(self, event):
        """
        Mouse press event
        :param event:
        """
        # SET DRAG POS WINDOW, without deprecation
        self.dragPos = event.globalPosition().toPoint()

    def exitHandler(self):
        """
        Exit handler
        """
        self.fade()


class RenameFileWindow(QMainWindow):
    """
    Rename File Window
    """

    def __init__(self, filepath):
        super().__init__()
        # SET AS GLOBAL WIDGETS
        # ///////////////////////////////////////////////////////////////
        self.dragPos = None
        self.ui = Ui_RenameWindow()
        self.ui.setupUi(self)
        self.filepath = filepath
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
        widgets.confirmButton.clicked.connect(self.confirm)
        widgets.cancelButton.clicked.connect(self.fade)
        widgets.closeAppBtn.clicked.connect(self.close)
        # SET CUSTOM THEME
        # ///////////////////////////////////////////////////////////////
        themeFile = "themes\\dracula_halloween.qss"

        # SET THEME AND HACKS
        UIFunctions.theme(self, themeFile, True)

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
            """
            Splits path names into tails and heads
            :param path:
            :return:
            """
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
        """
        Fade window out slowly
        """
        for i in range(10):
            i /= 10
            self.setWindowOpacity(1 - i)
            time.sleep(0.02)
        self.close()

    # RESIZE EVENTS
    # ///////////////////////////////////////////////////////////////
    def resizeEvent(self, event):
        """
        Resize event
        :param event:
        """
        # Update Size Grips
        UIFunctions.resize_grips(self)

    # MOUSE CLICK EVENTS
    # ///////////////////////////////////////////////////////////////
    def mousePressEvent(self, event):
        """
        Mouse press event
        :param event:
        """
        # SET DRAG POS WINDOW
        self.dragPos = event.globalPosition().toPoint()

    def exitHandler(self):
        """
        Exit handler
        """
        self.fade()


class DeleteConfirm(QMainWindow):
    """
    Delete Confirm Window
    """

    def __init__(self, index):
        super().__init__()
        # SET AS GLOBAL WIDGETS
        # ///////////////////////////////////////////////////////////////
        self.dragPos = None
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
        themeFile = "themes\\dracula_halloween.qss"

        # SET THEME AND HACKS
        UIFunctions.theme(self, themeFile, True)

        # SET HOME PAGE AND SELECT MENU
        # ///////////////////////////////////////////////////////////////
        widgets.stackedWidget.setCurrentWidget(widgets.home)
        # widgets.btn_home.setStyleSheet(UIFunctions.selectMenu(widgets.btn_home.styleSheet()))

    def yes(self):
        """
        The function takes the index of the file to be deleted and deletes it.
        """
        try:
            os.remove(self.index)
        except Exception as e:
            print(e)
            self.close()
        self.fade()

    def fade(self):
        """
        Fade window out slowly
        """
        for i in range(10):
            i /= 10
            self.setWindowOpacity(1 - i)
            time.sleep(0.02)
        self.close()

    # RESIZE EVENTS
    # ///////////////////////////////////////////////////////////////
    def resizeEvent(self, event):
        """
        Resize event
        :param event:
        """
        # Update Size Grips
        UIFunctions.resize_grips(self)

    # MOUSE CLICK EVENTS
    # ///////////////////////////////////////////////////////////////
    def mousePressEvent(self, event):
        """
        Mouse press event
        :param event:
        """
        # SET DRAG POS WINDOW, without deprecation
        self.dragPos = event.globalPosition().toPoint()

    def exitHandler(self):
        """
        Exit handler
        """
        self.fade()


class MoveFile(QMainWindow):
    """
    Move File Window
    """

    def __init__(self, index):
        super().__init__()
        # SET AS GLOBAL WIDGETS
        # ///////////////////////////////////////////////////////////////
        self.dragPos = None
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
        themeFile = "themes\\dracula_halloween.qss"

        # SET THEME AND HACKS
        UIFunctions.theme(self, themeFile, True)

        # SET HOME PAGE AND SELECT MENU
        # ///////////////////////////////////////////////////////////////
        widgets.stackedWidget.setCurrentWidget(widgets.home)
        # widgets.btn_home.setStyleSheet(UIFunctions.selectMenu(widgets.btn_home.styleSheet()))

    def yes(self):
        """
        The function takes the index of the file to be moved and moves it.
        :return:
        """
        self.newName = self.ui.fileNameBox.text()

        def path_leaf(path):  # Splits path names into tails and heads
            """
            Splits path names into tails and heads
            :param path:
            :return:
            """
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

    def openFile(self):
        """
        Opens file explorer to select a file
        """
        # Open file selection window
        self.filepath = QFileDialog.getExistingDirectory(
            self, "Select Directory")
        self.ui.fileNameBox.setText(self.filepath)

    def fade(self):
        """
        Fade window out slowly
        """
        for i in range(10):
            i /= 10
            self.setWindowOpacity(1 - i)
            time.sleep(0.02)
        self.close()

    # RESIZE EVENTS
    # ///////////////////////////////////////////////////////////////
    def resizeEvent(self, event):
        """
        Resize event
        :param event:
        """
        # Update Size Grips
        UIFunctions.resize_grips(self)

    # MOUSE CLICK EVENTS
    # ///////////////////////////////////////////////////////////////
    def mousePressEvent(self, event):
        """
        Mouse press event
        :param event:
        """
        # set drag pos window, without deprecation
        self.dragPos = event.globalPosition().toPoint()

    def exitHandler(self):
        """
        Exit handler
        """
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
    check_key_nonce()
    key = winreg.OpenKey(winreg.HKEY_CURRENT_USER, "Software\\" + title, 0, winreg.KEY_READ)
    aeskey, regtype = winreg.QueryValueEx(key, "key")
    nonce, regtype2 = winreg.QueryValueEx(key, "nonce")
    aeskey = bytes(aeskey, 'utf-8')
    nonce = bytes(nonce, 'utf-8')
    app = QApplication(sys.argv)
    window = LoginWindow()
    sys.exit(app.exec())
