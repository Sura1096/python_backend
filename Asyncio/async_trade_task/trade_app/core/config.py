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
    db_name = load_config().DB_NAME
    db_host = load_config().DB_HOST
    db_port = load_config().DB_PORT
    db_user = load_config().DB_USER
    db_pass = load_config().DB_PASS

    return f'postgresql+asyncpg://{db_user}:{db_pass}@{db_host}:{db_port}/{db_name}'


DATABASE_URL = get_database_url()
