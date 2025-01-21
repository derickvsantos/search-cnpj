import requests
from datetime import datetime
import locale
locale.setlocale(locale.LC_ALL, 'pt_BR.UTF-8')

class BuscaInformacoesCNPJ:
    def __init__(self, cnpj):
        self.cnpj = cnpj
        self.url = 'https://minhareceita.org/'
        self.response = self.get_data()
    
    def get_data(self):
        url = self.url + self.cnpj
        response = requests.get(url)
        self.raw_data = response.json()
        self._order_data()
        return self.raw_data
    
    def _order_data(self):
        self._format_contact_number()
        self._format_postal_code()
        self._format_date()
        self._format_capital()
        self._format_owners_dates()

    def _format_contact_number(self):
        number = self.raw_data.get('ddd_telefone_1', '')
        if number:
            if len(number) == 10:
                self.raw_data['ddd_telefone_1'] = f"({number[:2]}) {number[2:6]}-{number[6:]}"
            elif len(number) == 11:
                self.raw_data['ddd_telefone_1'] = f"({number[:2]}) {number[2:7]}-{number[7:]}"
    
    def _format_postal_code(self):
        cep = self.raw_data.get('cep', '')
        if cep:
            if len(cep) == 8:
                self.raw_data['cep'] = f"{cep[:5]}-{cep[5:]}"
    
    def _format_date(self):
        date = self.raw_data.get('data_inicio_atividade', '')
        if date:
            formated_date = datetime.strptime(date, '%Y-%m-%d')
            self.raw_data['data_inicio_atividade'] = formated_date.strftime('%d/%m/%Y')

    def _format_owners_dates(self):
        owners_data = self.raw_data.get('qsa', [])
        if owners_data:
            for idx, owner in enumerate(owners_data):
                date = owner['data_entrada_sociedade']
                formated_date = datetime.strptime(date, '%Y-%m-%d')
                self.raw_data['qsa'][idx]['data_entrada_sociedade'] = formated_date.strftime('%d/%m/%Y')
    
    def _format_capital(self):
        capital = self.raw_data.get('capital_social', 0)
        if capital:
            formatted_capital = locale.currency(capital / 100, grouping=True)
            self.raw_data['capital_social'] = formatted_capital



# busca = BuscaInformacoesCNPJ('10468447000143')