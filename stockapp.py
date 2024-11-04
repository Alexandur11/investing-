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
    QProgressBar, QPushButton, QScrollArea, QSizePolicy,
    QTabWidget, QVBoxLayout, QWidget)

class Ui_Widget(object):
    def setupUi(self, Widget):
        if not Widget.objectName():
            Widget.setObjectName(u"Widget")
        Widget.resize(800, 600)
        self.tabs_widget = QTabWidget(Widget)
        self.tabs_widget.setObjectName(u"tabs_widget")
        self.tabs_widget.setGeometry(QRect(0, 0, 801, 601))
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

        self.verticalLayout.addWidget(self.stock_search_manual_bar)

        self.stock_search_manual_button = QPushButton(self.layoutWidget)
        self.stock_search_manual_button.setObjectName(u"stock_search_manual_button")
        self.stock_search_manual_button.setStyleSheet(u"color: red;  /* Text color */")

        self.verticalLayout.addWidget(self.stock_search_manual_button)

        self.tabs_widget.addTab(self.stock_manual_search_tab, "")
        self.stock_auto_search_tab = QWidget()
        self.stock_auto_search_tab.setObjectName(u"stock_auto_search_tab")
        self.stock_auto_search_progress_bar = QProgressBar(self.stock_auto_search_tab)
        self.stock_auto_search_progress_bar.setObjectName(u"stock_auto_search_progress_bar")
        self.stock_auto_search_progress_bar.setGeometry(QRect(250, 510, 259, 24))
        self.stock_auto_search_progress_bar.setStyleSheet(u"color: red;  /* Text color */")
        self.stock_auto_search_progress_bar.setValue(24)
        self.widget = QWidget(self.stock_auto_search_tab)
        self.widget.setObjectName(u"widget")
        self.widget.setGeometry(QRect(250, 450, 261, 56))
        self.verticalLayout_2 = QVBoxLayout(self.widget)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.stock_search_auto_combo_box = QComboBox(self.widget)
        self.stock_search_auto_combo_box.setObjectName(u"stock_search_auto_combo_box")

        self.verticalLayout_2.addWidget(self.stock_search_auto_combo_box)

        self.stock_search_automation_button = QPushButton(self.widget)
        self.stock_search_automation_button.setObjectName(u"stock_search_automation_button")
        self.stock_search_automation_button.setStyleSheet(u"color: red;  /* Text color */")

        self.verticalLayout_2.addWidget(self.stock_search_automation_button)

        self.tabs_widget.addTab(self.stock_auto_search_tab, "")
        self.stock_search_settings = QWidget()
        self.stock_search_settings.setObjectName(u"stock_search_settings")
        self.layoutWidget1 = QWidget(self.stock_search_settings)
        self.layoutWidget1.setObjectName(u"layoutWidget1")
        self.layoutWidget1.setGeometry(QRect(0, 0, 151, 164))
        self.verticalLayout_3 = QVBoxLayout(self.layoutWidget1)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.analytics_check_box = QCheckBox(self.layoutWidget1)
        self.analytics_check_box.setObjectName(u"analytics_check_box")
        self.analytics_check_box.setStyleSheet(u"color: red; ")

        self.verticalLayout_3.addWidget(self.analytics_check_box)

        self.alpha_spread_check_box = QCheckBox(self.layoutWidget1)
        self.alpha_spread_check_box.setObjectName(u"alpha_spread_check_box")
        self.alpha_spread_check_box.setStyleSheet(u"color: red; ")

        self.verticalLayout_3.addWidget(self.alpha_spread_check_box)

        self.focus_guru_check_box = QCheckBox(self.layoutWidget1)
        self.focus_guru_check_box.setObjectName(u"focus_guru_check_box")
        self.focus_guru_check_box.setStyleSheet(u"color: red; ")

        self.verticalLayout_3.addWidget(self.focus_guru_check_box)

        self.macro_trends_check_box = QCheckBox(self.layoutWidget1)
        self.macro_trends_check_box.setObjectName(u"macro_trends_check_box")
        self.macro_trends_check_box.setStyleSheet(u"color: red; ")

        self.verticalLayout_3.addWidget(self.macro_trends_check_box)

        self.finance_charts_check_box = QCheckBox(self.layoutWidget1)
        self.finance_charts_check_box.setObjectName(u"finance_charts_check_box")
        self.finance_charts_check_box.setStyleSheet(u"color: red; ")

        self.verticalLayout_3.addWidget(self.finance_charts_check_box)

        self.companies_market_cap_check_box = QCheckBox(self.layoutWidget1)
        self.companies_market_cap_check_box.setObjectName(u"companies_market_cap_check_box")
        self.companies_market_cap_check_box.setStyleSheet(u"color: red; ")

        self.verticalLayout_3.addWidget(self.companies_market_cap_check_box)

        self.tabs_widget.addTab(self.stock_search_settings, "")
        self.information_tab = QWidget()
        self.information_tab.setObjectName(u"information_tab")
        self.information_scroll_area = QScrollArea(self.information_tab)
        self.information_scroll_area.setObjectName(u"information_scroll_area")
        self.information_scroll_area.setGeometry(QRect(60, 50, 661, 491))
        self.information_scroll_area.setWidgetResizable(True)
        self.scrollAreaWidgetContents = QWidget()
        self.scrollAreaWidgetContents.setObjectName(u"scrollAreaWidgetContents")
        self.scrollAreaWidgetContents.setGeometry(QRect(0, 0, 659, 489))
        self.information_scroll_area.setWidget(self.scrollAreaWidgetContents)
        self.tabs_widget.addTab(self.information_tab, "")

        self.retranslateUi(Widget)

        self.tabs_widget.setCurrentIndex(1)


        QMetaObject.connectSlotsByName(Widget)
    # setupUi

    def retranslateUi(self, Widget):
        Widget.setWindowTitle(QCoreApplication.translate("Widget", u"Widget", None))
        self.stock_search_manual_button.setText(QCoreApplication.translate("Widget", u"Search", None))
        self.tabs_widget.setTabText(self.tabs_widget.indexOf(self.stock_manual_search_tab), QCoreApplication.translate("Widget", u"Stock Search", None))
        self.stock_search_automation_button.setText(QCoreApplication.translate("Widget", u"Search", None))
        self.tabs_widget.setTabText(self.tabs_widget.indexOf(self.stock_auto_search_tab), QCoreApplication.translate("Widget", u"Auto Stock Search", None))
        self.analytics_check_box.setText(QCoreApplication.translate("Widget", u"Analytics Panel", None))
        self.alpha_spread_check_box.setText(QCoreApplication.translate("Widget", u"Alpha Spread", None))
        self.focus_guru_check_box.setText(QCoreApplication.translate("Widget", u"Focus Guru", None))
        self.macro_trends_check_box.setText(QCoreApplication.translate("Widget", u"Macro Trends", None))
        self.finance_charts_check_box.setText(QCoreApplication.translate("Widget", u"Finance Charts", None))
        self.companies_market_cap_check_box.setText(QCoreApplication.translate("Widget", u"Companies Market Cap", None))
        self.tabs_widget.setTabText(self.tabs_widget.indexOf(self.stock_search_settings), QCoreApplication.translate("Widget", u"Settings", None))
        self.tabs_widget.setTabText(self.tabs_widget.indexOf(self.information_tab), QCoreApplication.translate("Widget", u"Information", None))
    # retranslateUi

