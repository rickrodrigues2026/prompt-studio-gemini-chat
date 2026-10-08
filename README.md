# Prompt Studio

[![Python](https://img.shields.io/badge/Python-3.10%2B-3776AB?logo=python&logoColor=white)](https://www.python.org/)
[![Streamlit](https://img.shields.io/badge/Streamlit-1.40%2B-FF4B4B?logo=streamlit&logoColor=white)](https://streamlit.io/)
[![Gemini](https://img.shields.io/badge/Gemini-API-8E75FF?logo=google&logoColor=white)](https://ai.google.dev/)
[![License: MIT](https://img.shields.io/badge/License-MIT-green.svg)](LICENSE)

Prompt Studio is a bilingual AI chat application built with Python, Streamlit, and the Gemini API. The app is designed with English as the primary user experience, while Portuguese support is included for accessibility and broader usability.

## Why this project stands out

- Clear, recruiter-friendly portfolio presentation
- Practical use of AI API integration in a real user-facing app
- Bilingual UX with English-first design and Portuguese localization
- Secure secret management for local development and deployment
- Clean, readable structure for a small production-style project

## Features

- English-first interface with complete Portuguese localization
- Gemini-powered chat using the OpenAI-compatible API endpoint
- Starter prompts for faster interaction and onboarding
- Conversation history within the current session
- API status and error feedback for missing keys, auth failures, rate limits, and connectivity issues
- Responsive Streamlit layout with custom theming

## Tech stack

- Python 3.10+
- Streamlit
- OpenAI Python SDK
- Google Gemini API

## Project structure

```text
prompt-studio-gemini-chat/
├── app.py
├── requirements.txt
├── README.md
├── LICENSE
├── CONTRIBUTING.md
├── .gitignore
├── .streamlit/
│   ├── config.toml
│   ├── secrets.toml
│   └── secrets.toml.example
└── .venv/
```

## Run locally

### 1. Clone the repository

```bash
git clone https://github.com/rickrodrigues2026/prompt-studio-gemini-chat.git
cd prompt-studio-gemini-chat
```

### 2. Create a virtual environment

```bash
python -m venv .venv
source .venv/bin/activate
```

On Windows PowerShell:

```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
```

### 3. Install dependencies

```bash
python -m pip install --upgrade pip
python -m pip install -r requirements.txt
```

### 4. Configure API key

Copy the example secrets file:

```bash
cp .streamlit/secrets.toml.example .streamlit/secrets.toml
```

On Windows PowerShell:

```powershell
Copy-Item .streamlit/secrets.toml.example .streamlit/secrets.toml
```

Then add your Gemini API key:

```toml
GEMINI_API_KEY = "your-gemini-api-key"
```

### 5. Start the app

```bash
streamlit run app.py
```

## Deployment

This project is ready for deployment on Streamlit Community Cloud.

1. Push the repository to GitHub.
2. Open Streamlit Community Cloud.
3. Create a new app.
4. Set the app entry point to `app.py`.
5. Add `GEMINI_API_KEY` in the app secrets settings.

## Security note

Never commit a real API key. Keep secrets in `.streamlit/secrets.toml` or in your platform secret manager. The repository tracks only the example file.

## License

This project is licensed under the MIT License. See [LICENSE](LICENSE) for details.

## Contributing

Contributions are welcome. Please read [CONTRIBUTING.md](CONTRIBUTING.md) for development and PR guidelines.

---

# Prompt Studio (Português)

O Prompt Studio é uma aplicação de chat com IA em dois idiomas, desenvolvida com Python, Streamlit e a API Gemini. A experiência foi pensada em inglês como idioma principal, com suporte em português para acessibilidade e melhor alcance de público.

## Por que esse projeto chama atenção

- Apresentação clara e profissional para portfólio
- Uso prático de integração com API de IA em um app real
- UX bilíngue com foco em inglês e tradução para português
- Gerenciamento seguro de chaves em ambiente local e nuvem
- Estrutura organizada e fácil de compreender para um projeto de pequeno porte

## Recursos

- Interface em inglês com localização completa para português
- Chat com Gemini usando a API compatível com OpenAI
- Sugestões iniciais para deixar a experiência mais fluida
- Histórico de conversa na sessão atual
- Indicadores de status da API e mensagens de erro para chave ausente, autenticação, limite de requisições e conexão
- Layout responsivo com visual customizado em Streamlit

## Como executar localmente

```bash
git clone https://github.com/rickrodrigues2026/prompt-studio-gemini-chat.git
cd prompt-studio-gemini-chat
python -m venv .venv
source .venv/bin/activate
python -m pip install --upgrade pip
python -m pip install -r requirements.txt
cp .streamlit/secrets.toml.example .streamlit/secrets.toml
streamlit run app.py
```

No Windows PowerShell:

```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
python -m pip install --upgrade pip
python -m pip install -r requirements.txt
Copy-Item .streamlit/secrets.toml.example .streamlit/secrets.toml
streamlit run app.py
```

Edite o arquivo `.streamlit/secrets.toml` e adicione sua chave Gemini:

```toml
GEMINI_API_KEY = "sua-chave-gemini"
```

## Implantação

O projeto também pode ser implantado no Streamlit Community Cloud. Configure `app.py` como ponto de entrada e adicione `GEMINI_API_KEY` na seção de secrets da plataforma.

## Licença

Este projeto está licenciado sob a licença MIT. Consulte [LICENSE](LICENSE).

## Contribuições

Contribuições são bem-vindas. Consulte [CONTRIBUTING.md](CONTRIBUTING.md).
