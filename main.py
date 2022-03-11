import sys
import PyQt5
import matplotlib
import matplotlib.pyplot as plt
import numpy as np
from matplotlib.animation import FuncAnimation
from vista.main import Ui_MainWindow as ventanaPrincipal
from algoritmo import *

class MyApp(PyQt5.QtWidgets.QMainWindow, ventanaPrincipal):
    def __init__(self):
        PyQt5.QtWidgets.QMainWindow.__init__(self)
        ventanaPrincipal.__init__(self)
        self.setupUi(self)
        acciones(self)

def acciones(ventana):
    ventana.botonLimpioTodo.clicked.connect(lambda: generarGrafico(ventana))
    #ventana.botonLimpioTodo.clicked.connect(lambda: limpioTodo(ventana))
    ventana.botonGeneroSolucion.clicked.connect(lambda: algoritmoGeneticoGrafica(ventana))

def algoritmoGeneticoGrafica(ventana):
    password = ventana.ingresoPalabra.text()
    AG = inicializoAlgoritmo(password,ventana)
    df = obtenerAG(AG)
    generarGrafico(df)
    creoExcel(df)

def generarGrafico(df):
    #grafica de lineas
    plt.figure(figsize=[6, 6])
    plt.plot(df["generacion"], df["fitness mejor chromosoma"], label="Mejor Chromosoma")
    plt.plot(df["generacion"], df["fitness peor chromosoma"], label="Peor Chromosoma")
    plt.xlabel('Generaciones')  # override the xlabel
    plt.ylabel('Fitness')  # override the ylabel
    plt.title('Grafica de fitness por generacion')  # override the title
    plt.legend()
    plt.show()
    plt.savefig('Grafico de lineas.png')

    #grafica de puntos
    plt.figure(figsize=[6, 6])
    plt.plot(df["generacion"], df["fitness mejor chromosoma"], 'o', color='green', label="Mejor Chromosoma")
    plt.plot(df["generacion"], df["fitness peor chromosoma"], 'o', color='red', label="Peor Chromosoma")
    plt.xlabel('Generaciones')  # override the xlabel
    plt.ylabel('Fitness')  # override the ylabel
    plt.title('Grafica de fitness por cada generacion')  # override the title
    plt.legend()
    plt.show()
    plt.savefig('Grafico de puntos.png')

def creoExcel(df):
    try:
        name = PyQt5.QtWidgets.QFileDialog.getSaveFileName(None, "save csv file", "", "CSV files(*.csv)") #obtener ruta de guardado
        df.to_csv(name[0], index=False) #guardar el archivo
    except:
        print("no selecciono archivo a guardar")


def limpioTodo(ventana):
    ventana.ingresoPalabra.setText("")
    ventana.ingresoPoblacionInicial.setText("")
    ventana.ingresoNumeroGeneraciones.setText("")
    ventana.info1.setText("")
    ventana.info2.setText("")


if __name__ == '__main__':
    app = PyQt5.QtWidgets.QApplication(sys.argv)  # crea un objeto de aplicación (Argumentos de sys)
    window = MyApp()
    window.show()
    window.setFixedSize(window.size())
    app.exec_()