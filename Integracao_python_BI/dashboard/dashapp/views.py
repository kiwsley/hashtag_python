from dash import html,dcc,Input, Output
from dashapp import app, server

opcoes_dropdown = [
    {"label": "Dia 1", "value": "Dia 1"},
    {"label": "Dia 2", "value": "Dia 2"}
]

layout_dashboard  = html.Div([
    html.H2("Meu Dashboard"),
    dcc.Dropdown(id="dropdown", options=opcoes_dropdown, value="Dia 1"),
    dcc.Graph(id="grafico"),
])

layout_homepage = html.Div([
    html.H2("Criar conta"),
    html.Div([
        dcc.Input(id="email",type='email',placeholder='Seu e-mail ...'),
        dcc.Input(id="senha",type="password",placeholder="Senha"),
        html.Button("Criar conta",id="botao-criarconta"),
        dcc.Link("Já tem uma conta? faça a sua","/")

    ],className="form-column")

])

layout_login = html.Div([
    html.H2("Faça seu login"),
    html.Div([
        dcc.Input(id="email",type='email',placeholder='Seu e-mail ...'),
        dcc.Input(id="senha",type="password",placeholder="Senha"),
        html.Button("faça login",id="botao-login"),
        dcc.Link("Não tem uma conta? crie aqui","/")

    ],className="form-column")
])

layout_erro = html.Div([
    html.H2("Erro de acesso"),
    html.Div([
        dcc.Link("Clique Aqui para criar uma Conta","/"),
        dcc.Link("Clique para fazer login","/login")
    ],className="form-column")
    
])


app.layout = html.Div([
    dcc.Location(id='url', refresh = False),
    html.H1("Dashapp"),
    html.Div(id='conteudo_pagina')
    
])

@app.callback(Output("conteudo_pagina","children"),Input("url","pathname"))
def carregar_pagina(pathname):
    if pathname == '/':
        return layout_homepage
    elif pathname =='/dashboard':
        return layout_dashboard
    elif pathname =='/login':
        return layout_login
    elif pathname =='/erro':
        return layout_erro

@app.callback(Output("grafico", "figure"), Input("dropdown", "value"))
def atualizar_grafico(valor_dropdown):
    if valor_dropdown == "Dia 1":
        pontos = {"x": [1, 2, 3, 4], "y": [4, 1, 2, 1]}
        titulo = "Gráfico Dia 1"
    else:
        pontos = {"x": [1, 2, 3, 4], "y": [2, 3, 2, 4]}
        titulo = "Gráfico Dia 2"
    return {"layout": {"title": titulo}, "data": [pontos]}


@server.route("/novatela")
def nova_tela():
    return"nova tela pelo flask"