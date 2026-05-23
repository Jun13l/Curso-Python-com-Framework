import streamlit as st

st.title('🧙‍♂️  Classes com `type()`')

st.markdown("""
Esta aplicação demonstra como usar `type()` para construir uma classe dinamicamente em tempo de execução, 
definir um método de saudação e instanciá-la com um nome personalizado.
""")

nome_usuario = st.text_input("Digite um nome para a saudação:", value="Dev")


def funcao_saudacao(self):
    return f'Olá, {self.nome}! Seja bem-vindo ao mundo da metaprogramação.'

if st.button('Criar Classe, Instanciar e Executar'):
    
   
    Dinamica = type(
        'ClasseDinamica', 
        (object,), 
        {'saudacao': funcao_saudacao}
    )
    

    objeto_dinamico = Dinamica()
 
    objeto_dinamico.nome = nome_usuario
    
    st.success("Classe criada e instanciada com sucesso!")
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.metric(label="Tipo do Objeto", value=str(type(objeto_dinamico).__name__))
        st.caption("Repare que o nome da classe é exatamente o que passamos para o `type()`.")
        
    with col2:
        st.metric(label="Métodos Encontrados", value="saudacao()" if hasattr(objeto_dinamico, 'saudacao') else "Nenhum")
    

    resultado_metodo = objeto_dinamico.saudacao()
    
    st.info(f"**Resultado do método `.saudacao()`:**  \n{resultado_metodo}")