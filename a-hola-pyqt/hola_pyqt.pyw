# -*- coding: utf-8 -*-
u"""Crear una aplicación GUI con código.

hola_pyqt.pyw

Esta aplicación muestra un botón de pulsación con el texto 'Cerrar' sobre el
mismo. Cuando se da click en Cerrar, la aplicación finaliza.

Las aplicaciones con GUI se pueden guardar con la extensión .pyw para invocar
al interpretador Pythonw.exe en vez del interpretador Python.exe para que no
aparezca una ventana de consola cuando se ejecuta una aplicación Python GUI.

autor: Byron Quezada
web: https://github.com/byque
creado: 01/03/2018

"""
import sys
from PyQt4 import QtGui, QtCore


class VentanaDemo(QtGui.QWidget):
    """Hereda de la clase QWidget.

    QWidget es la clase base para todos los objetos de interfaz de usuario.

    """

    def __init__(self, parent=None):
        """Llamar al constructor por defecto de QWidget.

        El constructor por defecto no tiene clase padre y una widget sin padre
        se conoce como ventana.

        """
        super(VentanaDemo, self).__init__(parent)
        self.setGeometry(300, 300, 250, 100)
        self.setWindowTitle('Ventana Demo')
        salir = QtGui.QPushButton('Cerrar', self)
        salir.setGeometry(10, 10, 70, 40)
        self.connect(salir, QtCore.SIGNAL('clicked()'), QtGui.qApp,
                     QtCore.SLOT('quit()'))


app = QtGui.QApplication(sys.argv)
vd = VentanaDemo()
vd.show()
sys.exit(app.exec_())
