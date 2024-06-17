def calcular_novo_dia(dia: str, qtd_dias: int):
    dia_semana_indice = {"segunda": 0, "terça": 1, "quarta": 2, "quinta": 3, "sexta": 4, "sábado": 5, "domingo": 6}
    dia_semana_lista = ["Segunda", "Terça", "Quarta", "Quinta", "Sexta", "Sábado", "Domingo"]

    dia = dia.lower()
    indice = (dia_semana_indice[dia] + qtd_dias) % 7
    novo_dia = dia_semana_lista[indice]
    return novo_dia


def adicionar_tempo(inicio: str, duracao: str, dia: str = False):
    horas_duracao, minutos_duracao = map(int, duracao.split(":"))

    horario_inicio, am_pm = inicio.split()
    horas_inicio, minutos_inicio = map(int, horario_inicio.split(":"))
    troca_am_pm = {"AM": "PM", "PM": "AM"}

    total_minutos = minutos_inicio + minutos_duracao
    horas_extra = total_minutos // 60
    minutos_fim = total_minutos % 60

    total_horas = horas_inicio + horas_duracao + horas_extra
    qtd_trocas_am_pm = total_horas // 12
    horas_fim = total_horas % 12

    if horas_fim == 0:
        horas_fim == 12

    if am_pm == "PM" and (horas_inicio + horas_duracao) % 24 >= 12:
        qtd_trocas_am_pm += 1

    am_pm = troca_am_pm[am_pm] if qtd_trocas_am_pm % 2 == 1 else am_pm
    qtd_dias = total_horas // 24

    minutos_fim = f"{minutos_fim:02}"
    hora_retorno = f"{horas_fim}:{minutos_fim} {am_pm}"

    if dia:
        novo_dia = calcular_novo_dia(dia, qtd_dias)
        hora_retorno += f", {novo_dia}"

    if qtd_dias == 1:
        return hora_retorno + " (Dia seguinte)"
    elif qtd_dias > 1:
        return hora_retorno + f" ({qtd_dias} Dias depois)"

    return hora_retorno

