from pathlib import Path
from dotenv import load_dotenv

import os
import yaml


# CARGA DE VARIABLES DE ENTORNO
load_dotenv()
BASE_DIR = Path(__file__).resolve().parent.parent


# CARGA DE YAML
yaml_path = BASE_DIR / "config.yaml"
if yaml_path.exists():
    with open(yaml_path, "r", encoding="utf-8") as f:
        YAML_CONFIG = yaml.safe_load(f)
else:
    YAML_CONFIG = {}


# API KEYS
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")

# VALIDACION DE APIs
if not OPENAI_API_KEY:
    raise ValueError("OPENAI_API_KEY no configurada")

if not GEMINI_API_KEY:
    raise ValueError("GEMINI_API_KEY no configurada")


# MODELOS
MODELO1 = YAML_CONFIG.get(
    "modelo1",
    "OpenAI" # default
)
MODELO2 = YAML_CONFIG.get(
    "modelo2",
    "Gemini" # default
)
OPENAI_MODEL = YAML_CONFIG.get(
    "openai_model",
    "gpt-4o-mini" # default
)
GEMINI_MODEL = YAML_CONFIG.get(
    "gemini_model",
    "gemini-2.5-flash" # default
)

# TIMEOUTS EN LLAMADAS A API
TIMEOUT_OPENAI = YAML_CONFIG.get(
    "timeout_openai",
    20 # default
)
TIMEOUT_GEMINI = YAML_CONFIG.get(
    "timeout_gemini",
    10 # default
)

# APP
HOST = YAML_CONFIG.get(
    "host",
    "0.0.0.0" # default
)
PORT = YAML_CONFIG.get(
    "port",
    5000 # default
)
DEBUG = YAML_CONFIG.get(
    "debug",
    False # default
)

