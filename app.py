import streamlit as st
import google.generativeai as genai

# Configuração da Página
st.set_page_config(page_title="Nano Bet Design", page_icon="🎯")
st.title("🎯 Nano Bet Design App")

# AQUI ESTÁ A CORREÇÃO: A chave agora tem aspas ("")
api_key = "AIzaSyBRfe5Sf_hNdVWsLez9hFP3leoygEtcRQ"
genai.configure(api_key=api_key)

# O CÉREBRO DO AGENTE (Instruções dos Experts)
SYSTEM_PROMPT = """
Nome do Agente: Nano Bet Design. Persona: Diretor de Arte Pro.
Experts Cadastrados:
- Herculano: Rosa #df3891, Verde #c2ff35.
- Helder da Bet: Verde #00ff1e.
- Nascimento: Verde #37c200.
- Raquel Maia: Azul #22447f, Verde #c7ff28.
- Neto Lima: Ciano #64e6f9.
- Nalanda Tips: Roxo #cd00ff.
- MD: Verde #5acd51.
- Luiz Royal: Ciano #00fffc.
- Danda: Verde #00ff06.
- Camillo: Verde #00ff30.
- Bruno Karttos: Amarelo #f9b61d.
- Luisa Mendes: Roxo #8400ff.

Regras: 15% de margem no topo/base. Gerar prompts em INGLÊS.
Fluxo: 1. Saudação; 2. Triagem; 3. Prompt Técnico; 4. Ajustes.
"""

# Inicializar o modelo com as instruções
model = genai.GenerativeModel(
    model_name="gemini-1.5-flash",
    system_instruction=SYSTEM_PROMPT
)

if "chat" not in st.session_state:
    st.session_state.chat = model.start_chat(history=[])

# Mostrar o chat
for message in st.session_state.chat.history:
    role = "user" if message.role == "user" else "assistant"
    with st.chat_message(role):
        st.markdown(message.parts[0].text)

if prompt := st.chat_input("Para qual expert vamos criar hoje?"):
    with st.chat_message("user"):
        st.markdown(prompt)
    
    response = st.session_state.chat.send_message(prompt)
    
    with st.chat_message("assistant"):
        st.markdown(response.text)
