from PyQt5.QtWidgets import *
from PyQt5.QtCore import QThread, pyqtSignal, Qt, QUrl
from PyQt5.QtGui import QColor, QIcon, QDesktopServices
from PyQt5 import QtWidgets
from design import Ui_Form_cmail
import re
import os
import cmail


# Main Class
class Cmail(QtWidgets.QMainWindow, Ui_Form_cmail):
    def __init__(self):
        super().__init__()
        QThread.__init__(self)
        self.uiDesign = Ui_Form_cmail()
        self.uiDesign.setupUi(self)
        self.thread = LoopThread()
        os.environ["QT_AUTO_SCREEN_SCALE_FACTOR"] = "1"

        # Delete Window Flame
        #self.setWindowFlags(Qt.FramelessWindowHint)
        #self.setAttribute(Qt.WA_TranslucentBackground)

        # Icon
        self.setWindowIcon(QIcon("C:/Users/bedir/PycharmProjects/CMail/images/logo.png"))

        # Cmail Tab
        self.uiDesign.pushButton_stop.setEnabled(False)
        self.uiDesign.pushButton_deleteInfo.setEnabled(False)
        self.uiDesign.pushButton_deleteAll.setEnabled(False)

        # SHORTCUT
        self.uiDesign.lineEdit_mail.setText("project.confirmedmail@gmail.com")
        self.uiDesign.lineEdit_password.setText("oqpdhimwwadhbzqe")
        # -------------------------------

        cmail.my_mail = self.uiDesign.lineEdit_mail.text()
        cmail.my_password = self.uiDesign.lineEdit_password.text()

        self.uiDesign.pushButton_start.clicked.connect(self.clicked_on_start)
        self.uiDesign.pushButton_stop.clicked.connect(self.clicked_on_stop)
        self.uiDesign.pushButton_deleteInfo.clicked.connect(self.del_info)
        self.uiDesign.pushButton_deleteAll.clicked.connect(self.del_mail)

        self.uiDesign.label_status.setAlignment(Qt.AlignCenter)
        self.uiDesign.label_status.setStyleSheet("color: black; font:Helvatica; font-size: 10px;")

        # Logs Tab
        self.uiDesign.textBrowser_logsContent.setReadOnly(True)
        self.uiDesign.pushButton_logsClear.clicked.connect(self.uiDesign.textBrowser_logsContent.clear)

        # Settings Tab
        self.thread.mail_signal.connect(self.logs_mail)
        self.thread.info_signal.connect(self.logs_info)
        self.thread.cmail_signal.connect(self.logs_cmail)
        self.uiDesign.pushButton_background.clicked.connect(self.background_clicked)
        self.uiDesign.pushButton_confirmServices.clicked.connect(self.confirm_services)

        self.uiDesign.checkBox_notification.stateChanged.connect(self.check_notification)
        self.uiDesign.checkBox_deleteInfo.stateChanged.connect(self.check_deleteInfo)
        self.uiDesign.checkBox_checkService.stateChanged.connect(self.check_services)

        # EXIT
        self.uiDesign.pushButton_exit.clicked.connect(self.exit_app)
        # --------------------------------------

        # About Me
        self.uiDesign.pushButton_linkedIn.clicked.connect(self.contact_linkedin)
        self.uiDesign.pushButton_gitHub.clicked.connect(self.contact_github)
        self.uiDesign.pushButton_mail.clicked.connect(self.contact_mail)

        # Background Processes
        self.tray_icon = QtWidgets.QSystemTrayIcon(self)
        self.tray_icon.setIcon(QIcon("C:/Users/bedir/PycharmProjects/CMail/images/logo.png"))
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

    # Background Functions
    def background_clicked(self):
        self.message_box_information("Information", "Cmail is running in background.")
        self.add_log("Cmail is backgrounded.")
        self.hide()

    def on_tray_icon_clicked(self, reason):
        if reason == QtWidgets.QSystemTrayIcon.DoubleClick:
            self.showNormal()

    # Check if Given Mail Address is Valid
    def check_gmail(self):
        text = self.uiDesign.lineEdit_mail.text()
        email_regex = re.compile(r'[\w\.-]+@[\w\.-]+\.[\w\.-]')
        if email_regex.match(text):
            return True
        else:
            return False

    # Account Links
    def contact_linkedin(self):
        QDesktopServices.openUrl(QUrl('https://www.linkedin.com/in/bedirhanbudak/'))

    def contact_github(self):
        QDesktopServices.openUrl(QUrl('https://github.com/bedirhanbudak'))

    def contact_mail(self):
        QDesktopServices.openUrl(QUrl(f"mailto:bedirhanbudak_bb@hotmal.com"))

    # Connected with pushButton_start
    def clicked_on_start(self):
        if self.check_gmail():
            self.uiDesign.label_checkMsg.clear()
            self.thread.start()
            self.uiDesign.label_status.setText("Cmail is running.")
            self.uiDesign.label_status.setStyleSheet("color: green;")
            self.uiDesign.pushButton_stop.setEnabled(True)
            self.uiDesign.pushButton_start.setEnabled(False)
            self.uiDesign.pushButton_deleteInfo.setEnabled(True)
            self.uiDesign.pushButton_deleteAll.setEnabled(True)
            self.uiDesign.lineEdit_mail.setEnabled(False)
            self.uiDesign.lineEdit_password.setEnabled(False)
            if self.uiDesign.checkBox_notification.isChecked():
                self.message_box_information("Confirmed Info", "Cmail has been started.")
            self.add_log("Cmail has been started.")
        else:
            self.uiDesign.label_checkMsg.setText("Incorrect mail format!")
            self.message_box_information("Error", "Invalid Mail Address!")
            self.add_log("Invalid mail address entered.")

    # Connected with pushButton_stop
    def clicked_on_stop(self):
        self.thread.stop()
        self.uiDesign.label_status.setText("Cmail has stopped.")
        self.uiDesign.label_status.setStyleSheet("color: red;")
        self.uiDesign.pushButton_start.setEnabled(True)
        self.uiDesign.pushButton_stop.setEnabled(False)
        self.uiDesign.pushButton_deleteInfo.setEnabled(False)
        self.uiDesign.pushButton_deleteAll.setEnabled(False)
        self.uiDesign.lineEdit_mail.setEnabled(True)
        self.uiDesign.lineEdit_password.setEnabled(True)
        if self.uiDesign.checkBox_notification.isChecked():
            self.message_box_information("Confirmed Info", "Cmail has been stopped.")
        self.add_log("Cmail has been stopped.")

    # Connected with pushButton_confirmServices
    def confirm_services(self):
        cmail.imap_protocol = self.uiDesign.lineEdit_imap.text()
        cmail.smtp_protocol = self.uiDesign.lineEdit_smtpProtocol.text()
        cmail.smtp_port = self.uiDesign.lineEdit_smtpPort.text()
        print(cmail.imap_protocol)
        print(cmail.smtp_protocol)
        print(cmail.smtp_port)

    # Connected with pushButton_deleteInfo
    def del_info(self):
        self.message_box_question("Are you sure you want to delete \"Confirmed Mails\"?",
                                  self.thread.delete_info, self.uiDesign.pushButton_deleteInfo.setEnabled,
                                  "\"Confirmed Mails\" deleted.")

    # Connected with pushButton_deleteAll
    def del_mail(self):
        self.message_box_question("Are you sure you want to delete all except \"Confirmed Mails\"?",
                                  self.thread.delete_mail, self.uiDesign.pushButton_deleteAll.setEnabled,
                                  "All mails deleted except \"Confirmed Mails\"")

    # Incoming Mail Information
    def logs_mail(self):
        cmail.logs["mail"] = False
        self.add_log("You have a new mail!")

    def logs_info(self):
        cmail.logs["info"] = False
        self.add_log("You have a new Confirmation Mail.")

    def logs_cmail(self):
        cmail.logs["cmail"] = False
        self.uiDesign.textBrowser_logsContent.setTextColor(QColor('green'))
        self.uiDesign.textBrowser_logsContent.append("You have a new Confirmed Mail!")
        self.uiDesign.textBrowser_logsContent.setTextColor(QColor('black'))
        if self.uiDesign.checkBox_notification.isChecked():
            self.message_box_information("Confirmed Mail", "You have a new Confirmed Mail!")

    # CheckBoxes
    def check_notification(self):
        if self.uiDesign.checkBox_notification.isChecked():
            self.add_log("Notifications will be shown.")
        if not self.uiDesign.checkBox_notification.isChecked():
            self.add_log("Notifications will not be shown.")

    def check_deleteInfo(self):
        if self.uiDesign.checkBox_deleteInfo.isChecked():
            cmail.logs["del_info"] = True
            self.add_log("\"Confirmed Mails\" will be deleted after reading.")
        if not self.uiDesign.checkBox_deleteInfo.isChecked():
            self.add_log("\"Confirmed Mails\" will not be deleted after reading.")

    def check_services(self):
        if self.uiDesign.checkBox_checkService.isChecked():
            self.uiDesign.lineEdit_imap.setEnabled(True)
            self.uiDesign.lineEdit_smtpProtocol.setEnabled(True)
            self.uiDesign.lineEdit_smtpPort.setEnabled(True)
            self.uiDesign.pushButton_confirmServices.setEnabled(True)
            self.uiDesign.checkBox_checkService.setEnabled(False)

        if not self.uiDesign.checkBox_checkService.isChecked():
            self.uiDesign.lineEdit_imap.setEnabled(False)
            self.uiDesign.lineEdit_smtpProtocol.setEnabled(False)
            self.uiDesign.lineEdit_smtpPort.setEnabled(False)
            self.uiDesign.pushButton_confirmServices.setEnabled(False)

    # Add logs to textEdit_logs
    def add_log(self, text):
        self.uiDesign.textBrowser_logsContent.append("- " + text)

    # MessageBox for Information
    def message_box_information(self, title, text):
        msg = QMessageBox()
        msg.setIcon(QMessageBox.Information)
        msg.setWindowTitle(title)
        msg.setText(text)
        msg.setStandardButtons(QMessageBox.Ok)
        msg.exec_()

    # MessageBox for Questions
    def message_box_question(self, text, function, button, log):
        msg = QMessageBox()
        msg.setIcon(QMessageBox.Question)
        msg.setText(text)
        msg.setWindowTitle("Confirmation Message")
        msg.setStandardButtons(QMessageBox.Yes | QMessageBox.No)
        retval = msg.exec_()

        if retval == QMessageBox.Yes:
            function()
            button(False)
            if self.uiDesign.checkBox_notification.isChecked():
                msg = QMessageBox()
                msg.setIcon(QMessageBox.Information)
                msg.setText("Deleted")
                msg.setWindowTitle("Confirmed Info")
                msg.setStandardButtons(QMessageBox.Ok)
                msg.exec_()
            self.add_log(log)
        else:
            if self.uiDesign.checkBox_notification.isChecked():
                msg = QMessageBox()
                msg.setIcon(QMessageBox.Information)
                msg.setText("Cancelled")
                msg.setWindowTitle("Confirmed Info")
                msg.setStandardButtons(QMessageBox.Ok)
                msg.exec_()

    # ExitFunction
    def exit_app(self):
        cmail.exit_app()
        app.exit()


# Threads
class LoopThread(QThread):
    # Signals
    mail_signal = pyqtSignal()
    info_signal = pyqtSignal()
    cmail_signal = pyqtSignal()
    del_confirmed = pyqtSignal()

    def __init__(self):
        QThread.__init__(self)
        self.running = False

    # Run in Loop
    def run(self):
        self.running = True
        while self.running:
            cmail.start()
            if cmail.logs["mail"]:
                self.mail_signal.emit()
            if cmail.logs["info"]:
                self.info_signal.emit()
            if cmail.logs["cmail"]:
                self.cmail_signal.emit()

    # Break the Loop
    def stop(self):
        self.running = False

    # Delete Information Mails
    def delete_info(self):
        cmail.del_info()

    # Delete all mails except Flagged ones
    def delete_mail(self):
        cmail.del_mail()


# Show App
app = QApplication([])
app.setAttribute(Qt.AA_EnableHighDpiScaling, True)
window = Cmail()
#window.resize(1600, 900)
window.show()
app.exec_()
