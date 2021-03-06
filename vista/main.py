# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'main.ui'
#
# Created by: PyQt5 UI code generator 5.15.6
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1117, 667)
        MainWindow.setStyleSheet("background-color: rgb(170, 85, 0);")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(270, 40, 671, 51))
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(370, 300, 221, 21))
        self.label_2.setObjectName("label_2")
        self.ingresoPoblacionInicial = QtWidgets.QLineEdit(self.centralwidget)
        self.ingresoPoblacionInicial.setGeometry(QtCore.QRect(360, 340, 231, 22))
        self.ingresoPoblacionInicial.setObjectName("ingresoPoblacionInicial")
        self.ingresoNumeroGeneraciones = QtWidgets.QLineEdit(self.centralwidget)
        self.ingresoNumeroGeneraciones.setGeometry(QtCore.QRect(670, 340, 231, 22))
        self.ingresoNumeroGeneraciones.setObjectName("ingresoNumeroGeneraciones")
        self.botonDescifrado = QtWidgets.QRadioButton(self.centralwidget)
        self.botonDescifrado.setGeometry(QtCore.QRect(700, 390, 181, 20))
        self.botonDescifrado.setStyleSheet("font: 10pt \"MS Shell Dlg 2\";\n"
"color: rgb(255, 255, 255);")
        self.botonDescifrado.setObjectName("botonDescifrado")
        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        self.label_5.setGeometry(QtCore.QRect(100, 190, 201, 31))
        self.label_5.setObjectName("label_5")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(650, 300, 301, 21))
        self.label_3.setObjectName("label_3")
        self.ingresoPalabra = QtWidgets.QLineEdit(self.centralwidget)
        self.ingresoPalabra.setGeometry(QtCore.QRect(320, 190, 661, 31))
        self.ingresoPalabra.setObjectName("ingresoPalabra")
        self.botonGeneroSolucion = QtWidgets.QPushButton(self.centralwidget)
        self.botonGeneroSolucion.setGeometry(QtCore.QRect(400, 490, 171, 61))
        self.botonGeneroSolucion.setStyleSheet("color: rgb(255, 255, 255);\n"
"font: 75 10pt \"MS Shell Dlg 2\";")
        self.botonGeneroSolucion.setObjectName("botonGeneroSolucion")
        self.botonLimpioTodo = QtWidgets.QPushButton(self.centralwidget)
        self.botonLimpioTodo.setGeometry(QtCore.QRect(670, 490, 171, 61))
        self.botonLimpioTodo.setStyleSheet("color: rgb(255, 255, 255);\n"
"font: 75 10pt \"MS Shell Dlg 2\";")
        self.botonLimpioTodo.setObjectName("botonLimpioTodo")
        self.info1 = QtWidgets.QLabel(self.centralwidget)
        self.info1.setGeometry(QtCore.QRect(100, 740, 431, 21))
        self.info1.setObjectName("info1")
        self.info2 = QtWidgets.QLabel(self.centralwidget)
        self.info2.setGeometry(QtCore.QRect(650, 740, 431, 21))
        self.info2.setObjectName("info2")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1117, 26))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:14pt; font-weight:600; color:#ffffff;\">Descifrador De Contrase??as Usando Algoritmos Geneticos</span></p></body></html>"))
        self.label_2.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:10pt; font-weight:600; color:#ffffff;\">Ingrese Poblacion Inicial</span></p><p><span style=\" font-size:10pt;\"><br/></span></p></body></html>"))
        self.botonDescifrado.setText(_translate("MainWindow", "Descifrado Completo"))
        self.label_5.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:14pt; font-weight:600; color:#ffffff;\">Ingrese Palabra</span></p></body></html>"))
        self.label_3.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:10pt; font-weight:600; color:#ffffff;\">Ingrese Numero De Generaciones<br/></span></p></body></html>"))
        self.botonGeneroSolucion.setText(_translate("MainWindow", "Generar Solucion"))
        self.botonLimpioTodo.setText(_translate("MainWindow", "Limpiar Todo"))
        self.info1.setText(_translate("MainWindow", "<html><head/><body><p><br/></p></body></html>"))
        self.info2.setText(_translate("MainWindow", "<html><head/><body><p><br/></p></body></html>"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
