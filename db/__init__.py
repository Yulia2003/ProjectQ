from .users import users
from .publiks import publiks
from .base import metadata, engine

metadata.create_all(bind=engine)