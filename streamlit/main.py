import streamlit as st
import pandas as pd
import yfinance as yf
from datetime import timedelta

#criar as funções de carregamento de dados
#cotações itau

@st.cache_data
def carregarDados(empresas):
    textotickerts = " ".join(empresas)
    dadosAcao = yf.Tickers(textotickerts)
    cotacao = dadosAcao.history(period='1d',start ="2010-01-01" ,end="2024-07-01")
    cotacao=cotacao['Close']
    return cotacao

#preparação as visualização

acoes=['ITUB4.SA','VALE3.SA','ABEV3.SA','GGBR4.SA']
dados = carregarDados(acoes)




#criar a interface
st.write(""" 
# App preço de Ações
O Gráfico Abaoixo representa a evolução do preço das ações
""") #pode formatar

#lista de ações

#filtragem

st.sidebar.header("Filtros")

listaAcoes = st.sidebar.multiselect("Escolha as Ações para visualizar",dados.columns)

if listaAcoes:
    dados=dados[listaAcoes]
    if len(listaAcoes) == 1:
        acaoUnica =  listaAcoes[0]
        dados = dados.rename(columns={acaoUnica:"Close"})
   
#filtro de datas
dataInicial=dados.index.min().to_pydatetime()
dataFinal=dados.index.max().to_pydatetime()
intervaloData=st.sidebar.slider("Selecione o periodo", #Tupla das datas
                                min_value=dataInicial,
                                max_value=dataFinal,
                                value=(dataInicial,dataFinal),
                                step=timedelta(days=1))

dados= dados.loc[intervaloData[0]:intervaloData[1]]

st.line_chart(dados)

