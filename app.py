import os

import streamlit as st
from openai import (
    APIConnectionError,
    APIStatusError,
    AuthenticationError,
    OpenAI,
    OpenAIError,
    RateLimitError,
)


COPY = {
    "en": {
        "page_title": "Prompt Studio | Gemini Chat",
        "language": "Language",
        "sidebar_intro": "A small, thoughtful space to explore ideas with AI.",
        "connection": "GEMINI CONNECTION",
        "connected": "API key configured",
        "not_connected": "API key needed",
        "setup": "Add `GEMINI_API_KEY` to `.streamlit/secrets.toml` to enable chat.",
        "privacy": "Messages are sent to the Gemini API. Do not share sensitive information.",
        "clear": "Clear conversation",
        "about": "BUILT WITH",
        "title": "A clearer way to think out loud.",
        "subtitle": "A bilingual AI chat, powered by Gemini. Start with a prompt or bring your own question.",
        "online": "GEMINI 3.8 FLASH",
        "empty_title": "What would you like to explore?",
        "empty_copy": "Choose a starting point, or ask anything in your own words.",
        "prompts": [
            "Explain a complex idea in simple terms",
            "Help me plan a focused week",
            "Give me feedback on a project idea",
        ],
        "input": "Message Prompt Studio...",
        "system": "You are a thoughtful, concise, and practical assistant. Reply in the same language as the user's latest message.",
        "missing_key": "Chat is paused until a Gemini API key is configured. Add it to `.streamlit/secrets.toml`, then restart the app.",
        "auth_error": "Gemini rejected the API key. Check that it is valid and enabled for the Gemini API.",
        "rate_error": "The Gemini request limit was reached. Wait a moment and try again.",
        "connection_error": "Could not reach Gemini. Check your internet connection and try again.",
        "service_error": "Gemini could not complete this request. Please try again shortly.",
        "http_status": "Gemini HTTP status: {status_code}",
        "generic_error": "Something went wrong while generating a reply. Please try again.",
        "empty_response": "Gemini returned an empty response. Please try another message.",
        "footer": "An independent portfolio project · Python · Streamlit · Gemini API",
    },
    "pt": {
        "page_title": "Prompt Studio | Chat Gemini",
        "language": "Idioma",
        "sidebar_intro": "Um espaço simples e cuidadoso para explorar ideias com IA.",
        "connection": "CONEXÃO GEMINI",
        "connected": "Chave de API configurada",
        "not_connected": "Chave de API necessária",
        "setup": "Adicione `GEMINI_API_KEY` a `.streamlit/secrets.toml` para ativar o chat.",
        "privacy": "As mensagens são enviadas à API Gemini. Não compartilhe informações sensíveis.",
        "clear": "Limpar conversa",
        "about": "TECNOLOGIAS",
        "title": "Um jeito mais claro de pensar em voz alta.",
        "subtitle": "Um chat bilíngue com IA, integrado ao Gemini. Comece com uma sugestão ou faça sua pergunta.",
        "online": "GEMINI 3.8 FLASH",
        "empty_title": "O que você gostaria de explorar?",
        "empty_copy": "Escolha um ponto de partida ou pergunte com suas próprias palavras.",
        "prompts": [
            "Explique uma ideia complexa de forma simples",
            "Ajude-me a planejar uma semana produtiva",
            "Dê feedback sobre uma ideia de projeto",
        ],
        "input": "Envie uma mensagem ao Prompt Studio...",
        "system": "Você é um assistente atencioso, conciso e prático. Responda no mesmo idioma da mensagem mais recente do usuário.",
        "missing_key": "O chat está pausado até que uma chave da API Gemini seja configurada. Adicione-a a `.streamlit/secrets.toml` e reinicie o app.",
        "auth_error": "O Gemini não aceitou a chave da API. Confira se ela é válida e está habilitada para a API Gemini.",
        "rate_error": "O limite de solicitações do Gemini foi atingido. Aguarde um pouco e tente novamente.",
        "connection_error": "Não foi possível acessar o Gemini. Verifique sua conexão e tente novamente.",
        "service_error": "O Gemini não conseguiu concluir esta solicitação. Tente novamente em instantes.",
        "http_status": "Status HTTP do Gemini: {status_code}",
        "generic_error": "Ocorreu um erro ao gerar a resposta. Tente novamente.",
        "empty_response": "O Gemini retornou uma resposta vazia. Tente enviar outra mensagem.",
        "footer": "Projeto independente de portfólio · Python · Streamlit · API Gemini",
    },
}


st.set_page_config(
    page_title="Prompt Studio | Gemini Chat",
    page_icon="✳",
    layout="wide",
    initial_sidebar_state="expanded",
)

st.markdown(
    """
    <style>
    @import url('https://fonts.googleapis.com/css2?family=DM+Sans:wght@400;500;600;700&family=Manrope:wght@400;500;600;700;800&display=swap');

    :root {
        --ink: #172521;
        --muted: #68766f;
        --paper: #f7f8f4;
        --line: #dce3dc;
        --green: #315e4b;
        --lime: #d9f17c;
        --coral: #c5674c;
    }
    .stApp { background: var(--paper); color: var(--ink); }
    [data-testid="stHeader"] { background: transparent; }
    [data-testid="stSidebar"] {
        background: #edf1e9;
        border-right: 1px solid var(--line);
    }
    [data-testid="stSidebar"] > div { padding-top: 2rem; }
    .block-container { max-width: 1100px; padding-top: 3rem; padding-bottom: 2rem; }
    html, body, [class*="css"] { font-family: 'DM Sans', sans-serif; }
    h1, h2, h3 { font-family: 'Manrope', sans-serif !important; color: var(--ink); }
    h1 { font-size: 3rem !important; letter-spacing: 0 !important; line-height: 1.08 !important; }
    .brand { font: 800 1.05rem 'Manrope', sans-serif; letter-spacing: 0; color: var(--ink); }
    .brand-mark { display: inline-grid; place-items: center; width: 27px; height: 27px; margin-right: 8px; border-radius: 8px; background: var(--green); color: var(--lime); }
    .eyebrow { color: var(--green); font-size: .72rem; font-weight: 700; letter-spacing: 0; }
    .subtitle { color: var(--muted); font-size: 1.04rem; max-width: 640px; line-height: 1.65; }
    .status { display: inline-flex; align-items: center; gap: 8px; border: 1px solid var(--line); border-radius: 99px; padding: 8px 12px; color: var(--green); font-size: .72rem; font-weight: 700; letter-spacing: 0; white-space: nowrap; }
    .status-dot { width: 7px; height: 7px; border-radius: 50%; background: #79a873; }
    .key-state { border: 1px solid var(--line); border-radius: 8px; padding: 10px 12px; font-size: .82rem; font-weight: 600; }
    .key-state.connected { background: #e8f1e7; color: var(--green); }
    .key-state.pending { background: #fbede7; color: #814d3f; }
    .setup-notice { margin: 1rem 0; border: 1px solid #cbd9cc; border-left: 4px solid var(--green); border-radius: 8px; padding: 14px 16px; color: var(--ink); background: #edf3eb; font-size: .9rem; line-height: 1.55; }
    .empty-state { margin: 2.5rem 0 1rem; padding: 2rem 0 1rem; border-top: 1px solid var(--line); }
    .empty-state h2 { font-size: 1.35rem; margin-bottom: .4rem; }
    .empty-state p { color: var(--muted); margin-top: 0; }
    .sidebar-label { color: var(--muted); font-size: .68rem; font-weight: 700; letter-spacing: 0; margin: 1.8rem 0 .55rem; }
    .sidebar-note { color: var(--muted); font-size: .82rem; line-height: 1.55; }
    .stButton > button { border-radius: 8px; border-color: var(--line); color: var(--ink); background: rgba(255,255,255,.65); text-align: left; min-height: 3rem; transition: border-color .18s ease, background .18s ease, transform .18s ease; }
    .stButton > button:hover { border-color: var(--green); background: #fff; color: var(--green); transform: translateY(-1px); }
    .stButton > button:disabled { border-color: var(--line); color: var(--ink); background: #fff; opacity: 1; }
    [data-testid="stChatMessage"] { border: 1px solid var(--line); border-radius: 10px; background: rgba(255,255,255,.72); padding: 1rem 1.15rem; }
    [data-testid="stChatInput"] { border-color: #bfcbbf; border-radius: 10px; background: #fff; }
    [data-testid="stChatInput"]:focus-within { border-color: var(--green); box-shadow: 0 0 0 1px var(--green); }
    [data-testid="stBottom"] { background: transparent; }
    hr { border-color: var(--line); }
    .footer { border-top: 1px solid var(--line); padding-top: 1rem; margin-top: 3rem; color: var(--muted); font-size: .75rem; }
    @media (max-width: 640px) {
        .block-container { padding-top: 1.5rem; }
        h1 { font-size: 2.2rem !important; }
        .status { margin-top: .4rem; }
    }
    </style>
    """,
    unsafe_allow_html=True,
)


def get_api_key() -> str:
    try:
        secret_key = st.secrets.get("GEMINI_API_KEY", "")
    except FileNotFoundError:
        secret_key = ""
    return str(secret_key or os.getenv("GEMINI_API_KEY", "")).strip()


@st.cache_resource
def create_client(api_key: str) -> OpenAI:
    return OpenAI(
        api_key=api_key,
        base_url="https://generativelanguage.googleapis.com/v1beta/openai/",
        timeout=30.0,
        max_retries=2,
    )


def queue_prompt(prompt: str) -> None:
    st.session_state["pending_prompt"] = prompt


if "messages" not in st.session_state:
    st.session_state["messages"] = []

api_key = get_api_key()

with st.sidebar:
    st.markdown('<div class="brand"><span class="brand-mark">✳</span>Prompt Studio</div>', unsafe_allow_html=True)

    selected_language = st.session_state.get("language", "English")
    language_code = "pt" if selected_language == "Português" else "en"
    language = st.selectbox(
        COPY[language_code]["language"],
        options=["English", "Português"],
        index=0,
        key="language",
    )
    language_code = "pt" if language == "Português" else "en"
    text = COPY[language_code]
    st.markdown(f'<p class="sidebar-note">{text["sidebar_intro"]}</p>', unsafe_allow_html=True)

    st.markdown(f'<div class="sidebar-label">{text["connection"]}</div>', unsafe_allow_html=True)
    if api_key:
        st.markdown(f'<div class="key-state connected">{text["connected"]}</div>', unsafe_allow_html=True)
    else:
        st.markdown(f'<div class="key-state pending">{text["not_connected"]}</div>', unsafe_allow_html=True)
        st.caption(text["setup"])

    st.markdown(f'<div class="sidebar-note">{text["privacy"]}</div>', unsafe_allow_html=True)
    st.divider()
    if st.button(text["clear"], icon=":material/delete_outline:", use_container_width=True):
        st.session_state["messages"] = []
        st.rerun()

    st.markdown(f'<div class="sidebar-label">{text["about"]}</div>', unsafe_allow_html=True)
    st.markdown('<div class="sidebar-note">Python&nbsp;&nbsp;·&nbsp;&nbsp;Streamlit&nbsp;&nbsp;·&nbsp;&nbsp;Gemini API</div>', unsafe_allow_html=True)

st.title(text["title"])
header_left, header_right = st.columns([5, 1.5], vertical_alignment="center")
with header_left:
    st.markdown(f'<p class="subtitle">{text["subtitle"]}</p>', unsafe_allow_html=True)
with header_right:
    if api_key:
        st.markdown(f'<div class="status"><span class="status-dot"></span>{text["online"]}</div>', unsafe_allow_html=True)

if not api_key:
    st.markdown(f'<div class="setup-notice">{text["missing_key"]}</div>', unsafe_allow_html=True)

for message in st.session_state["messages"]:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

if not st.session_state["messages"]:
    st.markdown(
        f'<div class="empty-state"><h2>{text["empty_title"]}</h2><p>{text["empty_copy"]}</p></div>',
        unsafe_allow_html=True,
    )
    prompt_columns = st.columns(3)
    for index, prompt in enumerate(text["prompts"]):
        with prompt_columns[index]:
            st.button(
                prompt,
                key=f"starter_{language_code}_{index}",
                on_click=queue_prompt,
                args=(prompt,),
                disabled=not api_key,
                use_container_width=True,
            )

submitted_prompt = st.chat_input(text["input"], disabled=not api_key, max_chars=4000)
message_text = submitted_prompt or st.session_state.pop("pending_prompt", None)

if message_text and api_key:
    st.session_state["messages"].append({"role": "user", "content": message_text})
    with st.chat_message("user"):
        st.markdown(message_text)

    request_messages = [{"role": "system", "content": text["system"]}]
    request_messages.extend(st.session_state["messages"])

    with st.chat_message("assistant"):
        with st.spinner("Thinking..." if language_code == "en" else "Pensando..."):
            try:
                response = create_client(api_key).chat.completions.create(
                    model="gemini-3.8-flash",
                    messages=request_messages,
                )
                answer = response.choices[0].message.content
                answer = str(answer).strip() if answer else ""
                if answer:
                    st.markdown(answer)
                    st.session_state["messages"].append({"role": "assistant", "content": answer})
                else:
                    st.warning(text["empty_response"])
            except AuthenticationError:
                st.error(text["auth_error"])
            except RateLimitError:
                st.error(text["rate_error"])
            except APIConnectionError:
                st.error(text["connection_error"])
            except APIStatusError as error:
                st.error(text["service_error"])
                st.caption(text["http_status"].format(status_code=error.status_code))
            except OpenAIError:
                st.error(text["generic_error"])

st.markdown(f'<div class="footer">{text["footer"]}</div>', unsafe_allow_html=True)