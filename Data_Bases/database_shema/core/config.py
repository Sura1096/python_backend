from dataclasses import dataclass

from environs import Env


@dataclass
class DatabaseConfig:
    DB_NAME: str
    DB_HOST: str
    DB_PORT: str
    DB_USER: str
    DB_PASS: str


def load_config(path: str | None = None) -> DatabaseConfig:
    env: Env = Env()
    env.read_env(path)

    return DatabaseConfig(
        DB_NAME=env('DB_NAME'),
        DB_HOST=env('DB_HOST'),
        DB_PORT=env('DB_PORT'),
        DB_USER=env('DB_USER'),
        DB_PASS=env('DB_PASS'),
    )


def get_database_url() -> str:
    DB_NAME = load_config().DB_NAME
    DB_HOST = load_config().DB_HOST
    DB_PORT = load_config().DB_PORT
    DB_USER = load_config().DB_USER
    DB_PASS = load_config().DB_PASS

    return f'postgresql://{DB_USER}:{DB_PASS}@{DB_HOST}:{DB_PORT}/{DB_NAME}'


DATABASE_URL = get_database_url()
