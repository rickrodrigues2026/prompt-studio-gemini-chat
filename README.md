# Prompt Studio

[![Python](https://img.shields.io/badge/Python-3.10%2B-3776AB?logo=python&logoColor=white)](https://www.python.org/)
[![Streamlit](https://img.shields.io/badge/Streamlit-1.40%2B-FF4B4B?logo=streamlit&logoColor=white)](https://streamlit.io/)
[![Gemini API](https://img.shields.io/badge/Gemini-API-8E75FF?logo=google&logoColor=white)](https://ai.google.dev/)
[![License: MIT](https://img.shields.io/badge/License-MIT-green.svg)](LICENSE)
[![Open in Streamlit](https://static.streamlit.io/badges/streamlit_badge_black_white.svg)](https://prompt-studio-gemini-chat.streamlit.app)

A bilingual AI chat application built with **Python**, **Streamlit**, and **Google Gemini API**. Designed with English as the primary experience and Portuguese localization for accessibility.

## Overview

Prompt Studio is a focused, production-ready chat interface that demonstrates:
- Real-world integration with modern AI APIs (Gemini via OpenAI-compatible endpoints)
- Bilingual UX with English-first design principles
- Secure secret management for local development and cloud deployment
- Comprehensive error handling and user feedback
- Professional UI/UX patterns with custom Streamlit theming

## ✨ Key Features

- **English-First Interface** with complete Portuguese localization
- **Real-time AI Responses** powered by Google Gemini 3.8 Flash
- **Conversation History** within the active session
- **Smart Starter Prompts** to guide user interactions
- **API Status Indicator** with clear connection feedback
- **Comprehensive Error Handling** for authentication, rate limits, and connectivity
- **Responsive Design** optimized for desktop and mobile
- **Secure Secret Management** with `.gitignore` protection

## 🏗️ Architecture

```
┌─────────────────────────────────────────────┐
│         Streamlit Frontend (UI/UX)          │
│  - Bilingual Interface (EN/PT)              │
│  - Chat History Management                  │
│  - Real-time Status Display                 │
└──────────────────┬──────────────────────────┘
                   │
                   ▼
┌─────────────────────────────────────────────┐
│      OpenAI-Compatible API Client           │
│  - Gemini Model Integration                 │
│  - Error Handling & Retry Logic             │
│  - Session Caching                          │
└──────────────────┬──────────────────────────┘
                   │
                   ▼
┌─────────────────────────────────────────────┐
│   Google Gemini API (Cloud)                 │
│  - Model: gemini-1.5-flash                  │
│  - Endpoint: generativelanguage.googleapis  │
└─────────────────────────────────────────────┘
```

## 📋 Tech Stack

| Technology | Purpose |
|-----------|---------|
| **Python 3.10+** | Backend runtime |
| **Streamlit 1.40+** | Web framework & UI |
| **OpenAI SDK** | Gemini API client |
| **Google Gemini API** | Language model |

## 🚀 Quick Start

### Prerequisites

- Python 3.10 or newer
- [Gemini API key](https://aistudio.google.com/apikey) (free tier available)

### 1. Clone & Setup

```bash
# Clone repository
git clone https://github.com/rickrodrigues2026/prompt-studio-gemini-chat.git
cd prompt-studio-gemini-chat

# Create virtual environment
python -m venv .venv
source .venv/bin/activate  # On Windows: .\.venv\Scripts\Activate.ps1

# Install dependencies
python -m pip install --upgrade pip
python -m pip install -r requirements.txt
```

### 2. Configure API Key

```bash
# Copy secrets template
cp .streamlit/secrets.toml.example .streamlit/secrets.toml
```

Edit `.streamlit/secrets.toml`:
```toml
GEMINI_API_KEY = "your-gemini-api-key-here"
```

Get a free API key from [Google AI Studio](https://aistudio.google.com/apikey)

### 3. Run Locally

```bash
streamlit run app.py
```

The app will open at `http://localhost:8501`

## 📦 Project Structure

```
prompt-studio-gemini-chat/
├── app.py                      # Main Streamlit application
├── requirements.txt            # Python dependencies
├── README.md                   # This file
├── LICENSE                     # MIT License
├── CONTRIBUTING.md             # Contribution guidelines
├── .gitignore                  # Git ignore rules
├── .streamlit/
│   ├── config.toml            # Streamlit theme configuration
│   ├── secrets.toml           # Local secrets (git-ignored)
│   └── secrets.toml.example   # Template for secrets
└── .venv/                     # Virtual environment (local only)
```

## 🌐 Deployment

### Streamlit Community Cloud

1. Push repository to GitHub
2. Visit [Streamlit Community Cloud](https://share.streamlit.io/)
3. Create new app → Select repository & set `app.py` as entry point
4. Add `GEMINI_API_KEY` in **Secrets** section
5. Deploy

### Environment Variables

The app checks for `GEMINI_API_KEY` in this order:
1. `.streamlit/secrets.toml` (local development)
2. Streamlit Cloud Secrets (production)
3. System environment variable `GEMINI_API_KEY`

## 🔐 Security

- **Never commit real API keys** - `.streamlit/secrets.toml` is in `.gitignore`
- **Use `.streamlit/secrets.toml.example`** as a safe template
- **Treat secrets like database credentials** - handle with care
- **Messages sent to Gemini servers** - review privacy before sharing sensitive data

## 🎨 Customization

### Change Language Default

Edit the language selector default in `app.py`:

```python
selected_language = st.session_state.get("language", "English")  # Change to "Português"
```

### Modify Theme

Edit `.streamlit/config.toml`:

```toml
[theme]
primaryColor = "#315e4b"  # Your color here
```

## 🤝 Contributing

Contributions welcome! See [CONTRIBUTING.md](CONTRIBUTING.md) for:
- Code style guidelines
- Pull request process
- Development workflow
- Translation standards

## 📄 License

This project is licensed under the **MIT License** - see [LICENSE](LICENSE) for details.

## 👤 Author

Created by [rickrodrigues2026](https://github.com/rickrodrigues2026)

---

# Prompt Studio (Português)

Um aplicativo de chat com IA bilíngue, construído com **Python**, **Streamlit** e **API Gemini do Google**. Focado em inglês como experiência principal, com localização em português para acessibilidade.

## Visão Geral

O Prompt Studio é uma interface de chat organizada e pronta para produção que demonstra:
- Integração com APIs modernas de IA (Gemini via endpoints compatíveis com OpenAI)
- UX bilíngue com design focado em inglês
- Gerenciamento seguro de chaves para desenvolvimento local e cloud
- Tratamento abrangente de erros e feedback ao usuário
- Padrões profissionais de UI/UX com tema customizado no Streamlit

## ✨ Recursos Principais

- **Interface em Inglês** com tradução completa para português
- **Respostas em Tempo Real** da Gemini 3.8 Flash
- **Histórico de Conversa** na sessão ativa
- **Sugestões de Prompts** para guiar interações
- **Indicador de Status** com feedback claro de conexão
- **Tratamento de Erros Completo** para autenticação, limites e conectividade
- **Design Responsivo** otimizado para desktop e móvel
- **Gerenciamento Seguro** de secrets

## 🚀 Início Rápido

### Pré-requisitos

- Python 3.10 ou superior
- [Chave de API Gemini](https://aistudio.google.com/apikey) (nível gratuito disponível)

### 1. Clone e Configure

```bash
git clone https://github.com/rickrodrigues2026/prompt-studio-gemini-chat.git
cd prompt-studio-gemini-chat

python -m venv .venv
source .venv/bin/activate
python -m pip install --upgrade pip
python -m pip install -r requirements.txt
```

### 2. Configure a Chave de API

```bash
cp .streamlit/secrets.toml.example .streamlit/secrets.toml
```

Edite `.streamlit/secrets.toml`:
```toml
GEMINI_API_KEY = "sua-chave-gemini"
```

### 3. Execute Localmente

```bash
streamlit run app.py
```

### Implantação

Implante no [Streamlit Community Cloud](https://share.streamlit.io/) definindo `app.py` como ponto de entrada e adicionando `GEMINI_API_KEY` nos secrets.

## 🔐 Segurança

- Nunca commite chaves reais - `.streamlit/secrets.toml` está em `.gitignore`
- Use apenas `.streamlit/secrets.toml.example` como template seguro
- As mensagens são enviadas para servidores da Gemini - revise a privacidade antes de compartilhar dados sensíveis

## 📄 Licença

Licenciado sob a **Licença MIT** - veja [LICENSE](LICENSE)

## 🤝 Contribuições

Contribuições bem-vindas! Consulte [CONTRIBUTING.md](CONTRIBUTING.md)
