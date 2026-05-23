# import streamlit as st

# st.title('Hello World')


# st.number_input('Digite um numero')
# st.text_input('Digite')
# st.audio_input('Teste')
# st.image('img.jpg')
# st.data_input('')



# if st.button('mostrar'):
#     st.map



#-----------------------------------------------------------------------------
import streamlit as st
import pandas as pd



dados  =  {
'Dia': ['Jan','Fev','Mar'],
'Vendas':[5000.0,1000.0,9000.0]
}




df =  pd.DataFrame(dados)


if st.button('Gerar Grafico'):
    st.bar_chart(df.set_index('Dia'))




df2 =  pd.read_csv('vendas.csv')


if st.button('Gerar grafico'):
    st.bar_chart(df2, x = 'vendedor', y = 'venda')
    st.table(df2)

