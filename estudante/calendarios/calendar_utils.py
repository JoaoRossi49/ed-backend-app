from calendar import LocaleHTMLCalendar, monthrange
from datetime import datetime, date, timedelta
import itertools
import holidays


class CalendarUtils: 
    def __init__(self, locale='pt_BR.UTF-8', html_mes = None, dia_teorico = None, mes = None, ano = None, feriados = None, start_date = None, end_date = None, qtd_dias_treinamento_inicial = None):
        self.locale = locale
        self.html_mes = html_mes
        self.dia_teorico = dia_teorico  
        self.mes = mes
        self.ano = ano
        self.feriados = feriados
        self.start_date = start_date
        self.end_date = end_date
        self.qtd_dias_treinamento_inicial = qtd_dias_treinamento_inicial

    def pintar_dia(self):
        diasTeorico = 0
        nome_dia = ""
        
        for i in range(1, monthrange(self.ano, self.mes)[1] + 1):
            try:
                dia_atual = date(self.ano, self.mes, i)
                
                try:
                    amanha = date(self.ano, self.mes, i+1)
                except:
                    amanha = None

                nome_dia = dia_atual.strftime("%a").lower()     
                if not (self.start_date <= dia_atual <= self.end_date):
                    continue

                #Se o dia da próxima iteração for feriado e hoje for segunda ou sexta, será vermelho
                if ((nome_dia == 'mon' or nome_dia == 'thu') and amanha in self.feriados):
                    self.html_mes = self.html_mes.replace(f'<td class="{nome_dia}">{i}</td>', 
                                        f'<td class="highlight-holiday">{i}</td>')    
                    continue

                # Se for dia útil e feriado, será vermelho
                if dia_atual in self.feriados and nome_dia != 'sat' and nome_dia != 'sun':
                    self.html_mes = self.html_mes.replace(f'<td class="{nome_dia}">{i}</td>', 
                                        f'<td class="highlight-holiday">{i}</td>')
                    continue

                #os primeiros doze dias são de treinamento teórico
                if self.qtd_dias_treinamento_inicial != 0 and nome_dia != 'sat' and nome_dia != 'sun':
                    self.html_mes = self.html_mes.replace(f'<td class="{nome_dia}">{i}</td>', 
                                        f'<td class="highlight-twelve-days">{i}</td>')
                    diasTeorico += 1
                    self.qtd_dias_treinamento_inicial -= 1
                    continue        

                # Se tiver aula, será verde claro     
                if dia_atual.weekday() == self.dia_teorico:
                    self.html_mes = self.html_mes.replace(f'<td class="{nome_dia}">{i}</td>', 
                                        f'<td class="highlight">{i}</td>')
                    diasTeorico += 1
                    continue
                    
                #Se for um dia útil sem ser o dia de aula, será amarelo
                if dia_atual.weekday() != self.dia_teorico:
                    self.html_mes = self.html_mes.replace(f'<td class="{nome_dia}">{i}</td>', 
                                        f'<td class="highlight-work">{i}</td>')                 
                    continue

            except Exception as e:
                continue
        return self.html_mes


    def generate_html_calendar(self):
        # Inicializa o calendário com a localidade especificada
        cal = LocaleHTMLCalendar(locale='pt_BR.UTF-8')

        # Gera uma sequência de meses entre a data de início e de fim
        current_year = self.start_date.year
        current_month = self.start_date.month
        end_year = self.end_date.year
        end_month = self.end_date.month

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

    def calcular_data_pascoa(self, ano):
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

    def get_feriados(self):
        # Feriados nacionais e estaduais/microrregionais
        br_holidays = holidays.Brazil(years=range(self.start_date.year, self.end_date.year + 1), subdiv='SP')
        
        feriados_moveis = []
        for ano in range(self.start_date.year, self.end_date.year + 1):
            pascoa = self.calcular_data_pascoa(ano)
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