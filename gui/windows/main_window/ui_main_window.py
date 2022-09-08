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

# IMPORT PAGES
from gui.pages.ui_pages import Ui_application_pages

# MAIN WINDOW
class UI_MainWindow(object):
    def setup_ui(self, parent):
        if not parent.objectName():
            parent.setObjectName("MainWindow")

        # # # # # # # # # # # # # # # # 
        # SET INITIAL PARAMETERS
        # # # # # # # # # # # # # # # # 
        parent.resize(920, 600)
        parent.setMinimumSize(720, 480)

        # # # # # # # # # # # # # # # # 
        # CREATE CENTRAL WIDGET
        # # # # # # # # # # # # # # # # 
        self.central_frame = QFrame()

        # CREATE MAIN LAYOUT
        self.main_layout = QHBoxLayout(self.central_frame)
        self.main_layout.setContentsMargins(0,0,0,0)
        self.main_layout.setSpacing(0)

        # # # # # # # # # # # # # # # # 
        # LEFT MENU
        # # # # # # # # # # # # # # # # 
        self.left_menu = QFrame()
        self.left_menu.setStyleSheet("background-color: #44475a")
        self.left_menu.setMaximumWidth(50)
        self.left_menu.setMinimumWidth(50)

        # LEFT MENU LAYOUT
        self.left_menu_layout = QVBoxLayout(self.left_menu)
        self.left_menu_layout.setContentsMargins(0,0,0,0)
        self.left_menu_layout.setSpacing(0)

        # TOP FRAME MENU
        self.left_menu_top_frame = QFrame()
        self.left_menu_top_frame.setMinimumHeight(50)
        self.left_menu_top_frame.setObjectName("left_menu_top_frame")
        self.left_menu_top_frame.setStyleSheet("#left_menu_top_frame {background-color: red;}")

        # TOP FRAME LAYOUT
        self.left_menu_top_layout = QVBoxLayout(self.left_menu_top_frame)
        self.left_menu_top_layout.setContentsMargins(0,0,0,0)
        self.left_menu_top_layout.setSpacing(0)

        # TOP BUTTONS
        self.toggle_button = QPushButton("Toggle")
        self.btn_1 = QPushButton("1")
        self.btn_2 = QPushButton("2")

        # ADD BUTTONS TO LAYOUT
        self.left_menu_top_layout.addWidget(self.toggle_button)
        self.left_menu_top_layout.addWidget(self.btn_1)
        self.left_menu_top_layout.addWidget(self.btn_2)

        # # # # # # # # # # # # # # # # 
        # MENU SPACER
        # # # # # # # # # # # # # # # # 
        self.left_menu_spacer = QSpacerItem(20,20, QSizePolicy.Minimum, QSizePolicy.Expanding)

        # # # # # # # # # # # # # # # # 
        # BOTTOM FRAME MENU
        # # # # # # # # # # # # # # # # 
        self.left_menu_bottom_frame = QFrame()
        self.left_menu_bottom_frame.setMinimumHeight(50)
        self.left_menu_bottom_frame.setObjectName("left_menu_bottom_frame")
        self.left_menu_bottom_frame.setStyleSheet("#left_menu_bottom_frame {background-color: red;} ")

        # BOTTOM FRAME LAYOUT
        self.left_menu_bottom_layout = QVBoxLayout(self.left_menu_bottom_frame)
        self.left_menu_bottom_layout.setContentsMargins(0,0,0,0)
        self.left_menu_bottom_layout.setSpacing(0)

        # BOTTOM BUTTONS
        self.help_button = QPushButton("Ayuda")

        # ADD BOTTOM BUTTONS TO LAYOUT
        self.left_menu_bottom_layout.addWidget(self.help_button)

        # # # # # # # # # # # # # # # # 
        # LABEL VERSION
        # # # # # # # # # # # # # # # # 
        self.left_menu_label_version = QLabel("v0.0.1")
        self.left_menu_label_version.setAlignment(Qt.AlignCenter)
        self.left_menu_label_version.setMinimumHeight(25)
        self.left_menu_label_version.setMaximumHeight(25)
        self.left_menu_label_version.setStyleSheet("color: #c3ccdf")

        # ADD TO LAYOUT
        self.left_menu_layout.addWidget(self.left_menu_top_frame)
        self.left_menu_layout.addItem(self.left_menu_spacer)
        self.left_menu_layout.addWidget(self.left_menu_bottom_frame)
        self.left_menu_layout.addWidget(self.left_menu_label_version)

        # CONTENT
        self.content = QFrame()
        self.content.setStyleSheet("background-color: #282a36")

            # Content Layout
        self.content_layout = QVBoxLayout(self.content)
        self.content_layout.setContentsMargins(0,0,0,0)
        self.content_layout.setSpacing(0)

            # Top bar
        self.top_bar = QFrame()
        self.top_bar.setMinimumHeight(25)
        self.top_bar.setMaximumHeight(25)
        self.top_bar.setStyleSheet("background-color: #21232d; color: #6272a4")
        self.top_bar_layout = QHBoxLayout(self.top_bar)
        self.top_bar_layout.setContentsMargins(10,0,10,0)

            # left label
        self.top_label_left = QLabel("cmeVel")

            # top spacer
        self.top_spacer = QSpacerItem(20,20, QSizePolicy.Expanding, QSizePolicy.Minimum)

            # right label
        self.top_label_right = QLabel("Pagina inicial")
        self.top_label_right.setStyleSheet("font: 700 9pt 'Segoe UI'")

            # add to layout
        self.top_bar_layout.addWidget(self.top_label_left)
        self.top_bar_layout.addItem(self.top_spacer)
        self.top_bar_layout.addWidget(self.top_label_right)

            # Application to pages
        self.pages = QStackedWidget()
        self.pages.setStyleSheet("font-size: 12pt; color: #f8f8f2")
        self.ui_pages = Ui_application_pages()
        self.ui_pages.setupUi(self.pages)
        self.pages.setCurrentWidget(self.ui_pages.page_1)

            # Bottom bar
        self.bottom_bar = QFrame()
        self.bottom_bar.setMinimumHeight(25)
        self.bottom_bar.setMaximumHeight(25)
        self.bottom_bar.setStyleSheet("background-color: #21232d; color: #6272a4")

        self.bottom_bar_layout = QHBoxLayout(self.bottom_bar)
        self.bottom_bar_layout.setContentsMargins(10,0,10,0)

            # left label
        self.bottom_label_left = QLabel("Desarrollado por: Jose Angel Resendiz Aviles")

            # bottom spacer
        self.bottom_spacer = QSpacerItem(20,20, QSizePolicy.Expanding, QSizePolicy.Minimum)

            # right label
        self.bottom_label_right = QLabel("2022")

            # add to layout
        self.bottom_bar_layout.addWidget(self.bottom_label_left)
        self.bottom_bar_layout.addItem(self.bottom_spacer)
        self.bottom_bar_layout.addWidget(self.bottom_label_right)


            # Add to content layout
        self.content_layout.addWidget(self.top_bar)
        self.content_layout.addWidget(self.pages)
        self.content_layout.addWidget(self.bottom_bar)

        # ADD WIDGETS TO APP
        self.main_layout.addWidget(self.left_menu)
        self.main_layout.addWidget(self.content)

        # SET CENTRAL WIDGET
        parent.setCentralWidget(self.central_frame)