# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'osnova.ui'
##
## Created by: Qt User Interface Compiler version 6.6.2
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
from PySide6.QtWidgets import (QApplication, QCalendarWidget, QComboBox, QDateEdit,
    QFrame, QLabel, QListWidget, QListWidgetItem,
    QMainWindow, QPushButton, QSizePolicy, QStatusBar,
    QTabWidget, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(686, 703)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.tabWidget = QTabWidget(self.centralwidget)
        self.tabWidget.setObjectName(u"tabWidget")
        self.tabWidget.setGeometry(QRect(-10, 0, 681, 681))
        self.tab = QWidget()
        self.tab.setObjectName(u"tab")
        self.calendarWidget = QCalendarWidget(self.tab)
        self.calendarWidget.setObjectName(u"calendarWidget")
        self.calendarWidget.setGeometry(QRect(410, 40, 261, 191))
        self.label = QLabel(self.tab)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(200, 50, 81, 21))
        self.label.setMouseTracking(False)
        self.label.setFocusPolicy(Qt.NoFocus)
        self.label.setContextMenuPolicy(Qt.PreventContextMenu)
        self.label.setAcceptDrops(False)
        self.label.setFrameShape(QFrame.NoFrame)
        self.label.setFrameShadow(QFrame.Plain)
        self.label.setScaledContents(False)
        self.label.setOpenExternalLinks(False)
        self.btnSave = QPushButton(self.tab)
        self.btnSave.setObjectName(u"btnSave")
        self.btnSave.setGeometry(QRect(270, 590, 151, 61))
        self.dateEdit = QDateEdit(self.tab)
        self.dateEdit.setObjectName(u"dateEdit")
        self.dateEdit.setGeometry(QRect(290, 50, 101, 21))
        self.dateEdit.setDateTime(QDateTime(QDate(2023, 1, 1), QTime(0, 0, 0)))
        self.label_2 = QLabel(self.tab)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(30, 50, 171, 21))
        self.label_2.setMouseTracking(False)
        self.label_2.setFocusPolicy(Qt.NoFocus)
        self.label_2.setContextMenuPolicy(Qt.PreventContextMenu)
        self.label_2.setAcceptDrops(False)
        self.label_2.setFrameShape(QFrame.NoFrame)
        self.label_2.setFrameShadow(QFrame.Plain)
        self.label_2.setScaledContents(False)
        self.label_2.setOpenExternalLinks(False)
        self.btnAddCont = QPushButton(self.tab)
        self.btnAddCont.setObjectName(u"btnAddCont")
        self.btnAddCont.setGeometry(QRect(10, 590, 151, 61))
        self.label_3 = QLabel(self.tab)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setGeometry(QRect(30, 100, 91, 21))
        self.label_3.setMouseTracking(False)
        self.label_3.setFocusPolicy(Qt.NoFocus)
        self.label_3.setContextMenuPolicy(Qt.PreventContextMenu)
        self.label_3.setAcceptDrops(False)
        self.label_3.setFrameShape(QFrame.NoFrame)
        self.label_3.setFrameShadow(QFrame.Plain)
        self.label_3.setScaledContents(False)
        self.label_3.setOpenExternalLinks(False)
        self.comboBox = QComboBox(self.tab)
        self.comboBox.setObjectName(u"comboBox")
        self.comboBox.setGeometry(QRect(30, 80, 361, 22))
        self.btnEditCont = QPushButton(self.tab)
        self.btnEditCont.setObjectName(u"btnEditCont")
        self.btnEditCont.setGeometry(QRect(20, 150, 181, 61))
        self.btnDeletOsnova = QPushButton(self.tab)
        self.btnDeletOsnova.setObjectName(u"btnDeletOsnova")
        self.btnDeletOsnova.setGeometry(QRect(300, 200, 91, 41))
        font = QFont()
        font.setBold(False)
        font.setItalic(False)
        font.setUnderline(False)
        font.setStrikeOut(False)
        self.btnDeletOsnova.setFont(font)
        self.btnDeletOsnova.setMouseTracking(False)
        self.btnDeletOsnova.setTabletTracking(False)
        self.btnDeletOsnova.setStyleSheet(u"")
        self.listWidget_o = QListWidget(self.tab)
        self.listWidget_o.setObjectName(u"listWidget_o")
        self.listWidget_o.setGeometry(QRect(10, 250, 661, 331))
        self.btnClose = QPushButton(self.tab)
        self.btnClose.setObjectName(u"btnClose")
        self.btnClose.setGeometry(QRect(520, 590, 151, 61))
        self.tabWidget.addTab(self.tab, "")
        self.btnDeletOsnova.raise_()
        self.calendarWidget.raise_()
        self.label.raise_()
        self.btnSave.raise_()
        self.dateEdit.raise_()
        self.label_2.raise_()
        self.btnAddCont.raise_()
        self.label_3.raise_()
        self.comboBox.raise_()
        self.btnEditCont.raise_()
        self.listWidget_o.raise_()
        self.btnClose.raise_()
        self.tab_2 = QWidget()
        self.tab_2.setObjectName(u"tab_2")
        self.tabWidget.addTab(self.tab_2, "")
        self.tab_3 = QWidget()
        self.tab_3.setObjectName(u"tab_3")
        self.tabWidget.addTab(self.tab_3, "")
        self.tab_4 = QWidget()
        self.tab_4.setObjectName(u"tab_4")
        self.tabWidget.addTab(self.tab_4, "")
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)

        self.tabWidget.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.label.setText("")
        self.btnSave.setText(QCoreApplication.translate("MainWindow", u"\u0421\u043e\u0437\u0434\u0430\u0442\u044c \u0414\u043e\u043a\u0443\u043c\u0435\u043d\u0442", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"\u0414\u043e\u0433\u043e\u0432\u043e\u0440 \u043f\u043e\u0441\u0442\u0430\u0432\u043a\u0438 \u2116 \u0418\u041d_ ", None))
        self.btnAddCont.setText(QCoreApplication.translate("MainWindow", u"\u041d\u043e\u0432\u044b\u0439 \u043a\u043e\u043d\u0442\u0440\u0430\u0433\u0435\u043d\u0442", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"\u041a\u043e\u043d\u0442\u0440\u043e\u0430\u0433\u0435\u043d\u0442\u044b", None))
        self.btnEditCont.setText(QCoreApplication.translate("MainWindow", u"\u0418\u0437\u043c\u0435\u043d\u0438\u0442\u044c \u043a\u043e\u043d\u0442\u0440\u0430\u0433\u0435\u043d\u0442\u0430", None))
        self.btnDeletOsnova.setText(QCoreApplication.translate("MainWindow", u"\u0423\u0434\u0430\u043b\u0438\u0442\u044c", None))
        self.btnClose.setText(QCoreApplication.translate("MainWindow", u"\u0417\u0430\u043a\u0440\u044b\u0442\u044c", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), QCoreApplication.translate("MainWindow", u"\u0411\u041f\u041a \u0414\u043e\u0433\u043e\u0432\u043e\u0440\u0430", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), QCoreApplication.translate("MainWindow", u"\u0418\u041f  \u0414\u043e\u0433\u043e\u0432\u043e\u0440\u0430", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_3), QCoreApplication.translate("MainWindow", u"\u0411\u041f\u041a \u0414\u043e\u043f\u043d\u0438\u043a\u0438", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_4), QCoreApplication.translate("MainWindow", u"\u0418\u041f \u0414\u043e\u043f\u043d\u0438\u043a\u0438", None))
    # retranslateUi

