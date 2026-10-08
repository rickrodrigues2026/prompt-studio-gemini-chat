# Contributing to Prompt Studio

Thank you for contributing to this project.

## How to contribute

- Open an issue for bugs or feature suggestions.
- Create a branch for your work.
- Keep changes focused and easy to review.
- Test the app locally before opening a pull request.

## Local development

```bash
git clone https://github.com/rickrodrigues2026/prompt-studio-gemini-chat.git
cd prompt-studio-gemini-chat
python -m venv .venv
source .venv/bin/activate
python -m pip install -r requirements.txt
cp .streamlit/secrets.toml.example .streamlit/secrets.toml
streamlit run app.py
```

## Code expectations

- Write clear, readable Python code
- Prefer small, focused commits
- Keep UI copy in English as the primary language
- Add Portuguese translations when updating user-facing text
- Do not commit real API keys

## Pull request checklist

- [ ] App runs locally
- [ ] No secrets or keys committed
- [ ] User-facing text is updated in both languages when needed
- [ ] Documentation is updated if behavior changes
