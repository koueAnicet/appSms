import sys
from PyQt5.QtWidgets import QMainWindow, QApplication
from Widget.inerfaceSendSms import AccountPage


 
def main():
    app = QApplication(sys.argv)
    home = AccountPage()
    home.show()
    app.exec_()


if __name__ == '__main__':
    main()