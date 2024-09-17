from calendar import LocaleHTMLCalendar
from datetime import datetime, date, timedelta
import itertools
import holidays


def pintar_dia(html, dia, mes, ano, feriados, start_date, end_date, isPrimeiroMes):
    diasTeorico = 0
    nome_dia = ""
    qtd_dias_treinamento_inicial = 12 
    for i in range(1, 32):
        try:
            dia_atual = date(ano, mes, i)
            amanha = date(ano, mes, i+1)
            nome_dia = dia_atual.strftime("%a").lower()     

            if not (start_date <= dia_atual <= end_date):
                continue
            nome_dia = dia_atual.strftime("%a").lower()

            #Se o dia da próxima iteração for feriado e hoje for segunda ou sexta, será amarelo
            if ((nome_dia == 'mon' or nome_dia == 'thu') and amanha in feriados):
                html = html.replace(f'<td class="{nome_dia}">{i}</td>', 
                                    f'<td class="highlight-near-holiday">{i}</td>') 
                continue
                
            # Se for feriado, será vermelho
            if dia_atual in feriados:
                html = html.replace(f'<td class="{nome_dia}">{i}</td>', 
                                    f'<td class="highlight-holiday">{i}</td>')
                continue
            #os primeiros doze dias são de treinamento teórico
            if qtd_dias_treinamento_inicial != 0 and isPrimeiroMes and nome_dia != 'sat' and nome_dia != 'sun':
                html = html.replace(f'<td class="{nome_dia}">{i}</td>', 
                                    f'<td class="highlight">{i}</td>')
                diasTeorico += 1
                qtd_dias_treinamento_inicial -= 1        
                continue        
                
            # Se tiver aula, será verde           
            elif dia_atual.weekday() == dia:
                html = html.replace(f'<td class="{nome_dia}">{i}</td>', 
                                    f'<td class="highlight">{i}</td>')
                diasTeorico += 1

        except Exception as e:
            continue
    return html


def generate_html_calendar(start_date, end_date, locale='pt_BR.UTF-8'):
    # Inicializa o calendário com a localidade especificada
    cal = LocaleHTMLCalendar(locale=locale)

    # Converte as datas de string para datetime se necessário
    if isinstance(start_date, str):
        start_date = datetime.strptime(start_date, "%d/%m/%Y")
    if isinstance(end_date, str):
        end_date = datetime.strptime(end_date, "%d/%m/%Y")

    # Gera uma sequência de meses entre a data de início e de fim
    current_year = start_date.year
    current_month = start_date.month
    end_year = end_date.year
    end_month = end_date.month

    # Lista para armazenar os meses
    months = []

    for year, month in itertools.product(range(current_year, end_year + 1), range(1, 13)):
        if (year == current_year and month >= current_month) or (year == end_year and month <= end_month) or (year != current_year and year != end_year):
            months.append((year, month))

    # Gera o HTML para cada mês
    html_months_list = []
    for year, month in months:
        html_output = cal.formatmonth(year, month)
        html_output += "<br><br>"
        tupla = (date(year, month, 1), html_output)
        html_months_list.append(tupla)

    return html_months_list

def calcular_data_pascoa(ano):
    a = ano % 19
    b = ano // 100
    c = ano % 100
    d = b // 4
    e = b % 4
    f = (b + 8) // 25
    g = (b - f + 1) // 3
    h = (19 * a + b - d - g + 15) % 30
    i = c // 4
    k = c % 4
    l = (32 + 2 * e + 2 * i - h - k) % 7
    m = (a + 11 * h + 22 * l) // 451
    mes = (h + l - 7 * m + 114) // 31
    dia = ((h + l - 7 * m + 114) % 31) + 1
    return date(ano, mes, dia)

def get_feriados(ano_inicial, ano_final):
    # Feriados nacionais e estaduais/microrregionais
    br_holidays = holidays.Brazil(years=range(ano_inicial, ano_final + 1), subdiv='SP')
    
    feriados_moveis = []
    for ano in range(ano_inicial, ano_final + 1):
        pascoa = calcular_data_pascoa(ano)
        carnaval = pascoa - timedelta(days=47)  # Carnaval é 47 dias antes da Páscoa
        feriados_moveis.append(carnaval)
        aniversario_marilia = date(ano,4,4) #adiciona o aniversário de marília
        feriados_moveis.append(aniversario_marilia)
        vespera_natal = date(ano,12,24)
        feriados_moveis.append(vespera_natal)
    
    # Combinar feriados fixos e móveis
    todos_feriados = list(br_holidays.keys()) + feriados_moveis
    todos_feriados.sort()  # Ordenar por data
    
    # Converter para objetos date
    feriados_list = [date(feriado.year, feriado.month, feriado.day) for feriado in todos_feriados]

    return feriados_list