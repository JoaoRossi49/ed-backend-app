import calendar
from datetime import date, datetime
from .calendar_utils import generate_html_calendar, get_feriados, pintar_dia
from estudante.models import Matricula, DiaSemana

def gerar_calendario(matricula):
    estudante = Matricula.objects.get(numero_matricula=matricula)
    pessoa = estudante.pessoa

    nome_aprendiz = pessoa.nome
    empresa = estudante.empresa.nome_fantasia

    #Listar todos os dias associados a essa matricula e converter para str
    dias_da_semana_curso = ', '.join([dia.dia for dia in estudante.turma.dias_da_semana_curso.all()])
    dia_curso_nome_turma = dias_da_semana_curso + ' ' + estudante.hora_inicio_expediente + 'h ' + ' às ' + estudante.hora_fim_expediente + 'h'

    curso = estudante.curso.codigo + ' - ' + estudante.curso.nome
    inicio_contrato = estudante.data_inicio_contrato.strftime('%d/%m/%Y')
    fim_contrato = estudante.data_terminio_contrato.strftime('%d/%m/%Y')
    duracao_contrato = estudante.quantidade_meses_contrato

    horas_aula = int(estudante.curso.carga_horaria_aula.total_seconds() // 3600)
    carga_horaria = str(horas_aula) + 'h'

    # Ajustar as datas de início e fim
    start_date_str = "17/01/2024"
    end_date_str = "17/12/2025"
    
    diasTeorico = 0

    start_date = datetime.strptime(start_date_str, "%d/%m/%Y").date()
    end_date = datetime.strptime(end_date_str, "%d/%m/%Y").date()

    # Definir os feriados
    feriados = get_feriados(start_date.year, end_date.year)

    html_months_list = generate_html_calendar(start_date_str, end_date_str, locale='pt_BR')

    # Loop sobre anos e meses
    html_calendar = ''
    
    for index, (data, html) in enumerate(html_months_list):
        mes = data.month
        ano = data.year
        isPrimeiroAno = False
        if index == 0:
            isPrimeiroAno = True
            
        html = pintar_dia(html, 0, mes, ano, feriados, start_date, end_date, isPrimeiroAno)

        html = html.replace(' 2024', '')
        
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

