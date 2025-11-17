import streamlit as st
import pandas as pd
import streamlit.components.v1 as components

# ----------------------------------------------------
# CONFIGURAÇÃO DA PÁGINA
# ----------------------------------------------------
st.set_page_config(
    page_title="Mapa Integrado – Região Norte do Brasil",
    layout="wide",
    page_icon="🗺️"
)

# ----------------------------------------------------
# CSS PERSONALIZADO (VISUAL PROFISSIONAL)
# ----------------------------------------------------
st.markdown("""
<style>

    /* Fundo geral */
    .main {
        background-color: #f5f7fa;
    }

    /* Sidebar com gradiente */
    section[data-testid="stSidebar"] {
        background: linear-gradient(180deg, #081b3d, #0e295c);
        color: white !important;
    }
    section[data-testid="stSidebar"] * {
        color: white !important;
    }

    /* Título estilizado */
    .big-title {
        font-size: 40px;
        font-weight: 800;
        color: #0e295c;
        text-align: center;
        margin-top: -20px;
        animation: fadein 1s ease;
    }

    /* Subtítulo */
    .subtitle {
        font-size: 18px;
        color: #3a4a65;
        text-align: center;
        margin-top: -10px;
    }

    /* Cards */
    .card {
        background: white;
        padding: 20px;
        border-radius: 14px;
        box-shadow: 0 4px 12px rgba(0,0,0,0.08);
        border: 1px solid #e8ecf3;
        transition: transform 0.2s ease;
    }
    .card:hover {
        transform: translateY(-3px);
    }

    /* Animação */
    @keyframes fadein {
        from { opacity: 0; transform: translateY(-10px); }
        to { opacity: 1; transform: translateY(0); }
    }

</style>
""", unsafe_allow_html=True)


# ----------------------------------------------------
# TELA INICIAL PROFISSIONAL
# ----------------------------------------------------
def exibir_tela_inicial():

    st.markdown("<h1 class='big-title'>Mapa Integrado – Região Norte do Brasil</h1>", unsafe_allow_html=True)
    st.markdown("<p class='subtitle'>Painel Interativo de Análise Geoespacial</p>", unsafe_allow_html=True)

    st.markdown("<br>", unsafe_allow_html=True)

    # LOGO CENTRALIZADA
    col1, col2, col3, col4, col5 = st.columns([1, 1, 1, 1, 1])
    with col3:
        st.image("assets/ASSINATURA-MCOM-2.png", width=450)

    st.markdown("<br>", unsafe_allow_html=True)

    # CARDS DE APRESENTAÇÃO
    c1, c2, c3 = st.columns(3)

    with c1:
        st.markdown(
            "<div class='card'><b>📍 Objetivo:</b><br>Este painel foi desenvolvido para apresentação técnica do estudo sobre conectividade na Região Norte do Brasil.</div>",
            unsafe_allow_html=True
        )

    with c2:
        st.markdown(
            "<div class='card'><b>🛰️ Abordagem:</b><br>Mapas interativos, geolocalização e indicadores.</div>",
            unsafe_allow_html=True
        )

    with c3:
        st.markdown(
            "<div class='card'><b>🌎 Aplicação:</b><br>Tomada de decisão e inclusão digital no Norte do Brasil.</div>",
            unsafe_allow_html=True
        )

    st.markdown("<br><hr><br>", unsafe_allow_html=True)

    st.markdown("""
        ### 🧭 Como navegar
        Use o menu lateral para:

        - 🗺️ Visualizar mapas interativos  
        - 🔍 Analisar distâncias geográficas  
        

        ---
    """)


# ----------------------------------------------------
# DESCRIÇÕES DOS MAPAS
# ----------------------------------------------------
descricao_infovias = {
    "Mapa Norte": (
        "Mapa interativo que apresenta diversas camadas de visualização (Populacional, ERBs, GESAC, Escolas e Infovias)"
        " sendo possivel selecionar uma ou mais camadas para visualizar, por meio da caixa de seleção no canto superior direito do mapa."
    ),
}


# ----------------------------------------------------
# TELA DE MAPA INTERATIVO PROFISSIONAL
# ----------------------------------------------------
def exibir_mapa(df):

    # Sidebar (já estilizado pelo CSS)
    with st.sidebar:
        st.header("🗺️ Mapas Disponíveis")
        filtro_distancia = st.radio("Selecione um mapa:", list(descricao_infovias.keys()))

    # Header do Mapa
    st.markdown("<h1 class='big-title'>Mapa Interativo</h1>", unsafe_allow_html=True)
    st.markdown(f"<p class='subtitle'>Este painel apresenta um mapa interativo com múltiplas camadas geoespaciais, permitindo uma análise integrada de elementos fundamentais para o planejamento e expansão da conectividade na Região Norte do Brasil</p>", unsafe_allow_html=True)

    st.markdown("<br>", unsafe_allow_html=True)

    # LOGO CENTRALIZADA
    col1, col2, col3, col4, col5 = st.columns([1, 1, 1, 1, 1])
    with col3:
        st.image("assets/ASSINATURA-MCOM-2.png", width=420)

    st.markdown("<br>", unsafe_allow_html=True)

    # CARDS DE CONTEXTO
    a, b = st.columns(2)

    with a:
        st.markdown(
            "<div class='card'><b>📌 Mapa Selecionado:</b><br>"
            f"{filtro_distancia}</div>",
            unsafe_allow_html=True
        )

    with b:
        st.markdown(
            "<div class='card'><b>🔎 Descrição:</b><br>"
            f"{descricao_infovias[filtro_distancia]}</div>",
            unsafe_allow_html=True
        )

    st.markdown("<br>", unsafe_allow_html=True)

    # CARREGAR O MAPA HTML
    caminho_html = f"mapas/{filtro_distancia}.html"

    st.subheader("🌐 Visualização Interativa")

    try:
        with open(caminho_html, "r", encoding="utf-8") as f:
            mapa_html = f.read()

        components.html(
            mapa_html,
            height=820,
            width=None,
            scrolling=False
        )

    except FileNotFoundError:
        st.error(f"❌ Arquivo '{caminho_html}' não encontrado.")


# ----------------------------------------------------
# EXECUÇÃO
# ----------------------------------------------------
st.sidebar.title("📁 Navegação")
pagina = st.sidebar.radio("Ir para:", ["🏠 Início", "🗺️ Mapa Interativo"])

if pagina == "🏠 Início":
    exibir_tela_inicial()
elif pagina == "🗺️ Mapa Interativo":
    exibir_mapa(None)