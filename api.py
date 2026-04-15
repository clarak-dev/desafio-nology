from fastapi import FastAPI, Request
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from cashback import calcular_cashback
from database import criar_tabela, salvar_consulta, buscar_consultas_por_ip

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

criar_tabela()


class CashbackRequest(BaseModel):
    valor_produto: float
    percentual_desconto: float
    tipo_cliente: str


@app.get("/")
def home():
    return {"mensagem": "API de cashback funcionando"}


@app.post("/calcular")
def calcular(dados: CashbackRequest, request: Request):
    cashback = calcular_cashback(
        dados.valor_produto,
        dados.percentual_desconto,
        dados.tipo_cliente
    )

    ip_usuario = request.client.host

    salvar_consulta(
        ip_usuario,
        dados.tipo_cliente,
        dados.valor_produto,
        dados.percentual_desconto,
        cashback
    )

    return {
        "valor_produto": dados.valor_produto,
        "percentual_desconto": dados.percentual_desconto,
        "tipo_cliente": dados.tipo_cliente,
        "cashback": cashback
    }


@app.get("/historico")
def historico(request: Request):
    ip_usuario = request.client.host
    consultas = buscar_consultas_por_ip(ip_usuario)

    lista_historico = []

    for consulta in consultas:
        lista_historico.append({
            "tipo_cliente": consulta[0],
            "valor_produto": consulta[1],
            "percentual_desconto": consulta[2],
            "cashback": consulta[3]
        })

    return lista_historico