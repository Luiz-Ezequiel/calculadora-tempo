# Calculadora de Tempo

Este projeto é uma aplicação GUI (Interface Gráfica do Usuário) construída com Python e PyQt5 que permite ao usuário calcular a hora após adicionar uma quantidade específica de tempo a um horário inicial. A aplicação também considera o dia da semana e pode calcular o novo dia após a adição do tempo.

## Requisitos

- Python 3.x
- PyQt5

## Instalação

1. Clone o repositório.
2. Instale as dependências listadas em `requirements.txt`:
    ```bash
    pip install -r requirements.txt
    ```
3. Execute o script `GUI.py`:
    ```bash
    python GUI.py
    ```

## Arquivos

### GUI.py

Este arquivo contém a implementação da interface gráfica da aplicação.

#### Classes e Métodos

- **CalculadoraTempo(QWidget)**: Classe principal que cria a janela da aplicação.
  - **initUI(self)**: Inicializa a interface do usuário.
  - **onClick(self)**: Método chamado quando o botão "Calcular" é clicado. Ele utiliza a função `adicionar_tempo` do arquivo `calculadora_tempo.py` para calcular o novo horário e dia.

- **main()**: Função principal que inicia a aplicação.

### calculadora_tempo.py

Este arquivo contém a lógica de cálculo de tempo.

#### Funções

- **calcular_novo_dia(dia: str, qtd_dias: int)**: Calcula o novo dia da semana após adicionar uma quantidade de dias a um dia inicial.
- **adicionar_tempo(inicio: str, duracao: str, dia: str = False)**: Calcula o novo horário após adicionar uma duração a um horário inicial. Também pode calcular o novo dia da semana se fornecido.

## Como Usar

1. Insira o horário inicial nos campos "HH" (horas) e "MM" (minutos).
2. Selecione "AM" ou "PM" no combobox correspondente.
3. Selecione o dia da semana inicial.
4. Insira a quantidade de horas e minutos a serem somados no campo "Horas para Somar" no formato "HH:MM".
5. Clique no botão "Calcular".
6. O resultado será exibido na área de texto abaixo do botão, mostrando o novo horário e dia (se aplicável).

## Exemplo

Se o horário inicial for 10:30 AM na Segunda-feira e você adicionar 5 horas e 45 minutos, o resultado será 4:15 PM, Segunda-feira.

## Contato

Para mais informações, entre em contato através do email: [luiz.ezequiel2004@gmail.com](mailto:luiz.ezequiel2004@gmail.com).

Sinta-se à vontade para modificar e melhorar o código conforme necessário. Aproveite a calculadora de tempo!

---




Sinta-se à vontade para modificar e melhorar o código conforme necessário. Aproveite a calculadora de tempo!
