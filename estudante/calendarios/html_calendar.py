import calendar
from datetime import date, datetime
from .calendar_utils import CalendarUtils
from estudante.models import Matricula, DiaSemana

def gerar_calendario(matricula):
    estudante = Matricula.objects.get(numero_matricula=matricula)
    pessoa = estudante.pessoa

    nome_aprendiz = pessoa.nome
    empresa = estudante.empresa.nome_fantasia

    #Listar todos os dias associados a essa matricula e converter para str
    dias_da_semana_curso = ', '.join([str(dia.id) for dia in estudante.turma.dias_da_semana_curso.all()])
    dia_curso_nome_turma = dias_da_semana_curso + ' ' + estudante.hora_inicio_expediente + 'h ' + ' às ' + estudante.hora_fim_expediente + 'h'

    curso = estudante.curso.codigo + ' - ' + estudante.curso.nome
    inicio_contrato = estudante.data_inicio_contrato.strftime('%d/%m/%Y')
    fim_contrato = estudante.data_terminio_contrato.strftime('%d/%m/%Y')
    duracao_contrato = estudante.quantidade_meses_contrato

    horas_aula = int(estudante.curso.carga_horaria_aula.total_seconds() // 3600)
    carga_horaria = str(horas_aula) + 'h'

    # Ajustar as datas de início e fim
    start_date_str = inicio_contrato
    end_date_str = fim_contrato

    start_date = datetime.strptime(start_date_str, "%d/%m/%Y").date()
    end_date = datetime.strptime(end_date_str, "%d/%m/%Y").date()

    #Criação de instancia de configurações de geração do calendario
    calendar_utils = CalendarUtils()
    calendar_utils.qtd_dias_treinamento_inicial = 12
    calendar_utils.start_date = start_date
    calendar_utils.end_date = end_date
    calendar_utils.dia_teorico = int(dias_da_semana_curso[0])-1

    # Definir os feriados
    feriados = calendar_utils.get_feriados()

    calendar_utils.feriados = feriados

    #Gerar calendarios em lista
    html_months_list = calendar_utils.generate_html_calendar()

    #Variável de armazenamento de resultado
    html_calendar = ''

    # Loop sobre anos e meses
    for index, (data, html) in enumerate(html_months_list):
        calendar_utils.mes = data.month
        calendar_utils.ano = data.year
        calendar_utils.html_mes = html
            
        html = calendar_utils.pintar_dia()
        
        if index == 0 or index % 2 != 0:
            html_calendar += '<tr class="mes">'
            html_calendar += f'<td class="mes">{html}</td>'
            html_calendar += '<td></td>'
        else:
            html_calendar += f'<td class="mes" >{html}</td>'
            html_calendar += '<td></td>'
            html_calendar += '</tr class="mes">'  
    
    with open('estudante\calendarios\head.html', 'r', encoding='utf-8') as file:
        html_content = file.read()
    
    html_content = html_content.replace('[NOME_APRENDIZ]', nome_aprendiz)
    html_content = html_content.replace('[NOME_EMPRESA]', empresa)
    html_content = html_content.replace('[DIA_CURSO_NOME_TURMA]', dia_curso_nome_turma)
    html_content = html_content.replace('[CODIGO_NOME_CH_CURSO]', curso)
    html_content = html_content.replace('[INICIO_CONTRATO]', inicio_contrato)
    html_content = html_content.replace('[FIM_CONTRATO]', fim_contrato)
    html_content = html_content.replace('[DURACAO_CONTRATO]', str(duracao_contrato))
    html_content = html_content.replace('[CARGA_HORARIA]', carga_horaria)

        
    html_content += f"""
    <table border="0" cellpadding="0" cellspacing="0">
        {html_calendar}
            </table>
    </body>
    </html>
    """

    #filename = "calendario.html"

    #with open(filename, "w", encoding="utf-8") as file:
        #file.write(html_content)

    return html_content

