# Portfólio streamlit:

# Crie um portfólio programado a objetos com Streamlit

# Nome

# link do github

# imagem que te representa

# email ficticio

# whatsapp fictcion

# endereço fake

# link audio


import streamlit as st

st.set_page_config(page_title="Portfólio", page_icon="💻")


class Perfil:
    def __init__(self, nome, email, whatsapp, endereco,):
        self.nome = nome
        self.email = email
        self.whatsapp = whatsapp
        self.endereco = endereco
    
    def exibir_topo(self):
        st.title(self.nome)
        
        
    
        try:
            st.image('img.jpg', width=200, caption="")
        except:
            st.warning()

    def exibir_contatos(self):
        st.header("Contato")
        st.write(f" **Email:** {self.email}")
        st.write(f" **WhatsApp:** {self.whatsapp}")
        st.write(f" **Endereço** {self.endereco}")



class Projeto:
    def __init__(self, titulo, descricao, link_github):
        self.titulo = titulo
        self.descricao = descricao
        self.link = link_github

    def exibir_card(self):
        with st.container(border=True):
            st.subheader(self.titulo)
            st.write(self.descricao)
            st.link_button("Ver no GitHub", self.link)




juniel = Perfil(
    nome="Juniel Alves de Sousa",
    email="Juniel.20239@gmail.com",
    whatsapp="11 98498-743",
    endereco=": Av. Dr. Renato de Andrade Maia, 601 "

)


projeto1 = Projeto(
    titulo="Perfil Github",
    descricao="Meu Perfil no Github",
    link_github="https://github.com/Jun13l"
)



juniel.exibir_topo()

st.write("---") 


st.header("Github")
projeto1.exibir_card()

st.write("---") 


juniel.exibir_contatos()

st.audio("chuva.mp3")
