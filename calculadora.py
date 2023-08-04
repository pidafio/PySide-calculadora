from functools import partial

from PySide6.QtCore import Qt
from PySide6.QtWidgets import QMainWindow, QApplication, QWidget, QLineEdit, QLayout, QVBoxLayout, QGridLayout, \
    QPushButton


class Calculadora(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('calculadora')
        self.setFixedSize(250, 260)

        self.componente_general = QWidget(self)
        self.layout_general= QVBoxLayout()

        self.componente_general.setLayout(self.layout_general)
        self.setCentralWidget(self.componente_general)

        self._display_calculadora()
        self._botones_calculadora()

        self._conectar_botones()


    def _display_calculadora(self):
        self.texto_entrada = QLineEdit()
        self.texto_entrada.setFixedHeight(35)
        self.texto_entrada.setAlignment(Qt.AlignRight)
        self.texto_entrada.setReadOnly(True)
        self.layout_general.addWidget(self.texto_entrada)

    def _botones_calculadora(self):
        layout_botones= QGridLayout()
        self.btn = {
            '7': (0, 0), '8': (0, 1), '9': (0, 2), '/': (0, 3),
            '4': (1, 0), '5': (1, 1), '6': (1, 2), '*': (1, 3),
            '1': (2, 0), '2': (2, 1), '3': (2, 2), '-': (2, 3),
            '0': (3, 0), '.': (3, 1), 'c': (3, 2), '+': (3, 3), '=': (3, 4),
        }
        for texto_btn, posicion in self.btn.items():
            self.btn[texto_btn]= QPushButton(texto_btn)
            self.btn[texto_btn].setFixedSize(40,40)
            layout_botones.addWidget(self.btn[texto_btn], posicion[0], posicion[1])
            self.layout_general.addLayout(layout_botones)


    def _conectar_botones(self):
        for texto_boton, boton in self.btn.items():
            if texto_boton not in {'=', 'c'}:
                boton.clicked.connect(partial(self._construir_expresion, texto_boton))
            #opcion1
            elif texto_boton == 'c':
                boton.clicked.connect(self._limpiar_linea_entrada)
            #opcion2
            self.btn['='].clicked.connect(self._calcular_resultado)
            self.texto_entrada.returnPressed.connect(self._calcular_resultado)


    def _construir_expresion(self, texto_boton):
        exprecion=self.texto_entrada.text() + texto_boton
        self.texto_entrada.setText(exprecion)

    def _limpiar_linea_entrada(self):
        self.texto_entrada.setText('')

    def _calcular_resultado(self):
        try:
            resultado= str(eval(self.texto_entrada.text()))
            self.texto_entrada.setText(resultado)
        except Exception as e:
            resultado= self.texto_entrada.setText('error')


if __name__ == '__main__':
    app = QApplication()
    calculadora = Calculadora()
    calculadora.show()
    app.exec()