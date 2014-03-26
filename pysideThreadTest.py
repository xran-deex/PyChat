import sys, time
from PySide.QtCore import *
from PySide.QtGui  import *
 
class Main(QWidget):
 
    def __init__(self, parent=None):
        super(Main, self).__init__(parent)
 
        layout = QVBoxLayout(self)
 
        button = QPushButton("Press me")
        self.label = QLabel("Run #")
 
        map(layout.addWidget, [button, self.label])
        button.pressed.connect(self.buttonPressed)
 
    def buttonPressed(self):
        Thread().run(self.label)
 
class Thread(QThread):
 
    def run(self, label):
        for x in range(50):
            self.updateLabel(label)
            app.processEvents()
            time.sleep(.5)
 
    def updateLabel(self, label):
        try:
            number = int(label.text().split(" ")[-1])
            number += 1
        except ValueError:
            number = 0
        label.setText("Run %i" % number)
 
app = QApplication([])
main = Main()
main.show()
sys.exit(app.exec_())