import sys
from PyQt6.QtWidgets import QMainWindow, QApplication, QPushButton
from all import Ui_MainWindow

class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow,self).__init__()

        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.ui.stackedWidget.setCurrentIndex(0)

        self.ui.btsave.clicked.connect(self.show_page_5)
        self.ui.btsave1.clicked.connect(self.show_page)

    def show_page_5(self):
        self.ui.stackedWidget.setCurrentWidget(self.ui.page_5)

    def show_page(self):
        self.ui.stackedWidget.setCurrentWidget(self.ui.page)

    def on_user_btn_clicked(self):
        self.ui.stackedWidget.currentIndex(5)

    def on_stackedWidget_currentChange(self, index):
        btn_list = self.ui.menu_widget.findChildren(QPushButton) + self.ui.save_widget.findChildren(QPushButton)
        for btn in btn_list:
            if index in [5,6]:
                btn.setAutoExclusive(False)
                btn.setChecked(False)
            else:
                btn.setAutoExclusive(True)

    def on_bthome_toggled(self):
        self.ui.stackedWidget.setCurrentIndex(0)
    def on_bthistory_toggled(self):
        self.ui.stackedWidget.setCurrentIndex(1)
    def on_bthospital_toggled(self):
        self.ui.stackedWidget.setCurrentIndex(2)
    def on_btsetting_toggled(self):
        self.ui.stackedWidget.setCurrentIndex(3)
    def on_btsave_toggled(self):
        self.ui.stackedWidget.setCurrentIndex(4)

if __name__ == "__main__":
    app = QApplication(sys.argv)

    window = MainWindow()
    window.show()

    sys.exit(app.exec())