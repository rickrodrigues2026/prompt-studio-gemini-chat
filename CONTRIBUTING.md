# Contributing to Prompt Studio

Thank you for your interest in contributing to this project!

## Ways to Contribute

- **Report bugs** - Open an issue with clear reproduction steps
- **Suggest features** - Propose improvements or new capabilities
- **Improve documentation** - Fix typos, clarify instructions, add examples
- **Submit code** - Fix bugs or implement features via pull requests
- **Improve translations** - Help enhance English or Portuguese localization

## Code of Conduct

- Be respectful and inclusive
- Focus on the code, not the person
- Welcome feedback and constructive criticism

## Development Setup

### 1. Clone & Create Virtual Environment

```bash
git clone https://github.com/rickrodrigues2026/prompt-studio-gemini-chat.git
cd prompt-studio-gemini-chat
python -m venv .venv
source .venv/bin/activate  # Windows: .\.venv\Scripts\Activate.ps1
```

### 2. Install Dependencies

```bash
python -m pip install --upgrade pip
python -m pip install -r requirements.txt
```

### 3. Configure Secrets

```bash
cp .streamlit/secrets.toml.example .streamlit/secrets.toml
# Add your GEMINI_API_KEY
```

### 4. Test the App

```bash
streamlit run app.py
```

## Pull Request Process

### Before You Start

1. **Check existing issues** - Avoid duplicate work
2. **Open an issue first** - For major features, discuss approach
3. **Create a feature branch** - Use descriptive names like `feature/dark-mode` or `fix/api-timeout`

### Guidelines

- **Keep changes focused** - One feature/fix per PR
- **Test thoroughly** - Try both English and Portuguese interfaces
- **Write clear commit messages** - Explain what and why
- **Update docs** - Modify README if behavior changes
- **No API keys** - Never commit real secrets or credentials

### Code Style

- Follow PEP 8 conventions
- Use meaningful variable names
- Add docstrings to functions
- Keep functions small and focused
- Write comments for complex logic

Example:

```python
def get_api_key() -> str:
    """
    Retrieve the Gemini API key from Streamlit secrets or environment.
    
    Returns:
        str: The API key, or empty string if not found
    """
    try:
        return st.secrets.get("GEMINI_API_KEY", "")
    except FileNotFoundError:
        return os.getenv("GEMINI_API_KEY", "")
```

### Bilingual Requirements

When adding user-facing text:

1. **Add English copy first** to `COPY["en"]` dictionary
2. **Add Portuguese translation** to `COPY["pt"]` dictionary
3. **Test both languages** in the app UI
4. **Keep terminology consistent** across both languages

Example:

```python
COPY = {
    "en": {
        "my_feature": "My new feature",
    },
    "pt": {
        "my_feature": "Minha nova funcionalidade",
    },
}
```

### Commit Message Format

```
type: Brief description (50 chars max)

Optional longer explanation about why this change was needed.
- Point 1 about the change
- Point 2 about the change

Fixes #123
```

**Types:** `feat`, `fix`, `docs`, `style`, `refactor`, `test`, `chore`

### PR Checklist

Before submitting:

- [ ] Tested app with both English and Portuguese
- [ ] No real API keys or secrets committed
- [ ] Code follows style guidelines
- [ ] Commit messages are clear
- [ ] Documentation updated if needed
- [ ] Changes solve the stated problem

## Getting Help

- **Questions?** Open a GitHub Discussion
- **Bug found?** Create an Issue with details
- **Documentation unclear?** Let us know!

---

We appreciate your contributions to making Prompt Studio better! 🎉
