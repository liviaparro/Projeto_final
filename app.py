from flask import Flask, render_template, url_for, flash, request, redirect
from sqlalchemy.exc import SQLAlchemyError
from sqlalchemy import select, and_, func

from sqlalchemy import select, and_, func
from flask_login import login_manager, login_required, login_user, logout_user, current_user

from models import Centro_distribuicao, Emcomenda, Movimentacao, db_session, Funcionario
from routes import get_listar_unidades, get_listar_funcionarios, get_listar_clientes, get_listar_movimentacao, \
    get_listar_encomendas, post_funcionario, post_encomenda, post_cliente, post_unidade, \
    post_movimentacao, get_listar_remetentes, post_remetentes, post_verifica_email

app = Flask(__name__)
app.config['SECRET_KEY'] = '0000'


@app.route('/')
def home():
    return render_template("home.html")


@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        email = request.form.get('form_email')
        senha = request.form.get('form_senha')
        email_verificado = post_verifica_email(email)
        if email_verificado.status_code == 200: # se encontrou o funcionario pelo email
            print(email_verificado.json())
            if email_verificado.json()["funcionario"]["senha"] == senha : # se a senha do funcionario for igual
                return redirect(url_for('todas_encomendas'))
            else:

                return redirect(url_for('login'))
        else:

            return redirect(url_for('login'))
    return render_template('login.html')


@app.route('/logout')
def logout():
    logout_user()
    flash('Logout realizado com sucesso!', 'success')
    return redirect(url_for('login'))


@app.route('/funcionario', methods=['GET', 'POST'])
def todos_funcionarios():
    if request.method == 'POST':
        nome = request.form.get('form_nome')
        cpf = request.form.get('form_cpf')
        email = request.form.get('form_email')
        senha = request.form.get('form_senha')
        print(nome, cpf, email, senha)
        resposta = post_funcionario(nome, cpf, email, senha)

        dados_ = resposta.json()
        print(dados_)
        if resposta.status_code == 201:
            flash(message="Encomenda cadastrada com sucesso")
        else:
            flash(message="Erro ao cadastrar")

    funcionarios = get_listar_funcionarios()
    return render_template("login.html", funcionarios=funcionarios["funcionarios"])


@app.route('/encomendas', methods=['GET', 'POST'])
def todas_encomendas():
    if request.method == 'POST':
        print("dpf")
        fragilidade = request.form.get('fragilidade')
        tipo = request.form.get('tipo')
        cliente_id = request.form.get('cliente_id')
        remetente_id = request.form.get('remetente_id')
        print(fragilidade)
        print(tipo)
        print(cliente_id)
        print(remetente_id)

        resposta = post_encomenda(fragilidade, tipo, cliente_id, remetente_id)
        print("lko", resposta)
        dados_ = resposta.json()
        print(dados_)
        if resposta.status_code == 201:
            flash(message="Encomenda cadastrada com sucesso")
        else:
            flash(message="Erro ao cadastrar")
        # return redirect(url_for('encomendas'))
    # aqui=
    clientes = get_listar_clientes()

    rementente = get_listar_remetentes()
    encomendas = get_listar_encomendas()
    print(encomendas)
    return render_template("encomendas.html", encomendas=encomendas["encomendas"], clientes=clientes["clientes"],
                           remetentes=rementente["remetentes"])


@app.route('/usuario', methods=['GET', 'POST'])
def todos_clientes():
    if request.method == 'POST':
        nome = request.form.get('form_nome')
        email = request.form.get('form_email')
        cep = request.form.get('form_cep')
        rua = request.form.get('form_rua')
        bairro = request.form.get('form_bairro')
        cidade = request.form.get('form_cidade')
        estado = request.form.get('form_estado')
        numero_casa = request.form.get('form_numero_casa')
        complemento = request.form.get('form_complemento')

        resposta = post_cliente(nome, cep, rua, bairro, cidade, estado, numero_casa, complemento, email)

        dados_ = resposta.json()
        print(dados_)

        if resposta.status_code == 201:
            flash(message="Encomenda cadastrada com sucesso")
        else:
            flash(message="Erro ao cadastrar")

    usuarios = get_listar_clientes()
    return render_template("usuario.html", usuarios=usuarios["clientes"])


@app.route('/unidades', methods=['GET', 'POST'])
def todas_unidades():
    if request.method == 'POST':
        nome = request.form.get('form_nome')
        cidade = request.form.get('form_cidade')
        estado = request.form.get('form_estado')
        print("post")
        resposta = post_unidade(nome, cidade, estado)

        dados_ = resposta.json()
        print(dados_)

        if resposta.status_code == 201:
            flash(message="Encomenda cadastrada com sucesso")
        else:
            flash(message="Erro ao cadastrar")

    unidades = get_listar_unidades()
    print("get")
    return render_template("unidades.html", unidades=unidades["centro_distribuicao"])


@app.route('/movimentacoes', methods=['GET', 'POST'])
def todas_movimentacoes():
    if request.method == 'POST':
        localizacao = request.form.get('centro_id')
        encomenda_id = request.form.get('form_codigo')
        print(localizacao)
        resposta = post_movimentacao(localizacao, encomenda_id)
        dados_ = resposta.json()
        print(dados_)
        if resposta.status_code == 201:
            flash(message="Encomenda cadastrada com sucesso")
        else:
            flash(message="Erro ao cadastrar")
    centros = get_listar_unidades()
    print("centro", centros)
    movimentacoes = get_listar_movimentacao().json()
    print("movimentacaoes", movimentacoes)
    encomendas = get_listar_encomendas()

    return render_template("movimentacoes.html", movimentacoes=movimentacoes["movimentacoes"],
                           centros=centros["centro_distribuicao"], encomendas=encomendas["encomendas"])


@app.route('/remetentes', methods=['GET', 'POST'])
def todos_remetentes():
    if request.method == 'POST':
        nome = request.form.get('form_nome')
        cidade = request.form.get('form_cidade')
        estado = request.form.get('form_estado')
        print(nome)
        print(cidade)
        print(estado)
        resposta = post_remetentes(nome, cidade, estado)
        dados_ = resposta.json()
        print(dados_)

        if resposta.status_code == 201:
            flash(message="Encomenda cadastrada com sucesso")
        else:
            flash(message="Erro ao cadastrar")

    remetentes = get_listar_remetentes()
    print(remetentes)
    return render_template("remetente.html", remetentes=remetentes["remetentes"])


if __name__ == '__main__':
    app.run(debug=True, port=5001)
