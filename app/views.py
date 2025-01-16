from django.shortcuts import render
from django.views.generic import View
from app.utils.api import BuscaInformacoesCNPJ

def teste_url(request, *args, **kwargs):
    return render(request, 'app/pages/teste.html')

class SearchCNPJView(View):
    template_name = 'home.html'

    def get(self, request, *args, **kwargs):
        return render(request, self.template_name)
    
class SearchCNPJResultView(View):
    template_name = 'search.html'

    def get(self, request, *args, **kwargs):
        cnpj = request.GET.get('q', '')
        if cnpj:
            busca = BuscaInformacoesCNPJ(cnpj)
            cnpj_data = busca.raw_data
            
        return render(request, self.template_name, context={'data': cnpj_data})