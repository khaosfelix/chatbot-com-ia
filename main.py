# Chatbot com IA
# Input do chat (campo de mensagem)
# A cada mensagem que o usuário enviar:
    # Mostrar a mensagem que o usuário enviou no chat
    # Pegar a pergunta e enviar para uma IA responder
    # Exibir a resposta da IA na tela

# Streamlit -> Apenas com Python criar o frontend e backend do site
# A IA utilizada: OpenAI

import os
import streamlit as st
from openai import OpenAI


# Configuração da página
st.set_page_config(
    page_title="Chatbot com IA",
    page_icon="🔮",
    layout="centered",
)


# CSS da página
st.markdown("""
<style>
    .stApp {
        background:
            radial-gradient(circle at top left, rgba(130, 60, 255, 0.18), transparent 30%),
            radial-gradient(circle at top right, rgba(255, 0, 170, 0.10), transparent 25%),
            linear-gradient(180deg, #09070f 0%, #120b1f 45%, #050408 100%);
        color: #f5edff;
    }

    .block-container {
        padding-top: 2rem;
        padding-bottom: 2rem;
        max-width: 860px;
    }

    h1, h2, h3 {
        color: #f3e8ff !important;
        letter-spacing: 0.5px;
    }

    .hero-box {
        border: 1px solid rgba(180, 120, 255, 0.25);
        background: linear-gradient(135deg, rgba(25, 18, 40, 0.95), rgba(12, 10, 20, 0.92));
        border-radius: 22px;
        padding: 24px 24px 18px 24px;
        box-shadow: 0 0 30px rgba(120, 0, 255, 0.12);
        margin-bottom: 18px;
    }

    .hero-title {
        font-size: 2.2rem;
        font-weight: 800;
        margin-bottom: 0.35rem;
        color: #efe5ff;
    }

    .hero-subtitle {
        font-size: 1rem;
        color: #cdb8ef;
        line-height: 1.6;
        margin-bottom: 0;
    }

    .pill-row {
        display: flex;
        gap: 8px;
        flex-wrap: wrap;
        margin-top: 14px;
    }

    .pill {
        background: rgba(123, 57, 255, 0.14);
        color: #eadbff;
        border: 1px solid rgba(177, 125, 255, 0.20);
        padding: 6px 12px;
        border-radius: 999px;
        font-size: 0.88rem;
    }

    [data-testid="stChatMessage"] {
        background: rgba(18, 14, 29, 0.72);
        border: 1px solid rgba(172, 123, 255, 0.12);
        border-radius: 18px;
        padding: 10px 8px;
        box-shadow: 0 6px 20px rgba(0, 0, 0, 0.18);
        backdrop-filter: blur(6px);
    }

    [data-testid="stChatInput"] {
        background: rgba(14, 10, 22, 0.9);
        border-top: 1px solid rgba(172, 123, 255, 0.15);
        padding-top: 0.8rem;
    }

    .stTextInput > div > div,
    .stChatInputContainer textarea {
        background-color: rgba(20, 14, 32, 0.95) !important;
        color: #f7f2ff !important;
        border-radius: 14px !important;
        border: 1px solid rgba(170, 120, 255, 0.22) !important;
    }

    .stButton > button {
        background: linear-gradient(135deg, #6d28d9, #a21caf);
        color: white;
        border: none;
        border-radius: 12px;
        padding: 0.55rem 1rem;
        font-weight: 700;
    }

    .stButton > button:hover {
        filter: brightness(1.08);
        border: none;
    }

    [data-testid="stSidebar"] {
        background: linear-gradient(180deg, #0b0812, #151024);
        border-right: 1px solid rgba(172, 123, 255, 0.10);
    }

    .sidebar-card {
        background: rgba(25, 18, 40, 0.85);
        border: 1px solid rgba(172, 123, 255, 0.16);
        border-radius: 18px;
        padding: 16px;
        margin-top: 8px;
    }

    .small-note {
        color: #bca8d8;
        font-size: 0.9rem;
        line-height: 1.5;
    }

    .empty-state {
        border: 1px dashed rgba(172, 123, 255, 0.20);
        background: rgba(14, 10, 22, 0.65);
        border-radius: 18px;
        padding: 20px;
        margin-top: 8px;
        color: #d8c7f2;
    }
</style>
""", unsafe_allow_html=True)


# Configurar chave da API
api_key = st.secrets.get("OPENAI_API_KEY") if "OPENAI_API_KEY" in st.secrets else os.getenv("OPENAI_API_KEY")

if not api_key:
    st.error("Adicione sua chave da OpenAI em OPENAI_API_KEY para usar o chatbot.")
    st.stop()

modelo_ia = OpenAI(api_key=api_key)


# Sidebar
with st.sidebar:
    st.markdown("## 🖤 Sobre")
    st.markdown("""
    <div class="sidebar-card">
        <div class="small-note">
            Assistente de conversa com interface personalizada e histórico em tempo real.<br><br>
            Feito com <b>Python</b>, <b>Streamlit</b> e <b>OpenAI</b>.
        </div>
    </div>
    """, unsafe_allow_html=True)

    st.markdown("## ⚙️ Controles")
    limpar = st.button("Limpar conversa")

    st.markdown("""
    <div class="sidebar-card">
        <div class="small-note">
           Base para experimentos com interface, prompts e integração com IA
        </div>
    </div>
    """, unsafe_allow_html=True)


# Título e descrição
st.markdown("""
<div class="hero-box">
    <div class="hero-title">🔮 Chatbot com IA</div>
    <p class="hero-subtitle">
        Um chat com IA misturando tecnologia, criatividade e um toque místico
    </p>
    <div class="pill-row">
        <span class="pill">Python</span>
        <span class="pill">Streamlit</span>
        <span class="pill">OpenAI</span>
        <span class="pill">Dark aesthetic</span>
    </div>
</div>
""", unsafe_allow_html=True)


# Lista de mensagens
if "lista_mensagens" not in st.session_state:
    st.session_state["lista_mensagens"] = []

if limpar:
    st.session_state["lista_mensagens"] = []


# Input do usuário
texto_usuario = st.chat_input("Digite sua mensagem...")


# Mostrar mensagens antigas
for mensagem in st.session_state["lista_mensagens"]:
    role = mensagem["role"]
    content = mensagem["content"]

    avatar = "🦇" if role == "assistant" else "🖤"
    with st.chat_message(role, avatar=avatar):
        st.write(content)


# Estado inicial
if not st.session_state["lista_mensagens"]:
    st.markdown("""
    <div class="empty-state">
        <b>Algumas ideias para começar:</b><br><br>
        ✦ Me conte uma curiosidade histórica<br>
        ✦ Crie um poema em estilo gótico<br>
        ✦ Me explique um conceito de Python de forma simples<br>
        ✦ Sugira ideias para um projeto criativo com IA
    </div>
    """, unsafe_allow_html=True)


# Quando o usuário envia uma mensagem
if texto_usuario:
    with st.chat_message("user", avatar="🖤"):
        st.write(texto_usuario)

    mensagem_usuario = {"role": "user", "content": texto_usuario}
    st.session_state["lista_mensagens"].append(mensagem_usuario)

    with st.chat_message("assistant", avatar="🦇"):
        with st.spinner("Consultando a IA..."):
            resposta_ia = modelo_ia.chat.completions.create(
                messages=st.session_state["lista_mensagens"],
                model="gpt-4o"
            )

            texto_resposta_ia = resposta_ia.choices[0].message.content
            st.write(texto_resposta_ia)

    mensagem_ia = {"role": "assistant", "content": texto_resposta_ia}
    st.session_state["lista_mensagens"].append(mensagem_ia)
