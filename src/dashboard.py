import matplotlib.pyplot as plt

def mostrar_grafico_categoria(df):
    if 'categoria' not in df.columns:
        print("Coluna 'categoria' não encontrado no Dataframe.")
        return
    
    soma_por_categoria = df.groupby('categoria')['amount'].sum()

    plt.figure(figsize=(10, 6))
    soma_por_categoria.plot(kind='bar', color='skyblue')
    plt.title('Gastos por categoria')
    plt.xlabel('Categoria')
    plt.ylabel('Total gasto (R$)')
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.show()