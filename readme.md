# Projeto de ETL: Pipeline Automatizado de Dados de Vendas

![Status](https://img.shields.io/badge/Status-Concluído-brightgreen?style=for-the-badge) ![Python](https://img.shields.io/badge/Python-3.11-blue?style=for-the-badge&logo=python) ![SQLite](https://img.shields.io/badge/SQLite-3.3-blue?style=for-the-badge&logo=sqlite)

Este repositório contém o código de um pipeline de ETL (Extração, Transformação e Carga) completo e **automatizado**, desenvolvido em Python. O objetivo é simular um ambiente de produção onde dados de vendas são coletados de uma fonte online, processados e carregados em um banco de dados SQL para futuras análises.

Este projeto demonstra habilidades práticas em **Engenharia de Dados**, **automação de processos**, arquitetura de software e boas práticas de organização de código.

---

## 📈 Arquitetura do Pipeline

O fluxo de dados segue a seguinte arquitetura de ETL, orquestrada por scripts Python:

[Fonte (CSV no GitHub)] --> [1. Extração (extract.py)] --> [Dados Brutos (data/raw)] --> [2. Transformação (transform.py)] --> [Dados Processados (data/processed)] --> [3. Carga (load.py)] --> [Banco de Dados (database/vendas.db)]

Todo este processo é agendado para rodar diariamente sem intervenção humana.

---

## 🛠️ Tecnologias Utilizadas

*   **Linguagem:** Python 3
*   **Bibliotecas:**
    *   **Pandas:** Para manipulação e transformação dos dados em dataframes.
    *   **SQLite3:** Módulo nativo para a criação e gestão do banco de dados SQL.
*   **Banco de Dados:** SQLite
*   **Automação e Orquestração:**
    *   **`main.py`:** Script Python que serve como orquestrador, chamando os módulos de ETL na ordem correta.
    *   **Agendador de Tarefas do Windows:** Utilizado para **automatizar a execução diária** do pipeline, simulando um ambiente de produção real.

---

## 🚀 Funcionalidades

*   **Extração (Extract):** Coleta de forma robusta o dataset de vendas (`olist_orders_dataset.csv`) de um repositório público no GitHub.
*   **Transformação (Transform):**
    *   Converte colunas de texto para formatos `datetime`, tratando erros de forma programática.
    *   Renomeia colunas para o padrão do Data Warehouse (`snake_case`).
    *   Cria uma nova métrica de negócio (`tempo_aprovacao_horas`) através de engenharia de features, calculando o tempo em horas entre o pedido e a aprovação.
*   **Carga (Load):** Carrega os dados transformados em uma tabela (`pedidos`) dentro de um banco de dados SQLite, utilizando um método de substituição (`if_exists='replace'`) para garantir a atualização dos dados a cada nova execução.
*   **Automação:** O pipeline completo foi agendado para **execução diária autônoma**, garantindo que o banco de dados esteja sempre atualizado para as equipes de análise.

---

## 📁 Estrutura do Projeto

O projeto é organizado de forma modular para garantir clareza, manutenibilidade e escalabilidade:

pipeline_vendas_etl/
├── data/ # Armazena os dados (ignorado pelo Git)
├── database/ # Armazena o banco de dados (ignorado pelo Git)
├── scripts/ # Código fonte modularizado do pipeline
│ ├── extract.py
│ ├── transform.py
│ ├── load.py
│ └── main.py
├── .gitignore # Define arquivos/pastas ignorados pelo Git
├── requirements.txt # Lista de dependências Python
└── README.md # Esta documentação

*Observação: As pastas `data/` e `database/` são geradas dinamicamente e estão no `.gitignore` pois a boa prática em projetos de pipeline é versionar o código que GERA os dados, e não os dados em si.*

---

## ⚙️ Como Executar o Projeto

**1. Clone o repositório:**
```bash
git clone https://github.com/ramos-anderson/projeto-pipeline-vendas-etl.git
cd projeto-pipeline-vendas-etl

(Nota: Lembre-se de substituir o link acima pelo link correto do seu repositório!)

2. Crie e ative um ambiente virtual:

# Criar o ambiente
python -m venv venv

# Ativar no Windows
venv\Scripts\activate

3. Instale as dependências:

pip install -r requirements.txt

(Nota: Você precisará criar um arquivo requirements.txt com pandas dentro)

4. Execute o pipeline:
Para rodar o processo completo de ETL manualmente, execute o script principal.

python scripts/main.py

Ao final da execução, o banco de dados database/vendas.db estará criado e pronto para ser consultado.

---


