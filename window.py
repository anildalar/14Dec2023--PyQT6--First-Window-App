#1. Import Area
from mypackage.mysubmodule import Parent,Child
from PyQt7.QtWidgets import QApplication,QWidget


#2. Create Class Object
co = Parent()
co.sayHello()


app = QApplication("Anil")

app.exec()


window = QWidget()
window.show()

