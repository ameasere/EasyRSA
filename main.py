"""
Main Driver Code for EasyRSA
"""
# ///////////////////////////////////////////////////////////////
#
# BY: WANDERSON M.PIMENTA
# PROJECT MADE WITH: Qt Designer and PySide6
# V: 0.0.5
# ///////////////////////////////////////////////////////////////
# Developed by Bartosz Rzepka (DevPanada), Leighton Brooks (ameasere)
# 21477187 / 21472005
# Theme by Zeno Rocha: https://zenorocha.com/
import base64
import json
import os
import platform
import random
import string
import sys
import webbrowser
import shutil
from Cryptodome.Cipher import AES
import pyperclip
import requests
import rsa
import time
import ntpath
from threading import *
from PySide6 import QtGui, QtWidgets, QtCore
from PySide6.QtWidgets import QMainWindow
from modules import *
from PySide6.QtCore import *
import traceback
from Custom_Widgets.Widgets import *
import pyqrcode
#import faulthandler
import hashlib
# warnings.filterwarnings('ignore')
# os.environ['QT_DEBUG_PLUGINS'] = "1"
# FIX Problem for High DPI and Scale above 100%
# Check for High DPI or Scale above 100%, and set os.environ["QT_FONT_DPI"] accordingly
if platform.system() == "Windows":
    import ctypes
    import winreg

    if ctypes.windll.shcore.GetScaleFactorForDevice(0) > 100:
        os.environ["QT_FONT_DPI"] = str(ctypes.windll.shcore.GetScaleFactorForDevice(0) * 96 / 72)
    else:
        os.environ["QT_FONT_DPI"] = "96"
title = "EasyRSA"
description = "RSA made simple."


class WorkerSignals(QObject):
    '''
    Defines the signals available from a running worker thread.

    Supported signals are:

    finished
        No data

    error
        tuple (exctype, value, traceback.format_exc() )

    result
        object data returned from processing, anything

    '''
    finished = Signal()  # QtCore.Signal
    error = Signal(tuple)
    result = Signal(object)


class Worker(QRunnable):
    '''
    Worker thread

    Inherits from QRunnable to handler worker thread setup, signals and wrap-up.

    :param callback: The function callback to run on this worker thread. Supplied args and
                     kwargs will be passed through to the runner.
    :type callback: function
    :param args: Arguments to pass to the callback function
    :param kwargs: Keywords to pass to the callback function

    '''

    def __init__(self, fn, *args, **kwargs):
        super(Worker, self).__init__()
        # Store constructor arguments (re-used for processing)
        self.fn = fn
        self.args = args
        self.kwargs = kwargs
        self.signals = WorkerSignals()

    @Slot()  # QtCore.Slot
    def run(self):
        """
        Initialise the runner function with passed args, kwargs.
        """

        # Retrieve args/kwargs here; and fire processing using them
        try:
            result = self.fn(*self.args, **self.kwargs)
        except:
            traceback.print_exc()
            exctype, value = sys.exc_info()[:2]
            self.signals.error.emit((exctype, value, traceback.format_exc()))
        else:
            self.signals.result.emit(result)  # Return the result of the processing
        finally:
            self.signals.finished.emit()  # Done


# Check Windows registry for a key to see if there is an encryption key stored
# If there is, use it, if not, generate a new one and store it in the registry
def check_key_nonce():
    """
    Check Windows registry for a key to see if there is an encryption key stored
    :return:
    """
    if platform.system() == "Windows":
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
    else:
        # Generate keys
        aes_key = ''.join(random.choices(string.ascii_uppercase + string.digits, k=16))
        aes_nonce = ''.join(random.choices(string.ascii_uppercase + string.digits, k=16))
        # Create environment variables instead if they do not exist
        if not os.getenv("EASYRSA_KEY"):
            os.environ["EASYRSA_KEY"] = aes_key
        if not os.getenv("EASYRSA_NONCE"):
            os.environ["EASYRSA_NONCE"] = aes_nonce
        return aes_key, aes_nonce


def support():
    """
    Open support page
    :return:
    """
    webbrowser.get().open("https://github.com/ameasere/EasyRSA/issues")


class MainWindow(QMainWindow):
    """
    Dashboard
    """

    def __init__(self, anonymous=False, publickey=None, privatekey=None, sessionToken=None, username=None):
        # Call to QMainWindow as super
        super(MainWindow, self).__init__()
        self.loginWindow = None
        self.DZ_changeBitLength = None
        self.qrwindow = None
        self.regenKeysWindow = None
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        widgets = self.ui
        self.rt: RepeatedTimer | None = None
        self.model: QtWidgets.QFileSystemModel | None = None
        self.dragPos = None
        self.filepath: str | None = None
        self.anonymous = anonymous
        self.threadpool = QThreadPool()
        self.__publicKey = None
        self.__privateKey = None
        if anonymous:
            self.ui.enable2fa.setEnabled(False)
            self.ui.tooltip1.setToolTip('<html><head/><body><p><span style=" font-size:11pt; color:#ffffff;">2 Factor Authentication is disabled for anonymous users.</span></p></body></html>')
            self.ui.enable2fa.setStyleSheet('background-color: #6a6d75; font: 63 10pt "Raleway SemiBold";')
            self.ui.disabledText1.show()

            self.ui.changePw.setEnabled(False)
            self.ui.tooltip2.setToolTip('<html><head/><body><p><span style=" font-size:11pt; color:#ffffff;">Changing account password is disabled for anonymous users.</span></p></body></html>')
            self.ui.changePw.setStyleSheet('background-color: #6a6d75; font: 63 10pt "Raleway SemiBold";')
            self.ui.disabledText2.show()
        else:
            self.ui.disabledText1.hide()
            self.ui.disabledText2.hide()

        if publickey and privatekey and sessionToken and username:
            self.__publicKey = publickey
            self.__privateKey = privatekey
            self.__sessionToken = sessionToken
            self.__username = username
        else:
            self.__sessionToken = None
            self.__username = None

            # Check if the directory exists
            def generateKeys():
                """
                Generate keys
                :return:
                """
                (__publicKey, __privateKey) = rsa.newkeys(2048,
                                                          poolsize=psutil.cpu_count() if psutil.cpu_count() > 3 else 1)
                if not os.path.exists(os.getcwd() + "/.keys") or len(os.listdir(os.getcwd() + "/.keys")) == 0:
                    if not os.path.exists(os.getcwd() + "/.keys"):
                        os.mkdir(os.getcwd() + "/.keys")
                    # Export the keys to files and place them in ".keys" folder
                    with open(".keys/public.pem", "wb") as f:
                        f.write(__publicKey.save_pkcs1())
                        f.close()
                    with open(".keys/private.pem", "wb") as f:
                        f.write(__privateKey.save_pkcs1())
                        f.close()
                else:
                    # Read the keys
                    with open(".keys/public.pem", "rb") as f:
                        __publicKey = rsa.PublicKey.load_pkcs1(f.read())
                        f.close()
                    with open(".keys/private.pem", "rb") as f:
                        __privateKey = rsa.PrivateKey.load_pkcs1(f.read())
                        f.close()
                # Check if the .keys folder exists and has 2 keys in it

            if os.path.exists(os.getcwd() + "/.keys") and len(os.listdir(os.getcwd() + "/.keys")) == 2:
                # BFS
                def breadthFirstFileScan(root):
                    dirs = [root]
                    # while we has dirs to scan
                    while len(dirs):
                        nextDirs = []
                        for parent in dirs:
                            # scan each dir
                            for f in os.listdir(parent):
                                # if there is a dir, then save for next ittr
                                # if it  is a file then yield it (we'll return later)
                                ff = os.path.join(parent, f)
                                if os.path.isdir(ff):
                                    nextDirs.append(ff)
                                else:
                                    yield ff
                        # once we've done all the current dirs then
                        # we set up the next itter as the child dirs
                        # from the current itter.
                        dirs = nextDirs
                try:
                    for file in breadthFirstFileScan(os.getcwd() + "/.keys"):
                        if file.endswith(".pem"):
                            with open(file, "rb") as f:
                                if file.endswith("public.pem"):
                                    self.__publicKey = rsa.PublicKey.load_pkcs1(f.read())
                                elif file.endswith("private.pem"):
                                    self.__privateKey = rsa.PrivateKey.load_pkcs1(f.read())
                                f.close()
                    if not self.__publicKey or not self.__privateKey:
                        generateKeys()
                except Exception as e:
                    generateKeys()
            else:
                worker = Worker(generateKeys)
                worker.signals.result.connect(self.result)
                worker.signals.finished.connect(self.generateFinished)
                self.threadpool.start(worker)
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
        self.ui.titleLeftDescription.setText("Dashboard")

        themeFile = "themes/EasyRSA.qss"

        # SET THEME AND HACKS
        UIFunctions.theme(self, themeFile, True)

        # Search for config file
        stem = os.getcwd()
        stem += "/config/config.json"
        if not os.path.exists(os.getcwd()+"/config"):
            # Create JSON object
            try:
                os.mkdir(os.getcwd() + "/config")
            except FileExistsError:
                pass
            except OSError:
                pass
            if not os.path.exists(stem):
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
        self.ui.announceBox.hide()
        self.ui.openFilepathButton_2.clicked.connect(self.buttonClick)
        self.ui.filepathBox_2.returnPressed.connect(self.buttonClick)
        self.ui.encryptButton_2.clicked.connect(self.buttonClick)
        self.ui.decryptButton_2.clicked.connect(self.buttonClick)
        self.ui.encryptButton_3.clicked.connect(self.buttonClick)
        self.ui.decryptButton_3.clicked.connect(self.buttonClick)
        self.ui.closePopup.clicked.connect(self.buttonClick)
        self.ui.enable2fa.clicked.connect(self.buttonClick)
        self.ui.changePw.clicked.connect(self.buttonClick)

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

        self.ui.publicKeyDisplay.setPlainText(
            str(self.__publicKey) if self.__publicKey is not None else "Generating keys...")
        self.ui.privateKeyDisplay.setPlainText("PrivateKey(***********)")

        # Private Key Checkbox Tick
        self.ui.privateKeyCheckbox.stateChanged.connect(
            self.privateKeyCheckboxTick)

        # Copy Private Key
        self.ui.copyPrivateKeyButton.clicked.connect(self.buttonClick)
        self.ui.copyPublicKeyButton.clicked.connect(self.buttonClick)

        # Filespace Page functionality

        # Multiview Checkbox Tick
        self.ui.multiviewCheckbox_1.stateChanged.connect(self.buttonClick)
        self.ui.openDirectory_2.clicked.connect(self.buttonClick)
        self.ui.defaultLocation_2.clicked.connect(self.buttonClick)
        self.ui.goToDefault_2.clicked.connect(self.buttonClick)
        self.ui.goBackButton_2.clicked.connect(self.buttonClick)

        # Multiview disabled by default
        self.ui.currentDirectoryText.hide()
        self.ui.defaultLocation_2.hide()
        self.ui.driveInfo_2.hide()
        self.ui.driveInfoTitle_2.hide()
        self.ui.fileBrowserTree_2.hide()
        self.ui.goToDefault_2.hide()
        self.ui.openDirectory_2.hide()
        self.ui.parentDrive_2.hide()
        self.ui.parentDriveSpace_2.hide()
        self.ui.parentDriveTitle_2.hide()
        self.ui.goBackButton_2.hide()
        self.ui.multiviewDetailsBox.hide()
        self.ui.currentDirectory_2.hide()
        self.ui.filepathBox_2.show()
        self.ui.openFilepathButton_2.show()
        self.ui.border1.hide()
        self.ui.border2.hide()
        self.ui.encryptButton_3.hide()
        self.ui.decryptButton_3.hide()
        self.ui.closePopup.hide()
        self.ui.border1_2.hide()
        self.ui.border1_3.hide()

        self.ui.signFile.clicked.connect(self.buttonClick)
        self.ui.verifySignature.clicked.connect(self.buttonClick)
        self.ui.sha256.clicked.connect(self.buttonClick)
        self.ui.sha384.clicked.connect(self.buttonClick)
        self.ui.sha512.clicked.connect(self.buttonClick)
        self.ui.announceBox2.hide()


    def result(self): # Connector is blank, used solely for connecting from the Worker.
        pass

    def generateFinished(self):
        with open(".keys/public.pem", "rb") as f:
            self.__publicKey = rsa.PublicKey.load_pkcs1(f.read())
            f.close()
        with open(".keys/private.pem", "rb") as f:
            self.__privateKey = rsa.PrivateKey.load_pkcs1(f.read())
            f.close()
        self.__publicKey = str(self.__publicKey) # Private elements.
        self.__privateKey = str(self.__privateKey) # Private elements.
        # Update the UI
        self.ui.publicKeyDisplay.setPlainText(self.__publicKey)
        self.ui.privateKeyDisplay.setPlainText("PrivateKey(***********)")

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
        item = index.model().filePath(self.ui.fileBrowserTree_2.currentIndex())
        if not os.path.isfile(item):
            self.filepath = index.model().filePath(self.ui.fileBrowserTree_2.currentIndex())
            self.ui.fileBrowserTree_2.setRootIndex(
                self.model.index(self.filepath))
            self.ui.currentDirectory_2.setText(self.filepath)
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
                self.ui.announceBox.setStyleSheet("background-color: rgb(206, 55, 8);"
                                                  "border-top-left-radius :10px;"
                                                  "border-top-right-radius :10px;"
                                                  "border-bottom-left-radius :10px;"
                                                  "border-bottom-right-radius :10px;")
                self.ui.announceBox.setText("Failed to encrypt file. Please select a valid file "
                                            "(folders cannot be encrypted).")
                self.ui.announceBox.show()
                self.ui.closePopup.show()
                return
            self.filepath = index.model().filePath(index)
        if index is None:
            self.ui.announceBox.setStyleSheet("background-color: rgb(206, 55, 8);"
                                              "border-top-left-radius :10px;"
                                              "border-top-right-radius :10px;"
                                              "border-bottom-left-radius :10px;"
                                              "border-bottom-right-radius :10px;")
            self.ui.announceBox.setText("Failed to encrypt file. Please select a valid file "
                                        "(folders cannot be encrypted).")
            self.ui.announceBox.show()
            self.ui.closePopup.show()
            return
        if not os.path.isfile(self.filepath):
            self.ui.announceBox.setStyleSheet("background-color: rgb(206, 55, 8);"
                                              "border-top-left-radius :10px;"
                                              "border-top-right-radius :10px;"
                                              "border-bottom-left-radius :10px;"
                                              "border-bottom-right-radius :10px;")
            self.ui.announceBox.setText("Failed to encrypt file. Please select a valid file "
                                        "(folders cannot be encrypted).")
            self.ui.announceBox.show()
            self.ui.closePopup.show()
            return
        if os.stat(self.filepath).st_size == 0:
            self.ui.announceBox.setStyleSheet("background-color: rgb(206, 55, 8);"
                                              "border-top-left-radius :10px;"
                                              "border-top-right-radius :10px;"
                                              "border-bottom-left-radius :10px;"
                                              "border-bottom-right-radius :10px;")
            self.ui.announceBox.setText("Failed to encrypt file. This file is empty!")
            self.ui.announceBox.show()
            self.ui.closePopup.show()
            return
        self.ui.closePopup.hide()
        self.ui.announceBox.setStyleSheet("background-color: rgb(255, 159, 25);"
                                          "border-top-left-radius :10px;"
                                          "border-top-right-radius :10px;"
                                          "border-bottom-left-radius :10px;"
                                          "border-bottom-right-radius :10px;")
        self.ui.announceBox.setText("Encrypting file.. | Warning: This may take a while | Please wait..")
        self.ui.announceBox.show()
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
            for chunk in iter(lambda: f.read(round((int(self.configArray['defaultBitLength']) / 8) - 11)), b''):
                # Encrypt chunk
                rsa.encrypt(chunk, self.__publicKey)
                with open(new_filepath, 'ab') as e:
                    e.write(rsa.encrypt(chunk, self.__publicKey))
                    e.close()
            end = time.perf_counter()
            f.close()
        self.ui.announceBox.setStyleSheet("background-color: rgb(30, 200, 84);"
                                          "border-top-left-radius :10px;"
                                          "border-top-right-radius :10px;"
                                          "border-bottom-left-radius :10px;"
                                          "border-bottom-right-radius :10px;")
        self.ui.announceBox.setText("Encryption Complete! | Time taken: " + str(round(end - start, 2)) + " seconds | "
                                                                                                         "Filesize: " + str(
            round(os.stat(new_filepath).st_size / 1000000, 2)) + " MB")
        self.ui.announceBox.show()
        self.ui.closePopup.show()
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
                self.ui.announceBox.setStyleSheet("background-color: rgb(206, 55, 8);"
                                                  "border-top-left-radius :10px;"
                                                  "border-top-right-radius :10px;"
                                                  "border-bottom-left-radius :10px;"
                                                  "border-bottom-right-radius :10px;")
                self.ui.announceBox.setText("Failed to decrypt file. Please select a valid file "
                                            "(folders cannot be decrypted).")
                self.ui.announceBox.show()
                self.ui.closePopup.show()
                return
            self.filepath = index.model().filePath(index)
        if index is None:
            self.ui.announceBox.setStyleSheet("background-color: rgb(206, 55, 8);"
                                              "border-top-left-radius :10px;"
                                              "border-top-right-radius :10px;"
                                              "border-bottom-left-radius :10px;"
                                              "border-bottom-right-radius :10px;")
            self.ui.announceBox.setText("Failed to decrypt file. Please select a valid file "
                                        "(folders cannot be decrypted).")
            self.ui.announceBox.show()
            self.ui.closePopup.show()
            return
        if not os.path.isfile(self.filepath):
            self.ui.announceBox.setStyleSheet("background-color: rgb(206, 55, 8);"
                                              "border-top-left-radius :10px;"
                                              "border-top-right-radius :10px;"
                                              "border-bottom-left-radius :10px;"
                                              "border-bottom-right-radius :10px;")
            self.ui.announceBox.setText("Failed to decrypt file. Please select a valid file "
                                        "(folders cannot be decrypted).")
            self.ui.announceBox.show()
            self.ui.closePopup.show()
            return
        if os.stat(self.filepath).st_size == 0:
            self.ui.announceBox.setText("Failed to decrypt file. This file is empty!")
            self.ui.closePopup.show()
            return
        self.ui.closePopup.hide()
        self.ui.announceBox.setStyleSheet("background-color: rgb(255, 159, 25);"
                                          "border-top-left-radius :10px;"
                                          "border-top-right-radius :10px;"
                                          "border-bottom-left-radius :10px;"
                                          "border-bottom-right-radius :10px;")
        self.ui.announceBox.setText("Decrypting file.. | Warning: This may take a while | Please wait..")
        self.ui.announceBox.show()
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
            for chunk in iter(lambda: f.read(round(int(self.configArray['defaultBitLength']) / 8)), b''):
                # Encrypt chunk
                try:
                    with open(new_filepath, 'ab') as d:
                        d.write(rsa.decrypt(chunk, self.__privateKey))
                        d.close()
                except rsa.pkcs1.DecryptionError as e:
                    # Set the error message into the announcement box
                    self.ui.announceBox.setStyleSheet("background-color: rgb(206, 55, 8);"
                                                      "border-top-left-radius :10px;"
                                                      "border-top-right-radius :10px;"
                                                      "border-bottom-left-radius :10px;"
                                                      "border-bottom-right-radius :10px;")
                    self.ui.announceBox.setText("Decryption failed! | Error: " + str(e))
                    self.ui.announceBox.show()
                    self.ui.closePopup.show()
                    os.remove(new_filepath)
                    return False
            end = time.perf_counter()
            f.close()
        self.ui.announceBox.setStyleSheet("background-color: rgb(30, 200, 84);"
                                          "border-top-left-radius :10px;"
                                          "border-top-right-radius :10px;"
                                          "border-bottom-left-radius :10px;"
                                          "border-bottom-right-radius :10px;")
        self.ui.announceBox.setText("Decryption Complete! | Time taken: " + str(round(end - start, 2)) + " seconds | "
                                                                                                         "Filesize: " + str(
            round(os.stat(new_filepath).st_size / 1000000, 2)) + " MB")
        self.ui.announceBox.show()
        self.ui.closePopup.show()
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
        # only hide the announcement box if the colour is not yellow (since it means it's doing something)
        if not self.ui.announceBox.styleSheet().__contains__("background-color: rgb(255, 159, 25);"):
            self.ui.announceBox.hide()
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
                # self.ui.titleLeftDescription.setText("Dashboard")  # SET PAGE
                self.ui.stackedWidget.setCurrentWidget(
                    self.ui.home)  # RESET ANOTHERS BUTTONS SELECTED
                UIFunctions.resetStyle(self, btnName)
                btn.setStyleSheet(
                    UIFunctions.selectMenu(
                        btn.styleSheet()))  # SELECT MENU
                self.ui.titleLeftDescription.setText("Dashboard")
            case "btn_filespace":
                # self.ui.titleLeftDescription.setText("Filespace")
                self.ui.stackedWidget.setCurrentWidget(self.ui.filespace)
                UIFunctions.resetStyle(self, btnName)
                btn.setStyleSheet(UIFunctions.selectMenu(btn.styleSheet()))
                self.ui.titleLeftDescription.setText("D.M.E")
            case "btn_security":
                # self.ui.titleLeftDescription.setText("Security")
                self.ui.stackedWidget.setCurrentWidget(self.ui.Security)
                UIFunctions.resetStyle(self, btnName)
                btn.setStyleSheet(UIFunctions.selectMenu(btn.styleSheet()))
                self.ui.titleLeftDescription.setText("Security")
            case "btn_account":
                # self.ui.titleLeftDescription.setText("Account")
                self.ui.stackedWidget.setCurrentWidget(self.ui.Account)
                UIFunctions.resetStyle(self, btnName)
                btn.setStyleSheet(UIFunctions.selectMenu(btn.styleSheet()))
                self.ui.titleLeftDescription.setText("Account")
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
                webbrowser.get().open("https://ameasere.com/easyrsa#faq")
            case "btn_report":
                support()
            case "btn_more":
                webbrowser.get().open("https://ameasere.com/")
            case "copyPrivateKeyButton":
                pyperclip.copy(self.ui.privateKeyDisplay.toPlainText())
            case "copyPublicKeyButton":
                pyperclip.copy(self.ui.publicKeyDisplay.toPlainText())
            case "multiviewCheckbox_1":
                if self.ui.multiviewCheckbox_1.isChecked():
                    self.ui.backer1.hide()
                    self.ui.filepathBox_2.hide()
                    self.ui.openFilepathButton_2.hide()
                    self.ui.encryptButton_2.hide()
                    self.ui.decryptButton_2.hide()
                    self.ui.defaultLocation_2.show()
                    self.ui.multiviewDetailsBox.show()
                    self.ui.driveInfo_2.show()
                    self.ui.driveInfoTitle_2.show()
                    self.ui.fileBrowserTree_2.show()
                    self.ui.goToDefault_2.show()
                    self.ui.openDirectory_2.show()
                    self.ui.parentDrive_2.show()
                    self.ui.parentDriveSpace_2.show()
                    self.ui.selectFileToEncryptText.hide()
                    self.ui.parentDriveTitle_2.show()
                    self.ui.goBackButton_2.show()
                    self.ui.currentDirectory_2.show()
                    self.ui.currentDirectoryText.show()
                    self.ui.encryptButton_3.show()
                    self.ui.decryptButton_3.show()
                    self.ui.border1.show()
                    self.ui.border2.show()
                    self.ui.border1_2.show()
                    self.ui.border1_3.show()
                    self.model = QFileSystemModel()
                    self.model.setRootPath(os.getcwd())
                    self.ui.fileBrowserTree_2.setModel(
                        self.model)  # Set the model
                    if os.path.exists(self.configArray["defaultSDLocation"]):
                        self.ui.fileBrowserTree_2.setRootIndex(
                            self.model.index(self.configArray['defaultSDLocation']) if self.configArray[
                                                                                           'defaultSDLocation'] != ""
                            else
                            self.model.index(
                                os.getcwd()))  # Set the first displaying directory
                    # If directory in defaultSDLocation doesn't exist on the
                    # current machine, use current directory
                    else:
                        self.ui.fileBrowserTree_2.setRootIndex(
                            self.model.index(os.getcwd()))
                        self.model.index(os.getcwd())
                    self.ui.fileBrowserTree_2.doubleClicked.connect(
                        self.openFile)
                    self.ui.fileBrowserTree_2.setAlternatingRowColors(
                        False)  # Set the alternating row colors
                    self.ui.fileBrowserTree_2.setSortingEnabled(
                        True)  # Set the sorting
                    # Default sort by name
                    self.ui.fileBrowserTree_2.sortByColumn(0, Qt.AscendingOrder)
                    self.ui.fileBrowserTree_2.setColumnWidth(0, 200)
                    self.ui.fileBrowserTree_2.setColumnWidth(1, 150)
                    self.ui.fileBrowserTree_2.setColumnWidth(2, 200)
                    self.ui.fileBrowserTree_2.setColumnWidth(3, 200)
                    # Set the context menu
                    self.ui.fileBrowserTree_2.setContextMenuPolicy(
                        QtCore.Qt.ContextMenuPolicy.CustomContextMenu)
                    # (right clicking)
                    self.ui.fileBrowserTree_2.customContextMenuRequested.connect(
                        self.contextMenu)  # Custom right click
                    # menu
                    # self.ui.fileBrowserTree_2.doubleClicked.connect() #
                    # Double-clicking on a file has a special effect
                    drivestats = DriveStatistics()
                    self.ui.parentDrive_2.setText(
                        "Parent Drive: %s" % drivestats.parentDrive)
                    self.ui.parentDriveSpace_2.setValue(
                        drivestats.parentDriveSpace)
                    self.ui.driveInfo_2.setText(drivestats.driveInformation)
                    self.filepath = self.model.filePath(
                        self.ui.fileBrowserTree_2.rootIndex())
                    self.ui.currentDirectory_2.setText(self.filepath)
                    if not self.rt:
                        self.rt = RepeatedTimer(5, self.driveStatistics)
                        self.rt.start()
                    else:
                        self.rt.start()
                else:
                    self.rt.stop()
                    self.ui.defaultLocation_2.hide()
                    self.ui.driveInfo_2.hide()
                    self.ui.driveInfoTitle_2.hide()
                    self.ui.fileBrowserTree_2.hide()
                    self.ui.goToDefault_2.hide()
                    self.ui.openDirectory_2.hide()
                    self.ui.parentDrive_2.hide()
                    self.ui.goBackButton_2.hide()
                    self.ui.currentDirectoryText.hide()
                    self.ui.currentDirectory_2.hide()
                    self.ui.multiviewDetailsBox.hide()
                    self.ui.parentDriveSpace_2.hide()
                    self.ui.parentDriveTitle_2.hide()
                    self.ui.selectFileToEncryptText.show()
                    self.ui.backer1.show()
                    self.ui.filepathBox_2.show()
                    self.ui.openFilepathButton_2.show()
                    self.ui.encryptButton_2.show()
                    self.ui.decryptButton_2.show()
                    self.ui.encryptButton_3.hide()
                    self.ui.decryptButton_3.hide()
                    self.ui.border1_2.hide()
                    self.ui.border1_3.hide()
                    self.ui.border1.hide()
                    self.ui.border2.hide()
            case "openFilepathButton_2":
                self.filepath = QFileDialog.getOpenFileName(
                    self, "Select File", os.getcwd(), "All Files (*)")[0]
                if self.filepath == "":
                    return
                self.ui.filepathBox_2.setText(self.filepath)
            case "openDirectory_2":
                self.filepath = QFileDialog.getExistingDirectory(
                    self, "Select Directory", os.getcwd())
                if self.filepath == "":
                    return
                self.ui.fileBrowserTree_2.setRootIndex(
                    self.model.index(self.filepath))
                self.ui.currentDirectory_2.setText(self.filepath)
            case "defaultLocation_2":
                self.filepath = QFileDialog.getExistingDirectory(
                    self, "Select Directory", os.getcwd())
                if self.filepath == "":
                    return
                self.ui.fileBrowserTree_2.setRootIndex(
                    self.model.index(self.filepath))
                self.configArray["defaultSDLocation"] = self.filepath
                with open("config/config.json", "w") as f:
                    json.dump(self.configArray, f)
                    f.close()
                self.ui.currentDirectory_2.setText(self.filepath)
            case "goToDefault_2":
                self.ui.fileBrowserTree_2.setRootIndex(
                    self.model.index(self.configArray['defaultSDLocation']))
                self.ui.currentDirectory_2.setText(self.configArray['defaultSDLocation'])
            case "encryptButton_2":
                self.filepath = self.ui.filepathBox_2.text()
                if self.filepath == "":
                    self.ui.announceBox.setStyleSheet("background-color: rgb(206, 55, 8);"
                                                      "border-top-left-radius :10px;"
                                                      "border-top-right-radius :10px;"
                                                      "border-bottom-left-radius :10px;"
                                                      "border-bottom-right-radius :10px;")
                    self.ui.announceBox.setText("Failed to encrypt file. Please select a valid file "
                                                "(folders cannot be encrypted).")
                    self.ui.announceBox.show()
                    self.ui.closePopup.show()
                    return
                p1 = Thread(target=self.encrypt, args=(self.filepath,))
                p1.start()
            case "encryptButton_3":
                self.filepath = self.model.filePath(self.ui.fileBrowserTree_2.currentIndex())
                if self.filepath == "":
                    self.ui.announceBox.setStyleSheet("background-color: rgb(206, 55, 8);"
                                                      "border-top-left-radius :10px;"
                                                      "border-top-right-radius :10px;"
                                                      "border-bottom-left-radius :10px;"
                                                      "border-bottom-right-radius :10px;")
                    self.ui.announceBox.setText("Please click on the file you wish to encrypt.")
                    self.ui.announceBox.show()
                    self.ui.closePopup.show()
                    return
                p1 = Thread(target=self.encrypt, args=(self.filepath,))
                p1.start()
            case "decryptButton_3":
                self.filepath = self.model.filePath(self.ui.fileBrowserTree_2.currentIndex())
                if self.filepath == "":
                    self.ui.announceBox.setStyleSheet("background-color: rgb(206, 55, 8);"
                                                      "border-top-left-radius :10px;"
                                                      "border-top-right-radius :10px;"
                                                      "border-bottom-left-radius :10px;"
                                                      "border-bottom-right-radius :10px;")
                    self.ui.announceBox.setText("Please click on the file you wish to decrypt.")
                    self.ui.announceBox.show()
                    self.ui.closePopup.show()
                    return
                p1 = Thread(target=self.decrypt, args=(self.filepath,))
                p1.start()
            case "closePopup":
                self.ui.announceBox.hide()
                self.ui.closePopup.hide()
            case "filepathBox_2":
                self.filepath = self.ui.filepathBox_2.text()
                if self.filepath == "":
                    self.ui.announceBox.setStyleSheet("background-color: rgb(206, 55, 8);"
                                                      "border-top-left-radius :10px;"
                                                      "border-top-right-radius :10px;"
                                                      "border-bottom-left-radius :10px;"
                                                      "border-bottom-right-radius :10px;")
                    self.ui.announceBox.setText("No file has been selected.")
                    self.ui.announceBox.show()
                    self.ui.closePopup.show()
                    return
                p1 = Thread(target=self.encrypt, args=(self.filepath,))
                p1.start()
            case "decryptButton_2":
                self.filepath = self.ui.filepathBox_2.text()
                if self.filepath == "":
                    self.ui.announceBox.setStyleSheet("background-color: rgb(206, 55, 8);"
                                                      "border-top-left-radius :10px;"
                                                      "border-top-right-radius :10px;"
                                                      "border-bottom-left-radius :10px;"
                                                      "border-bottom-right-radius :10px;")
                    self.ui.announceBox.setText("Failed to decrypt file. Please select a valid file "
                                                "(folders cannot be encrypted).")
                    self.ui.announceBox.show()
                    self.ui.closePopup.show()
                    return
                p1 = Thread(target=self.decrypt, args=(self.filepath,))
                p1.start()
            case "goBackButton_2":
                self.filepath = self.model.filePath(
                    self.ui.fileBrowserTree_2.rootIndex())
                self.filepath = os.path.dirname(self.filepath)
                self.ui.fileBrowserTree_2.setRootIndex(
                    self.model.index(self.filepath))
                self.ui.currentDirectory_2.setText(self.filepath)
            case "enable2fa":
                cipher = AES.new(aeskey, AES.MODE_EAX, nonce=nonce)
                ciphertext = cipher.encrypt(base64.b64encode(self.__privateKey.save_pkcs1()))
                encryptedKey = base64.b64encode(ciphertext)
                postData = {"Email": self.__username, "token": self.__sessionToken, "prv": encryptedKey}
                farequest = requests.post("https://ameasere.com.ameasere.com/easyrsa/2fa/registerTOTP.php", postData)
                response = farequest.content.decode("utf-8")
                # Generate QR code
                self.qrwindow = TwoFactorAuthWindow(response, encryptedKey, self.__username, self.__sessionToken)
                self.qrwindow.show()
            case "signFile":
                # Open file dialog
                self.filepath = QFileDialog.getOpenFileName(self, "Select file to sign", self.configArray['defaultSDLocation'], "All Files (*)")[0]
                if self.filepath == "":
                    self.ui.announceBox2.setStyleSheet("background-color: rgb(206, 55, 8);"
                                                        "border-top-left-radius :10px;"
                                                        "border-top-right-radius :10px;"
                                                        "border-bottom-left-radius :10px;"
                                                        "border-bottom-right-radius :10px;")
                    self.ui.announceBox2.setText("No file has been selected.")
                    self.ui.announceBox2.show()
                    self.ui.closePopup.show()
                    return
                self.ui.announceBox2.setStyleSheet("background-color: rgb(255, 159, 25);"
                                                   "border-top-left-radius :10px;"
                                                   "border-top-right-radius :10px;"
                                                   "border-bottom-left-radius :10px;"
                                                   "border-bottom-right-radius :10px;")
                self.ui.announceBox2.setText("Signing file...")
                self.ui.announceBox2.show()
                self.ui.closePopup.show()
                worker = Worker(self.signFile, self.filepath)
                worker.signals.result.connect(self.sendToNull)
                worker.signals.finished.connect(self.sendToNull)
                self.threadpool.start(worker)
            case "verifySignature":
                # Open file dialog
                self.filepath = \
                QFileDialog.getOpenFileName(self, "Select file to sign", self.configArray['defaultSDLocation'],
                                            "All Files (*)")[0]
                if self.filepath == "":
                    self.ui.announceBox2.setStyleSheet("background-color: rgb(206, 55, 8);"
                                                       "border-top-left-radius :10px;"
                                                       "border-top-right-radius :10px;"
                                                       "border-bottom-left-radius :10px;"
                                                       "border-bottom-right-radius :10px;")
                    self.ui.announceBox2.setText("No file has been selected.")
                    self.ui.announceBox2.show()
                    self.ui.closePopup.show()
                    return
                self.ui.announceBox2.setStyleSheet("background-color: rgb(255, 159, 25);"
                                                   "border-top-left-radius :10px;"
                                                   "border-top-right-radius :10px;"
                                                   "border-bottom-left-radius :10px;"
                                                   "border-bottom-right-radius :10px;")
                self.ui.announceBox2.setText("Signing file...")
                self.ui.announceBox2.show()
                self.ui.closePopup.show()
                worker = Worker(self.verifySignature, self.filepath)
                worker.signals.result.connect(self.sendToNull)
                worker.signals.finished.connect(self.sendToNull)
                self.threadpool.start(worker)
            case "sha384":
                # Open file dialog
                self.filepath = \
                QFileDialog.getOpenFileName(self, "Select file to generate checksum", self.configArray['defaultSDLocation'], "All Files (*)")[0]
                if self.filepath == "":
                    self.ui.announceBox2.setStyleSheet("background-color: rgb(206, 55, 8);"
                                                          "border-top-left-radius :10px;"
                                                         "border-top-right-radius :10px;"
                                                         "border-bottom-left-radius :10px;"
                                                         "border-bottom-right-radius :10px;")
                    self.ui.announceBox2.setText("No file has been selected.")
                    self.ui.announceBox2.show()
                    self.ui.closePopup.show()
                    return
                self.ui.announceBox2.setStyleSheet("background-color: rgb(255, 159, 25);"
                                                    "border-top-left-radius :10px;"
                                                    "border-top-right-radius :10px;"
                                                    "border-bottom-left-radius :10px;"
                                                    "border-bottom-right-radius :10px;")
                self.ui.announceBox2.setText("Generating SHA384 checksum...")
                self.ui.announceBox2.show()
                self.ui.closePopup.show()
                worker = Worker(self.SHA, self.filepath, "sha384")
                worker.signals.result.connect(self.sendToNull)
                worker.signals.finished.connect(self.sendToNull)
                self.threadpool.start(worker)
            case "sha512":
                # Open file dialog
                self.filepath = \
                    QFileDialog.getOpenFileName(self, "Select file to generate checksum",
                                                self.configArray['defaultSDLocation'], "All Files (*)")[0]
                if self.filepath == "":
                    self.ui.announceBox2.setStyleSheet("background-color: rgb(206, 55, 8);"
                                                       "border-top-left-radius :10px;"
                                                       "border-top-right-radius :10px;"
                                                       "border-bottom-left-radius :10px;"
                                                       "border-bottom-right-radius :10px;")
                    self.ui.announceBox2.setText("No file has been selected.")
                    self.ui.announceBox2.show()
                    self.ui.closePopup.show()
                    return
                self.ui.announceBox2.setStyleSheet("background-color: rgb(255, 159, 25);"
                                                   "border-top-left-radius :10px;"
                                                   "border-top-right-radius :10px;"
                                                   "border-bottom-left-radius :10px;"
                                                   "border-bottom-right-radius :10px;")
                self.ui.announceBox2.setText("Generating SHA384 checksum...")
                self.ui.announceBox2.show()
                self.ui.closePopup.show()
                worker = Worker(self.SHA, self.filepath, "sha512")
                worker.signals.result.connect(self.sendToNull)
                worker.signals.finished.connect(self.sendToNull)
                self.threadpool.start(worker)
            case "sha256":
                # Open file dialog
                self.filepath = \
                    QFileDialog.getOpenFileName(self, "Select file to generate checksum",
                                                self.configArray['defaultSDLocation'], "All Files (*)")[0]
                if self.filepath == "":
                    self.ui.announceBox2.setStyleSheet("background-color: rgb(206, 55, 8);"
                                                       "border-top-left-radius :10px;"
                                                       "border-top-right-radius :10px;"
                                                       "border-bottom-left-radius :10px;"
                                                       "border-bottom-right-radius :10px;")
                    self.ui.announceBox2.setText("No file has been selected.")
                    self.ui.announceBox2.show()
                    self.ui.closePopup.show()
                    return
                self.ui.announceBox2.setStyleSheet("background-color: rgb(255, 159, 25);"
                                                   "border-top-left-radius :10px;"
                                                   "border-top-right-radius :10px;"
                                                   "border-bottom-left-radius :10px;"
                                                   "border-bottom-right-radius :10px;")
                self.ui.announceBox2.setText("Generating SHA384 checksum...")
                self.ui.announceBox2.show()
                self.ui.closePopup.show()
                worker = Worker(self.SHA, self.filepath, "sha256")
                worker.signals.result.connect(self.sendToNull)
                worker.signals.finished.connect(self.sendToNull)
                self.threadpool.start(worker)
            case "changePw":
                webbrowser.get().open("https://ameasere.com.ameasere.com/easyrsa/chngPw.php")
            case _:
                print("%s button not found." % btnName)
        self.ui.signAndVerify.setEnabled(False)
        self.ui.generateChecksum.setEnabled(False)

    def sendToNull(self):
        pass

    def SHA(self, filepath, hashType: str):
        if isinstance(filepath, str):
            self.filepath = filepath

        try:
            with open(self.filepath, "rb") as f:
                fileContent = f.read()
                f.close()
            match hashType:
                case "sha384":
                    start = time.time()
                    checksum = hashlib.sha384(fileContent).hexdigest()
                    end = time.time()
                case "sha512":
                    start = time.time()
                    checksum = hashlib.sha512(fileContent).hexdigest()
                    end = time.time()
                case "sha256":
                    start = time.time()
                    checksum = hashlib.sha256(fileContent).hexdigest()
                    end = time.time()
                case _:
                    raise Exception("Hash type not supported.")

            with open(self.filepath + "." + hashType, "w") as f:
                f.write(checksum)
                f.close()
            self.ui.announceBox2.setStyleSheet("background-color: rgb(30, 200, 84);"
                                                  "border-top-left-radius :10px;"
                                                    "border-top-right-radius :10px;"
                                                    "border-bottom-left-radius :10px;"
                                                    "border-bottom-right-radius :10px;")
            self.ui.announceBox2.setText("Checksum generated successfully in: %s seconds. | %s " % (str(round(end - start, 2)), checksum))
            self.ui.announceBox2.show()
            self.ui.closePopup.show()
        except Exception as e:
            self.ui.announceBox2.setStyleSheet("background-color: rgb(206, 55, 8);"
                                                  "border-top-left-radius :10px;"
                                                    "border-top-right-radius :10px;"
                                                    "border-bottom-left-radius :10px;"
                                                    "border-bottom-right-radius :10px;")
            self.ui.announceBox2.setText("Failed to generate checksum: %s" % repr(e))
            self.ui.announceBox2.show()
            self.ui.closePopup.show()

    def signFile(self, filepath):
        if isinstance(filepath, str):
            self.filepath = filepath
        # Read file
        try:
            with open(self.filepath, "rb") as f:
                data = f.read()
                f.close()
            # Sign file
            start = time.time()
            hash = rsa.compute_hash(data, "SHA-1")
            signature = rsa.sign(hash, self.__privateKey, "SHA-1")
            end = time.time()
            # Write signature to file
            with open(self.filepath + ".sig", "wb") as f:
                f.write(signature)
                f.close()
            timetaken = end - start
            self.ui.announceBox2.setStyleSheet("""background-color: rgb(30, 200, 84);
                                                  border-top-left-radius :10px;
                                                  border-top-right-radius :10px;
                                                  border-bottom-left-radius :10px;
                                                  border-bottom-right-radius :10px;""")
            self.ui.announceBox2.setText("File signed successfully in: %s seconds. | Saved to: %s" % (round(timetaken, 2), self.filepath + ".sig"))
            self.ui.announceBox2.show()
            self.ui.closePopup.show()
        except Exception as e:
            self.ui.announceBox2.setStyleSheet("background-color: rgb(206, 55, 8);"
                                               "border-top-left-radius :10px;"
                                               "border-top-right-radius :10px;"
                                               "border-bottom-left-radius :10px;"
                                               "border-bottom-right-radius :10px;")
            self.ui.announceBox2.setText("Failed to sign file.")
            self.ui.announceBox2.show()
            self.ui.closePopup.show()


    def verifySignature(self, filepath):
        if isinstance(filepath, str):
            self.filepath = filepath
        with open(self.filepath.replace(".sig", ""), "rb") as f:
            data = f.read()
            f.close()
        with open(self.filepath, "rb") as f:
            signature = f.read()
            f.close()
        start = time.time()
        hash = rsa.compute_hash(data, "SHA-1")
        try:
            rsa.verify(hash, signature, self.__publicKey)
            end = time.time()
            timetaken = end - start
            self.ui.announceBox2.setStyleSheet("""background-color: rgb(30, 200, 84);
                                                              border-top-left-radius :10px;
                                                              border-top-right-radius :10px;
                                                              border-bottom-left-radius :10px;
                                                              border-bottom-right-radius :10px;""")
            self.ui.announceBox2.setText("Signature verified in: %s seconds" % (
            round(timetaken, 2)))
            self.ui.announceBox2.show()
            self.ui.closePopup.show()
        except rsa.pkcs1.VerificationError:
            self.ui.announceBox2.setStyleSheet("background-color: rgb(206, 55, 8);"
                                               "border-top-left-radius :10px;"
                                               "border-top-right-radius :10px;"
                                               "border-bottom-left-radius :10px;"
                                               "border-bottom-right-radius :10px;")
            self.ui.announceBox2.setText("File signature is invalid.")
            self.ui.announceBox2.show()
            self.ui.closePopup.show()
            return


    # Multiview drive statistics

    def driveStatistics(self):
        """
        Drive statistics for multiview, in realtime
        """
        drivestats = DriveStatistics()
        self.ui.parentDrive_2.setText(
            "Parent Drive: %s" %
            drivestats.parentDrive)
        self.ui.parentDriveSpace_2.setValue(drivestats.parentDriveSpace)
        self.ui.driveInfo_2.setText(drivestats.driveInformation)

    # Private Key Checkbox Tick
    def privateKeyCheckboxTick(self):
        """
        Private Key Checkbox Tick event
        :return:
        """
        if self.ui.privateKeyCheckbox.isChecked():
            self.ui.privateKeyDisplay.setPlainText(
                str(self.__privateKey) if self.__privateKey else "Generating keys...")
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
            if self.ui.fileBrowserTree_2.currentIndex().isValid() and not self.model.isDir(
                    self.ui.fileBrowserTree_2.currentIndex()):
                index = self.ui.fileBrowserTree_2.currentIndex()
                file_path = self.model.filePath(index)
                self.rename = RenameFileWindow(file_path)
                self.rename.show()
            else:
                # Set the window title
                self.ui.announceBox.setStyleSheet("background-color: rgb(206, 55, 8);"
                                                  "border-top-left-radius :10px;"
                                                  "border-top-right-radius :10px;"
                                                  "border-bottom-left-radius :10px;"
                                                  "border-bottom-right-radius :10px;")
                self.ui.announceBox.setText("Failed to rename file. Please select a valid file "
                                            "(folders cannot be renamed).")
                self.ui.announceBox.show()
                self.setWindowTitle("EasyRSA - No file selected")

        def deleteFile():
            """
            Delete file
            """
            # Check if the file is a directory
            if self.ui.fileBrowserTree_2.currentIndex().isValid() and not self.model.isDir(
                    self.ui.fileBrowserTree_2.currentIndex()):
                index = self.ui.fileBrowserTree_2.currentIndex()
                file_path = self.model.filePath(index)
                self.delete = DeleteConfirm(file_path)
                self.delete.show()
            else:
                # Set the window title
                self.ui.announceBox.setStyleSheet("background-color: rgb(206, 55, 8);"
                                                  "border-top-left-radius :10px;"
                                                  "border-top-right-radius :10px;"
                                                  "border-bottom-left-radius :10px;"
                                                  "border-bottom-right-radius :10px;")
                self.ui.announceBox.setText("Failed to delete file. Please select a valid file "
                                            "(folders cannot be deleted).")
                self.ui.announceBox.show()
                self.setWindowTitle("EasyRSA - No file selected")

        def moveFile():
            """
            Move file
            """
            if self.ui.fileBrowserTree_2.currentIndex().isValid() and not self.model.isDir(
                    self.ui.fileBrowserTree_2.currentIndex()):
                index = self.ui.fileBrowserTree_2.currentIndex()
                file_path = self.model.filePath(index)
                self.move = MoveFile(file_path)
                self.move.show()
            else:
                # Set the window title
                self.ui.announceBox.setStyleSheet("background-color: rgb(206, 55, 8);"
                                                  "border-top-left-radius :10px;"
                                                  "border-top-right-radius :10px;"
                                                  "border-bottom-left-radius :10px;"
                                                  "border-bottom-right-radius :10px;")
                self.ui.announceBox.setText("Failed to move file. Please select a valid file "
                                            "(folders cannot be moved).")
                self.ui.announceBox.show()
                self.setWindowTitle("EasyRSA - No file selected")

        def duplicateFile():
            """
            Duplicate file
            """
            if self.ui.fileBrowserTree_2.currentIndex().isValid() and not self.model.isDir(
                    self.ui.fileBrowserTree_2.currentIndex()):
                index = self.ui.fileBrowserTree_2.currentIndex()
                file_path = self.model.filePath(index)
                ext = "." + file_path.split(".")[len(file_path.split(".")) - 1]
                duplicate_file_path = file_path.replace(ext, "(copy)" + ext)
                while os.path.exists(duplicate_file_path):
                    duplicate_file_path = file_path.replace(ext, "(copy)" + ext)
                shutil.copy(file_path, duplicate_file_path)
            else:
                # Set the window title
                self.ui.announceBox.setStyleSheet("background-color: rgb(206, 55, 8);"
                                                  "border-top-left-radius :10px;"
                                                  "border-top-right-radius :10px;"
                                                  "border-bottom-left-radius :10px;"
                                                  "border-bottom-right-radius :10px;")
                self.ui.announceBox.setText("Failed to duplicate file. Please select a valid file "
                                            "(folders cannot be duplicated).")
                self.ui.announceBox.show()
                self.setWindowTitle("EasyRSA - No file selected")

        """
        Custom Context Menu
        :return:
        """
        menu = QtWidgets.QMenu()
        menu.setStyleSheet(
            "QMenu {background-color: rgb(33, 37, 43); font: 8pt \"Raleway SemiBold\"; color: rgb(170, 99, 255); text-align: center}"
            "QMenu::item:selected {color: rgb(255, 255, 255); background-color: rgb(170, 99, 255); border-style: "
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
            lambda: Thread(target=self.encrypt, args=(self.ui.fileBrowserTree_2.currentIndex(),)).start())
        decryptAction.triggered.connect(
            lambda: Thread(target=self.decrypt, args=(self.ui.fileBrowserTree_2.currentIndex(),)).start())
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

class TwoFactorAuthWindow(QMainWindow):
    """
    Rename File Window
    """

    def __init__(self, uri, encryptedKey, email, token):
        super().__init__()
        # SET AS GLOBAL WIDGETS
        # ///////////////////////////////////////////////////////////////
        self.dragPos = None
        self.ui = Ui_TwoFactorWindow()
        self.ui.setupUi(self)
        self.URI = uri
        self.encryptedKey = encryptedKey
        self.email = email
        self.token = token
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
        widgets.closeAppBtn.clicked.connect(self.close)
        widgets.codebox.hide()
        widgets.announceBox.hide()
        # SET CUSTOM THEME
        # ///////////////////////////////////////////////////////////////
        themeFile = "themes/EasyRSA.qss"

        # SET THEME AND HACKS
        UIFunctions.theme(self, themeFile, True)

        # SET HOME PAGE AND SELECT MENU
        # ///////////////////////////////////////////////////////////////
        widgets.stackedWidget.setCurrentWidget(widgets.home)
        # widgets.btn_home.setStyleSheet(UIFunctions.selectMenu(widgets.btn_home.styleSheet()))
        qrcode = pyqrcode.create(self.URI)
        qrcode.png("qrcode.png", scale=6)
        pixmap = QPixmap("qrcode.png")
        widgets.qrcode.setPixmap(pixmap)
        os.remove("qrcode.png")

    def confirm(self):
        self.ui.codebox.show()
        self.ui.dashboardTitle_2.setText("Please enter the code from your authenticator app below to confirm.")
        self.ui.confirmButton.setText("Confirm")
        self.ui.confirmButton.clicked.connect(self.confirm2)

    def confirm2(self):
        code = self.ui.codebox.text()
        if code == "" or len(code) != 6:
            self.ui.announceBox.setStyleSheet("background-color: rgb(206, 55, 8);"
                                              "border-top-left-radius :10px;"
                                              "border-top-right-radius :10px;"
                                              "border-bottom-left-radius :10px;"
                                              "border-bottom-right-radius :10px;")
            self.ui.announceBox.setText("Please enter a valid code.")
            self.ui.announceBox.show()
        else:
            postData = {"Email": self.email, "token": self.token, "code": code, "prv": self.encryptedKey}
            faenable = requests.post("https://ameasere.com.ameasere.com/easyrsa/2fa/registerTOTP.php", data=postData)
            if faenable.content.decode('utf-8') == "2FA Enabled.":
                self.ui.announceBox.setStyleSheet("background-color: rgb(30, 200, 84);"
                                                  "border-top-left-radius :10px;"
                                                  "border-top-right-radius :10px;"
                                                  "border-bottom-left-radius :10px;"
                                                  "border-bottom-right-radius :10px;")
                self.ui.announceBox.setText("2FA has been enabled.")
                self.ui.announceBox.show()
                self.ui.confirmButton.setText("Close")
                self.ui.confirmButton.clicked.connect(self.close)
                self.ui.codebox.hide()
            elif faenable.content.decode('utf-8') == "Too many tries.":
                self.ui.announceBox.setStyleSheet("background-color: rgb(206, 55, 8);"
                                                  "border-top-left-radius :10px;"
                                                  "border-top-right-radius :10px;"
                                                  "border-bottom-left-radius :10px;"
                                                  "border-bottom-right-radius :10px;")
                self.ui.announceBox.setText("Too many tries. Please try again later.")
                self.ui.announceBox.show()
            else:
                self.ui.announceBox.setStyleSheet("background-color: rgb(206, 55, 8);"
                                                  "border-top-left-radius :10px;"
                                                  "border-top-right-radius :10px;"
                                                  "border-bottom-left-radius :10px;"
                                                  "border-bottom-right-radius :10px;")
                self.ui.announceBox.setText(faenable.content.decode("utf-8"))
                self.ui.announceBox.show()
                print(faenable.content.decode("utf-8"))
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


class LoginWindow(QMainWindow):
    """
    Login Screen
    """

    def __init__(self):
        # SET AS GLOBAL WIDGETS
        # ///////////////////////////////////////////////////////////////
        super().__init__()
        self.authcode = None
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
        widgets.fasubmit.clicked.connect(self.fasubmit)
        # widgets.cancelbutton.clicked.connect(self.register)
        # widgets.submitbutton.clicked.connect(self.login)
        widgets.anonMode.clicked.connect(self.anonymousMode)
        widgets.closeAppBtn.clicked.connect(self.close)
        # USE CUSTOM TITLE BAR | USE AS "False" FOR MAC OR LINUX
        # ///////////////////////////////////////////////////////////////
        Settings.ENABLE_CUSTOM_TITLE_BAR = titleBarFlag

        widgets.supportButton.clicked.connect(lambda: support())
        # widgets.supportButton_2.clicked.connect(lambda: support())
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
        themeFile = "themes/EasyRSA.qss"

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
        response = requests.post("https://ameasere.com.ameasere.com/easyrsa/login.php",
                                 data=postData).content.decode('utf-8')
        if len(response) > 0 and response != "Email or Password incorrect." and response != "Field/s empty" and response != "User is not verified." and response != "2FA":
            self.__sessionToken = response
            request = requests.post("https://api.ameasere.com/easyrsa/keys.php", data=postData)
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
        elif response == "2FA":
            self.ui.stackedWidget.setCurrentWidget(self.ui.twofactor)
        else:
            self.ui.responsetitle.setText(response)

    def register(self):
        """
        Register
        """
        self.fade()
        self.main = RegisterWindow()
        self.main.show()
    def fasubmit(self):
        self.authcode = self.ui.codebox.text()
        postData = {"Email": self.username, "Password": self.password, "code": self.authcode}
        response = requests.post("https://api.ameasere.com/easyrsa/2fa/verify.php", data=postData).content.decode('utf-8')
        if response != "Failed":
            self.__sessionToken = response
            request = requests.post("https://api.ameasere.com/easyrsa/keys.php", data=postData)
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
            self.mainWindow = MainWindow(publickey=publickey, privatekey=privatekey,
                                        sessionToken=self.__sessionToken,
                                        username=self.username)
            self.mainWindow.ui.extraLabel.setText(self.username)
            self.mainWindow.show()
        else:
            self.ui.responsetitle.setText("Incorrect code.")


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
        self.login = None
        self.dragPos = None
        self.ui = Ui_RegisterWindow()
        self.ui.setupUi(self)
        self.threadpool = QThreadPool()
        widgets = self.ui
        widgets.cancelRegisterButton.clicked.connect(self.login)
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
        themeFile = "themes/EasyRSA.qss"

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
        self.hide()
        self.login = LoginWindow()
        self.login.show()

    def register(self):
        self.ui.responsetitle.setText("Registering...")
        worker = Worker(self.registerThread)
        worker.signals.result.connect(self.result)
        worker.signals.finished.connect(self.genFinished)
        self.threadpool.start(worker)
    def registerThread(self):
        emailaddress = self.ui.emailbox.text()
        postData = {"Email": emailaddress}
        response = requests.post("https://api.ameasere.com/easyrsa/register.php", data=postData).content.decode(
            'utf-8')
        if response == "Error: Email already registered." or response == "Failed to enter data. Please try again":
            self.ui.responsetitle.setText(response)
        else:
            publicKey, privateKey = rsa.newkeys(2048, poolsize=psutil.cpu_count() if psutil.cpu_count() > 3 else 1)
            # Encrypt the public key
            cipher = AES.new(aeskey, AES.MODE_EAX, nonce=nonce)
            ciphertext = cipher.encrypt(base64.b64encode(publicKey.save_pkcs1()))
            # Encrypt the private key
            cipher2 = AES.new(aeskey, AES.MODE_EAX, nonce=nonce)
            ciphertext2 = cipher2.encrypt(base64.b64encode(privateKey.save_pkcs1()))
            postData = {"Email": emailaddress, "pub": base64.b64encode(ciphertext),
                        "prv": base64.b64encode(ciphertext2)}
            response = requests.post("https://api.ameasere.com/easyrsa/register.php",
                                     data=postData).content.decode(
                'utf-8')
            self.ui.responsetitle.setText(response)
    def result(self):
        pass
    def genFinished(self):
        pass
        #self.ui.responsetitle.setText("Link sent to your email address. Please check your spam folder if you don't see it in your inbox.")

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
        themeFile = "themes/EasyRSA.qss"

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
        self.__privateKey = None
        self.__publicKey = None
        self.dragPos = None
        self.ui = Ui_RegenerateKeysWindow()
        self.ui.setupUi(self)
        self.parentWindow = mainWindow
        self.anonymous = anonymousFlag
        self.__sessionToken = sessionToken
        self.__username = username
        self.threadpool = QThreadPool()
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
        themeFile = "themes/EasyRSA.qss"

        # SET THEME AND HACKS
        UIFunctions.theme(self, themeFile, True)

        # SET HOME PAGE AND SELECT MENU
        # ///////////////////////////////////////////////////////////////
        widgets.stackedWidget.setCurrentWidget(widgets.home)
        # widgets.btn_home.setStyleSheet(UIFunctions.selectMenu(widgets.btn_home.styleSheet()))

    def yes(self):
        def regenerateKeys():
            """
            Regenerate keys
            """
            with open("config/config.json", "r") as f:
                config = json.load(f)
                defaultBitLength = config["defaultBitLength"]
                f.close()
            (self.__publicKey, self.__privateKey) = rsa.newkeys(int(defaultBitLength),
                                                                poolsize=psutil.cpu_count() if psutil.cpu_count() > 3 else 1)
            if self.anonymous:
                # Delete the keys
                os.remove(".keys/public.pem")
                os.remove(".keys/private.pem")
                if not os.path.exists(os.getcwd() + "/.keys"):
                    os.mkdir(os.getcwd() + "/.keys")
                # Export the keys to files and place them in ".keys" folder
                with open(".keys/public.pem", "wb") as f:
                    f.write(self.__publicKey.save_pkcs1())
                    f.close()
                with open(".keys/private.pem", "wb") as f:
                    f.write(self.__privateKey.save_pkcs1())
                    f.close()
                print("Keys regenerated.")
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
                r = requests.post("https://api.ameasere.com/easyrsa/updateKeys.php", data=data)
                # Check if the request was successful
                if r.text == "200":
                    pass
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
            worker = Worker(regenerateKeys)
            worker.signals.result.connect(self.result)
            worker.signals.finished.connect(self.regenFinished)

            self.threadpool.start(worker)
        except Exception as e:
            self.ui.usertitle_2.setText("An error occurred")

    def result(self):
        pass

    def regenFinished(self):
        # Read the public key and private key
        with open(".keys/public.pem", "rb") as f:
            self.__publicKey = rsa.PublicKey.load_pkcs1(f.read())
            f.close()
        with open(".keys/private.pem", "rb") as f:
            self.__privateKey = rsa.PrivateKey.load_pkcs1(f.read())
            f.close()
        self.parentWindow.__publicKey = self.__publicKey
        self.parentWindow.__privateKey = self.__privateKey
        self.parentWindow.ui.publicKeyDisplay.setPlainText(str(self.__publicKey))
        # If private key checkbox is checked
        if self.parentWindow.ui.privateKeyCheckbox.isChecked():
            self.parentWindow.ui.publicKeyDisplay.setPlainText(str(self.__privateKey))

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
        themeFile = "themes/EasyRSA.qss"

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
        with open("config/config.json", "r") as f:
            config = json.load(f)
            f.close()
        config["defaultBitLength"] = bitLength
        with open("config/config.json", "w") as f:
            json.dump(config, f, indent=4)
            f.close()
        # Update the UI
        self.ui.warningLabel.setText(
            "Bit length updated successfully. To use this new length, you will have to regenerate your keys.")
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
        themeFile = "themes/EasyRSA.qss"

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
        themeFile = "themes/EasyRSA.qss"

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
        themeFile = "themes/EasyRSA.qss"

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
    #faulthandler.enable()
    match platform.system():  # Check the OS
        case "Windows":  # If Windows
            import ctypes  # Windows exclusive library

            # arbitrary string, can be anything
            myappid = 'theenigmaproject.crypto.easyRSA.004'
            ctypes.windll.shell32.SetCurrentProcessExplicitAppUserModelID(
                myappid)  # Set the AppID. Needed for
            # taskbar icon and window icons to work.
            # Variable holding the value for if we have a custom titlebar or
            # not. This is broken
            titleBarFlag = True
            # on any other OS.
        case other:
            titleBarFlag = False

    if platform.system() == "Windows":
        check_key_nonce()
        key = winreg.OpenKey(winreg.HKEY_CURRENT_USER, "Software\\" + title, 0, winreg.KEY_READ)
        aeskey, regtype = winreg.QueryValueEx(key, "key")
        nonce, regtype2 = winreg.QueryValueEx(key, "nonce")
    else:
        # Get key and nonce from env
        aeskey, nonce = check_key_nonce()
    aeskey = bytes(aeskey, 'utf-8')
    nonce = bytes(nonce, 'utf-8')
    app = QApplication(sys.argv)
    window = LoginWindow()
    sys.exit(app.exec())
