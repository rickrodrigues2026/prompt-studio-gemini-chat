# Prompt Studio - Development Notes

## Overview

Prompt Studio is a bilingual AI chat application built with Python, Streamlit, and Google Gemini API, designed with English as the primary experience and Portuguese localization for accessibility.

## Key Architecture Decisions

### Bilingual Strategy (EN/PT)

- **English is the default/primary language** for the interface
- **Portuguese is available via language selector** for accessibility
- All user-facing text is stored in the `COPY` dictionary with `en` and `pt` keys
- When adding new features, always provide translations for both languages

### API Integration

- Uses OpenAI Python SDK for compatibility with Gemini's OpenAI-compatible endpoint
- Model: `gemini-1.5-flash` (update as newer versions become stable)
- Endpoint: `https://generativelanguage.googleapis.com/v1beta/openai/`
- API key managed via Streamlit secrets (local) and Streamlit Cloud Secrets (production)

### Error Handling

- Specific error types for: authentication, rate limits, connectivity, service errors
- Localized error messages in both languages
- Graceful degradation - app is viewable even without API key

### Session Management

- Chat history stored in `st.session_state["messages"]`
- Conversation resets on app restart
- Starter prompts queued via `st.session_state["pending_prompt"]`

## Design Philosophy

### User Experience

- **Accessibility First** - Clear error states, helpful guidance, no confusing UX
- **Minimalist Interface** - Focused workspace without distraction
- **Instant Feedback** - Status indicator, loading states, immediate validation
- **Mobile-Friendly** - Responsive Streamlit layout works on all screen sizes

### Code Quality

- Clear, readable Python following PEP 8
- Comprehensive docstrings and comments
- Modular functions with single responsibilities
- Type hints where applicable

### Security

- API keys never stored in version control
- `.streamlit/secrets.toml` always in `.gitignore`
- Only `.streamlit/secrets.toml.example` is committed (as template)
- Privacy notice shown to users before chat starts

## Development Workflow

1. **Feature Planning** - Discuss in issues before implementation
2. **Branch Strategy** - Create feature branches from `main`
3. **Testing** - Test with both languages before PR
4. **Documentation** - Update README/CONTRIBUTING for changes
5. **Code Review** - Keep changes focused and well-commented

## Future Enhancements

Potential improvements (not required):

- [ ] Support for additional languages
- [ ] Conversation history export (JSON/PDF)
- [ ] Model selection dropdown (if budget supports multiple models)
- [ ] Adjustable system prompt for different personalities
- [ ] User preferences saved to Streamlit Cloud storage
- [ ] Dark mode theme option

## Troubleshooting

### App won't start

```bash
# Clear Streamlit cache
streamlit cache clear
# Restart with fresh run
streamlit run app.py
```

### API key errors

- Verify key is in `.streamlit/secrets.toml`
- Check key is valid at [Google AI Studio](https://aistudio.google.com/apikey)
- Ensure key has Gemini API enabled

### Portuguese text not showing

- Check browser language settings
- Clear browser cache
- Verify translation is present in `COPY["pt"]` dictionary

## Resources

- [Streamlit Docs](https://docs.streamlit.io/)
- [Gemini API Docs](https://ai.google.dev/docs)
- [OpenAI Python SDK](https://github.com/openai/openai-python)
- [PEP 8 Style Guide](https://pep8.org/)

---

Questions? Open an issue or start a discussion!
