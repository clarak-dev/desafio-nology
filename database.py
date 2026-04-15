import os
import psycopg2
from dotenv import load_dotenv

load_dotenv()


def conectar():
    conexao = psycopg2.connect(
        dbname=os.getenv("DB_NAME"),
        user=os.getenv("DB_USER"),
        password=os.getenv("DB_PASSWORD"),
        host=os.getenv("DB_HOST"),
        port=os.getenv("DB_PORT")
    )
    return conexao


def criar_tabela():
    conexao = conectar()
    cursor = conexao.cursor()

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS consultas (
            id SERIAL PRIMARY KEY,
            ip VARCHAR(100) NOT NULL,
            tipo_cliente VARCHAR(20) NOT NULL,
            valor_produto NUMERIC(10, 2) NOT NULL,
            percentual_desconto NUMERIC(10, 2) NOT NULL,
            cashback NUMERIC(10, 2) NOT NULL
        )
    """)

    conexao.commit()
    cursor.close()
    conexao.close()


def salvar_consulta(ip, tipo_cliente, valor_produto, percentual_desconto, cashback):
    conexao = conectar()
    cursor = conexao.cursor()

    cursor.execute("""
        INSERT INTO consultas (ip, tipo_cliente, valor_produto, percentual_desconto, cashback)
        VALUES (%s, %s, %s, %s, %s)
    """, (ip, tipo_cliente, valor_produto, percentual_desconto, cashback))

    conexao.commit()
    cursor.close()
    conexao.close()


def buscar_consultas_por_ip(ip):
    conexao = conectar()
    cursor = conexao.cursor()

    cursor.execute("""
        SELECT tipo_cliente, valor_produto, percentual_desconto, cashback
        FROM consultas
        WHERE ip = %s
        ORDER BY id DESC
    """, (ip,))

    resultados = cursor.fetchall()

    cursor.close()
    conexao.close()

    return resultados