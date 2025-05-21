import pandas as pd
import os

def ler_extrato(caminho_arquivo):
    try:
        df = pd.read_csv(caminho_arquivo)
        print("Extrato enviado com sucesso")
        return df
    except Exception as e:
        print(f"Erro ao ler o arquivo {e}")
        return None
    
def listar_arquivos_csv(pasta='data/extratos'):
    arquivos = [f for f in os.listdir(pasta) if f.endswith('.csv')]
    return [os.path.join(pasta, f) for f in arquivos]