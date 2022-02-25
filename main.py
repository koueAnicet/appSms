from PySide2 import QtWidgets 

class App(QtWidgets.QtWidget):
    def __init__(self) -> None:
        super().__init__()
        self.setWindowTitle("Horloge")

app=QtWidgets.QApplication()
win =App()
win.show
app.excet

