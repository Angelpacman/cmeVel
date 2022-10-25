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

# IMPORT QT CORE
from qt_core import *

# IMPORT MAIN WINDOW
from gui.windows.main_window.ui_main_window import *


# MAIN WINDOW
class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        # self.animation = None
        self.setWindowTitle("Coronal Mass Ejection Analyzer")

        # SETUP MAIN WINDOW
        self.ui = UI_MainWindow()
        self.ui.setup_ui(self)

        # Toggle button
        self.ui.toggle_button.clicked.connect(self.toggle_button)

        # Home button
        self.ui.btn_1_home.clicked.connect(self.home)

        # Btn load Data
        self.ui.btn_2_data.clicked.connect(self.loadData)

        # Btn draw Cone
        self.ui.btn_3_cone.clicked.connect(self.takeCone)

        # Display curves
        self.ui.btn_4_curves.clicked.connect(self.displayCurves)

        # Fit Gaussian
        self.ui.btn_5_gaussFit.clicked.connect(self.gaussFit)

        # Check velocity and parameter graphs
        self.ui.btn_6_checkGraphs.clicked.connect(self.checkGraphs)

        # Help button
        self.ui.btn_7_help.clicked.connect(self.help)

        # Config
        self.ui.settings_btn.clicked.connect(self.settings)

        # Show app
        self.show()

    def reset_selection(self):
        for btn in self.ui.left_menu.findChildren(QPushButton):
            try:
                btn.set_active(False)
            except:
                pass

    def toggle_button(self):
        # get menu width
        menu_width = self.ui.left_menu.width()

        # check with
        width = 50
        if menu_width == 50:
            width = 200

        # start animation
        self.animation = QPropertyAnimation(self.ui.left_menu, b"minimumWidth")
        self.animation.setStartValue(menu_width)
        self.animation.setEndValue(width)
        self.animation.setDuration(150)
        self.animation.setEasingCurve(QEasingCurve.InOutSine)
        self.animation.start()

    def home(self):
        self.reset_selection()
        self.ui.pages.setCurrentWidget(self.ui.ui_pages.page_1)
        self.ui.btn_1_home.set_active(True)

    def loadData(self):
        self.reset_selection()
        self.ui.pages.setCurrentWidget(self.ui.ui_pages.page_2)
        self.ui.btn_2_data.set_active(True)

    def takeCone(self):
        self.reset_selection()
        self.ui.pages.setCurrentWidget(self.ui.ui_pages.page_3)
        self.ui.btn_3_cone.set_active(True)

    def displayCurves(self):
        self.reset_selection()
        self.ui.pages.setCurrentWidget(self.ui.ui_pages.page_4)
        self.ui.btn_4_curves.set_active(True)

    def gaussFit(self):
        self.reset_selection()
        self.ui.pages.setCurrentWidget(self.ui.ui_pages.page_5)
        self.ui.btn_5_gaussFit.set_active(True)

    def checkGraphs(self):
        self.reset_selection()
        self.ui.pages.setCurrentWidget(self.ui.ui_pages.page_6)
        self.ui.btn_6_checkGraphs.set_active(True)

    def settings(self):
        self.reset_selection()
        self.ui.pages.setCurrentWidget(self.ui.ui_pages.page_7)
        self.ui.settings_btn.set_active(True)

    def help(self):
        self.reset_selection()
        self.ui.pages.setCurrentWidget(self.ui.ui_pages.page_8)
        self.ui.btn_7_help.set_active(True)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    sys.exit(app.exec())
