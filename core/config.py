from starlette.config import Config

config = Config(".env")

DATABASE_URL = config("PQ_DATABASE_URL", cast=str, default="")
ACCESS_TOKEN_EXPIRE_MINUTES = 60
ALGORITHM = "HS256"
SECRET_KEY = config("PQ_SECRET_KEY", cast=str, default="b860c3e0077112d75dc094bba3395270e8731aacc6913d426a538298a53c5615")