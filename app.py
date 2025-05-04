# Etapa 1: Ler CSV ignorando as 8 primeiras linhas (metadados)
import csv

def detectar_sep(cabecalho):
    if ';' in cabecalho: return ';'
    elif ',' in cabecalho: return ','
    else: return ';'  # Padrão

with open(file_path, 'r', encoding='latin1') as f:
    linhas = f.readlines()

# Detectar separador
sep = detectar_sep(linhas[8])  # linha do cabeçalho real
colunas = linhas[8].strip().split(sep)
dados = linhas[9:]  # dados reais

# Recriar o CSV somente com cabeçalho + dados corretos
from io import StringIO
csv_limpo = StringIO()
csv_limpo.write(sep.join(colunas) + '\n')
csv_limpo.writelines(dados)
csv_limpo.seek(0)

# Ler com pandas
df = pd.read_csv(csv_limpo, sep=sep)
