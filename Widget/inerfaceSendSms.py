from distutils import command
from email import message
from PyQt5.QtWidgets import QMainWindow, QApplication,QFileSystemModel,QFileDialog,QMessageBox
from Widget.app_send_sms import Ui_MainWindow
#from PyQt5.QtGui import QPixmap
#from email.mime.text import MIMEText
#import smtplib
import sqlite3


class AccountPage(QMainWindow,Ui_MainWindow):
    def __init__(self):
        super(AccountPage, self).__init__()
        self.setupUi(self)

        
        self.send_btn.clicked.connect(self.SendSms)
        
    def SendSms(self):
        if self.user_name.text()=="" or self.user_speech.toPlainText()=="" or self.user_number.text()=="":
            QMessageBox.about(self,'infos',"champs obligatoires")
        elif self.user_number.text().isalpha() or self.user_number.text().isspace():
            QMessageBox.warning(self,'alert','number most do a numeric!')
        else:
            if len(self.user_number.text())<0:
                n=QMessageBox.warning(self,"refuse","enregistrement refusé!")
                self.user_number.setText(self.user_number.text()+' short number')
            elif len(self.user_number.text())==10:
                SendSmsDic={
                "user": self.user_name.text(),
                "number": self.user_number.text(),
                "speech": self.user_speech.toPlainText(),#pour obtenir le texte entrer dans "textEdit"
                } 
                #-----------------------connexion----------
                con= sqlite3.connect("base_db.db")

                c=con.cursor()
                
                command="""CREATE TABLE IF NOT EXISTS smsSend(
                    user text,
                    number integer,
                    speech text
                )"""
                c.execute(command)
                #---------------sinsertion des données-----------------------
                command1="INSERT INTO smsSend  VALUES(:user, :number, :speech)"
                c.execute(command1,SendSmsDic)


                con.commit()
                con.close()

                
                
                self.user_name.clear()
                self.user_number.clear()
                self.user_speech.clear()
    
                QMessageBox.about(self,"validate","Succès d'enregistrement \nMessage envoyé avec succès!")
            
    def sendSms(self):
        pass

    