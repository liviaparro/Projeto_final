import requests

base_url = "http://10.135.232.26:5000"

def get_listar_clientes():
    url = f"{base_url}/todos_clientes"
    resposta = requests.get(url)
    return resposta.json()

def post_cliente(nome,cep, rua, bairro ,cidade ,estado, numero_casa, complemento, email):
    url = f"{base_url}/usuario"
    dados= {
        "nome": nome,
        "cep" : cep,
        "rua": rua,
        "bairro": bairro,
        "cidade": cidade,
        "estado": estado,
        "numero_casa": numero_casa,
        "complemento": complemento,
        "email": email
    }
    resposta = requests.post(url, json=dados)
    return resposta

def get_listar_encomendas():
    url = f"{base_url}/todas_encomendas"
    resposta = requests.get(url)
    return resposta.json()

def post_encomenda(fragilidade, tipo,cliente_id, remetente_id):
    url = f"{base_url}/encomendas"
    dados= {

        "fragilidade": fragilidade,
        "tipo": tipo,
        "cliente_id": cliente_id,
        "remetente_id": remetente_id,
    }
    resposta = requests.post(url, json=dados)
    return resposta


def get_listar_funcionarios():
    url = f"{base_url}/todos_funcionarios"
    resposta = requests.get(url)
    return resposta.json()

def post_funcionario(nome, cpf, email, senha):
    url = f"{base_url}/funcionario"
    dados= {
        "nome": nome,
        "cpf": cpf,
        "email": email,
        "senha": senha,

    }
    resposta = requests.post(url, json=dados)
    return resposta

def get_listar_unidades():
    url = f"{base_url}/todas_unidades"
    resposta = requests.get(url)
    return resposta.json()

def post_unidade(nome, cidade, estado):
    url = f"{base_url}/unidades"
    dados= {
        "nome": nome,
        "cidade": cidade,
        "estado": estado
    }
    resposta = requests.post(url, json=dados)
    return resposta

def get_listar_movimentacao():
    url = f"{base_url}/todas_movimentacoes"
    resposta = requests.get(url)
    return resposta

def post_movimentacao(localizacao,encomenda_id ):
    url = f"{base_url}/movimentacoes"
    dados= {
        "encomenda_id": encomenda_id,
        "centro_id": localizacao,

    }
    resposta = requests.post(url, json=dados)
    return resposta

def get_listar_remetentes():
    url = f"{base_url}/todos_remetentes"
    resposta = requests.get(url)
    return resposta.json()

def post_remetentes(nome, cidade, estado):
    url = f"{base_url}/remetente"
    dados= {
        "nome": nome,
        "cidade": cidade,
        "estado": estado
    }
    resposta = requests.post(url, json=dados)
    return resposta

def post_verifica_email(email):
    url = f"{base_url}/verificar_email"
    dados = {
        "email": email
    }
    resposta = requests.post(url, json=dados)
    return resposta