# scripts/extract.py

import pandas as pd
import os

def extract_data():
    """
    Extrai dados de um URL confiável (o seu GitHub) e
    os salva na pasta 'data/raw'.
    """
    # URL do arquivo CSV no seu próprio repositório GitHub (versão Raw)
    url = "https://raw.githubusercontent.com/ramos-anderson/projeto-sql-rfm-ecommerce/main/olist_orders_dataset.csv"
    
    # Define o caminho para salvar o arquivo bruto
    raw_data_path = "data/raw/olist_orders.csv"
    
    # Cria o diretório se ele não existir
    os.makedirs(os.path.dirname(raw_data_path), exist_ok=True)
    
    print(f"Iniciando download de: {url}")
    try:
        # Lê o CSV diretamente do URL e o salva no caminho especificado
        df = pd.read_csv(url)
        df.to_csv(raw_data_path, index=False)
        print(f"Dados brutos salvos com sucesso em: {raw_data_path}")

    except Exception as e:
        print(f"\n--- ERRO CRÍTICO ---")
        print(f"Não foi possível baixar os dados do seu GitHub. Erro: {e}")
        print("SOLUÇÃO: Verifique se o link está correto e se o repositório é público.")
        print("--------------------")
        exit(1) # Para o pipeline se o download falhar

if __name__ == "__main__":
    extract_data()