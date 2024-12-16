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
from PySide6.QtWidgets import (QApplication, QCheckBox, QComboBox, QFrame,
    QGroupBox, QHBoxLayout, QLabel, QLineEdit,
    QProgressBar, QPushButton, QRadioButton, QSizePolicy,
    QTabWidget, QTextBrowser, QTextEdit, QVBoxLayout,
    QWidget)

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
        self.stock_manual_search_vertical_layout = QVBoxLayout(self.layoutWidget)
        self.stock_manual_search_vertical_layout.setObjectName(u"stock_manual_search_vertical_layout")
        self.stock_manual_search_vertical_layout.setContentsMargins(0, 0, 0, 0)
        self.stock_search_manual_bar = QLineEdit(self.layoutWidget)
        self.stock_search_manual_bar.setObjectName(u"stock_search_manual_bar")
        self.stock_search_manual_bar.setStyleSheet(u"color: white;  /* Text color */")

        self.stock_manual_search_vertical_layout.addWidget(self.stock_search_manual_bar)

        self.stock_search_manual_button = QPushButton(self.layoutWidget)
        self.stock_search_manual_button.setObjectName(u"stock_search_manual_button")
        self.stock_search_manual_button.setStyleSheet(u"color: white;  /* Text color */")

        self.stock_manual_search_vertical_layout.addWidget(self.stock_search_manual_button)

        self.tabs_widget.addTab(self.stock_manual_search_tab, "")
        self.stock_auto_search_tab = QWidget()
        self.stock_auto_search_tab.setObjectName(u"stock_auto_search_tab")
        self.stock_auto_search_progress_bar = QProgressBar(self.stock_auto_search_tab)
        self.stock_auto_search_progress_bar.setObjectName(u"stock_auto_search_progress_bar")
        self.stock_auto_search_progress_bar.setGeometry(QRect(250, 510, 259, 24))
        self.stock_auto_search_progress_bar.setStyleSheet(u"color: white;")
        self.stock_auto_search_progress_bar.setMaximum(99)
        self.stock_auto_search_progress_bar.setValue(1)
        self.layoutWidget1 = QWidget(self.stock_auto_search_tab)
        self.layoutWidget1.setObjectName(u"layoutWidget1")
        self.layoutWidget1.setGeometry(QRect(250, 450, 261, 56))
        self.stock_auto_search_vertical_layout = QVBoxLayout(self.layoutWidget1)
        self.stock_auto_search_vertical_layout.setObjectName(u"stock_auto_search_vertical_layout")
        self.stock_auto_search_vertical_layout.setContentsMargins(0, 0, 0, 0)
        self.stock_search_auto_combo_box = QComboBox(self.layoutWidget1)
        self.stock_search_auto_combo_box.setObjectName(u"stock_search_auto_combo_box")
        self.stock_search_auto_combo_box.setStyleSheet(u"color: white;  /* Text color */")

        self.stock_auto_search_vertical_layout.addWidget(self.stock_search_auto_combo_box)

        self.stock_search_automation_button = QPushButton(self.layoutWidget1)
        self.stock_search_automation_button.setObjectName(u"stock_search_automation_button")
        self.stock_search_automation_button.setStyleSheet(u"color: white;  /* Text color */")

        self.stock_auto_search_vertical_layout.addWidget(self.stock_search_automation_button)

        self.tabs_widget.addTab(self.stock_auto_search_tab, "")
        self.stock_comparison_tab = QWidget()
        self.stock_comparison_tab.setObjectName(u"stock_comparison_tab")
        self.stock_a_frame = QFrame(self.stock_comparison_tab)
        self.stock_a_frame.setObjectName(u"stock_a_frame")
        self.stock_a_frame.setGeometry(QRect(0, 0, 371, 271))
        self.stock_a_frame.setStyleSheet(u"background: black;")
        self.stock_a_frame.setFrameShape(QFrame.Shape.StyledPanel)
        self.stock_a_frame.setFrameShadow(QFrame.Shadow.Raised)
        self.debt_management_a = QLabel(self.stock_a_frame)
        self.debt_management_a.setObjectName(u"debt_management_a")
        self.debt_management_a.setGeometry(QRect(0, 30, 99, 16))
        self.debt_management_a.setStyleSheet(u"color: white;  /* Text color */")
        self.layoutWidget2 = QWidget(self.stock_a_frame)
        self.layoutWidget2.setObjectName(u"layoutWidget2")
        self.layoutWidget2.setGeometry(QRect(0, 0, 216, 26))
        self.stock_a_horizontal_layout = QHBoxLayout(self.layoutWidget2)
        self.stock_a_horizontal_layout.setObjectName(u"stock_a_horizontal_layout")
        self.stock_a_horizontal_layout.setContentsMargins(0, 0, 0, 0)
        self.stock_search_a_bar = QLineEdit(self.layoutWidget2)
        self.stock_search_a_bar.setObjectName(u"stock_search_a_bar")
        self.stock_search_a_bar.setStyleSheet(u"color: white;")

        self.stock_a_horizontal_layout.addWidget(self.stock_search_a_bar)

        self.stock_search_a_button = QPushButton(self.layoutWidget2)
        self.stock_search_a_button.setObjectName(u"stock_search_a_button")
        self.stock_search_a_button.setStyleSheet(u"QPushButton {\n"
"    border: 2px solid black;         /* Default border */\n"
"    border-radius: 5px;              /* Rounded corners */\n"
"    background-color: lightgray;     /* Default background color */\n"
"}\n"
"QPushButton:pressed {\n"
"    border: 3px solid red;           /* Thicker border when clicked */\n"
"    background-color: lightblue;     /* Background color when pressed */\n"
"}\n"
"QPushButton:hover {\n"
"    border: 2px dashed blue;         /* Dashed border on hover */\n"
"    background-color: lightgreen;    /* Background color when hovered */\n"
"}\n"
"")

        self.stock_a_horizontal_layout.addWidget(self.stock_search_a_button)

        self.stock_a_efficiency = QLabel(self.stock_a_frame)
        self.stock_a_efficiency.setObjectName(u"stock_a_efficiency")
        self.stock_a_efficiency.setGeometry(QRect(160, 30, 51, 16))
        self.stock_a_efficiency.setStyleSheet(u"color: white;  /* Text color */")
        self.stock_a_price_estimates = QLabel(self.stock_a_frame)
        self.stock_a_price_estimates.setObjectName(u"stock_a_price_estimates")
        self.stock_a_price_estimates.setGeometry(QRect(290, 30, 79, 16))
        self.stock_a_price_estimates.setStyleSheet(u"color: white;  /* Text color */")
        self.layoutWidget_11 = QWidget(self.stock_a_frame)
        self.layoutWidget_11.setObjectName(u"layoutWidget_11")
        self.layoutWidget_11.setGeometry(QRect(290, 50, 81, 221))
        self.stock_a_price_estimates_vertical_layout = QVBoxLayout(self.layoutWidget_11)
        self.stock_a_price_estimates_vertical_layout.setSpacing(0)
        self.stock_a_price_estimates_vertical_layout.setObjectName(u"stock_a_price_estimates_vertical_layout")
        self.stock_a_price_estimates_vertical_layout.setContentsMargins(0, 0, 0, 0)
        self.stock_a_pe = QLabel(self.layoutWidget_11)
        self.stock_a_pe.setObjectName(u"stock_a_pe")
        self.stock_a_pe.setEnabled(False)
        self.stock_a_pe.setStyleSheet(u"color: white;  /* Text color */")

        self.stock_a_price_estimates_vertical_layout.addWidget(self.stock_a_pe)

        self.stock_a_peg = QLabel(self.layoutWidget_11)
        self.stock_a_peg.setObjectName(u"stock_a_peg")
        self.stock_a_peg.setEnabled(False)
        self.stock_a_peg.setStyleSheet(u"color: white;  /* Text color */")

        self.stock_a_price_estimates_vertical_layout.addWidget(self.stock_a_peg)

        self.stock_a_ps = QLabel(self.layoutWidget_11)
        self.stock_a_ps.setObjectName(u"stock_a_ps")
        self.stock_a_ps.setEnabled(False)
        self.stock_a_ps.setStyleSheet(u"color: white;  /* Text color */")

        self.stock_a_price_estimates_vertical_layout.addWidget(self.stock_a_ps)

        self.stock_a_pb = QLabel(self.layoutWidget_11)
        self.stock_a_pb.setObjectName(u"stock_a_pb")
        self.stock_a_pb.setEnabled(False)
        self.stock_a_pb.setStyleSheet(u"color: white;  /* Text color */")

        self.stock_a_price_estimates_vertical_layout.addWidget(self.stock_a_pb)

        self.stock_a_pfcf = QLabel(self.layoutWidget_11)
        self.stock_a_pfcf.setObjectName(u"stock_a_pfcf")
        self.stock_a_pfcf.setEnabled(False)
        self.stock_a_pfcf.setStyleSheet(u"color: white;  /* Text color */")

        self.stock_a_price_estimates_vertical_layout.addWidget(self.stock_a_pfcf)

        self.layoutWidget3 = QWidget(self.stock_a_frame)
        self.layoutWidget3.setObjectName(u"layoutWidget3")
        self.layoutWidget3.setGeometry(QRect(0, 50, 161, 221))
        self.stock_a_debt_management_vertical_layout = QVBoxLayout(self.layoutWidget3)
        self.stock_a_debt_management_vertical_layout.setSpacing(0)
        self.stock_a_debt_management_vertical_layout.setObjectName(u"stock_a_debt_management_vertical_layout")
        self.stock_a_debt_management_vertical_layout.setContentsMargins(0, 0, 0, 0)
        self.stock_a_cash_to_debt = QLabel(self.layoutWidget3)
        self.stock_a_cash_to_debt.setObjectName(u"stock_a_cash_to_debt")
        self.stock_a_cash_to_debt.setEnabled(False)
        self.stock_a_cash_to_debt.setStyleSheet(u"color: white;  /* Text color */")

        self.stock_a_debt_management_vertical_layout.addWidget(self.stock_a_cash_to_debt)

        self.stock_a_debt_to_equity = QLabel(self.layoutWidget3)
        self.stock_a_debt_to_equity.setObjectName(u"stock_a_debt_to_equity")
        self.stock_a_debt_to_equity.setEnabled(False)
        self.stock_a_debt_to_equity.setStyleSheet(u"color: white;  /* Text color */")

        self.stock_a_debt_management_vertical_layout.addWidget(self.stock_a_debt_to_equity)

        self.stock_a_debt_to_ebitda = QLabel(self.layoutWidget3)
        self.stock_a_debt_to_ebitda.setObjectName(u"stock_a_debt_to_ebitda")
        self.stock_a_debt_to_ebitda.setEnabled(False)
        self.stock_a_debt_to_ebitda.setStyleSheet(u"color: white;  /* Text color */")

        self.stock_a_debt_management_vertical_layout.addWidget(self.stock_a_debt_to_ebitda)

        self.stock_a_interest_coverage = QLabel(self.layoutWidget3)
        self.stock_a_interest_coverage.setObjectName(u"stock_a_interest_coverage")
        self.stock_a_interest_coverage.setEnabled(False)
        self.stock_a_interest_coverage.setStyleSheet(u"color: white;  /* Text color */")

        self.stock_a_debt_management_vertical_layout.addWidget(self.stock_a_interest_coverage)

        self.stock_a_current_ratio = QLabel(self.layoutWidget3)
        self.stock_a_current_ratio.setObjectName(u"stock_a_current_ratio")
        self.stock_a_current_ratio.setEnabled(False)
        self.stock_a_current_ratio.setStyleSheet(u"color: white;  /* Text color */")

        self.stock_a_debt_management_vertical_layout.addWidget(self.stock_a_current_ratio)

        self.layoutWidget4 = QWidget(self.stock_a_frame)
        self.layoutWidget4.setObjectName(u"layoutWidget4")
        self.layoutWidget4.setGeometry(QRect(170, 50, 111, 221))
        self.stock_a_efficiency_vertical_layout = QVBoxLayout(self.layoutWidget4)
        self.stock_a_efficiency_vertical_layout.setSpacing(0)
        self.stock_a_efficiency_vertical_layout.setObjectName(u"stock_a_efficiency_vertical_layout")
        self.stock_a_efficiency_vertical_layout.setContentsMargins(0, 0, 0, 0)
        self.stock_a_roa = QLabel(self.layoutWidget4)
        self.stock_a_roa.setObjectName(u"stock_a_roa")
        self.stock_a_roa.setEnabled(False)
        self.stock_a_roa.setStyleSheet(u"color: white;  /* Text color */")

        self.stock_a_efficiency_vertical_layout.addWidget(self.stock_a_roa)

        self.stock_a_roe = QLabel(self.layoutWidget4)
        self.stock_a_roe.setObjectName(u"stock_a_roe")
        self.stock_a_roe.setEnabled(False)
        self.stock_a_roe.setStyleSheet(u"color: white;  /* Text color */")

        self.stock_a_efficiency_vertical_layout.addWidget(self.stock_a_roe)

        self.stock_a_roic = QLabel(self.layoutWidget4)
        self.stock_a_roic.setObjectName(u"stock_a_roic")
        self.stock_a_roic.setEnabled(False)
        self.stock_a_roic.setStyleSheet(u"color: white;  /* Text color */")

        self.stock_a_efficiency_vertical_layout.addWidget(self.stock_a_roic)

        self.stock_c_frame = QFrame(self.stock_comparison_tab)
        self.stock_c_frame.setObjectName(u"stock_c_frame")
        self.stock_c_frame.setGeometry(QRect(0, 290, 371, 281))
        self.stock_c_frame.setStyleSheet(u"background: black;")
        self.stock_c_frame.setFrameShape(QFrame.Shape.StyledPanel)
        self.stock_c_frame.setFrameShadow(QFrame.Shadow.Raised)
        self.layoutWidget_3 = QWidget(self.stock_c_frame)
        self.layoutWidget_3.setObjectName(u"layoutWidget_3")
        self.layoutWidget_3.setGeometry(QRect(0, 0, 216, 26))
        self.stock_c_horizontal_layout = QHBoxLayout(self.layoutWidget_3)
        self.stock_c_horizontal_layout.setObjectName(u"stock_c_horizontal_layout")
        self.stock_c_horizontal_layout.setContentsMargins(0, 0, 0, 0)
        self.stock_search_c_bar = QLineEdit(self.layoutWidget_3)
        self.stock_search_c_bar.setObjectName(u"stock_search_c_bar")
        self.stock_search_c_bar.setStyleSheet(u"color: white;")

        self.stock_c_horizontal_layout.addWidget(self.stock_search_c_bar)

        self.stock_search_c_button = QPushButton(self.layoutWidget_3)
        self.stock_search_c_button.setObjectName(u"stock_search_c_button")
        self.stock_search_c_button.setStyleSheet(u"QPushButton {\n"
"    border: 2px solid black;         /* Default border */\n"
"    border-radius: 5px;              /* Rounded corners */\n"
"    background-color: lightgray;     /* Default background color */\n"
"}\n"
"QPushButton:pressed {\n"
"    border: 3px solid red;           /* Thicker border when clicked */\n"
"    background-color: lightblue;     /* Background color when pressed */\n"
"}\n"
"QPushButton:hover {\n"
"    border: 2px dashed blue;         /* Dashed border on hover */\n"
"    background-color: lightgreen;    /* Background color when hovered */\n"
"}\n"
"")

        self.stock_c_horizontal_layout.addWidget(self.stock_search_c_button)

        self.debt_management_c = QLabel(self.stock_c_frame)
        self.debt_management_c.setObjectName(u"debt_management_c")
        self.debt_management_c.setGeometry(QRect(0, 30, 99, 16))
        self.debt_management_c.setStyleSheet(u"color: white;  /* Text color */")
        self.stock_c_efficiency = QLabel(self.stock_c_frame)
        self.stock_c_efficiency.setObjectName(u"stock_c_efficiency")
        self.stock_c_efficiency.setGeometry(QRect(160, 30, 51, 16))
        self.stock_c_efficiency.setStyleSheet(u"color: white;  /* Text color */")
        self.stock_c_price_estimates = QLabel(self.stock_c_frame)
        self.stock_c_price_estimates.setObjectName(u"stock_c_price_estimates")
        self.stock_c_price_estimates.setGeometry(QRect(287, 30, 79, 16))
        self.stock_c_price_estimates.setStyleSheet(u"color: white;  /* Text color */")
        self.layoutWidget_5 = QWidget(self.stock_c_frame)
        self.layoutWidget_5.setObjectName(u"layoutWidget_5")
        self.layoutWidget_5.setGeometry(QRect(0, 50, 161, 231))
        self.stock_c_debt_management_vertical_layout = QVBoxLayout(self.layoutWidget_5)
        self.stock_c_debt_management_vertical_layout.setSpacing(0)
        self.stock_c_debt_management_vertical_layout.setObjectName(u"stock_c_debt_management_vertical_layout")
        self.stock_c_debt_management_vertical_layout.setContentsMargins(0, 0, 0, 0)
        self.stock_c_cash_to_debt = QLabel(self.layoutWidget_5)
        self.stock_c_cash_to_debt.setObjectName(u"stock_c_cash_to_debt")
        self.stock_c_cash_to_debt.setEnabled(False)
        self.stock_c_cash_to_debt.setStyleSheet(u"color: white;  /* Text color */")

        self.stock_c_debt_management_vertical_layout.addWidget(self.stock_c_cash_to_debt)

        self.stock_c_debt_to_equity = QLabel(self.layoutWidget_5)
        self.stock_c_debt_to_equity.setObjectName(u"stock_c_debt_to_equity")
        self.stock_c_debt_to_equity.setEnabled(False)
        self.stock_c_debt_to_equity.setStyleSheet(u"color: white;  /* Text color */")

        self.stock_c_debt_management_vertical_layout.addWidget(self.stock_c_debt_to_equity)

        self.stock_c_debt_to_ebitda = QLabel(self.layoutWidget_5)
        self.stock_c_debt_to_ebitda.setObjectName(u"stock_c_debt_to_ebitda")
        self.stock_c_debt_to_ebitda.setEnabled(False)
        self.stock_c_debt_to_ebitda.setStyleSheet(u"color: white;  /* Text color */")

        self.stock_c_debt_management_vertical_layout.addWidget(self.stock_c_debt_to_ebitda)

        self.stock_c_interest_coverage = QLabel(self.layoutWidget_5)
        self.stock_c_interest_coverage.setObjectName(u"stock_c_interest_coverage")
        self.stock_c_interest_coverage.setEnabled(False)
        self.stock_c_interest_coverage.setStyleSheet(u"color: white;  /* Text color */")

        self.stock_c_debt_management_vertical_layout.addWidget(self.stock_c_interest_coverage)

        self.stock_c_current_ratio = QLabel(self.layoutWidget_5)
        self.stock_c_current_ratio.setObjectName(u"stock_c_current_ratio")
        self.stock_c_current_ratio.setEnabled(False)
        self.stock_c_current_ratio.setStyleSheet(u"color: white;  /* Text color */")

        self.stock_c_debt_management_vertical_layout.addWidget(self.stock_c_current_ratio)

        self.layoutWidget_8 = QWidget(self.stock_c_frame)
        self.layoutWidget_8.setObjectName(u"layoutWidget_8")
        self.layoutWidget_8.setGeometry(QRect(170, 60, 101, 221))
        self.stock_c_efficiency_vertical_layout = QVBoxLayout(self.layoutWidget_8)
        self.stock_c_efficiency_vertical_layout.setSpacing(0)
        self.stock_c_efficiency_vertical_layout.setObjectName(u"stock_c_efficiency_vertical_layout")
        self.stock_c_efficiency_vertical_layout.setContentsMargins(0, 0, 0, 0)
        self.stock_c_roa = QLabel(self.layoutWidget_8)
        self.stock_c_roa.setObjectName(u"stock_c_roa")
        self.stock_c_roa.setEnabled(False)
        self.stock_c_roa.setStyleSheet(u"color: white;  /* Text color */")

        self.stock_c_efficiency_vertical_layout.addWidget(self.stock_c_roa)

        self.stock_c_roe = QLabel(self.layoutWidget_8)
        self.stock_c_roe.setObjectName(u"stock_c_roe")
        self.stock_c_roe.setEnabled(False)
        self.stock_c_roe.setStyleSheet(u"color: white;  /* Text color */")

        self.stock_c_efficiency_vertical_layout.addWidget(self.stock_c_roe)

        self.stock_c_roic = QLabel(self.layoutWidget_8)
        self.stock_c_roic.setObjectName(u"stock_c_roic")
        self.stock_c_roic.setEnabled(False)
        self.stock_c_roic.setStyleSheet(u"color: white;  /* Text color */")

        self.stock_c_efficiency_vertical_layout.addWidget(self.stock_c_roic)

        self.layoutWidget_12 = QWidget(self.stock_c_frame)
        self.layoutWidget_12.setObjectName(u"layoutWidget_12")
        self.layoutWidget_12.setGeometry(QRect(290, 60, 81, 221))
        self.stock_c_price_estimates_vertical_layout = QVBoxLayout(self.layoutWidget_12)
        self.stock_c_price_estimates_vertical_layout.setSpacing(0)
        self.stock_c_price_estimates_vertical_layout.setObjectName(u"stock_c_price_estimates_vertical_layout")
        self.stock_c_price_estimates_vertical_layout.setContentsMargins(0, 0, 0, 0)
        self.stock_c_pe = QLabel(self.layoutWidget_12)
        self.stock_c_pe.setObjectName(u"stock_c_pe")
        self.stock_c_pe.setEnabled(False)
        self.stock_c_pe.setStyleSheet(u"color: white;  /* Text color */")

        self.stock_c_price_estimates_vertical_layout.addWidget(self.stock_c_pe)

        self.stock_c_peg = QLabel(self.layoutWidget_12)
        self.stock_c_peg.setObjectName(u"stock_c_peg")
        self.stock_c_peg.setEnabled(False)
        self.stock_c_peg.setStyleSheet(u"color: white;  /* Text color */")

        self.stock_c_price_estimates_vertical_layout.addWidget(self.stock_c_peg)

        self.stock_c_ps = QLabel(self.layoutWidget_12)
        self.stock_c_ps.setObjectName(u"stock_c_ps")
        self.stock_c_ps.setEnabled(False)
        self.stock_c_ps.setStyleSheet(u"color: white;  /* Text color */")

        self.stock_c_price_estimates_vertical_layout.addWidget(self.stock_c_ps)

        self.stock_c_pb = QLabel(self.layoutWidget_12)
        self.stock_c_pb.setObjectName(u"stock_c_pb")
        self.stock_c_pb.setEnabled(False)
        self.stock_c_pb.setStyleSheet(u"color: white;  /* Text color */")

        self.stock_c_price_estimates_vertical_layout.addWidget(self.stock_c_pb)

        self.stock_c_pfcf = QLabel(self.layoutWidget_12)
        self.stock_c_pfcf.setObjectName(u"stock_c_pfcf")
        self.stock_c_pfcf.setEnabled(False)
        self.stock_c_pfcf.setStyleSheet(u"color: white;  /* Text color */")

        self.stock_c_price_estimates_vertical_layout.addWidget(self.stock_c_pfcf)

        self.stock_b_frame = QFrame(self.stock_comparison_tab)
        self.stock_b_frame.setObjectName(u"stock_b_frame")
        self.stock_b_frame.setGeometry(QRect(410, 0, 381, 271))
        self.stock_b_frame.setStyleSheet(u"background: black;")
        self.stock_b_frame.setFrameShape(QFrame.Shape.StyledPanel)
        self.stock_b_frame.setFrameShadow(QFrame.Shadow.Raised)
        self.layoutWidget_2 = QWidget(self.stock_b_frame)
        self.layoutWidget_2.setObjectName(u"layoutWidget_2")
        self.layoutWidget_2.setGeometry(QRect(0, 0, 216, 26))
        self.stock_b_horizontal_layout = QHBoxLayout(self.layoutWidget_2)
        self.stock_b_horizontal_layout.setObjectName(u"stock_b_horizontal_layout")
        self.stock_b_horizontal_layout.setContentsMargins(0, 0, 0, 0)
        self.stock_search_b_bar = QLineEdit(self.layoutWidget_2)
        self.stock_search_b_bar.setObjectName(u"stock_search_b_bar")
        self.stock_search_b_bar.setStyleSheet(u"color: white;")

        self.stock_b_horizontal_layout.addWidget(self.stock_search_b_bar)

        self.stock_search_b_button = QPushButton(self.layoutWidget_2)
        self.stock_search_b_button.setObjectName(u"stock_search_b_button")
        self.stock_search_b_button.setStyleSheet(u"QPushButton {\n"
"    border: 2px solid black;         /* Default border */\n"
"    border-radius: 5px;              /* Rounded corners */\n"
"    background-color: lightgray;     /* Default background color */\n"
"}\n"
"QPushButton:pressed {\n"
"    border: 3px solid red;           /* Thicker border when clicked */\n"
"    background-color: lightblue;     /* Background color when pressed */\n"
"}\n"
"QPushButton:hover {\n"
"    border: 2px dashed blue;         /* Dashed border on hover */\n"
"    background-color: lightgreen;    /* Background color when hovered */\n"
"}\n"
"")

        self.stock_b_horizontal_layout.addWidget(self.stock_search_b_button)

        self.debt_management_b = QLabel(self.stock_b_frame)
        self.debt_management_b.setObjectName(u"debt_management_b")
        self.debt_management_b.setGeometry(QRect(0, 30, 99, 16))
        self.debt_management_b.setStyleSheet(u"color: white;  /* Text color */")
        self.stock_b_efficiency = QLabel(self.stock_b_frame)
        self.stock_b_efficiency.setObjectName(u"stock_b_efficiency")
        self.stock_b_efficiency.setGeometry(QRect(160, 30, 51, 16))
        self.stock_b_efficiency.setStyleSheet(u"color: white;  /* Text color */")
        self.stock_b_price_estimates = QLabel(self.stock_b_frame)
        self.stock_b_price_estimates.setObjectName(u"stock_b_price_estimates")
        self.stock_b_price_estimates.setGeometry(QRect(300, 30, 79, 16))
        self.stock_b_price_estimates.setStyleSheet(u"color: white;  /* Text color */")
        self.layoutWidget_7 = QWidget(self.stock_b_frame)
        self.layoutWidget_7.setObjectName(u"layoutWidget_7")
        self.layoutWidget_7.setGeometry(QRect(0, 50, 151, 221))
        self.stock_b_debt_management_vertical_layout = QVBoxLayout(self.layoutWidget_7)
        self.stock_b_debt_management_vertical_layout.setSpacing(0)
        self.stock_b_debt_management_vertical_layout.setObjectName(u"stock_b_debt_management_vertical_layout")
        self.stock_b_debt_management_vertical_layout.setContentsMargins(0, 0, 0, 0)
        self.stock_b_cash_to_debt = QLabel(self.layoutWidget_7)
        self.stock_b_cash_to_debt.setObjectName(u"stock_b_cash_to_debt")
        self.stock_b_cash_to_debt.setEnabled(False)
        self.stock_b_cash_to_debt.setStyleSheet(u"color: white;  /* Text color */")

        self.stock_b_debt_management_vertical_layout.addWidget(self.stock_b_cash_to_debt)

        self.stock_b_debt_to_equity = QLabel(self.layoutWidget_7)
        self.stock_b_debt_to_equity.setObjectName(u"stock_b_debt_to_equity")
        self.stock_b_debt_to_equity.setEnabled(False)
        self.stock_b_debt_to_equity.setStyleSheet(u"color: white;  /* Text color */")

        self.stock_b_debt_management_vertical_layout.addWidget(self.stock_b_debt_to_equity)

        self.stock_b_debt_to_ebitda = QLabel(self.layoutWidget_7)
        self.stock_b_debt_to_ebitda.setObjectName(u"stock_b_debt_to_ebitda")
        self.stock_b_debt_to_ebitda.setEnabled(False)
        self.stock_b_debt_to_ebitda.setStyleSheet(u"color: white;  /* Text color */")

        self.stock_b_debt_management_vertical_layout.addWidget(self.stock_b_debt_to_ebitda)

        self.stock_b_interest_coverage = QLabel(self.layoutWidget_7)
        self.stock_b_interest_coverage.setObjectName(u"stock_b_interest_coverage")
        self.stock_b_interest_coverage.setEnabled(False)
        self.stock_b_interest_coverage.setStyleSheet(u"color: white;  /* Text color */")

        self.stock_b_debt_management_vertical_layout.addWidget(self.stock_b_interest_coverage)

        self.stock_b_current_ratio = QLabel(self.layoutWidget_7)
        self.stock_b_current_ratio.setObjectName(u"stock_b_current_ratio")
        self.stock_b_current_ratio.setEnabled(False)
        self.stock_b_current_ratio.setStyleSheet(u"color: white;  /* Text color */")

        self.stock_b_debt_management_vertical_layout.addWidget(self.stock_b_current_ratio)

        self.layoutWidget_9 = QWidget(self.stock_b_frame)
        self.layoutWidget_9.setObjectName(u"layoutWidget_9")
        self.layoutWidget_9.setGeometry(QRect(170, 50, 111, 221))
        self.stock_b_efficiency_vertical_layout = QVBoxLayout(self.layoutWidget_9)
        self.stock_b_efficiency_vertical_layout.setSpacing(0)
        self.stock_b_efficiency_vertical_layout.setObjectName(u"stock_b_efficiency_vertical_layout")
        self.stock_b_efficiency_vertical_layout.setContentsMargins(0, 0, 0, 0)
        self.stock_b_roa = QLabel(self.layoutWidget_9)
        self.stock_b_roa.setObjectName(u"stock_b_roa")
        self.stock_b_roa.setEnabled(False)
        self.stock_b_roa.setStyleSheet(u"color: white;  /* Text color */")

        self.stock_b_efficiency_vertical_layout.addWidget(self.stock_b_roa)

        self.stock_b_roe = QLabel(self.layoutWidget_9)
        self.stock_b_roe.setObjectName(u"stock_b_roe")
        self.stock_b_roe.setEnabled(False)
        self.stock_b_roe.setStyleSheet(u"color: white;  /* Text color */")

        self.stock_b_efficiency_vertical_layout.addWidget(self.stock_b_roe)

        self.stock_b_roic = QLabel(self.layoutWidget_9)
        self.stock_b_roic.setObjectName(u"stock_b_roic")
        self.stock_b_roic.setEnabled(False)
        self.stock_b_roic.setStyleSheet(u"color: white;  /* Text color */")

        self.stock_b_efficiency_vertical_layout.addWidget(self.stock_b_roic)

        self.layoutWidget5 = QWidget(self.stock_b_frame)
        self.layoutWidget5.setObjectName(u"layoutWidget5")
        self.layoutWidget5.setGeometry(QRect(310, 45, 61, 221))
        self.stock_b_price_estimates_vertical_layout = QVBoxLayout(self.layoutWidget5)
        self.stock_b_price_estimates_vertical_layout.setSpacing(0)
        self.stock_b_price_estimates_vertical_layout.setObjectName(u"stock_b_price_estimates_vertical_layout")
        self.stock_b_price_estimates_vertical_layout.setContentsMargins(0, 0, 0, 0)
        self.stock_b_pe = QLabel(self.layoutWidget5)
        self.stock_b_pe.setObjectName(u"stock_b_pe")
        self.stock_b_pe.setEnabled(False)
        self.stock_b_pe.setStyleSheet(u"color: white;  /* Text color */")

        self.stock_b_price_estimates_vertical_layout.addWidget(self.stock_b_pe)

        self.stock_b_peg = QLabel(self.layoutWidget5)
        self.stock_b_peg.setObjectName(u"stock_b_peg")
        self.stock_b_peg.setEnabled(False)
        self.stock_b_peg.setStyleSheet(u"color: white;  /* Text color */")

        self.stock_b_price_estimates_vertical_layout.addWidget(self.stock_b_peg)

        self.stock_b_ps = QLabel(self.layoutWidget5)
        self.stock_b_ps.setObjectName(u"stock_b_ps")
        self.stock_b_ps.setEnabled(False)
        self.stock_b_ps.setStyleSheet(u"color: white;  /* Text color */")

        self.stock_b_price_estimates_vertical_layout.addWidget(self.stock_b_ps)

        self.stock_b_pb = QLabel(self.layoutWidget5)
        self.stock_b_pb.setObjectName(u"stock_b_pb")
        self.stock_b_pb.setEnabled(False)
        self.stock_b_pb.setStyleSheet(u"color: white;  /* Text color */")

        self.stock_b_price_estimates_vertical_layout.addWidget(self.stock_b_pb)

        self.stock_b_pfcf = QLabel(self.layoutWidget5)
        self.stock_b_pfcf.setObjectName(u"stock_b_pfcf")
        self.stock_b_pfcf.setEnabled(False)
        self.stock_b_pfcf.setStyleSheet(u"color: white;  /* Text color */")

        self.stock_b_price_estimates_vertical_layout.addWidget(self.stock_b_pfcf)

        self.stock_d_frame = QFrame(self.stock_comparison_tab)
        self.stock_d_frame.setObjectName(u"stock_d_frame")
        self.stock_d_frame.setGeometry(QRect(410, 290, 381, 281))
        self.stock_d_frame.setStyleSheet(u"background: black;")
        self.stock_d_frame.setFrameShape(QFrame.Shape.StyledPanel)
        self.stock_d_frame.setFrameShadow(QFrame.Shadow.Raised)
        self.layoutWidget_4 = QWidget(self.stock_d_frame)
        self.layoutWidget_4.setObjectName(u"layoutWidget_4")
        self.layoutWidget_4.setGeometry(QRect(0, 0, 216, 26))
        self.stock_d_horizontal_layout = QHBoxLayout(self.layoutWidget_4)
        self.stock_d_horizontal_layout.setSpacing(0)
        self.stock_d_horizontal_layout.setObjectName(u"stock_d_horizontal_layout")
        self.stock_d_horizontal_layout.setContentsMargins(0, 0, 0, 0)
        self.stock_search_d_bar = QLineEdit(self.layoutWidget_4)
        self.stock_search_d_bar.setObjectName(u"stock_search_d_bar")
        self.stock_search_d_bar.setStyleSheet(u"color: white;")

        self.stock_d_horizontal_layout.addWidget(self.stock_search_d_bar)

        self.stock_search_d_button = QPushButton(self.layoutWidget_4)
        self.stock_search_d_button.setObjectName(u"stock_search_d_button")
        self.stock_search_d_button.setStyleSheet(u"QPushButton {\n"
"    border: 2px solid black;         /* Default border */\n"
"    border-radius: 5px;              /* Rounded corners */\n"
"    background-color: lightgray;     /* Default background color */\n"
"}\n"
"QPushButton:pressed {\n"
"    border: 3px solid red;           /* Thicker border when clicked */\n"
"    background-color: lightblue;     /* Background color when pressed */\n"
"}\n"
"QPushButton:hover {\n"
"    border: 2px dashed blue;         /* Dashed border on hover */\n"
"    background-color: lightgreen;    /* Background color when hovered */\n"
"}\n"
"")

        self.stock_d_horizontal_layout.addWidget(self.stock_search_d_button)

        self.debt_management_d = QLabel(self.stock_d_frame)
        self.debt_management_d.setObjectName(u"debt_management_d")
        self.debt_management_d.setGeometry(QRect(0, 30, 99, 16))
        self.debt_management_d.setStyleSheet(u"color: white;  /* Text color */")
        self.stock_d_efficiency = QLabel(self.stock_d_frame)
        self.stock_d_efficiency.setObjectName(u"stock_d_efficiency")
        self.stock_d_efficiency.setGeometry(QRect(160, 30, 51, 16))
        self.stock_d_efficiency.setStyleSheet(u"color: white;  /* Text color */")
        self.stock_d_price_estimates = QLabel(self.stock_d_frame)
        self.stock_d_price_estimates.setObjectName(u"stock_d_price_estimates")
        self.stock_d_price_estimates.setGeometry(QRect(299, 30, 79, 16))
        self.stock_d_price_estimates.setStyleSheet(u"color: white;  /* Text color */")
        self.layoutWidget_6 = QWidget(self.stock_d_frame)
        self.layoutWidget_6.setObjectName(u"layoutWidget_6")
        self.layoutWidget_6.setGeometry(QRect(0, 50, 151, 231))
        self.stock_d_debt_management_vertical_layout = QVBoxLayout(self.layoutWidget_6)
        self.stock_d_debt_management_vertical_layout.setSpacing(0)
        self.stock_d_debt_management_vertical_layout.setObjectName(u"stock_d_debt_management_vertical_layout")
        self.stock_d_debt_management_vertical_layout.setContentsMargins(0, 0, 0, 0)
        self.stock_d_cash_to_debt = QLabel(self.layoutWidget_6)
        self.stock_d_cash_to_debt.setObjectName(u"stock_d_cash_to_debt")
        self.stock_d_cash_to_debt.setEnabled(False)
        self.stock_d_cash_to_debt.setStyleSheet(u"color: white;  /* Text color */")

        self.stock_d_debt_management_vertical_layout.addWidget(self.stock_d_cash_to_debt)

        self.stock_d_debt_to_equity = QLabel(self.layoutWidget_6)
        self.stock_d_debt_to_equity.setObjectName(u"stock_d_debt_to_equity")
        self.stock_d_debt_to_equity.setEnabled(False)
        self.stock_d_debt_to_equity.setStyleSheet(u"color: white;  /* Text color */")

        self.stock_d_debt_management_vertical_layout.addWidget(self.stock_d_debt_to_equity)

        self.stock_d_debt_to_ebitda = QLabel(self.layoutWidget_6)
        self.stock_d_debt_to_ebitda.setObjectName(u"stock_d_debt_to_ebitda")
        self.stock_d_debt_to_ebitda.setEnabled(False)
        self.stock_d_debt_to_ebitda.setStyleSheet(u"color: white;  /* Text color */")

        self.stock_d_debt_management_vertical_layout.addWidget(self.stock_d_debt_to_ebitda)

        self.stock_d_interest_coverage = QLabel(self.layoutWidget_6)
        self.stock_d_interest_coverage.setObjectName(u"stock_d_interest_coverage")
        self.stock_d_interest_coverage.setEnabled(False)
        self.stock_d_interest_coverage.setStyleSheet(u"color: white;  /* Text color */")

        self.stock_d_debt_management_vertical_layout.addWidget(self.stock_d_interest_coverage)

        self.stock_d_current_ratio = QLabel(self.layoutWidget_6)
        self.stock_d_current_ratio.setObjectName(u"stock_d_current_ratio")
        self.stock_d_current_ratio.setEnabled(False)
        self.stock_d_current_ratio.setStyleSheet(u"color: white;  /* Text color */")

        self.stock_d_debt_management_vertical_layout.addWidget(self.stock_d_current_ratio)

        self.layoutWidget_10 = QWidget(self.stock_d_frame)
        self.layoutWidget_10.setObjectName(u"layoutWidget_10")
        self.layoutWidget_10.setGeometry(QRect(170, 60, 101, 221))
        self.stock_d_efficiency_vertical_layout = QVBoxLayout(self.layoutWidget_10)
        self.stock_d_efficiency_vertical_layout.setSpacing(0)
        self.stock_d_efficiency_vertical_layout.setObjectName(u"stock_d_efficiency_vertical_layout")
        self.stock_d_efficiency_vertical_layout.setContentsMargins(0, 0, 0, 0)
        self.stock_d_roa = QLabel(self.layoutWidget_10)
        self.stock_d_roa.setObjectName(u"stock_d_roa")
        self.stock_d_roa.setEnabled(False)
        self.stock_d_roa.setStyleSheet(u"color: white;  /* Text color */")

        self.stock_d_efficiency_vertical_layout.addWidget(self.stock_d_roa)

        self.stock_d_roe = QLabel(self.layoutWidget_10)
        self.stock_d_roe.setObjectName(u"stock_d_roe")
        self.stock_d_roe.setEnabled(False)
        self.stock_d_roe.setStyleSheet(u"color: white;  /* Text color */")

        self.stock_d_efficiency_vertical_layout.addWidget(self.stock_d_roe)

        self.stock_d_roic = QLabel(self.layoutWidget_10)
        self.stock_d_roic.setObjectName(u"stock_d_roic")
        self.stock_d_roic.setEnabled(False)
        self.stock_d_roic.setStyleSheet(u"color: white;  /* Text color */")

        self.stock_d_efficiency_vertical_layout.addWidget(self.stock_d_roic)

        self.layoutWidget_13 = QWidget(self.stock_d_frame)
        self.layoutWidget_13.setObjectName(u"layoutWidget_13")
        self.layoutWidget_13.setGeometry(QRect(300, 60, 71, 221))
        self.stock_d_price_estimates_vertical_layout = QVBoxLayout(self.layoutWidget_13)
        self.stock_d_price_estimates_vertical_layout.setSpacing(0)
        self.stock_d_price_estimates_vertical_layout.setObjectName(u"stock_d_price_estimates_vertical_layout")
        self.stock_d_price_estimates_vertical_layout.setContentsMargins(0, 0, 0, 0)
        self.stock_d_pe = QLabel(self.layoutWidget_13)
        self.stock_d_pe.setObjectName(u"stock_d_pe")
        self.stock_d_pe.setEnabled(False)
        self.stock_d_pe.setStyleSheet(u"color: white;  /* Text color */")

        self.stock_d_price_estimates_vertical_layout.addWidget(self.stock_d_pe)

        self.stock_d_peg = QLabel(self.layoutWidget_13)
        self.stock_d_peg.setObjectName(u"stock_d_peg")
        self.stock_d_peg.setEnabled(False)
        self.stock_d_peg.setStyleSheet(u"color: white;  /* Text color */")

        self.stock_d_price_estimates_vertical_layout.addWidget(self.stock_d_peg)

        self.stock_d_ps = QLabel(self.layoutWidget_13)
        self.stock_d_ps.setObjectName(u"stock_d_ps")
        self.stock_d_ps.setEnabled(False)
        self.stock_d_ps.setStyleSheet(u"color: white;  /* Text color */")

        self.stock_d_price_estimates_vertical_layout.addWidget(self.stock_d_ps)

        self.stock_d_pb = QLabel(self.layoutWidget_13)
        self.stock_d_pb.setObjectName(u"stock_d_pb")
        self.stock_d_pb.setEnabled(False)
        self.stock_d_pb.setStyleSheet(u"color: white;  /* Text color */")

        self.stock_d_price_estimates_vertical_layout.addWidget(self.stock_d_pb)

        self.stock_d_pfcf = QLabel(self.layoutWidget_13)
        self.stock_d_pfcf.setObjectName(u"stock_d_pfcf")
        self.stock_d_pfcf.setEnabled(False)
        self.stock_d_pfcf.setStyleSheet(u"color: white;  /* Text color */")

        self.stock_d_price_estimates_vertical_layout.addWidget(self.stock_d_pfcf)

        self.tabs_widget.addTab(self.stock_comparison_tab, "")
        self.educational_tab = QWidget()
        self.educational_tab.setObjectName(u"educational_tab")
        self.debt_management_label = QLabel(self.educational_tab)
        self.debt_management_label.setObjectName(u"debt_management_label")
        self.debt_management_label.setGeometry(QRect(290, 10, 111, 16))
        self.debt_management_label.setStyleSheet(u"color: white;")
        self.de_label = QLabel(self.educational_tab)
        self.de_label.setObjectName(u"de_label")
        self.de_label.setGeometry(QRect(10, 40, 171, 16))
        self.de_label.setStyleSheet(u"color: white;")
        self.de_label.setOpenExternalLinks(False)
        self.d_eb_label = QLabel(self.educational_tab)
        self.d_eb_label.setObjectName(u"d_eb_label")
        self.d_eb_label.setGeometry(QRect(10, 60, 161, 16))
        self.d_eb_label.setStyleSheet(u"color: white;")
        self.cr_label = QLabel(self.educational_tab)
        self.cr_label.setObjectName(u"cr_label")
        self.cr_label.setGeometry(QRect(10, 100, 171, 16))
        self.cr_label.setStyleSheet(u"color: white;")
        self.ctdr_label = QLabel(self.educational_tab)
        self.ctdr_label.setObjectName(u"ctdr_label")
        self.ctdr_label.setGeometry(QRect(10, 120, 201, 16))
        self.ctdr_label.setStyleSheet(u"color: white;")
        self.effectiveness_label = QLabel(self.educational_tab)
        self.effectiveness_label.setObjectName(u"effectiveness_label")
        self.effectiveness_label.setGeometry(QRect(290, 150, 71, 16))
        self.effectiveness_label.setStyleSheet(u"color: white;")
        self.roic_label = QLabel(self.educational_tab)
        self.roic_label.setObjectName(u"roic_label")
        self.roic_label.setGeometry(QRect(10, 180, 141, 16))
        self.roic_label.setStyleSheet(u"color: white;")
        self.profit_margins_label = QLabel(self.educational_tab)
        self.profit_margins_label.setObjectName(u"profit_margins_label")
        self.profit_margins_label.setGeometry(QRect(10, 200, 81, 16))
        self.profit_margins_label.setStyleSheet(u"color: white;")
        self.roe_label = QLabel(self.educational_tab)
        self.roe_label.setObjectName(u"roe_label")
        self.roe_label.setGeometry(QRect(10, 220, 131, 16))
        self.roe_label.setStyleSheet(u"color: white;")
        self.roa_label = QLabel(self.educational_tab)
        self.roa_label.setObjectName(u"roa_label")
        self.roa_label.setGeometry(QRect(10, 240, 131, 16))
        self.roa_label.setStyleSheet(u"color: white;")
        self.net_assets_label = QLabel(self.educational_tab)
        self.net_assets_label.setObjectName(u"net_assets_label")
        self.net_assets_label.setGeometry(QRect(10, 260, 151, 16))
        self.net_assets_label.setStyleSheet(u"color: white;")
        self.price_estimates_label = QLabel(self.educational_tab)
        self.price_estimates_label.setObjectName(u"price_estimates_label")
        self.price_estimates_label.setGeometry(QRect(290, 290, 81, 16))
        self.price_estimates_label.setStyleSheet(u"color: white;")
        self.pe_label = QLabel(self.educational_tab)
        self.pe_label.setObjectName(u"pe_label")
        self.pe_label.setGeometry(QRect(10, 320, 191, 16))
        self.pe_label.setStyleSheet(u"color: white;")
        self.pe_label_2 = QLabel(self.educational_tab)
        self.pe_label_2.setObjectName(u"pe_label_2")
        self.pe_label_2.setGeometry(QRect(10, 340, 271, 16))
        self.pe_label_2.setStyleSheet(u"color: white;")
        self.pe_label_3 = QLabel(self.educational_tab)
        self.pe_label_3.setObjectName(u"pe_label_3")
        self.pe_label_3.setGeometry(QRect(10, 360, 281, 16))
        self.pe_label_3.setStyleSheet(u"color: white;")
        self.icr_label = QLabel(self.educational_tab)
        self.icr_label.setObjectName(u"icr_label")
        self.icr_label.setGeometry(QRect(10, 80, 221, 16))
        self.icr_label.setStyleSheet(u"color: white;")
        self.p_fcf_label = QLabel(self.educational_tab)
        self.p_fcf_label.setObjectName(u"p_fcf_label")
        self.p_fcf_label.setGeometry(QRect(10, 390, 171, 16))
        self.p_fcf_label.setStyleSheet(u"color: white;")
        self.peg_label = QLabel(self.educational_tab)
        self.peg_label.setObjectName(u"peg_label")
        self.peg_label.setGeometry(QRect(10, 410, 151, 16))
        self.peg_label.setStyleSheet(u"color: white;")
        self.ps_label = QLabel(self.educational_tab)
        self.ps_label.setObjectName(u"ps_label")
        self.ps_label.setGeometry(QRect(10, 430, 141, 16))
        self.ps_label.setStyleSheet(u"color: white;")
        self.pb_label = QLabel(self.educational_tab)
        self.pb_label.setObjectName(u"pb_label")
        self.pb_label.setGeometry(QRect(10, 450, 151, 16))
        self.pb_label.setStyleSheet(u"color: white;")
        self.tabs_widget.addTab(self.educational_tab, "")
        self.chat_bot_tab = QWidget()
        self.chat_bot_tab.setObjectName(u"chat_bot_tab")
        self.text_browser = QTextBrowser(self.chat_bot_tab)
        self.text_browser.setObjectName(u"text_browser")
        self.text_browser.setGeometry(QRect(10, 10, 771, 471))
        self.text_browser.setStyleSheet(u"background: black;\n"
"color: white;")
        self.chat_bot_search_button = QPushButton(self.chat_bot_tab)
        self.chat_bot_search_button.setObjectName(u"chat_bot_search_button")
        self.chat_bot_search_button.setGeometry(QRect(560, 490, 75, 71))
        self.chat_bot_search_button.setStyleSheet(u"background: transparent;\n"
"color:white;")
        self.chat_bot_text_edit = QTextEdit(self.chat_bot_tab)
        self.chat_bot_text_edit.setObjectName(u"chat_bot_text_edit")
        self.chat_bot_text_edit.setGeometry(QRect(150, 490, 411, 71))
        self.chat_bot_text_edit.setStyleSheet(u"background: white;")
        self.chat_bot_settings = QGroupBox(self.chat_bot_tab)
        self.chat_bot_settings.setObjectName(u"chat_bot_settings")
        self.chat_bot_settings.setGeometry(QRect(640, 489, 151, 81))
        self.chat_bot_settings.setStyleSheet(u"background:transparent;")
        self.gemini_flash_button = QRadioButton(self.chat_bot_settings)
        self.gemini_flash_button.setObjectName(u"gemini_flash_button")
        self.gemini_flash_button.setGeometry(QRect(10, 10, 111, 20))
        self.gemini_flash_button.setStyleSheet(u"color:white;")
        self.gemini_pro_button = QRadioButton(self.chat_bot_settings)
        self.gemini_pro_button.setObjectName(u"gemini_pro_button")
        self.gemini_pro_button.setGeometry(QRect(10, 30, 101, 20))
        self.gemini_pro_button.setStyleSheet(u"color:white;\n"
"")
        self.gpt_4o_mini_button = QRadioButton(self.chat_bot_settings)
        self.gpt_4o_mini_button.setObjectName(u"gpt_4o_mini_button")
        self.gpt_4o_mini_button.setGeometry(QRect(10, 50, 89, 20))
        self.gpt_4o_mini_button.setStyleSheet(u"color:white;")
        self.tabs_widget.addTab(self.chat_bot_tab, "")
        self.stock_search_settings = QWidget()
        self.stock_search_settings.setObjectName(u"stock_search_settings")
        self.layoutWidget6 = QWidget(self.stock_search_settings)
        self.layoutWidget6.setObjectName(u"layoutWidget6")
        self.layoutWidget6.setGeometry(QRect(0, 0, 151, 164))
        self.stock_search_settings_vertical_layout = QVBoxLayout(self.layoutWidget6)
        self.stock_search_settings_vertical_layout.setObjectName(u"stock_search_settings_vertical_layout")
        self.stock_search_settings_vertical_layout.setContentsMargins(0, 0, 0, 0)
        self.analytics_check_box = QCheckBox(self.layoutWidget6)
        self.analytics_check_box.setObjectName(u"analytics_check_box")
        self.analytics_check_box.setStyleSheet(u"color: white; ")

        self.stock_search_settings_vertical_layout.addWidget(self.analytics_check_box)

        self.alpha_spread_check_box = QCheckBox(self.layoutWidget6)
        self.alpha_spread_check_box.setObjectName(u"alpha_spread_check_box")
        self.alpha_spread_check_box.setStyleSheet(u"color: white; ")

        self.stock_search_settings_vertical_layout.addWidget(self.alpha_spread_check_box)

        self.focus_guru_check_box = QCheckBox(self.layoutWidget6)
        self.focus_guru_check_box.setObjectName(u"focus_guru_check_box")
        self.focus_guru_check_box.setStyleSheet(u"color: white; ")

        self.stock_search_settings_vertical_layout.addWidget(self.focus_guru_check_box)

        self.macro_trends_check_box = QCheckBox(self.layoutWidget6)
        self.macro_trends_check_box.setObjectName(u"macro_trends_check_box")
        self.macro_trends_check_box.setStyleSheet(u"color: white; ")

        self.stock_search_settings_vertical_layout.addWidget(self.macro_trends_check_box)

        self.finance_charts_check_box = QCheckBox(self.layoutWidget6)
        self.finance_charts_check_box.setObjectName(u"finance_charts_check_box")
        self.finance_charts_check_box.setStyleSheet(u"color: white; ")

        self.stock_search_settings_vertical_layout.addWidget(self.finance_charts_check_box)

        self.companies_market_cap_check_box = QCheckBox(self.layoutWidget6)
        self.companies_market_cap_check_box.setObjectName(u"companies_market_cap_check_box")
        self.companies_market_cap_check_box.setStyleSheet(u"color: white; ")

        self.stock_search_settings_vertical_layout.addWidget(self.companies_market_cap_check_box)

        self.tabs_widget.addTab(self.stock_search_settings, "")

        self.retranslateUi(stock_app)

        self.tabs_widget.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(stock_app)
    # setupUi

    def retranslateUi(self, stock_app):
        stock_app.setWindowTitle(QCoreApplication.translate("stock_app", u"Widget", None))
#if QT_CONFIG(accessibility)
        self.tabs_widget.setAccessibleName(QCoreApplication.translate("stock_app", u"app_tabs_widget", None))
#endif // QT_CONFIG(accessibility)
#if QT_CONFIG(accessibility)
        self.stock_manual_search_tab.setAccessibleName(QCoreApplication.translate("stock_app", u"manual_search_tab_widget", None))
#endif // QT_CONFIG(accessibility)
        self.stock_search_manual_button.setText(QCoreApplication.translate("stock_app", u"Search", None))
        self.tabs_widget.setTabText(self.tabs_widget.indexOf(self.stock_manual_search_tab), QCoreApplication.translate("stock_app", u"Stock Search", None))
#if QT_CONFIG(accessibility)
        self.stock_auto_search_tab.setAccessibleName(QCoreApplication.translate("stock_app", u"auto_search_tab_widget", None))
#endif // QT_CONFIG(accessibility)
        self.stock_search_automation_button.setText(QCoreApplication.translate("stock_app", u"Search", None))
        self.tabs_widget.setTabText(self.tabs_widget.indexOf(self.stock_auto_search_tab), QCoreApplication.translate("stock_app", u"Auto Stock Search", None))
#if QT_CONFIG(accessibility)
        self.stock_comparison_tab.setAccessibleName(QCoreApplication.translate("stock_app", u"comparison_search_tab_widget", None))
#endif // QT_CONFIG(accessibility)
#if QT_CONFIG(accessibility)
        self.stock_a_frame.setAccessibleName(QCoreApplication.translate("stock_app", u"stock_a_frame_widget", None))
#endif // QT_CONFIG(accessibility)
        self.debt_management_a.setText(QCoreApplication.translate("stock_app", u"Debt Management", None))
        self.stock_search_a_button.setText(QCoreApplication.translate("stock_app", u"Compare", None))
        self.stock_a_efficiency.setText(QCoreApplication.translate("stock_app", u"Efficiency", None))
        self.stock_a_price_estimates.setText(QCoreApplication.translate("stock_app", u"Price Estimates", None))
        self.stock_a_pe.setText(QCoreApplication.translate("stock_app", u"P/E", None))
        self.stock_a_peg.setText(QCoreApplication.translate("stock_app", u"PEG", None))
        self.stock_a_ps.setText(QCoreApplication.translate("stock_app", u"P/S", None))
        self.stock_a_pb.setText(QCoreApplication.translate("stock_app", u"P/B", None))
        self.stock_a_pfcf.setText(QCoreApplication.translate("stock_app", u"P/FCF", None))
        self.stock_a_cash_to_debt.setText(QCoreApplication.translate("stock_app", u"Cash to Debt", None))
        self.stock_a_debt_to_equity.setText(QCoreApplication.translate("stock_app", u"D/Equity Ratio", None))
#if QT_CONFIG(accessibility)
        self.stock_a_debt_to_ebitda.setAccessibleName("")
#endif // QT_CONFIG(accessibility)
        self.stock_a_debt_to_ebitda.setText(QCoreApplication.translate("stock_app", u"D/EBITDA", None))
        self.stock_a_interest_coverage.setText(QCoreApplication.translate("stock_app", u"Interest Coverage", None))
        self.stock_a_current_ratio.setText(QCoreApplication.translate("stock_app", u"Current", None))
        self.stock_a_roa.setText(QCoreApplication.translate("stock_app", u"ROA", None))
        self.stock_a_roe.setText(QCoreApplication.translate("stock_app", u"ROE", None))
        self.stock_a_roic.setText(QCoreApplication.translate("stock_app", u"ROIC", None))
#if QT_CONFIG(accessibility)
        self.stock_c_frame.setAccessibleName(QCoreApplication.translate("stock_app", u"stock_c_frame_widget", None))
#endif // QT_CONFIG(accessibility)
        self.stock_search_c_button.setText(QCoreApplication.translate("stock_app", u"Compare", None))
        self.debt_management_c.setText(QCoreApplication.translate("stock_app", u"Debt Management", None))
        self.stock_c_efficiency.setText(QCoreApplication.translate("stock_app", u"Efficiency", None))
        self.stock_c_price_estimates.setText(QCoreApplication.translate("stock_app", u"Price Estimates", None))
        self.stock_c_cash_to_debt.setText(QCoreApplication.translate("stock_app", u"Cash to Debt", None))
        self.stock_c_debt_to_equity.setText(QCoreApplication.translate("stock_app", u"D/Equity Ratio", None))
        self.stock_c_debt_to_ebitda.setText(QCoreApplication.translate("stock_app", u"D/EBITDA", None))
        self.stock_c_interest_coverage.setText(QCoreApplication.translate("stock_app", u"Interest Coverage", None))
        self.stock_c_current_ratio.setText(QCoreApplication.translate("stock_app", u"Current", None))
        self.stock_c_roa.setText(QCoreApplication.translate("stock_app", u"ROA", None))
        self.stock_c_roe.setText(QCoreApplication.translate("stock_app", u"ROE", None))
        self.stock_c_roic.setText(QCoreApplication.translate("stock_app", u"ROIC", None))
        self.stock_c_pe.setText(QCoreApplication.translate("stock_app", u"P/E", None))
        self.stock_c_peg.setText(QCoreApplication.translate("stock_app", u"PEG", None))
        self.stock_c_ps.setText(QCoreApplication.translate("stock_app", u"P/S", None))
        self.stock_c_pb.setText(QCoreApplication.translate("stock_app", u"P/B", None))
        self.stock_c_pfcf.setText(QCoreApplication.translate("stock_app", u"P/FCF", None))
#if QT_CONFIG(accessibility)
        self.stock_b_frame.setAccessibleName(QCoreApplication.translate("stock_app", u"stock_b_frame_widget", None))
#endif // QT_CONFIG(accessibility)
        self.stock_search_b_button.setText(QCoreApplication.translate("stock_app", u"Compare", None))
        self.debt_management_b.setText(QCoreApplication.translate("stock_app", u"Debt Management", None))
        self.stock_b_efficiency.setText(QCoreApplication.translate("stock_app", u"Efficiency", None))
        self.stock_b_price_estimates.setText(QCoreApplication.translate("stock_app", u"Price Estimates", None))
        self.stock_b_cash_to_debt.setText(QCoreApplication.translate("stock_app", u"Cash to Debt", None))
        self.stock_b_debt_to_equity.setText(QCoreApplication.translate("stock_app", u"D/Equity Ratio", None))
        self.stock_b_debt_to_ebitda.setText(QCoreApplication.translate("stock_app", u"D/EBITDA", None))
        self.stock_b_interest_coverage.setText(QCoreApplication.translate("stock_app", u"Interest Coverage", None))
        self.stock_b_current_ratio.setText(QCoreApplication.translate("stock_app", u"Current", None))
        self.stock_b_roa.setText(QCoreApplication.translate("stock_app", u"ROA", None))
        self.stock_b_roe.setText(QCoreApplication.translate("stock_app", u"ROE", None))
        self.stock_b_roic.setText(QCoreApplication.translate("stock_app", u"ROIC", None))
        self.stock_b_pe.setText(QCoreApplication.translate("stock_app", u"P/E", None))
        self.stock_b_peg.setText(QCoreApplication.translate("stock_app", u"PEG", None))
        self.stock_b_ps.setText(QCoreApplication.translate("stock_app", u"P/S", None))
        self.stock_b_pb.setText(QCoreApplication.translate("stock_app", u"P/B", None))
        self.stock_b_pfcf.setText(QCoreApplication.translate("stock_app", u"P/FCF", None))
#if QT_CONFIG(accessibility)
        self.stock_d_frame.setAccessibleName(QCoreApplication.translate("stock_app", u"stock_d_frame_widget", None))
#endif // QT_CONFIG(accessibility)
        self.stock_search_d_button.setText(QCoreApplication.translate("stock_app", u"Compare", None))
        self.debt_management_d.setText(QCoreApplication.translate("stock_app", u"Debt Management", None))
        self.stock_d_efficiency.setText(QCoreApplication.translate("stock_app", u"Efficiency", None))
        self.stock_d_price_estimates.setText(QCoreApplication.translate("stock_app", u"Price Estimates", None))
        self.stock_d_cash_to_debt.setText(QCoreApplication.translate("stock_app", u"Cash to Debt", None))
        self.stock_d_debt_to_equity.setText(QCoreApplication.translate("stock_app", u"D/Equity Ratio", None))
        self.stock_d_debt_to_ebitda.setText(QCoreApplication.translate("stock_app", u"D/EBITDA", None))
        self.stock_d_interest_coverage.setText(QCoreApplication.translate("stock_app", u"Interest Coverage", None))
        self.stock_d_current_ratio.setText(QCoreApplication.translate("stock_app", u"Current", None))
        self.stock_d_roa.setText(QCoreApplication.translate("stock_app", u"ROA", None))
        self.stock_d_roe.setText(QCoreApplication.translate("stock_app", u"ROE", None))
        self.stock_d_roic.setText(QCoreApplication.translate("stock_app", u"ROIC", None))
        self.stock_d_pe.setText(QCoreApplication.translate("stock_app", u"P/E", None))
        self.stock_d_peg.setText(QCoreApplication.translate("stock_app", u"PEG", None))
        self.stock_d_ps.setText(QCoreApplication.translate("stock_app", u"P/S", None))
        self.stock_d_pb.setText(QCoreApplication.translate("stock_app", u"P/B", None))
        self.stock_d_pfcf.setText(QCoreApplication.translate("stock_app", u"P/FCF", None))
        self.tabs_widget.setTabText(self.tabs_widget.indexOf(self.stock_comparison_tab), QCoreApplication.translate("stock_app", u"Stock Comparison", None))
#if QT_CONFIG(accessibility)
        self.educational_tab.setAccessibleName(QCoreApplication.translate("stock_app", u"educational_tab_widget", None))
#endif // QT_CONFIG(accessibility)
        self.debt_management_label.setText(QCoreApplication.translate("stock_app", u"Debt Management", None))
        self.de_label.setText(QCoreApplication.translate("stock_app", u"D/E Ratio : Optimal under 1/0.5", None))
        self.d_eb_label.setText(QCoreApplication.translate("stock_app", u"D/EBITDA : Optimal under 2.5", None))
        self.cr_label.setText(QCoreApplication.translate("stock_app", u"Current Ratio : Optimal over 1.0", None))
        self.ctdr_label.setText(QCoreApplication.translate("stock_app", u"Cash To Debt Ratio : Optimal over 0.20", None))
        self.effectiveness_label.setText(QCoreApplication.translate("stock_app", u"Effectiveness", None))
        self.roic_label.setText(QCoreApplication.translate("stock_app", u"ROIC : Optimal over 12 %", None))
        self.profit_margins_label.setText(QCoreApplication.translate("stock_app", u"Profit Margins", None))
        self.roe_label.setText(QCoreApplication.translate("stock_app", u"ROE : Optimal over 12 %", None))
        self.roa_label.setText(QCoreApplication.translate("stock_app", u"ROA : Optimal over 5 %", None))
        self.net_assets_label.setText(QCoreApplication.translate("stock_app", u"Net Assets long-term chart", None))
        self.price_estimates_label.setText(QCoreApplication.translate("stock_app", u"Price Estimates", None))
        self.pe_label.setText(QCoreApplication.translate("stock_app", u"P/E : 10/11 if Company Growth <= 0", None))
        self.pe_label_2.setText(QCoreApplication.translate("stock_app", u"P/E : 15/17 if Company Growth between 5 and 7 %", None))
        self.pe_label_3.setText(QCoreApplication.translate("stock_app", u"P/E : 20/25 if Company Growth between 10 and 12 %", None))
        self.icr_label.setText(QCoreApplication.translate("stock_app", u"Interest Coverage Ration : Optimal over 5", None))
        self.p_fcf_label.setText(QCoreApplication.translate("stock_app", u"P/FCF Ratio : Optimal under 25", None))
        self.peg_label.setText(QCoreApplication.translate("stock_app", u"PEG Ratio : Optimal under 1", None))
        self.ps_label.setText(QCoreApplication.translate("stock_app", u"P/S Ratio: Optimal under 2", None))
        self.pb_label.setText(QCoreApplication.translate("stock_app", u"P/B Ratio : Optimal under 3", None))
        self.tabs_widget.setTabText(self.tabs_widget.indexOf(self.educational_tab), QCoreApplication.translate("stock_app", u"Educational", None))
#if QT_CONFIG(accessibility)
        self.chat_bot_tab.setAccessibleName(QCoreApplication.translate("stock_app", u"chat_bot_widget", None))
#endif // QT_CONFIG(accessibility)
        self.chat_bot_search_button.setText(QCoreApplication.translate("stock_app", u"Search", None))
        self.chat_bot_settings.setTitle("")
        self.gemini_flash_button.setText(QCoreApplication.translate("stock_app", u"gemini-1.5-flash", None))
        self.gemini_pro_button.setText(QCoreApplication.translate("stock_app", u"gemini-1.5-pro", None))
        self.gpt_4o_mini_button.setText(QCoreApplication.translate("stock_app", u"gpt-4o-mini", None))
        self.tabs_widget.setTabText(self.tabs_widget.indexOf(self.chat_bot_tab), QCoreApplication.translate("stock_app", u"Chat Bot", None))
#if QT_CONFIG(accessibility)
        self.stock_search_settings.setAccessibleName(QCoreApplication.translate("stock_app", u"settings_search_tab_widget", None))
#endif // QT_CONFIG(accessibility)
        self.analytics_check_box.setText(QCoreApplication.translate("stock_app", u"Analytics Panel", None))
        self.alpha_spread_check_box.setText(QCoreApplication.translate("stock_app", u"Alpha Spread", None))
        self.focus_guru_check_box.setText(QCoreApplication.translate("stock_app", u"Focus Guru", None))
        self.macro_trends_check_box.setText(QCoreApplication.translate("stock_app", u"Macro Trends", None))
        self.finance_charts_check_box.setText(QCoreApplication.translate("stock_app", u"Finance Charts", None))
        self.companies_market_cap_check_box.setText(QCoreApplication.translate("stock_app", u"Companies Market Cap", None))
        self.tabs_widget.setTabText(self.tabs_widget.indexOf(self.stock_search_settings), QCoreApplication.translate("stock_app", u"Settings", None))
    # retranslateUi

