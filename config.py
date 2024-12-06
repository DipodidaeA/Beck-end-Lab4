import os

PROPAGATE_EXCEPTIONS = True
FLASK_DEBUG = True
SQLALCHEMY_DATABASE_URI = f'postgresql://{os.environ.get("POSTGRES_USER")}:{os.environ.get("POSTGRES_PASSWORD")}@{os.environ.get("POSTGRES_HOST")}/{os.environ.get("POSTGRES_DB")}'
SQLALCHEMY_TRACK_MODIFICATIONS = False
API_TITLE = "Lab3"
API_VERSION = "v2"
OPENAPI_VERSION = "3.0.3"
OPENAPI_URL_PREFIX = "/"
OPENAPI_SWAGGER_UI_PATH = "/swagger-ui"
OPENAPI_SWAGGER_UI_URL = "https://cdn.jsdelivr.net/npm/swagger-ui-dist/"
JWT_SECRET_KEY = os.getenv("JWT_SECRET_KEY")