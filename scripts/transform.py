# scripts/transform.py

import pandas as pd
import os

def transform_data():
    """
    Lê os dados brutos, aplica transformações e salva
    o resultado na pasta 'data/processed'.
    """
    raw_data_path = "data/raw/olist_orders.csv"
    processed_data_path = "data/processed/olist_orders_processed.csv"
    
    print("Iniciando transformação dos dados...")
    df = pd.read_csv(raw_data_path)
    
    # 1. Renomear colunas para maior clareza
    df = df.rename(columns={"order_purchase_timestamp": "data_pedido"})
    
    # 2. Converter as colunas de data de texto (object) para datetime.
    #    Este é o passo CRÍTICO que corrige o TypeError.
    #    'errors=coerce' transforma datas inválidas em NaT (Not a Time).
    df['data_pedido'] = pd.to_datetime(df['data_pedido'], errors='coerce')
    df['order_approved_at'] = pd.to_datetime(df['order_approved_at'], errors='coerce')
    
    # 3. Criar uma nova coluna calculando a diferença em horas.
    #    Agora a subtração funciona, pois estamos operando com datetimes.
    df['tempo_aprovacao_horas'] = (df['order_approved_at'] - df['data_pedido']).dt.total_seconds() / 3600
    
    # 4. Salvar o arquivo processado
    os.makedirs(os.path.dirname(processed_data_path), exist_ok=True)
    df.to_csv(processed_data_path, index=False)
    
    print(f"Dados transformados salvos com sucesso em: {processed_data_path}")

if __name__ == "__main__":
    transform_data()