# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'pagesWjFJdY.ui'
##
## Created by: Qt User Interface Compiler version 6.2.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from qt_core import *

class Ui_application_pages(object):
    def setupUi(self, application_pages):
        if not application_pages.objectName():
            application_pages.setObjectName(u"application_pages")
        application_pages.resize(582, 436)
        # # # # # # # # # # # # # # # #
        #
        # Pagina 1 HOME
        #
        # # # # # # # # # # # # # # # #

        self.page_1 = QWidget()
        self.page_1.setObjectName(u"page_1")
        self.gridLayout = QGridLayout(self.page_1)
        self.gridLayout.setObjectName(u"gridLayout")
        #
        fileLogo = "gui/images/icons/logo.svg"
        self.get_size = QSvgRenderer(fileLogo)
        self.svg_widget = QSvgWidget(fileLogo)
        self.svg_widget.setFixedSize(128, 128)
        self.gridLayout.addWidget(self.svg_widget, 1, 0, 1, 1)
        #
        self.label_1 = QLabel(self.page_1)
        self.label_1.setObjectName(u"label_1")
        self.label_1.setAlignment(Qt.AlignCenter)
        self.gridLayout.addWidget(self.label_1, 2, 0, 1, 1)
        # self.gridLayout.addWidget(self.label_1, Qt.AlignCenter, Qt.AlignCenter)

        self.label_empty = QLabel(self.page_1)
        self.label_empty.setObjectName(u"label_empty")
        self.label_empty.setAlignment(Qt.AlignCenter)

        self.gridLayout.addWidget(self.label_empty, 0, 0, 1, 1)
        # self.gridLayout.addWidget(self.label_empty, Qt.AlignCenter, Qt.AlignCenter)

        self.label_empty2 = QLabel(self.page_1)
        self.label_empty2.setObjectName(u"label_empty2")
        self.label_empty2.setAlignment(Qt.AlignCenter)

        self.gridLayout.addWidget(self.label_empty2, 3, 0, 1, 1)
        # self.gridLayout.addWidget(self.label_empty, Qt.AlignCenter, Qt.AlignCenter)

        application_pages.addWidget(self.page_1)

        # # # # # # # # # # # # # # # #
        #
        # Pagina 2 DATA
        #
        # # # # # # # # # # # # # # # #

        self.page_2 = QWidget()
        self.page_2.setObjectName(u"page_2")
        self.verticalLayout_2 = QVBoxLayout(self.page_2)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.label_2 = QLabel(self.page_2)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setAlignment(Qt.AlignCenter)

        self.verticalLayout_2.addWidget(self.label_2)

        application_pages.addWidget(self.page_2)

        # # # # # # # # # # # # # # # #
        #
        # Pagina 3 DRAW CONE
        #
        # # # # # # # # # # # # # # # #

        self.page_3 = QWidget()
        self.page_3.setObjectName(u"page_3")
        self.verticalLayout_3 = QVBoxLayout(self.page_3)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.label_3 = QLabel(self.page_3)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setAlignment(Qt.AlignCenter)

        self.verticalLayout_3.addWidget(self.label_3)

        application_pages.addWidget(self.page_3)

        # # # # # # # # # # # # # # # #
        #
        # Pagina 4 ENHANCE GRAPHS
        #
        # # # # # # # # # # # # # # # #

        self.page_4 = QWidget()
        self.page_4.setObjectName(u"page_4")
        self.verticalLayout_4 = QVBoxLayout(self.page_4)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.label_4 = QLabel(self.page_4)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setAlignment(Qt.AlignCenter)

        self.verticalLayout_4.addWidget(self.label_4)

        application_pages.addWidget(self.page_4)

        # # # # # # # # # # # # # # # #
        #
        # Pagina 5 FIT GAUSSIANS
        #
        # # # # # # # # # # # # # # # #

        self.page_5 = QWidget()
        self.page_5.setObjectName(u"page_5")
        self.verticalLayout_5 = QVBoxLayout(self.page_5)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.label_5 = QLabel(self.page_5)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setAlignment(Qt.AlignCenter)

        self.verticalLayout_5.addWidget(self.label_5)

        application_pages.addWidget(self.page_5)

        # # # # # # # # # # # # # # # #
        #
        # Pagina 6 PLOT PARAMETERS
        #
        # # # # # # # # # # # # # # # #

        self.page_6 = QWidget()
        self.page_6.setObjectName(u"page_6")
        self.verticalLayout_6 = QVBoxLayout(self.page_6)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.label_6 = QLabel(self.page_6)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setAlignment(Qt.AlignCenter)

        self.verticalLayout_6.addWidget(self.label_6)

        application_pages.addWidget(self.page_6)

        # # # # # # # # # # # # # # # #
        #
        # Pagina 7 SETTINGS
        #
        # # # # # # # # # # # # # # # #

        self.page_7 = QWidget()
        self.page_7.setObjectName(u"page_7")
        self.verticalLayout_7 = QVBoxLayout(self.page_7)
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.label_7 = QLabel(self.page_7)
        self.label_7.setObjectName(u"label_7")
        self.label_7.setAlignment(Qt.AlignCenter)

        self.verticalLayout_7.addWidget(self.label_7)

        # # # # # # # # # # # # # # # #
        #
        # Pagina 8 HELP
        #
        # # # # # # # # # # # # # # # #

        application_pages.addWidget(self.page_7)
        self.page_8 = QWidget()
        self.page_8.setObjectName(u"page_8")
        self.verticalLayout_8 = QVBoxLayout(self.page_8)
        self.verticalLayout_8.setObjectName(u"verticalLayout_8")
        self.label_8 = QLabel(self.page_8)
        self.label_8.setObjectName(u"label_8")
        self.label_8.setAlignment(Qt.AlignCenter)

        self.verticalLayout_8.addWidget(self.label_8)

        application_pages.addWidget(self.page_8)

        self.retranslateUi(application_pages)

        application_pages.setCurrentIndex(7)

        QMetaObject.connectSlotsByName(application_pages)
        # setupUi

    def retranslateUi(self, applicationPages):
        applicationPages.setWindowTitle(QCoreApplication.translate("applicationPages", u"StackedWidget", None))
        self.label_1.setText(QCoreApplication.translate("applicationPages", u"Pagina Inicial", None))
        self.label_2.setText(QCoreApplication.translate("applicationPages", u"Cargar Datos", None))
        self.label_3.setText(QCoreApplication.translate("applicationPages", u"Dibujar Cono", None))
        self.label_4.setText(QCoreApplication.translate("applicationPages", u"Mejorar despliegue de curvas", None))
        self.label_5.setText(QCoreApplication.translate("applicationPages", u"Ajustar gaussiana", None))
        self.label_6.setText(
            QCoreApplication.translate("applicationPages", u"Analizar gr\u00e1ficas de parametros", None))
        self.label_7.setText(QCoreApplication.translate("applicationPages", u"Settings", None))
        self.label_8.setText(QCoreApplication.translate("applicationPages", u"Obtener ayuda", None))
    # retranslateUi

