import streamlit as st
import google.generativeai as genai

genai.configure(api_key="AIzaSyBp_GIqeKnOOdJN3_7V_s5mVWtJBooBcLc")
model = genai.GenerativeModel("gemini-2.0-flash")

st.set_page_config(page_title="Gerador de Histórias", page_icon="📖")


def gerar_inicio_historia(prompt):
    try:
        response = model.generate_content(prompt)
        return response.text
    except Exception as e:
        return f"Erro ao gerar história: {str(e)}"


st.title("📚 Gerador de Início de História com IA")


nome_protagonista = st.text_input("Nome do Protagonista:")
genero = st.selectbox("Gênero Literário:", ["Fantasia", "Ficção Científica", "Mistério", "Aventura"])
local_inicial = st.radio("Local Inicial da História:",
                         ["Uma floresta antiga", "Uma cidade futurista", "Um castelo assombrado", "Uma nave espacial à deriva"])
frase_desafio = st.text_area("Frase de Efeito ou Desafio Inicial:")


if st.button("Gerar Início da História"):
    if nome_protagonista.strip() and frase_desafio.strip():
        with st.spinner("Gerando a história..."):

            prompt = (
                f"Crie o início de uma história do gênero '{genero}' com o protagonista chamado '{nome_protagonista}'. "
                f"A história começa em '{local_inicial}'. Incorpore a seguinte frase ou desafio no início: '{frase_desafio}'. "
                "A história deve conter um ou dois parágrafos e despertar a curiosidade do leitor."
            )
            historia = gerar_inicio_historia(prompt)
            st.subheader("✨ Início da História:")
            st.write(historia)
    else:
        st.warning("Por favor, preencha o nome do protagonista e a frase de desafio.")