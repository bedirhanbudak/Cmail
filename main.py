from PyQt5.QtWidgets import *
from PyQt5.QtCore import QThread, pyqtSignal, Qt, QUrl, QPoint
from PyQt5.QtGui import QColor, QIcon, QDesktopServices
from PyQt5 import QtWidgets
from design import Ui_Form_cmail
import re
import os
import imaplib
import cmail


# Main Class
class Cmail(QtWidgets.QMainWindow, Ui_Form_cmail):
    def __init__(self):
        super().__init__()  # Call the parent class constructor
        QThread.__init__(self)  # Initialize the QThread base class
        self.uiDesign = Ui_Form_cmail()  # Instance of Ui_Form_cmail
        self.uiDesign.setupUi(self)  # Set up the UI design
        self.thread = LoopThread()  # Instance of LoopThread
        os.environ["QT_AUTO_SCREEN_SCALE_FACTOR"] = "1"

        # Setting the Window Title
        self.setWindowTitle("Cmail")

        # Delete Window Flame
        self.setWindowFlags(Qt.FramelessWindowHint)
        self.setAttribute(Qt.WA_TranslucentBackground)

        # Icon
        self.setWindowIcon(QIcon("images/logo.png"))

        # Cmail Tab
        self.uiDesign.pushButton_stop.setEnabled(False)
        self.uiDesign.pushButton_infoDEL.setEnabled(False)
        self.uiDesign.pushButton_allDEL.setEnabled(False)
        self.uiDesign.label_invalid.clear()

        self.setTabOrder(self.uiDesign.lineEdit_email, self.uiDesign.lineEdit_password)
        self.setTabOrder(self.uiDesign.lineEdit_password, self.uiDesign.pushButton_start)
        self.setTabOrder(self.uiDesign.pushButton_start, self.uiDesign.pushButton_stop)
        self.uiDesign.lineEdit_password.returnPressed.connect(self.uiDesign.pushButton_start.click)
        self.uiDesign.lineEdit_email.returnPressed.connect(self.uiDesign.pushButton_start.click)

        self.uiDesign.pushButton_start.clicked.connect(self.clicked_on_start)
        self.uiDesign.pushButton_stop.clicked.connect(self.clicked_on_stop)
        self.thread.error_signal.connect(self.login_error)

        # Logs Tab
        self.uiDesign.textBrowser_logHistory.setReadOnly(True)
        self.uiDesign.pushButton_clearLogs.clicked.connect(self.uiDesign.textBrowser_logHistory.clear)

        # Settings Tab
        self.thread.email_signal.connect(self.logs_email)
        self.thread.info_signal.connect(self.logs_info)
        self.thread.cmail_signal.connect(self.logs_cmail)

        self.uiDesign.pushButton_infoDEL.clicked.connect(self.del_info)
        self.uiDesign.pushButton_allDEL.clicked.connect(self.del_email)

        self.uiDesign.checkBox_notifications.stateChanged.connect(self.check_notification)
        self.uiDesign.checkBox_autoDEL.stateChanged.connect(self.check_deleteInfo)

        # Info
        self.uiDesign.pushButton_linkedIn.clicked.connect(self.contact_linkedin)
        self.uiDesign.pushButton_gitHub.clicked.connect(self.contact_github)
        self.uiDesign.pushButton_email.clicked.connect(self.contact_email)
        self.uiDesign.pushButton_guide.clicked.connect(self.link_guide)
        self.uiDesign.pushButton_license.clicked.connect(self.link_license)

        # Minimize & Quit Buttons
        self.uiDesign.pushButton_minimize_1.clicked.connect(self.background_clicked)
        self.uiDesign.pushButton_minimize_2.clicked.connect(self.background_clicked)
        self.uiDesign.pushButton_minimize_3.clicked.connect(self.background_clicked)
        self.uiDesign.pushButton_minimize_4.clicked.connect(self.background_clicked)
        self.uiDesign.pushButton_exit_1.clicked.connect(self.exit_app)
        self.uiDesign.pushButton_exit_2.clicked.connect(self.exit_app)
        self.uiDesign.pushButton_exit_3.clicked.connect(self.exit_app)
        self.uiDesign.pushButton_exit_4.clicked.connect(self.exit_app)

        # Tray menu processes
        self.tray_icon = QtWidgets.QSystemTrayIcon(self)
        self.tray_icon.setIcon(QIcon("images/logo.png"))
        self.tray_icon.setToolTip("Cmail is running in background.")
        self.tray_icon.show()
        self.tray_icon.activated.connect(self.on_tray_icon_clicked)
        show_action = QtWidgets.QAction("Show", self)
        show_action.triggered.connect(self.showNormal)
        minimize_action = QtWidgets.QAction("Hide", self)
        minimize_action.triggered.connect(self.hide)
        quit_action = QtWidgets.QAction("Quit", self)
        quit_action.triggered.connect(QtWidgets.qApp.quit)
        tray_menu = QtWidgets.QMenu()
        tray_menu.addAction(show_action)
        tray_menu.addAction(minimize_action)
        tray_menu.addSeparator()
        tray_menu.addAction(quit_action)
        self.tray_icon.setContextMenu(tray_menu)

    # Connected to pushButton_start
    def clicked_on_start(self):
        if self.check_format() and not self.uiDesign.lineEdit_password.text().strip() == "":
            cmail.user_email_address = self.uiDesign.lineEdit_email.text()
            cmail.user_password = self.uiDesign.lineEdit_password.text()
            cmail.imap_protocol = self.uiDesign.lineEdit_imapServer.text()
            cmail.smtp_protocol = self.uiDesign.lineEdit_smtpServer.text()
            cmail.smtp_port = self.uiDesign.lineEdit_smtpPort.text()
            self.uiDesign.label_invalid.clear()
            self.thread.start()
            self.uiDesign.label_status.setText("Cmail is running")
            self.uiDesign.label_status.setStyleSheet("color: green;")
            self.uiDesign.pushButton_stop.setEnabled(True)
            self.uiDesign.pushButton_start.setEnabled(False)
            self.uiDesign.pushButton_infoDEL.setEnabled(True)
            self.uiDesign.pushButton_allDEL.setEnabled(True)
            self.uiDesign.lineEdit_email.setEnabled(False)
            self.uiDesign.lineEdit_password.setEnabled(False)
            self.uiDesign.lineEdit_imapServer.setEnabled(False)
            self.uiDesign.lineEdit_smtpServer.setEnabled(False)
            self.uiDesign.lineEdit_smtpPort.setEnabled(False)
            if self.uiDesign.checkBox_notifications.isChecked():
                self.message_box_information("Confirmed Info", "Cmail has been started.")
            self.add_log("Cmail has been started.")
        else:
            self.uiDesign.label_invalid.setText("Invalid format")
            self.message_box_information("Error", "Invalid e-mail address or password!")
            self.add_log("Invalid e-mail address or password entered.")

    # Connected to pushButton_stop
    def clicked_on_stop(self):
        self.thread.stop()
        self.uiDesign.label_status.setText("Cmail has stopped")
        self.uiDesign.label_status.setStyleSheet("color: red;")
        self.uiDesign.pushButton_start.setEnabled(True)
        self.uiDesign.pushButton_stop.setEnabled(False)
        self.uiDesign.pushButton_infoDEL.setEnabled(False)
        self.uiDesign.pushButton_allDEL.setEnabled(False)
        self.uiDesign.lineEdit_email.setEnabled(True)
        self.uiDesign.lineEdit_password.setEnabled(True)
        self.uiDesign.lineEdit_imapServer.setEnabled(True)
        self.uiDesign.lineEdit_smtpServer.setEnabled(True)
        self.uiDesign.lineEdit_smtpPort.setEnabled(True)
        if self.uiDesign.checkBox_notifications.isChecked():
            self.message_box_information("Confirmed Info", "Cmail has been stopped.")
        self.add_log("Cmail has been stopped.")
        cmail.confirmation_codes.clear()
        cmail.logs = {key: False for key in cmail.logs}

    # Check if Given E-Mail Address is Valid
    def check_format(self):
        text = self.uiDesign.lineEdit_email.text()
        email_regex = re.compile(r'[\w\.-]+@[\w\.-]+\.[\w\.-]')
        if email_regex.match(text):
            return True
        else:
            return False

    # Connected to error_signal
    def login_error(self):
        if self.uiDesign.checkBox_notifications.isChecked():
            self.message_box_information("Error", "The e-mail address or password is incorrect!")
        self.add_log("Failed to login!")
        self.uiDesign.label_invalid.setText("Login failed")
        self.clicked_on_stop()

    # Incoming e-mail information
    def logs_email(self):
        cmail.logs["email"] = False  # Set to default value to reuse
        self.add_log("You have a new e-mail!")

    def logs_info(self):
        cmail.logs["info"] = False  # Set to default value to reuse
        self.add_log("You have a new information e-mail.")

    def logs_cmail(self):
        cmail.logs["cmail"] = False  # Set to default value to reuse
        self.uiDesign.textBrowser_logHistory.setTextColor(QColor('green'))
        self.add_log("You have a new Confirmed Mail!")
        self.uiDesign.textBrowser_logHistory.setTextColor(QColor('white'))
        if self.uiDesign.checkBox_notifications.isChecked():
            self.message_box_information("Confirmed Mail", "You have a new Confirmed Mail!")

    # Connected to pushButton_infoDEL
    def del_info(self):
        self.message_box_question("Are you sure you want to delete information e-mails?",
                                  self.thread.delete_info, self.uiDesign.pushButton_infoDEL.setEnabled,
                                  "Information e-mails deleted.")

    # Connected to pushButton_allDEL
    def del_email(self):
        self.message_box_question("Are you sure you want to delete all except Confirmed Mails?",
                                  self.thread.delete_email, self.uiDesign.pushButton_allDEL.setEnabled,
                                  "All e-mails deleted except Confirmed Mails.")

    # Checkboxes
    def check_notification(self):
        if self.uiDesign.checkBox_notifications.isChecked():
            self.add_log("Notifications will be displayed.")
        if not self.uiDesign.checkBox_notifications.isChecked():
            self.add_log("Notifications will not be displayed.")

    def check_deleteInfo(self):
        if self.uiDesign.checkBox_autoDEL.isChecked():
            cmail.logs["del_info"] = True  # Auto delete on
            self.add_log("Information e-mails will be deleted after reading.")
        if not self.uiDesign.checkBox_autoDEL.isChecked():
            cmail.logs["del_info"] = False  # Auto delete off
            self.add_log("Information e-mails will not be deleted after reading.")

    # Account Links
    def contact_linkedin(self):  # LinkedIn address
        QDesktopServices.openUrl(QUrl('https://linkedin.com/in/bedirhanbudak/'))

    def contact_github(self):  # GitHub address
        QDesktopServices.openUrl(QUrl('https://github.com/bedirhanbudak'))

    def contact_email(self):  # E-mail address
        QDesktopServices.openUrl(QUrl(f"mailto:bedirhan.budak@hotmail.com"))

    def link_guide(self):  # Cmail GitHub Page
        QDesktopServices.openUrl(QUrl("https://github.com/bedirhanbudak/Cmail"))

    def link_license(self):  # License message box
        self.message_box_information("License", "Confirmed Mail Demo Version\n\n" +
                                     "Copyright © 2023 Bedirhan Budak\n" +
                                     "under GNU GPL v3 license")

    # Background Functions
    def background_clicked(self):
        self.message_box_information("Information", "Cmail is minimized.")
        self.add_log("Cmail is minimized.")
        self.hide()  # Hide the interface

    def on_tray_icon_clicked(self, reason):
        if reason == QtWidgets.QSystemTrayIcon.DoubleClick:
            self.showNormal()  # Show the interface

    # Exit Function
    def exit_app(self):
        msg = QMessageBox()  # Create an instance of QMessageBox
        msg.setIcon(QMessageBox.Question)
        msg.setText("Are you sure you want to quit Cmail?")
        msg.setWindowTitle("Confirmation Message")
        msg.setStandardButtons(QMessageBox.Ok | QMessageBox.Cancel)
        retval = msg.exec_()  # The value returned by exec_()

        if retval == QMessageBox.Ok:  # If the "OK" button is pressed
            app.exit()  # Exit the application

    # Add logs to textEdit_logs
    def add_log(self, text):
        self.uiDesign.textBrowser_logHistory.append("- " + text)

    # MessageBox for Information
    def message_box_information(self, title, text):
        msg = QMessageBox()  # Create an instance of QMessageBox
        msg.setIcon(QMessageBox.Information)
        msg.setWindowTitle(title)
        msg.setText(text)
        msg.setStandardButtons(QMessageBox.Ok)
        msg.exec_()  # Show the message box

    # MessageBox for Questions
    def message_box_question(self, text, function, button, log):
        msg = QMessageBox()  # Create an instance of QMessageBox
        msg.setIcon(QMessageBox.Question)
        msg.setText(text)
        msg.setWindowTitle("Confirmation Message")
        msg.setStandardButtons(QMessageBox.Yes | QMessageBox.No)
        retval = msg.exec_()  # The value returned by exec_()
        if retval == QMessageBox.Yes:  # If the "Yes" button is pressed
            function()  # Call the function
            button(False)  # Set the button
            if self.uiDesign.checkBox_notifications.isChecked():
                msg = QMessageBox()  # Create an instance of QMessageBox
                msg.setIcon(QMessageBox.Information)
                msg.setText("Deleted successfully")
                msg.setWindowTitle("Confirmed Info")
                msg.setStandardButtons(QMessageBox.Ok)
                msg.exec_()
            self.add_log(log)  # Add log record
        else:
            if self.uiDesign.checkBox_notifications.isChecked():
                msg = QMessageBox()  # Create an instance of QMessageBox
                msg.setIcon(QMessageBox.Information)
                msg.setText("Cancelled by user")
                msg.setWindowTitle("Confirmed Info")
                msg.setStandardButtons(QMessageBox.Ok)
                msg.exec_()  # Show the message box

    # Draggable frameless window
    def mousePressEvent(self, event):
        self.oldPos = event.globalPos()

    def mouseMoveEvent(self, event):
        delta = QPoint(event.globalPos() - self.oldPos)
        self.move(self.x() + delta.x(), self.y() + delta.y())
        self.oldPos = event.globalPos()

    def _resize(self):
        window = self.window().windowHandle()
        window.startSystemResize(Qt.LeftEdge)


# Threads
class LoopThread(QThread):
    # Signals
    email_signal = pyqtSignal()
    info_signal = pyqtSignal()
    cmail_signal = pyqtSignal()
    del_confirmed = pyqtSignal()
    error_signal = pyqtSignal()

    def __init__(self):
        QThread.__init__(self)
        self.running = False

    # Running in Loop
    def run(self):
        self.running = True  # The thread is running
        while self.running:  # While the thread is running
            try:
                cmail.start()  # Call the start() function from cmail.py
            except imaplib.IMAP4.error:  # If a login error occurs
                self.running = False  # Terminate the loop
                self.error_signal.emit()
            if cmail.logs["email"]:  # New e-mail log record
                self.email_signal.emit()
            if cmail.logs["info"]:  # New information e-mail log record
                self.info_signal.emit()
            if cmail.logs["cmail"]:  # New Confirmed Mail log record
                self.cmail_signal.emit()

    # Break the Loop
    def stop(self):
        self.running = False  # Terminate the loop

    # Delete information e-mails
    def delete_info(self):
        cmail.del_info()  # Call the del_info function from cmail.py

    # Delete all e-mails except flagged ones
    def delete_email(self):
        cmail.del_email()  # Call the del_email function from cmail.py


# Show App
app = QApplication([])  # Create an instance of the QApplication
app.setAttribute(Qt.AA_EnableHighDpiScaling, True)
window = Cmail()  # Create an instance of Cmail
window.show()  # Display the window
app.exec_()  # Show the application
