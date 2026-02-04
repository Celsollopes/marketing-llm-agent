import streamlit as st
from dotenv import load_dotenv
from backend import MarketingAssistant

# Carrega as variáveis de ambiente do arquivo .env (se rodando localmente)
load_dotenv()

# Configuração da Página
st.set_page_config(
    page_title="Gerador de Posts IA",
    page_icon="🤖",
    layout="centered"
)

# Título e Subtítulo
st.title("🤖 Agente de Marketing Digital")
st.markdown("---")

# Inicializa o Backend
# Usamos session_state para não reiniciar a classe a cada clique, economizando recursos
if "agent" not in st.session_state:
    try:
        st.session_state.agent = MarketingAssistant()
    except ValueError as e:
        st.error(f"Erro de configuração: {e}")
        st.stop()

# Layout de Colunas para os Inputs
col1, col2 = st.columns(2)

with col1:
    platform = st.selectbox(
        "Para qual rede social?",
        ["Instagram", "LinkedIn", "Twitter/X", "Facebook", "Blog"]
    )

with col2:
    tone = st.selectbox(
        "Qual o tom de voz?",
        ["Profissional e Sério", "Divertido e Casual", "Inspirador", "Vendas/Persuasivo", "Educativo"]
    )

topic = st.text_area(
    "Sobre o que você quer falar?",
    placeholder="Ex: Dicas para aprender Python em 2026, Benefícios da meditação, Promoção de Black Friday...",
    height=100
)

generate_btn = st.button("✨ Gerar Post", type="primary", use_container_width=True)

# Área de Resultado
if generate_btn:
    if not topic:
        st.warning("Por favor, digite um tópico para o post.")
    else:
        with st.spinner("Criando conteúdo incrível para você..."):
            try:
                result = st.session_state.agent.generate_post(topic, platform, tone)
                
                st.success("Post gerado com sucesso!")
                st.markdown("### Pré-visualização")
                st.markdown("---")
                st.markdown(result)
                
                # Botão útil para copiar
                st.text_area("Copiar Texto", value=result, height=250)
                
            except Exception as e:
                st.error(f"Ocorreu um erro: {e}")

# Rodapé profissional
st.markdown("---")
st.caption("Desenvolvido para fins de estudo em Engenharia de Prompt e LLMs.")