from src.extrator import listar_arquivos_csv, ler_extrato
from src.classificador import classificar_gastos
from src.dashboard import mostrar_grafico_categoria

def main():
    arquivos = listar_arquivos_csv()
    if not arquivos:
        print("Nenhum arquivo CSV encontrado em 'data/extratos'.")
        return

    for arquivo in arquivos:
        print(f"Lendo: {arquivo}")
        df = ler_extrato(arquivo)
        df = classificar_gastos(df, coluna_descricao='title')
        print(df[['title', 'categoria']].head())

        mostrar_grafico_categoria(df)

if __name__ == "__main__":
    main()
