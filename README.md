# Prompt Studio

A bilingual AI chat built with Python, Streamlit, and the Gemini API. The interface opens in English by default, with Portuguese available from the language selector.

## Preview

Prompt Studio provides a focused chat workspace with conversation history, starter prompts, clear API status, and helpful error states. The interface remains usable as a preview before an API key is configured.

## Features

- English-first interface with full Portuguese localization
- Gemini chat completions through Google's OpenAI-compatible API
- Conversation history and one-click starter prompts
- API key stored outside source code, with local and Streamlit Cloud setup
- Localized handling for missing keys, rate limits, authentication, and connection errors
- Responsive Streamlit layout

## Run locally

Requires Python 3.10 or newer.

```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
python -m pip install -r requirements.txt
Copy-Item .streamlit/secrets.toml.example .streamlit/secrets.toml
```

Add a Gemini API key to `.streamlit/secrets.toml`:

```toml
GEMINI_API_KEY = "your-gemini-api-key"
```

Get a key from [Google AI Studio](https://aistudio.google.com/apikey), then start the app:

```powershell
streamlit run app.py
```

The example secrets file is safe to commit; `.streamlit/secrets.toml` is ignored by Git. Never publish a real API key.

## Deploy

Deploy the repository with [Streamlit Community Cloud](https://share.streamlit.io/), set `app.py` as the entry point, and add `GEMINI_API_KEY` in the app's Secrets settings.

## Tech stack

Python · Streamlit · OpenAI Python SDK · Gemini API

---

# Prompt Studio (Português)

Um chat bilíngue com IA, criado com Python, Streamlit e a API Gemini. A interface abre em inglês por padrão; selecione português no menu lateral.

## Recursos

- Interface em inglês com localização completa para português
- Respostas do Gemini pela API compatível com OpenAI
- Histórico da conversa e sugestões para começar
- Chave de API protegida fora do código-fonte
- Mensagens de erro traduzidas e interface responsiva
- Tela de demonstração disponível mesmo sem configurar a chave

## Executar localmente

É necessário ter Python 3.10 ou superior. Siga as instruções de instalação da seção [Run locally](#run-locally) e configure sua chave Gemini em `.streamlit/secrets.toml`. Para iniciar, execute `streamlit run app.py`.

Para publicar, use o [Streamlit Community Cloud](https://share.streamlit.io/) e configure `GEMINI_API_KEY` na área de Secrets do aplicativo.