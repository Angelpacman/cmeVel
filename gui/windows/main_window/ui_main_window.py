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


# IMPORT QT CORE
from qt_core import *

# MAIN WINDOW
class UI_MainWindow(object):
    def setup_ui(self, parent):
        if not parent.objectName():
            parent.setObjectName("MainWindow")

        # SET INITIAL PARAMETERS
        parent.resize(920, 600)
        parent.setMinimumSize(720, 480)