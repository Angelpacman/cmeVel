# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
#
# AUTHOR: JOSE ANGEL RESENDIZ AVILES
#
# PROJECT CREATED WITH:  PySide6, astropy, scipy, matplotlib, numpy
#
# This project has MIT license and is intented to provide a Graphical
# use interface to have insigts from fit images relatives to Coronal
# Mass Ejections (CME)
#
# Github profile: @Angelpacman
#
# v0.0.1
#
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

# IMPORT MODULES
import sys
import os

#IMPORT QT CORE
from qt_core import *

#IMPORT MAIN WINDOW
from gui.windows.main_window.ui_main_window import UI_MainWindow

# MAIN WINDOW
class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        # SETUP MAIN WINDOW
        self.ui = UI_MainWindow()
        self.ui.setup_ui(self)


        # Show app
        self.show()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    sys.exit(app.exec())
    