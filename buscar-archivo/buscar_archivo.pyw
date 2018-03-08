# -*- coding: utf-8 -*-
u"""Buscar un archivo.

buscar_archivo.pyw

Esta aplicación muestra un botón de pulsación con el texto 'Buscar'. Cuando se
hace click en Buscar, la aplicación abre el gestor de archivos nativo del
sistema. Una vez seleccionado el archivo, el programa copia la ruta del archivo
a un cuadro de texto.

autor: Byron Quezada
web: https://github.com/byque
creado: 07/03/2018

"""
import sys
from PyQt4 import QtCore, QtGui
from PyQt4.QtGui import QApplication, QDialog
from PyQt4.QtGui import QPlainTextEdit, QPushButton, QFileDialog
from PyQt4.QtCore import QString


class VentanaDemo(QDialog):
    """Hereda de la clase QDialog."""

    def __init__(self, parent=None):
        """Llamar al constructor por defecto de QDialog."""
        super(VentanaDemo, self).__init__(parent)

        self.ruta_archivo = QString()

        # Parámetros de la ventana de diálogo
        self.setGeometry(300, 300, 400, 100)
        self.setWindowTitle('Buscar Archivo')

        # Crear el cuadro de texto para mostrar la ruta del archivo
        self.ruta_gui = QPlainTextEdit(self.ruta_archivo, self)
        self.ruta_gui.setGeometry(10, 10, 300, 25)

        # Crear el botón para buscar un archivo
        self.buscar_btn = QPushButton('Buscar', self)
        self.buscar_btn.setGeometry(320, 10, 70, 40)
        # Demo de método stático para QFileDialog
        self.connect(self.buscar_btn, QtCore.SIGNAL('clicked()'),
                     self.get_ruta)

        # Crear el botón para salir del programa
        self.salir_btn = QPushButton('Cerrar', self)
        self.salir_btn.setGeometry(320, 50, 70, 40)
        self.connect(self.salir_btn, QtCore.SIGNAL('clicked()'), QtGui.qApp,
                     QtCore.SLOT('quit()'))

    def get_ruta(self):
        """Abrir QFileDialog."""
        self.ruta_archivo = QFileDialog.getOpenFileName(self, 'Open file',
                                                        'c:\\')
        self.ruta_gui.setPlainText(self.ruta_archivo)


def main():
    """Definir un programa con main."""
    app = QApplication(sys.argv)
    vd = VentanaDemo()
    vd.show()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()
