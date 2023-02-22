from starlette.config import Config

config = Config(".env")

OPENAI_KEY = config("OPENAI_KEY", cast=str)
