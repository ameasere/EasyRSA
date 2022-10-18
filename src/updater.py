import time,requests,sys,os,urllib.request,warnings,platform
from PySide6 import QtWidgets, QtCore, QtGui
from PySide6.QtWidgets import QFileSystemModel, QMainWindow
warnings.filterwarnings('ignore')
systemLabel = platform.system()
if systemLabel == "Windows":
    import ctypes
    myappid = 'theenigmaproject.salvation.9' # arbitrary string
    ctypes.windll.shell32.SetCurrentProcessExplicitAppUserModelID(myappid)
    titleBarFlag = True
else:
    titleBarFlag = False
creditHTML = '''
<!DOCTYPE HTML PUBLIC "-//W3C//DTD HTML 4.0//EN" "https://www.w3.org/TR/REC-html40/strict.dtd">
<html><head><meta name="qrichtext" content="1" /><style type="text/css">
p, li { white-space: pre-wrap; }
</style></head><body style=" font-family:'Segoe UI'; font-size:10pt; font-weight:400; font-style:normal;">
<p align="center" style=" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;"><span style=" font-size:12pt; font-weight:600; color:#ff79c6;">Credit</span></p>
<p align="center" style=" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;"><span style=" color:#bd93f9;">Theme by: Zeno Rocha</span></p>
<p align="center" style=" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;"><span style=" color:#bd93f9;">UI framework by: Wanderson M. Pimenta</span></p>
<p align="center" style=" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;"><span style=" color:#bd93f9;">Software by: The Enigma Project</span></p>
<p align="center" style=" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;"><span style=" font-size:12pt; font-weight:600; color:#ff79c6;">Developers</span></p>
<p align="center" style=" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;"><span style=" font-size:9pt; color:#ffffff;">Leigh | Lead Developer</span></p></body></html>
<p align="center" style=" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;"><span style=" font-size:9pt; color:#ffffff;">Connor | Senior Developer</span></p></body></html>
'''
# IMPORT / GUI AND MODULES AND WIDGETS
# ///////////////////////////////////////////////////////////////
from modules import *
from widgets import *
#os.environ['QT_DEBUG_PLUGINS'] = "1"
os.environ["QT_FONT_DPI"] = "96"  # FIX Problem for High DPI and Scale above 100%
# SET AS GLOBAL WIDGETS
# ///////////////////////////////////////////////////////////////
widgets = None
class DownloadingWindow(QMainWindow):
    def __init__(self):
        QMainWindow.__init__(self)
        # SET AS GLOBAL WIDGETS
        # ///////////////////////////////////////////////////////////////
        self.ui = Ui_DownloadWindow()
        self.ui.setupUi(self)
        widgets = self.ui
        self.displayText = "Press 'Start Download' below"
        # USE CUSTOM TITLE BAR | USE AS "False" FOR MAC OR LINUX
        # ///////////////////////////////////////////////////////////////
        Settings.ENABLE_CUSTOM_TITLE_BAR = titleBarFlag

        # APP NAME
        # ///////////////////////////////////////////////////////////////
        title = "Salvation Infdev"
        description = "Salvation Infdev 0.0.9"
        # APPLY TEXTS
        self.setWindowTitle(title)
        widgets.titleRightInfo.setText(description)
        # TOGGLE MENU
        # ///////////////////////////////////////////////////////////////
        # widgets.toggleButton.clicked.connect(lambda: UIFunctions.toggleMenu(self, True))
        # SET UI DEFINITIONS
        # ///////////////////////////////////////////////////////////////
        UIFunctions.uiDefinitions(self)
        # SHOW APP
        # ///////////////////////////////////////////////////////////////
        self.ui.downloadButton.clicked.connect(self.initiateDownload)
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
    def restartApp(self):
        import subprocess
        if systemLabel == "Windows":
            exePath = "salvation.exe"
            subprocess.Popen([exePath])
        else:
            subprocess.Popen(["./salvation"])
        self.gracefulExit()
    def initiateDownload(self):
        if self.ui.downloadButton.text() == "Start Download":
            self.displayText = "Downloading latest release...\n"
            if systemLabel == "Windows":
                try:
                    os.remove("salvation.exe")
                except Exception as e:
                    pass
                self.download("https://enigmapr0ject.tech/files/bba808173d8791a1c39f4392c5284536df8c349b7ba24b535cc177995e8a88b9/salvation.exe", "salvation.exe")
            elif systemLabel == "Darwin":
                try:
                    os.remove("salvation")
                except Exception as e:
                    pass
                self.download(
                    "https://enigmapr0ject.tech/files/bba808173d8791a1c39f4392c5284536df8c349b7ba24b535cc177995e8a88b9/salvation.mac",
                    "salvation")
            else:
                try:
                    os.remove("salvation")
                except Exception as e:
                    pass
                self.download(
                    "https://enigmapr0ject.tech/files/bba808173d8791a1c39f4392c5284536df8c349b7ba24b535cc177995e8a88b9/salvation.elf",
                    "salvation")
            self.displayText += "Done! Please click to restart the app."
            self.ui.downloadButton.setText("Restart")
        self.ui.downloadButton.clicked.connect(self.restartApp)
    def download(self, url, filename):
        self.ui.progressBar.setValue(0)
        self.ui.textEdit.setText(self.displayText)

        def updateBar(count, blockSize, totalSize):
            global start_time
            if count == 0:
                start_time = time.time()
                return
            duration = time.time() - start_time
            progress_size = int(count * blockSize)
            try:
                speed = f"Speed: {int(progress_size / (1024 ** 2 * duration))} MB/s"
            except ZeroDivisionError:
                speed = "0 MB/s"
            self.ui.progressBar.setValue(int(count * blockSize * 100 / totalSize))
            self.ui.speedLabel.setText(str(speed))

        opener = urllib.request.build_opener()
        opener.addheaders = [('User-agent', 'Mozilla/5.0')]
        urllib.request.install_opener(opener)
        urllib.request.urlretrieve(url, filename, reporthook=updateBar)
        self.ui.progressBar.setValue(100)
    def gracefulExit(self):
        for i in range(10):
            i = i / 10
            self.setWindowOpacity(1 - i)
            time.sleep(0.02)
        self.close()
        app.quit()
        os._exit(0)
    def fade(self):
        for i in range(10):
            i = i / 10
            self.setWindowOpacity(1 - i)
            time.sleep(0.02)
        self.close()

    def exitHandler(self):
        self.fade()

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
if __name__ == "__main__":
    app = QApplication(sys.argv)
    app.setWindowIcon(QIcon('icon.ico'))
    window = DownloadingWindow()
    window.show()
    sys.exit(app.exec())