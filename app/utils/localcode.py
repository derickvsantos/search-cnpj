import PyPDF2
import re

class PDFExtract:
    def __init__(self, pdf_file):
        self.pdf_file = pdf_file
        self.pdf_data = self._ler_pdf()
        self.senha = self._capturar_senha()
        self.unidade = self._capturar_unidade()

    def _ler_pdf(self):
        pdf_data = PyPDF2.PdfReader(self.pdf_file)
        return [pagina.extract_text() for pagina in pdf_data.pages]

    def _capturar_senha(self):
        pagina_senha_raw = self.pdf_data[0]
        pagina_senha = pagina_senha_raw.replace('\n', ' ')
        match = re.search(r"SENHA:\s*([A-Z0-9]+)", pagina_senha)
        if match:
            senha = match.group(1)
            return senha
        else:
            raise Exception("Não foi possível encontrar a senha")
        
    def _capturar_unidade(self):
        pagina_unidade_raw = self.pdf_data[0]
        pagina_unidade = pagina_unidade_raw.replace('\n', ' ')
        match = re.search(r"FOLHA DE ROSTO - ([^\s]{1,}.*?)(?=\s{2,})", pagina_unidade)
        if match:
            unidade = match.group(1)
            return unidade
        else:
            raise Exception("Não foi possível encontrar a unidade")

        
## Keyword Robot ###
def capturar_informacoes_pdf(pdf_file):
    try:
        pdf_data = PDFExtract(pdf_file)
        return pdf_data.senha, pdf_data.unidade
    except Exception as e:
        print(f"Erro ao capturar unidade do PDF")
        raise Exception(e)

path_pdf = r'C:\Users\user\Desktop\testepdf\Documento_0.pdf'
senha, unidade = capturar_informacoes_pdf(path_pdf)
print(senha)
print(unidade)