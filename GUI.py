import sys

from calculatora_tempo import adicionar_tempo
from PyQt5.QtWidgets import (
    QApplication, QWidget, QVBoxLayout, QHBoxLayout, QLabel, QLineEdit, QComboBox, QPushButton, QTextEdit
)
from PyQt5.QtCore import pyqtSlot


class CalculadoraTempo(QWidget):
    def __init__(self):
        super().__init__()

        self.resultados = None
        self.calcular_botao = None
        self.horas_somar = None
        self.dia_selecao = None
        self.ampm_selecao = None
        self.minuto_input = None
        self.hora_input = None
        self.initUI()

    def initUI(self):
        main_layout = QVBoxLayout()

        tempo_layout = QHBoxLayout()
        self.hora_input = QLineEdit(self)
        self.hora_input.setPlaceholderText('HH')
        self.minuto_input = QLineEdit(self)
        self.minuto_input.setPlaceholderText('MM')
        self.ampm_selecao = QComboBox(self)
        self.ampm_selecao.addItems(['AM', 'PM'])
        tempo_layout.addWidget(QLabel('Tempo:'))
        tempo_layout.addWidget(self.hora_input)
        tempo_layout.addWidget(self.minuto_input)
        tempo_layout.addWidget(self.ampm_selecao)

        dia_layout = QHBoxLayout()
        self.dia_selecao = QComboBox(self)
        self.dia_selecao.addItems(['Domingo', 'Segunda', 'Terça', 'Quarta', 'Quinta', 'Sexta', 'Sábado'])
        dia_layout.addWidget(QLabel('Dia:'))
        dia_layout.addWidget(self.dia_selecao)

        soma_horas_layout = QHBoxLayout()
        self.horas_somar = QLineEdit(self)
        self.horas_somar.setPlaceholderText('11:11')
        soma_horas_layout.addWidget(QLabel('Horas para Somar:'))
        soma_horas_layout.addWidget(self.horas_somar)

        botao_layout = QHBoxLayout()
        self.calcular_botao = QPushButton('Calcular', self)
        self.calcular_botao.clicked.connect(self.onClick)

        botao_layout.addWidget(self.calcular_botao)

        self.resultados = QTextEdit(self)
        self.resultados.setReadOnly(True)
        self.resultados.setFixedSize(400, 50)

        main_layout.addLayout(tempo_layout)
        main_layout.addLayout(dia_layout)
        main_layout.addLayout(soma_horas_layout)
        main_layout.addLayout(botao_layout)
        main_layout.addWidget(QLabel('Resultado:'))
        main_layout.addWidget(self.resultados)

        self.setLayout(main_layout)
        self.setWindowTitle('Calculadora de Tempo')

    @pyqtSlot()
    def onClick(self):
        novo_horario = adicionar_tempo(f"{self.hora_input.text()}:{self.minuto_input.text()} "
                                       f"{self.ampm_selecao.currentText()}", f"{self.horas_somar.text()}",
                                       f"{self.dia_selecao.currentText()}")
        self.resultados.setHtml(novo_horario)


def main():
    calc_app = QApplication([])
    calc_window = CalculadoraTempo()
    calc_window.show()
    sys.exit(calc_app.exec())


if __name__ == "__main__":
    main()
