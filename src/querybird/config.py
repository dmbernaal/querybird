from starlette.config import Config

config = Config(".env")

OPENAI_KEY = config("OPENAI_KEY", cast=str)
OPENAI_ORG = config("OPENAI_ORG", cast=str)
