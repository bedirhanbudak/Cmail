from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Form_cmail(object):
    def setupUi(self, Form_cmail):
        Form_cmail.setObjectName("Form_cmail")
        Form_cmail.resize(338, 376)
        Form_cmail.setMinimumSize(QtCore.QSize(320, 360))
        self.gridLayout_9 = QtWidgets.QGridLayout(Form_cmail)
        self.gridLayout_9.setObjectName("gridLayout_9")
        self.tabWidget_cmail = QtWidgets.QTabWidget(Form_cmail)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.tabWidget_cmail.sizePolicy().hasHeightForWidth())
        self.tabWidget_cmail.setSizePolicy(sizePolicy)
        self.tabWidget_cmail.setMinimumSize(QtCore.QSize(320, 360))
        font = QtGui.QFont()
        font.setFamily("Helvetica")
        self.tabWidget_cmail.setFont(font)
        self.tabWidget_cmail.setStyleSheet("QTabBar::tab {width: 77px; height: 33px; text-align: center;}\n"
"QTabWidget::tab-bar {alignment: center;}\n"
"\n"
"")
        self.tabWidget_cmail.setObjectName("tabWidget_cmail")
        self.tab_cmail = QtWidgets.QWidget()
        self.tab_cmail.setStyleSheet(" QTabWidget>QWidget>QWidget{border-image:url(\"C:/Users/bedir/PycharmProjects/CMail/images/cmail.png\"); border-radius:10px;}")
        self.tab_cmail.setObjectName("tab_cmail")
        self.gridLayout_3 = QtWidgets.QGridLayout(self.tab_cmail)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.pushButton_start = QtWidgets.QPushButton(self.tab_cmail)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(10)
        sizePolicy.setHeightForWidth(self.pushButton_start.sizePolicy().hasHeightForWidth())
        self.pushButton_start.setSizePolicy(sizePolicy)
        self.pushButton_start.setMinimumSize(QtCore.QSize(90, 30))
        self.pushButton_start.setMaximumSize(QtCore.QSize(90, 30))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_start.setFont(font)
        self.pushButton_start.setStyleSheet("QPushButton {\n"
"    background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0.477, stop:0 rgba(11, 131, 120, 219), stop:1 rgba(85, 98, 112, 226));\n"
"    color: rgba(255, 255, 255, 210);\n"
"    border-radius: 15px;\n"
"   }\n"
"\n"
"QPushButton:hover {\n"
"    background-color: qlineargradient(spread:pad, x1:0, y1:0.505682, x2:1, y2:0.477, stop:0 rgba(150, 123, 111, 219), stop:1 rgba(85, 81, 84, 226));\n"
"    }\n"
"\n"
"QPushButton:pressed {\n"
"    padding-left: 5px;\n"
"    padding-top: 5px;\n"
"    background-color: rgba(150, 123, 111, 255);\n"
"    }")
        self.pushButton_start.setObjectName("pushButton_start")
        self.gridLayout_3.addWidget(self.pushButton_start, 5, 1, 1, 1, QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
        self.lineEdit_password = QtWidgets.QLineEdit(self.tab_cmail)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(20)
        sizePolicy.setHeightForWidth(self.lineEdit_password.sizePolicy().hasHeightForWidth())
        self.lineEdit_password.setSizePolicy(sizePolicy)
        self.lineEdit_password.setMinimumSize(QtCore.QSize(180, 30))
        self.lineEdit_password.setMaximumSize(QtCore.QSize(180, 30))
        self.lineEdit_password.setStyleSheet("background-color: rgba(0, 0, 0, 0);\n"
"border: none;\n"
"border-bottom: 2px solid rgba(46, 82, 101, 200);\n"
"color: white;\n"
"padding-bottom: 7px;\n"
"")
        self.lineEdit_password.setEchoMode(QtWidgets.QLineEdit.Password)
        self.lineEdit_password.setObjectName("lineEdit_password")
        self.gridLayout_3.addWidget(self.lineEdit_password, 3, 1, 1, 2, QtCore.Qt.AlignVCenter)
        self.lineEdit_email = QtWidgets.QLineEdit(self.tab_cmail)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lineEdit_email.sizePolicy().hasHeightForWidth())
        self.lineEdit_email.setSizePolicy(sizePolicy)
        self.lineEdit_email.setMinimumSize(QtCore.QSize(180, 30))
        self.lineEdit_email.setMaximumSize(QtCore.QSize(180, 30))
        self.lineEdit_email.setStyleSheet("background-color: rgba(0, 0, 0, 0);\n"
"border: none;\n"
"border-bottom: 2px solid rgba(46, 82, 101, 200);\n"
"color: white;\n"
"padding-bottom: 7px;\n"
"")
        self.lineEdit_email.setObjectName("lineEdit_email")
        self.gridLayout_3.addWidget(self.lineEdit_email, 2, 1, 1, 2, QtCore.Qt.AlignVCenter)
        self.label_status = QtWidgets.QLabel(self.tab_cmail)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(50)
        sizePolicy.setHeightForWidth(self.label_status.sizePolicy().hasHeightForWidth())
        self.label_status.setSizePolicy(sizePolicy)
        self.label_status.setMinimumSize(QtCore.QSize(200, 60))
        self.label_status.setMaximumSize(QtCore.QSize(200, 60))
        font = QtGui.QFont()
        font.setBold(False)
        font.setItalic(True)
        font.setWeight(50)
        self.label_status.setFont(font)
        self.label_status.setStyleSheet("color: rgba(255, 255, 255, 255);")
        self.label_status.setAlignment(QtCore.Qt.AlignCenter)
        self.label_status.setObjectName("label_status")
        self.gridLayout_3.addWidget(self.label_status, 6, 1, 1, 2, QtCore.Qt.AlignHCenter)
        self.pushButton_exit_1 = QtWidgets.QPushButton(self.tab_cmail)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(100)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton_exit_1.sizePolicy().hasHeightForWidth())
        self.pushButton_exit_1.setSizePolicy(sizePolicy)
        self.pushButton_exit_1.setMinimumSize(QtCore.QSize(20, 20))
        self.pushButton_exit_1.setMaximumSize(QtCore.QSize(20, 20))
        font = QtGui.QFont()
        font.setFamily("Webdings")
        font.setPointSize(12)
        self.pushButton_exit_1.setFont(font)
        self.pushButton_exit_1.setStyleSheet("QPushButton {\n"
"    background-color: rgba(0, 0, 0, 0);\n"
"    color: rgba(255, 255, 255, 255);\n"
"   }\n"
"\n"
"QPushButton:hover {\n"
"    color: rgba(210, 4, 45, 255);\n"
"    }\n"
"\n"
"QPushButton:pressed {\n"
"    padding-left: 5px;\n"
"    padding-top: 5px;\n"
"    }")
        self.pushButton_exit_1.setObjectName("pushButton_exit_1")
        self.gridLayout_3.addWidget(self.pushButton_exit_1, 0, 3, 1, 1, QtCore.Qt.AlignRight|QtCore.Qt.AlignTop)
        self.pushButton_stop = QtWidgets.QPushButton(self.tab_cmail)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(10)
        sizePolicy.setHeightForWidth(self.pushButton_stop.sizePolicy().hasHeightForWidth())
        self.pushButton_stop.setSizePolicy(sizePolicy)
        self.pushButton_stop.setMinimumSize(QtCore.QSize(90, 30))
        self.pushButton_stop.setMaximumSize(QtCore.QSize(90, 30))
        font = QtGui.QFont()
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.pushButton_stop.setFont(font)
        self.pushButton_stop.setStyleSheet("QPushButton {\n"
"    background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0.477, stop:0 rgba(11, 131, 120, 219), stop:1 rgba(85, 98, 112, 226));\n"
"    color: rgba(255, 255, 255, 210);\n"
"    border-radius: 15px;\n"
"   }\n"
"\n"
"QPushButton:hover {\n"
"    background-color: qlineargradient(spread:pad, x1:0, y1:0.505682, x2:1, y2:0.477, stop:0 rgba(150, 123, 111, 219), stop:1 rgba(85, 81, 84, 226));\n"
"    }\n"
"\n"
"QPushButton:pressed {\n"
"    padding-left: 5px;\n"
"    padding-top: 5px;\n"
"    background-color: rgba(150, 123, 111, 255);\n"
"    }")
        self.pushButton_stop.setObjectName("pushButton_stop")
        self.gridLayout_3.addWidget(self.pushButton_stop, 5, 2, 1, 1, QtCore.Qt.AlignRight|QtCore.Qt.AlignTop)
        self.pushButton_minimize_1 = QtWidgets.QPushButton(self.tab_cmail)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(100)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton_minimize_1.sizePolicy().hasHeightForWidth())
        self.pushButton_minimize_1.setSizePolicy(sizePolicy)
        self.pushButton_minimize_1.setMinimumSize(QtCore.QSize(20, 20))
        self.pushButton_minimize_1.setMaximumSize(QtCore.QSize(20, 20))
        font = QtGui.QFont()
        font.setFamily("Webdings")
        font.setPointSize(12)
        self.pushButton_minimize_1.setFont(font)
        self.pushButton_minimize_1.setStyleSheet("QPushButton {\n"
"    background-color: rgba(0, 0, 0, 0);\n"
"    color: rgba(255, 255, 255, 255);\n"
"   }\n"
"\n"
"QPushButton:hover {\n"
"    color: rgba(85, 98, 112, 255);\n"
"    }\n"
"\n"
"QPushButton:pressed {\n"
"    padding-left: 5px;\n"
"    padding-top: 5px;\n"
"    }")
        self.pushButton_minimize_1.setObjectName("pushButton_minimize_1")
        self.gridLayout_3.addWidget(self.pushButton_minimize_1, 0, 0, 1, 1, QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
        self.label_cmailTitle = QtWidgets.QLabel(self.tab_cmail)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(50)
        sizePolicy.setHeightForWidth(self.label_cmailTitle.sizePolicy().hasHeightForWidth())
        self.label_cmailTitle.setSizePolicy(sizePolicy)
        self.label_cmailTitle.setMinimumSize(QtCore.QSize(200, 40))
        self.label_cmailTitle.setMaximumSize(QtCore.QSize(200, 40))
        font = QtGui.QFont()
        font.setFamily("System")
        font.setPointSize(8)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.label_cmailTitle.setFont(font)
        self.label_cmailTitle.setStyleSheet("color: white;\n"
"border: none;\n"
"border-bottom: 2px solid rgba(0, 125, 0, 200);\n"
"padding-bottom: 7px;")
        self.label_cmailTitle.setAlignment(QtCore.Qt.AlignCenter)
        self.label_cmailTitle.setObjectName("label_cmailTitle")
        self.gridLayout_3.addWidget(self.label_cmailTitle, 0, 1, 1, 2, QtCore.Qt.AlignHCenter|QtCore.Qt.AlignTop)
        self.label_invalid = QtWidgets.QLabel(self.tab_cmail)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(20)
        sizePolicy.setHeightForWidth(self.label_invalid.sizePolicy().hasHeightForWidth())
        self.label_invalid.setSizePolicy(sizePolicy)
        self.label_invalid.setMinimumSize(QtCore.QSize(110, 25))
        self.label_invalid.setMaximumSize(QtCore.QSize(110, 25))
        font = QtGui.QFont()
        font.setFamily("Helvetica")
        self.label_invalid.setFont(font)
        self.label_invalid.setStyleSheet("color: rgba(210, 4, 45, 255);")
        self.label_invalid.setObjectName("label_invalid")
        self.gridLayout_3.addWidget(self.label_invalid, 4, 1, 1, 1, QtCore.Qt.AlignTop)
        self.pushButton_start.raise_()
        self.pushButton_stop.raise_()
        self.label_invalid.raise_()
        self.label_status.raise_()
        self.lineEdit_password.raise_()
        self.lineEdit_email.raise_()
        self.pushButton_exit_1.raise_()
        self.pushButton_minimize_1.raise_()
        self.label_cmailTitle.raise_()
        self.tabWidget_cmail.addTab(self.tab_cmail, "")
        self.tab_logs = QtWidgets.QWidget()
        self.tab_logs.setStyleSheet(" QTabWidget>QWidget>QWidget{border-image:url(\"C:/Users/bedir/PycharmProjects/CMail/images/logs.jpg\"); border-radius:10px;}")
        self.tab_logs.setObjectName("tab_logs")
        self.gridLayout_4 = QtWidgets.QGridLayout(self.tab_logs)
        self.gridLayout_4.setObjectName("gridLayout_4")
        self.pushButton_exit_2 = QtWidgets.QPushButton(self.tab_logs)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(100)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton_exit_2.sizePolicy().hasHeightForWidth())
        self.pushButton_exit_2.setSizePolicy(sizePolicy)
        self.pushButton_exit_2.setMinimumSize(QtCore.QSize(20, 20))
        self.pushButton_exit_2.setMaximumSize(QtCore.QSize(20, 20))
        font = QtGui.QFont()
        font.setFamily("Webdings")
        font.setPointSize(12)
        self.pushButton_exit_2.setFont(font)
        self.pushButton_exit_2.setStyleSheet("QPushButton {\n"
"    background-color: rgba(0, 0, 0, 0);\n"
"    color: rgba(255, 255, 255, 255);\n"
"   }\n"
"\n"
"QPushButton:hover {\n"
"    color: rgba(210, 4, 45, 255);\n"
"    }\n"
"\n"
"QPushButton:pressed {\n"
"    padding-left: 5px;\n"
"    padding-top: 5px;\n"
"    }")
        self.pushButton_exit_2.setObjectName("pushButton_exit_2")
        self.gridLayout_4.addWidget(self.pushButton_exit_2, 0, 2, 1, 1, QtCore.Qt.AlignRight|QtCore.Qt.AlignTop)
        self.pushButton_minimize_2 = QtWidgets.QPushButton(self.tab_logs)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(100)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton_minimize_2.sizePolicy().hasHeightForWidth())
        self.pushButton_minimize_2.setSizePolicy(sizePolicy)
        self.pushButton_minimize_2.setMinimumSize(QtCore.QSize(20, 20))
        self.pushButton_minimize_2.setMaximumSize(QtCore.QSize(20, 20))
        font = QtGui.QFont()
        font.setFamily("Webdings")
        font.setPointSize(12)
        self.pushButton_minimize_2.setFont(font)
        self.pushButton_minimize_2.setStyleSheet("QPushButton {\n"
"    background-color: rgba(0, 0, 0, 0);\n"
"    color: rgba(255, 255, 255, 255);\n"
"   }\n"
"\n"
"QPushButton:hover {\n"
"    color: rgba(85, 98, 112, 255);\n"
"    }\n"
"\n"
"QPushButton:pressed {\n"
"    padding-left: 5px;\n"
"    padding-top: 5px;\n"
"    }")
        self.pushButton_minimize_2.setObjectName("pushButton_minimize_2")
        self.gridLayout_4.addWidget(self.pushButton_minimize_2, 0, 0, 1, 1, QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
        self.textBrowser_logHistory = QtWidgets.QTextBrowser(self.tab_logs)
        self.textBrowser_logHistory.setEnabled(False)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(20)
        sizePolicy.setHeightForWidth(self.textBrowser_logHistory.sizePolicy().hasHeightForWidth())
        self.textBrowser_logHistory.setSizePolicy(sizePolicy)
        self.textBrowser_logHistory.setMinimumSize(QtCore.QSize(220, 200))
        self.textBrowser_logHistory.setMaximumSize(QtCore.QSize(220, 200))
        self.textBrowser_logHistory.setStyleSheet("background-color: rgba(0, 0, 0, 0);\n"
"color: rgba(255, 255, 255, 255);")
        self.textBrowser_logHistory.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.textBrowser_logHistory.setObjectName("textBrowser_logHistory")
        self.gridLayout_4.addWidget(self.textBrowser_logHistory, 1, 1, 1, 1)
        self.pushButton_clearLogs = QtWidgets.QPushButton(self.tab_logs)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(20)
        sizePolicy.setHeightForWidth(self.pushButton_clearLogs.sizePolicy().hasHeightForWidth())
        self.pushButton_clearLogs.setSizePolicy(sizePolicy)
        self.pushButton_clearLogs.setMinimumSize(QtCore.QSize(120, 30))
        self.pushButton_clearLogs.setMaximumSize(QtCore.QSize(120, 30))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(12)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.pushButton_clearLogs.setFont(font)
        self.pushButton_clearLogs.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.pushButton_clearLogs.setStyleSheet("QPushButton {\n"
"    color: rgba(255, 255, 255, 255);\n"
"    border-radius: 1px;\n"
"    }\n"
"\n"
"QPushButton:hover {\n"
"    color: rgba(200, 200, 200, 200);\n"
"    }\n"
"\n"
"QPushButton:pressed {\n"
"    color: rgba(150, 150, 150, 150);\n"
"    }")
        self.pushButton_clearLogs.setObjectName("pushButton_clearLogs")
        self.gridLayout_4.addWidget(self.pushButton_clearLogs, 2, 1, 1, 1, QtCore.Qt.AlignHCenter|QtCore.Qt.AlignBottom)
        self.label_logsTitle = QtWidgets.QLabel(self.tab_logs)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(20)
        sizePolicy.setHeightForWidth(self.label_logsTitle.sizePolicy().hasHeightForWidth())
        self.label_logsTitle.setSizePolicy(sizePolicy)
        self.label_logsTitle.setMinimumSize(QtCore.QSize(200, 30))
        self.label_logsTitle.setMaximumSize(QtCore.QSize(200, 30))
        font = QtGui.QFont()
        font.setFamily("System")
        font.setPointSize(8)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.label_logsTitle.setFont(font)
        self.label_logsTitle.setStyleSheet("color: white;")
        self.label_logsTitle.setAlignment(QtCore.Qt.AlignCenter)
        self.label_logsTitle.setObjectName("label_logsTitle")
        self.gridLayout_4.addWidget(self.label_logsTitle, 0, 1, 1, 1, QtCore.Qt.AlignHCenter|QtCore.Qt.AlignTop)
        self.tabWidget_cmail.addTab(self.tab_logs, "")
        self.tab_settings = QtWidgets.QWidget()
        self.tab_settings.setStyleSheet(" QTabWidget>QWidget>QWidget{border-image:url(\"C:/Users/bedir/PycharmProjects/CMail/images/settings.png\"); border-radius:10px;}")
        self.tab_settings.setObjectName("tab_settings")
        self.gridLayout_5 = QtWidgets.QGridLayout(self.tab_settings)
        self.gridLayout_5.setObjectName("gridLayout_5")
        self.groupBox_cleaning = QtWidgets.QGroupBox(self.tab_settings)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(20)
        sizePolicy.setHeightForWidth(self.groupBox_cleaning.sizePolicy().hasHeightForWidth())
        self.groupBox_cleaning.setSizePolicy(sizePolicy)
        self.groupBox_cleaning.setMinimumSize(QtCore.QSize(260, 90))
        self.groupBox_cleaning.setMaximumSize(QtCore.QSize(260, 90))
        self.groupBox_cleaning.setStyleSheet("color:rgba(255, 255, 255, 255);")
        self.groupBox_cleaning.setAlignment(QtCore.Qt.AlignCenter)
        self.groupBox_cleaning.setObjectName("groupBox_cleaning")
        self.gridLayout_7 = QtWidgets.QGridLayout(self.groupBox_cleaning)
        self.gridLayout_7.setObjectName("gridLayout_7")
        self.label_warning = QtWidgets.QLabel(self.groupBox_cleaning)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(10)
        sizePolicy.setHeightForWidth(self.label_warning.sizePolicy().hasHeightForWidth())
        self.label_warning.setSizePolicy(sizePolicy)
        self.label_warning.setMinimumSize(QtCore.QSize(240, 15))
        self.label_warning.setMaximumSize(QtCore.QSize(240, 15))
        font = QtGui.QFont()
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.label_warning.setFont(font)
        self.label_warning.setStyleSheet("color: rgba(210, 4, 45, 255);")
        self.label_warning.setAlignment(QtCore.Qt.AlignCenter)
        self.label_warning.setObjectName("label_warning")
        self.gridLayout_7.addWidget(self.label_warning, 1, 0, 1, 1)
        self.pushButton_allDEL = QtWidgets.QPushButton(self.groupBox_cleaning)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(50)
        sizePolicy.setHeightForWidth(self.pushButton_allDEL.sizePolicy().hasHeightForWidth())
        self.pushButton_allDEL.setSizePolicy(sizePolicy)
        self.pushButton_allDEL.setMinimumSize(QtCore.QSize(120, 30))
        self.pushButton_allDEL.setMaximumSize(QtCore.QSize(100, 30))
        self.pushButton_allDEL.setStyleSheet("color:rgba(0, 0, 0, 255);")
        self.pushButton_allDEL.setObjectName("pushButton_allDEL")
        self.gridLayout_7.addWidget(self.pushButton_allDEL, 2, 1, 1, 1, QtCore.Qt.AlignRight|QtCore.Qt.AlignTop)
        self.pushButton_infoDEL = QtWidgets.QPushButton(self.groupBox_cleaning)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(50)
        sizePolicy.setHeightForWidth(self.pushButton_infoDEL.sizePolicy().hasHeightForWidth())
        self.pushButton_infoDEL.setSizePolicy(sizePolicy)
        self.pushButton_infoDEL.setMinimumSize(QtCore.QSize(120, 30))
        self.pushButton_infoDEL.setMaximumSize(QtCore.QSize(100, 30))
        self.pushButton_infoDEL.setStyleSheet("color: rgba(0, 0, 0, 255);")
        self.pushButton_infoDEL.setObjectName("pushButton_infoDEL")
        self.gridLayout_7.addWidget(self.pushButton_infoDEL, 2, 0, 1, 1, QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
        self.gridLayout_5.addWidget(self.groupBox_cleaning, 2, 0, 1, 4, QtCore.Qt.AlignHCenter|QtCore.Qt.AlignTop)
        self.checkBox_notifications = QtWidgets.QCheckBox(self.tab_settings)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(20)
        sizePolicy.setHeightForWidth(self.checkBox_notifications.sizePolicy().hasHeightForWidth())
        self.checkBox_notifications.setSizePolicy(sizePolicy)
        self.checkBox_notifications.setMinimumSize(QtCore.QSize(200, 20))
        self.checkBox_notifications.setMaximumSize(QtCore.QSize(200, 20))
        self.checkBox_notifications.setStyleSheet("color:rgba(255, 255, 255, 255);")
        self.checkBox_notifications.setChecked(True)
        self.checkBox_notifications.setObjectName("checkBox_notifications")
        self.gridLayout_5.addWidget(self.checkBox_notifications, 3, 1, 1, 1)
        self.pushButton_exit_3 = QtWidgets.QPushButton(self.tab_settings)
        self.pushButton_exit_3.setMinimumSize(QtCore.QSize(20, 20))
        self.pushButton_exit_3.setMaximumSize(QtCore.QSize(20, 20))
        font = QtGui.QFont()
        font.setFamily("Webdings")
        font.setPointSize(12)
        self.pushButton_exit_3.setFont(font)
        self.pushButton_exit_3.setStyleSheet("QPushButton {\n"
"    background-color: rgba(0, 0, 0, 0);\n"
"    color: rgba(255, 255, 255, 255);\n"
"   }\n"
"\n"
"QPushButton:hover {\n"
"    color: rgba(210, 4, 45, 255);\n"
"    }\n"
"\n"
"QPushButton:pressed {\n"
"    padding-left: 5px;\n"
"    padding-top: 5px;\n"
"    }")
        self.pushButton_exit_3.setObjectName("pushButton_exit_3")
        self.gridLayout_5.addWidget(self.pushButton_exit_3, 0, 3, 1, 1, QtCore.Qt.AlignRight)
        self.pushButton_minimize_3 = QtWidgets.QPushButton(self.tab_settings)
        self.pushButton_minimize_3.setMinimumSize(QtCore.QSize(20, 20))
        self.pushButton_minimize_3.setMaximumSize(QtCore.QSize(20, 20))
        font = QtGui.QFont()
        font.setFamily("Webdings")
        font.setPointSize(12)
        self.pushButton_minimize_3.setFont(font)
        self.pushButton_minimize_3.setStyleSheet("QPushButton {\n"
"    background-color: rgba(0, 0, 0, 0);\n"
"    color: rgba(255, 255, 255, 255);\n"
"   }\n"
"\n"
"QPushButton:hover {\n"
"    color: rgba(85, 98, 112, 255);\n"
"    }\n"
"\n"
"QPushButton:pressed {\n"
"    padding-left: 5px;\n"
"    padding-top: 5px;\n"
"    }")
        self.pushButton_minimize_3.setObjectName("pushButton_minimize_3")
        self.gridLayout_5.addWidget(self.pushButton_minimize_3, 0, 0, 1, 1, QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
        self.checkBox_autoDEL = QtWidgets.QCheckBox(self.tab_settings)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(20)
        sizePolicy.setHeightForWidth(self.checkBox_autoDEL.sizePolicy().hasHeightForWidth())
        self.checkBox_autoDEL.setSizePolicy(sizePolicy)
        self.checkBox_autoDEL.setMinimumSize(QtCore.QSize(200, 20))
        self.checkBox_autoDEL.setMaximumSize(QtCore.QSize(200, 20))
        self.checkBox_autoDEL.setStyleSheet("color:rgba(255, 255, 255, 255);")
        self.checkBox_autoDEL.setObjectName("checkBox_autoDEL")
        self.gridLayout_5.addWidget(self.checkBox_autoDEL, 4, 1, 1, 1, QtCore.Qt.AlignHCenter|QtCore.Qt.AlignTop)
        self.groupBox_service = QtWidgets.QGroupBox(self.tab_settings)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(20)
        sizePolicy.setHeightForWidth(self.groupBox_service.sizePolicy().hasHeightForWidth())
        self.groupBox_service.setSizePolicy(sizePolicy)
        self.groupBox_service.setMinimumSize(QtCore.QSize(260, 120))
        self.groupBox_service.setMaximumSize(QtCore.QSize(260, 120))
        self.groupBox_service.setStyleSheet("color: rgba(255, 255, 255, 255);")
        self.groupBox_service.setAlignment(QtCore.Qt.AlignCenter)
        self.groupBox_service.setObjectName("groupBox_service")
        self.gridLayout_8 = QtWidgets.QGridLayout(self.groupBox_service)
        self.gridLayout_8.setObjectName("gridLayout_8")
        self.label_imapServer = QtWidgets.QLabel(self.groupBox_service)
        self.label_imapServer.setMinimumSize(QtCore.QSize(80, 20))
        self.label_imapServer.setMaximumSize(QtCore.QSize(80, 20))
        self.label_imapServer.setStyleSheet("color:rgba(255, 255, 255, 255);")
        self.label_imapServer.setAlignment(QtCore.Qt.AlignCenter)
        self.label_imapServer.setObjectName("label_imapServer")
        self.gridLayout_8.addWidget(self.label_imapServer, 0, 0, 1, 1)
        self.lineEdit_imapServer = QtWidgets.QLineEdit(self.groupBox_service)
        self.lineEdit_imapServer.setEnabled(True)
        self.lineEdit_imapServer.setMinimumSize(QtCore.QSize(160, 20))
        self.lineEdit_imapServer.setMaximumSize(QtCore.QSize(160, 20))
        self.lineEdit_imapServer.setStyleSheet("color: rgba(0 ,0, 0, 255);\n"
"border-radius: 10px;")
        self.lineEdit_imapServer.setText("")
        self.lineEdit_imapServer.setAlignment(QtCore.Qt.AlignCenter)
        self.lineEdit_imapServer.setPlaceholderText("")
        self.lineEdit_imapServer.setObjectName("lineEdit_imapServer")
        self.gridLayout_8.addWidget(self.lineEdit_imapServer, 0, 1, 1, 1)
        self.label_smtpServer = QtWidgets.QLabel(self.groupBox_service)
        self.label_smtpServer.setMinimumSize(QtCore.QSize(80, 20))
        self.label_smtpServer.setMaximumSize(QtCore.QSize(80, 20))
        self.label_smtpServer.setStyleSheet("color:rgba(255, 255, 255, 255);")
        self.label_smtpServer.setAlignment(QtCore.Qt.AlignCenter)
        self.label_smtpServer.setObjectName("label_smtpServer")
        self.gridLayout_8.addWidget(self.label_smtpServer, 1, 0, 1, 1)
        self.lineEdit_smtpServer = QtWidgets.QLineEdit(self.groupBox_service)
        self.lineEdit_smtpServer.setEnabled(True)
        self.lineEdit_smtpServer.setMinimumSize(QtCore.QSize(160, 20))
        self.lineEdit_smtpServer.setMaximumSize(QtCore.QSize(160, 20))
        self.lineEdit_smtpServer.setStyleSheet("color: rgba(0 ,0, 0, 255);\n"
"border-radius: 10px;")
        self.lineEdit_smtpServer.setText("")
        self.lineEdit_smtpServer.setAlignment(QtCore.Qt.AlignCenter)
        self.lineEdit_smtpServer.setPlaceholderText("")
        self.lineEdit_smtpServer.setObjectName("lineEdit_smtpServer")
        self.gridLayout_8.addWidget(self.lineEdit_smtpServer, 1, 1, 1, 1)
        self.label_smtpPort = QtWidgets.QLabel(self.groupBox_service)
        self.label_smtpPort.setMinimumSize(QtCore.QSize(80, 20))
        self.label_smtpPort.setMaximumSize(QtCore.QSize(80, 20))
        self.label_smtpPort.setStyleSheet("color:rgba(255, 255, 255, 255);")
        self.label_smtpPort.setAlignment(QtCore.Qt.AlignCenter)
        self.label_smtpPort.setObjectName("label_smtpPort")
        self.gridLayout_8.addWidget(self.label_smtpPort, 2, 0, 1, 1)
        self.lineEdit_smtpPort = QtWidgets.QLineEdit(self.groupBox_service)
        self.lineEdit_smtpPort.setEnabled(True)
        self.lineEdit_smtpPort.setMinimumSize(QtCore.QSize(80, 20))
        self.lineEdit_smtpPort.setMaximumSize(QtCore.QSize(80, 20))
        self.lineEdit_smtpPort.setStyleSheet("color: rgba(0 ,0, 0, 255);\n"
"border-radius: 10px;")
        self.lineEdit_smtpPort.setText("")
        self.lineEdit_smtpPort.setAlignment(QtCore.Qt.AlignCenter)
        self.lineEdit_smtpPort.setPlaceholderText("")
        self.lineEdit_smtpPort.setObjectName("lineEdit_smtpPort")
        self.gridLayout_8.addWidget(self.lineEdit_smtpPort, 2, 1, 1, 1)
        self.gridLayout_5.addWidget(self.groupBox_service, 1, 0, 1, 4, QtCore.Qt.AlignHCenter|QtCore.Qt.AlignTop)
        self.groupBox_service.raise_()
        self.groupBox_cleaning.raise_()
        self.pushButton_exit_3.raise_()
        self.pushButton_minimize_3.raise_()
        self.checkBox_autoDEL.raise_()
        self.checkBox_notifications.raise_()
        self.tabWidget_cmail.addTab(self.tab_settings, "")
        self.tab_info = QtWidgets.QWidget()
        self.tab_info.setStyleSheet(" QTabWidget>QWidget>QWidget{border-image:url(\"C:/Users/bedir/PycharmProjects/CMail/images/information.jpg\"); border-radius:10px;}")
        self.tab_info.setObjectName("tab_info")
        self.gridLayout_6 = QtWidgets.QGridLayout(self.tab_info)
        self.gridLayout_6.setObjectName("gridLayout_6")
        self.pushButton_exit_4 = QtWidgets.QPushButton(self.tab_info)
        self.pushButton_exit_4.setMinimumSize(QtCore.QSize(20, 20))
        self.pushButton_exit_4.setMaximumSize(QtCore.QSize(20, 20))
        font = QtGui.QFont()
        font.setFamily("Webdings")
        font.setPointSize(12)
        self.pushButton_exit_4.setFont(font)
        self.pushButton_exit_4.setStyleSheet("QPushButton {\n"
"    background-color: rgba(0, 0, 0, 0);\n"
"    color: rgba(255, 255, 255, 255);\n"
"   }\n"
"\n"
"QPushButton:hover {\n"
"    color: rgba(210, 4, 45, 255);\n"
"    }\n"
"\n"
"QPushButton:pressed {\n"
"    padding-left: 5px;\n"
"    padding-top: 5px;\n"
"    }")
        self.pushButton_exit_4.setObjectName("pushButton_exit_4")
        self.gridLayout_6.addWidget(self.pushButton_exit_4, 0, 2, 1, 1, QtCore.Qt.AlignRight|QtCore.Qt.AlignTop)
        self.pushButton_guide = QtWidgets.QPushButton(self.tab_info)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(20)
        sizePolicy.setHeightForWidth(self.pushButton_guide.sizePolicy().hasHeightForWidth())
        self.pushButton_guide.setSizePolicy(sizePolicy)
        self.pushButton_guide.setMinimumSize(QtCore.QSize(150, 40))
        self.pushButton_guide.setMaximumSize(QtCore.QSize(150, 40))
        font = QtGui.QFont()
        font.setFamily("System")
        font.setPointSize(8)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_guide.setFont(font)
        self.pushButton_guide.setStyleSheet("QPushButton {\n"
"    background-color: rgba(0, 0, 0, 80);\n"
"    color: rgba(85, 98, 112, 255);\n"
"    border-radius:10px;\n"
"   }\n"
"\n"
"QPushButton:hover {\n"
"    color: rgba(34, 139, 34, 255);\n"
"    }\n"
"\n"
"QPushButton:pressed {\n"
"    padding-left: 5px;\n"
"    padding-top: 5px;\n"
"    }")
        self.pushButton_guide.setObjectName("pushButton_guide")
        self.gridLayout_6.addWidget(self.pushButton_guide, 2, 1, 1, 1, QtCore.Qt.AlignHCenter|QtCore.Qt.AlignVCenter)
        self.pushButton_minimize_4 = QtWidgets.QPushButton(self.tab_info)
        self.pushButton_minimize_4.setMinimumSize(QtCore.QSize(20, 20))
        self.pushButton_minimize_4.setMaximumSize(QtCore.QSize(20, 20))
        font = QtGui.QFont()
        font.setFamily("Webdings")
        font.setPointSize(12)
        self.pushButton_minimize_4.setFont(font)
        self.pushButton_minimize_4.setStyleSheet("QPushButton {\n"
"    background-color: rgba(0, 0, 0, 0);\n"
"    color: rgba(255, 255, 255, 255);\n"
"   }\n"
"\n"
"QPushButton:hover {\n"
"    color: rgba(85, 98, 112, 255);\n"
"    }\n"
"\n"
"QPushButton:pressed {\n"
"    padding-left: 5px;\n"
"    padding-top: 5px;\n"
"    }")
        self.pushButton_minimize_4.setObjectName("pushButton_minimize_4")
        self.gridLayout_6.addWidget(self.pushButton_minimize_4, 0, 0, 1, 1, QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
        self.horizontalLayout_contact = QtWidgets.QHBoxLayout()
        self.horizontalLayout_contact.setObjectName("horizontalLayout_contact")
        self.pushButton_linkedIn = QtWidgets.QPushButton(self.tab_info)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(100)
        sizePolicy.setVerticalStretch(20)
        sizePolicy.setHeightForWidth(self.pushButton_linkedIn.sizePolicy().hasHeightForWidth())
        self.pushButton_linkedIn.setSizePolicy(sizePolicy)
        self.pushButton_linkedIn.setMinimumSize(QtCore.QSize(50, 80))
        self.pushButton_linkedIn.setMaximumSize(QtCore.QSize(50, 100))
        fontId = QtGui.QFontDatabase.addApplicationFont("fonts/Social Media Circled.otf")
        families = QtGui.QFontDatabase.applicationFontFamilies(fontId)
        font = QtGui.QFont(families[0])
        font.setFamily("Social Media Circled")
        font.setPointSize(24)
        self.pushButton_linkedIn.setFont(font)
        self.pushButton_linkedIn.setStyleSheet("QPushButton {\n"
"    background-color: rgba(0, 0, 0, 0);\n"
"    color: rgba(85, 98, 112, 255);\n"
"   }\n"
"\n"
"QPushButton:hover {\n"
"    color: rgba(0, 114, 177, 255);\n"
"    }\n"
"\n"
"QPushButton:pressed {\n"
"    padding-left: 5px;\n"
"    padding-top: 5px;\n"
"    }")
        self.pushButton_linkedIn.setObjectName("pushButton_linkedIn")
        self.horizontalLayout_contact.addWidget(self.pushButton_linkedIn)
        self.pushButton_gitHub = QtWidgets.QPushButton(self.tab_info)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(100)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton_gitHub.sizePolicy().hasHeightForWidth())
        self.pushButton_gitHub.setSizePolicy(sizePolicy)
        self.pushButton_gitHub.setMinimumSize(QtCore.QSize(50, 80))
        self.pushButton_gitHub.setMaximumSize(QtCore.QSize(50, 100))
        font = QtGui.QFont(families[0])
        font.setFamily("Social Media Circled")
        font.setPointSize(24)
        self.pushButton_gitHub.setFont(font)
        self.pushButton_gitHub.setStyleSheet("QPushButton {\n"
"    background-color: rgba(0, 0, 0, 0);\n"
"    color: rgba(85, 98, 112, 255);\n"
"   }\n"
"\n"
"QPushButton:hover {\n"
"    color: rgba(23, 21, 21, 255);\n"
"    }\n"
"\n"
"QPushButton:pressed {\n"
"    padding-left: 5px;\n"
"    padding-top: 5px;\n"
"    }")
        self.pushButton_gitHub.setObjectName("pushButton_gitHub")
        self.horizontalLayout_contact.addWidget(self.pushButton_gitHub)
        self.pushButton_email = QtWidgets.QPushButton(self.tab_info)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(100)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton_email.sizePolicy().hasHeightForWidth())
        self.pushButton_email.setSizePolicy(sizePolicy)
        self.pushButton_email.setMinimumSize(QtCore.QSize(50, 80))
        self.pushButton_email.setMaximumSize(QtCore.QSize(50, 100))
        font = QtGui.QFont(families[0])
        font.setFamily("Social Media Circled")
        font.setPointSize(24)
        self.pushButton_email.setFont(font)
        self.pushButton_email.setStyleSheet("QPushButton {\n"
"    background-color: rgba(0, 0, 0, 0);\n"
"    color: rgba(85, 98, 112, 255);\n"
"   }\n"
"\n"
"QPushButton:hover {\n"
"    color: rgba(234, 234, 234, 234);\n"
"    }\n"
"\n"
"QPushButton:pressed {\n"
"    padding-left: 5px;\n"
"    padding-top: 5px;\n"
"    }")
        self.pushButton_email.setObjectName("pushButton_email")
        self.horizontalLayout_contact.addWidget(self.pushButton_email)
        self.gridLayout_6.addLayout(self.horizontalLayout_contact, 5, 0, 1, 3)
        self.pushButton_license = QtWidgets.QPushButton(self.tab_info)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(10)
        sizePolicy.setHeightForWidth(self.pushButton_license.sizePolicy().hasHeightForWidth())
        self.pushButton_license.setSizePolicy(sizePolicy)
        self.pushButton_license.setMinimumSize(QtCore.QSize(261, 25))
        self.pushButton_license.setMaximumSize(QtCore.QSize(250, 25))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(8)
        font.setBold(False)
        font.setWeight(50)
        font.setStrikeOut(False)
        self.pushButton_license.setFont(font)
        self.pushButton_license.setStyleSheet("QPushButton {\n"
"    background-color: rgba(0, 0, 0, 80);\n"
"    color: rgba(255, 255, 255, 255);\n"
"    border-radius:10px;\n"
"   }\n"
"\n"
"QPushButton:hover {\n"
"    color: rgba(85, 98, 112, 255);\n"
"    }\n"
"\n"
"QPushButton:pressed {\n"
"    padding-left: 5px;\n"
"    padding-top: 5px;\n"
"    }")
        self.pushButton_license.setObjectName("pushButton_license")
        self.gridLayout_6.addWidget(self.pushButton_license, 6, 0, 1, 3, QtCore.Qt.AlignHCenter|QtCore.Qt.AlignBottom)
        self.label_version = QtWidgets.QLabel(self.tab_info)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(20)
        sizePolicy.setHeightForWidth(self.label_version.sizePolicy().hasHeightForWidth())
        self.label_version.setSizePolicy(sizePolicy)
        self.label_version.setMinimumSize(QtCore.QSize(150, 80))
        self.label_version.setMaximumSize(QtCore.QSize(150, 80))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        self.label_version.setFont(font)
        self.label_version.setStyleSheet("color:white;\n"
"border-radius:10px;")
        self.label_version.setObjectName("label_version")
        self.gridLayout_6.addWidget(self.label_version, 0, 1, 1, 1, QtCore.Qt.AlignHCenter|QtCore.Qt.AlignVCenter)
        self.pushButton_minimize_4.raise_()
        self.pushButton_exit_4.raise_()
        self.pushButton_guide.raise_()
        self.pushButton_license.raise_()
        self.label_version.raise_()
        self.tabWidget_cmail.addTab(self.tab_info, "")
        self.gridLayout_9.addWidget(self.tabWidget_cmail, 0, 0, 1, 1)

        self.retranslateUi(Form_cmail)
        self.tabWidget_cmail.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(Form_cmail)

    def retranslateUi(self, Form_cmail):
        _translate = QtCore.QCoreApplication.translate
        Form_cmail.setWindowTitle(_translate("Form_cmail", "Form"))
        self.pushButton_start.setText(_translate("Form_cmail", "Start"))
        self.lineEdit_password.setPlaceholderText(_translate("Form_cmail", "Password"))
        self.lineEdit_email.setPlaceholderText(_translate("Form_cmail", "E-mail address"))
        self.label_status.setText(_translate("Form_cmail", "Click on Start"))
        self.pushButton_exit_1.setToolTip(_translate("Form_cmail", "Exit"))
        self.pushButton_exit_1.setText(_translate("Form_cmail", "r"))
        self.pushButton_stop.setText(_translate("Form_cmail", "Stop"))
        self.pushButton_minimize_1.setToolTip(_translate("Form_cmail", "Minimize to tray menu"))
        self.pushButton_minimize_1.setText(_translate("Form_cmail", "2"))
        self.label_cmailTitle.setText(_translate("Form_cmail", "Confirmed Mail"))
        self.label_invalid.setText(_translate("Form_cmail", "Invalid e-mail"))
        self.tabWidget_cmail.setTabText(self.tabWidget_cmail.indexOf(self.tab_cmail), _translate("Form_cmail", "Cmail"))
        self.pushButton_exit_2.setToolTip(_translate("Form_cmail", "Exit"))
        self.pushButton_exit_2.setText(_translate("Form_cmail", "r"))
        self.pushButton_minimize_2.setToolTip(_translate("Form_cmail", "Minimize to tray menu"))
        self.pushButton_minimize_2.setText(_translate("Form_cmail", "2"))
        self.pushButton_clearLogs.setText(_translate("Form_cmail", "Clear Logs"))
        self.label_logsTitle.setText(_translate("Form_cmail", "History Logs"))
        self.tabWidget_cmail.setTabText(self.tabWidget_cmail.indexOf(self.tab_logs), _translate("Form_cmail", "Logs"))
        self.groupBox_cleaning.setTitle(_translate("Form_cmail", "Inbox Cleaning"))
        self.label_warning.setText(_translate("Form_cmail", "Be careful when using!"))
        self.pushButton_allDEL.setToolTip(_translate("Form_cmail", "Delete all e-mails except marked ones"))
        self.pushButton_allDEL.setText(_translate("Form_cmail", "DEL not confirmed"))
        self.pushButton_infoDEL.setToolTip(_translate("Form_cmail", "Delete information e-mails"))
        self.pushButton_infoDEL.setText(_translate("Form_cmail", "DEL information"))
        self.checkBox_notifications.setText(_translate("Form_cmail", "Show notifications"))
        self.pushButton_exit_3.setToolTip(_translate("Form_cmail", "Exit"))
        self.pushButton_exit_3.setText(_translate("Form_cmail", "r"))
        self.pushButton_minimize_3.setToolTip(_translate("Form_cmail", "Minimize to tray menu"))
        self.pushButton_minimize_3.setText(_translate("Form_cmail", "2"))
        self.checkBox_autoDEL.setText(_translate("Form_cmail", "Auto DEL information"))
        self.groupBox_service.setTitle(_translate("Form_cmail", "Service Adjustment"))
        self.label_imapServer.setText(_translate("Form_cmail", "IMAP Server:"))
        self.lineEdit_imapServer.setPlaceholderText(_translate("Form_cmail", "imap.example.com"))
        self.label_smtpServer.setText(_translate("Form_cmail", "SMTP Server:"))
        self.lineEdit_smtpServer.setPlaceholderText(_translate("Form_cmail", "smtp.example.com"))
        self.label_smtpPort.setText(_translate("Form_cmail", "SMTP Port:"))
        self.lineEdit_smtpPort.setPlaceholderText(_translate("Form_cmail", "xxx"))
        self.tabWidget_cmail.setTabText(self.tabWidget_cmail.indexOf(self.tab_settings), _translate("Form_cmail", "Settings"))
        self.pushButton_exit_4.setToolTip(_translate("Form_cmail", "Exit"))
        self.pushButton_exit_4.setText(_translate("Form_cmail", "r"))
        self.pushButton_guide.setText(_translate("Form_cmail", "User Guide"))
        self.pushButton_minimize_4.setToolTip(_translate("Form_cmail", "Minimize to tray menu"))
        self.pushButton_minimize_4.setText(_translate("Form_cmail", "2"))
        self.pushButton_linkedIn.setText(_translate("Form_cmail", "C"))
        self.pushButton_gitHub.setText(_translate("Form_cmail", ")"))
        self.pushButton_email.setText(_translate("Form_cmail", "k"))
        self.pushButton_license.setText(_translate("Form_cmail", "Copyright © 2023 Bedirhan BUDAK"))
        self.label_version.setText(_translate("Form_cmail", "<html><head/><body><p align=\"center\"><span style=\" font-size:11pt; font-weight:600;\">Confirmed Mail</span></p><p align=\"center\"><span style=\" font-style:italic;\">Demo Version</span></p></body></html>"))
        self.tabWidget_cmail.setTabText(self.tabWidget_cmail.indexOf(self.tab_info), _translate("Form_cmail", "Info"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form_cmail = QtWidgets.QWidget()
    ui = Ui_Form_cmail()
    ui.setupUi(Form_cmail)
    Form_cmail.show()
    sys.exit(app.exec_())
