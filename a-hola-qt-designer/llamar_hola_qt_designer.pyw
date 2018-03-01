# -*- coding: utf-8 -*-
u"""Aplicación GUI que usa un script generado a partir de.

llamar_hola_qt_designer.pyw

Esta aplicación muestra un botón de pulsación con el texto 'Limpiar' sobre el
mismo. Cuando se da click en Limpiar se borra el contenido de la caja de texto.

autor: Byron Quezada
web: https://github.com/byque
creado: 01/03/2018

"""
import sys
from PyQt4 import QtGui
from hola_qt_designer import Ui_Dialog


class MiForm(QtGui.QDialog):
    """Clase que importa."""

    def __init__(self, parent=None):
        """Llamar al constructor por defecto de QDialog.

        El constructor por defecto no tiene clase padre.

        """
        super(MiForm, self).__init__(parent)
        self.ui = Ui_Dialog()
        self.ui.setupUi(self)


if __name__ == "__main__":
    app = QtGui.QApplication(sys.argv)
    miapp = MiForm()
    miapp.show()
    sys.exit(app.exec_())
