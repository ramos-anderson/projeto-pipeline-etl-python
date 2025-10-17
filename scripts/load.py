import pandas as pd
from sqlalchemy import create_engine
import os

def load_data():
    """
    Lê os dados processados e os carrega em um banco de dados SQLite.
    """
    processed_data_path = "data/processed/olist_orders_processed.csv"
    db_path = "database/vendas.db"
    table_name = "pedidos"
    
    # Cria o diretório do banco de dados se não existir
    os.makedirs(os.path.dirname(db_path), exist_ok=True)
    
    # Cria a conexão com o banco de dados
    # A sintaxe 'sqlite:///' indica um arquivo local
    engine = create_engine(f'sqlite:///{db_path}')
    
    print("Iniciando carregamento dos dados para o banco de dados...")
    # Lê o arquivo processado
    df = pd.read_csv(processed_data_path)
    
    # Carrega os dados para o banco de dados
    # if_exists='replace' substitui a tabela a cada execução.
    df.to_sql(table_name, engine, if_exists='replace', index=False)
    
    print(f"Dados carregados com sucesso na tabela '{table_name}' em '{db_path}'")

if __name__ == "__main__":
    load_data()