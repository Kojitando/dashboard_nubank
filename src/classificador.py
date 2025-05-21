import pandas as pd

regras_categorias = {
    'Alimentação': ['mcdonald', 'ifood', 'restaurante', 'padaria', 'cacau'],
    'Transporte': ['uber', '99', 'posto',],
    'Saúde': ['drogaria', 'hospital', 'farmácia'],
    'Assinaturas': ['netflix', 'crunchyroll', 'prime', 'spotify', 'academia', 'celular'],
    'Educação': ['faculdade', 'cruzeiro', 'curso'],
    'Compras': ['mercado', 'supermercado', 'magalu', 'amazon', 'shopee', 'americanas'],
    'Moradia': ['aluguel', 'condominio', 'luz', 'agua', 'internet'],
    'Outros': []
}

def classificar_categoria(descricao):
    descricao = str(descricao).lower()
    for categoria, palavras in regras_categorias.items():
        if any(palavra in descricao for palavra in palavras):
            return categoria 
    return 'Outros' 

def classificar_gastos(df, coluna_descricao='descricao'):
    if coluna_descricao not in df.columns:
        print(f"Coluna '{coluna_descricao}' nao encontrada no DataFrame.")
        return df
    
    df['categoria'] = df[coluna_descricao].apply(classificar_categoria)
    return df