from extract import extract_data
from transform import transform_data
from load import load_data

def run_pipeline():
    """
    Executa o pipeline de ETL completo.
    """
    print("==== INICIANDO PIPELINE DE ETL DE VENDAS ====")
    
    # 1. Extração
    extract_data()
    
    # 2. Transformação
    transform_data()
    
    # 3. Carregamento
    load_data()
    
    print("==== PIPELINE FINALIZADO COM SUCESSO ====")

if __name__ == "__main__":
    run_pipeline()