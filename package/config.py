import os

# Centralized configuration for model selection across clients
# Default to GPT-5 mini unless overridden by the environment variable
DEFAULT_MODEL = os.getenv("DEFAULT_MODEL", "gpt-5-mini")

def get_default_model() -> str:
    """Return the default model name used by clients.

    - Reads `DEFAULT_MODEL` env var when the module is imported.
    - Falls back to "gpt-5-mini" to enable GPT-5 mini for all clients by default.
    """
    return DEFAULT_MODEL
