# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'stockapp.ui'
##
## Created by: Qt User Interface Compiler version 6.7.3
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QCheckBox, QComboBox, QLineEdit,
    QProgressBar, QPushButton, QSizePolicy, QTabWidget,
    QVBoxLayout, QWidget)

class Ui_stock_app(object):
    def setupUi(self, stock_app):
        if not stock_app.objectName():
            stock_app.setObjectName(u"stock_app")
        stock_app.resize(800, 600)
        self.tabs_widget = QTabWidget(stock_app)
        self.tabs_widget.setObjectName(u"tabs_widget")
        self.tabs_widget.setGeometry(QRect(0, 0, 801, 601))
        self.tabs_widget.setStyleSheet(u"background-color: green;  /* Replace #3498db with any color code */\n"
"")
        self.stock_manual_search_tab = QWidget()
        self.stock_manual_search_tab.setObjectName(u"stock_manual_search_tab")
        self.layoutWidget = QWidget(self.stock_manual_search_tab)
        self.layoutWidget.setObjectName(u"layoutWidget")
        self.layoutWidget.setGeometry(QRect(280, 460, 221, 56))
        self.verticalLayout = QVBoxLayout(self.layoutWidget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.stock_search_manual_bar = QLineEdit(self.layoutWidget)
        self.stock_search_manual_bar.setObjectName(u"stock_search_manual_bar")
        self.stock_search_manual_bar.setStyleSheet(u"color: white;  /* Text color */")

        self.verticalLayout.addWidget(self.stock_search_manual_bar)

        self.stock_search_manual_button = QPushButton(self.layoutWidget)
        self.stock_search_manual_button.setObjectName(u"stock_search_manual_button")
        self.stock_search_manual_button.setStyleSheet(u"color: white;  /* Text color */")

        self.verticalLayout.addWidget(self.stock_search_manual_button)

        self.tabs_widget.addTab(self.stock_manual_search_tab, "")
        self.stock_auto_search_tab = QWidget()
        self.stock_auto_search_tab.setObjectName(u"stock_auto_search_tab")
        self.stock_auto_search_progress_bar = QProgressBar(self.stock_auto_search_tab)
        self.stock_auto_search_progress_bar.setObjectName(u"stock_auto_search_progress_bar")
        self.stock_auto_search_progress_bar.setGeometry(QRect(250, 510, 259, 24))
        self.stock_auto_search_progress_bar.setStyleSheet(u"color: white;  /* Text color */")
        self.stock_auto_search_progress_bar.setRange(0,99)
        self.layoutWidget1 = QWidget(self.stock_auto_search_tab)
        self.layoutWidget1.setObjectName(u"layoutWidget1")
        self.layoutWidget1.setGeometry(QRect(250, 450, 261, 56))
        self.verticalLayout_2 = QVBoxLayout(self.layoutWidget1)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.stock_search_auto_combo_box = QComboBox(self.layoutWidget1)
        self.stock_search_auto_combo_box.setObjectName(u"stock_search_auto_combo_box")
        self.stock_search_auto_combo_box.setStyleSheet(u"color: white;  /* Text color */")

        self.verticalLayout_2.addWidget(self.stock_search_auto_combo_box)

        self.stock_search_automation_button = QPushButton(self.layoutWidget1)
        self.stock_search_automation_button.setObjectName(u"stock_search_automation_button")
        self.stock_search_automation_button.setStyleSheet(u"color: white;  /* Text color */")

        self.verticalLayout_2.addWidget(self.stock_search_automation_button)

        self.tabs_widget.addTab(self.stock_auto_search_tab, "")
        self.stock_search_settings = QWidget()
        self.stock_search_settings.setObjectName(u"stock_search_settings")
        self.layoutWidget2 = QWidget(self.stock_search_settings)
        self.layoutWidget2.setObjectName(u"layoutWidget2")
        self.layoutWidget2.setGeometry(QRect(0, 0, 151, 164))
        self.verticalLayout_3 = QVBoxLayout(self.layoutWidget2)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.analytics_check_box = QCheckBox(self.layoutWidget2)
        self.analytics_check_box.setObjectName(u"analytics_check_box")
        self.analytics_check_box.setStyleSheet(u"color: white; ")

        self.verticalLayout_3.addWidget(self.analytics_check_box)

        self.alpha_spread_check_box = QCheckBox(self.layoutWidget2)
        self.alpha_spread_check_box.setObjectName(u"alpha_spread_check_box")
        self.alpha_spread_check_box.setStyleSheet(u"color: white; ")

        self.verticalLayout_3.addWidget(self.alpha_spread_check_box)

        self.focus_guru_check_box = QCheckBox(self.layoutWidget2)
        self.focus_guru_check_box.setObjectName(u"focus_guru_check_box")
        self.focus_guru_check_box.setStyleSheet(u"color: white; ")

        self.verticalLayout_3.addWidget(self.focus_guru_check_box)

        self.macro_trends_check_box = QCheckBox(self.layoutWidget2)
        self.macro_trends_check_box.setObjectName(u"macro_trends_check_box")
        self.macro_trends_check_box.setStyleSheet(u"color: white; ")

        self.verticalLayout_3.addWidget(self.macro_trends_check_box)

        self.finance_charts_check_box = QCheckBox(self.layoutWidget2)
        self.finance_charts_check_box.setObjectName(u"finance_charts_check_box")
        self.finance_charts_check_box.setStyleSheet(u"color: white; ")

        self.verticalLayout_3.addWidget(self.finance_charts_check_box)

        self.companies_market_cap_check_box = QCheckBox(self.layoutWidget2)
        self.companies_market_cap_check_box.setObjectName(u"companies_market_cap_check_box")
        self.companies_market_cap_check_box.setStyleSheet(u"color: white; ")

        self.verticalLayout_3.addWidget(self.companies_market_cap_check_box)

        self.tabs_widget.addTab(self.stock_search_settings, "")
        self.retranslateUi(stock_app)

        self.tabs_widget.setCurrentIndex(3)


        QMetaObject.connectSlotsByName(stock_app)
    # setupUi

    def retranslateUi(self, stock_app):
        stock_app.setWindowTitle(QCoreApplication.translate("stock_app", u"Widget", None))
        self.stock_search_manual_button.setText(QCoreApplication.translate("stock_app", u"Search", None))
        self.tabs_widget.setTabText(self.tabs_widget.indexOf(self.stock_manual_search_tab), QCoreApplication.translate("stock_app", u"Stock Search", None))
        self.stock_search_automation_button.setText(QCoreApplication.translate("stock_app", u"Search", None))
        self.tabs_widget.setTabText(self.tabs_widget.indexOf(self.stock_auto_search_tab), QCoreApplication.translate("stock_app", u"Auto Stock Search", None))
        self.analytics_check_box.setText(QCoreApplication.translate("stock_app", u"Analytics Panel", None))
        self.alpha_spread_check_box.setText(QCoreApplication.translate("stock_app", u"Alpha Spread", None))
        self.focus_guru_check_box.setText(QCoreApplication.translate("stock_app", u"Focus Guru", None))
        self.macro_trends_check_box.setText(QCoreApplication.translate("stock_app", u"Macro Trends", None))
        self.finance_charts_check_box.setText(QCoreApplication.translate("stock_app", u"Finance Charts", None))
        self.companies_market_cap_check_box.setText(QCoreApplication.translate("stock_app", u"Companies Market Cap", None))
        self.tabs_widget.setTabText(self.tabs_widget.indexOf(self.stock_search_settings), QCoreApplication.translate("stock_app", u"Settings", None))

    # retranslateUi

