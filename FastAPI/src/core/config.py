import os

from dotenv import find_dotenv, load_dotenv

load_dotenv(find_dotenv('.env'))


class Settings:
    DB_HOST: str = os.environ.get('DB_HOST')
    DB_PORT: str = os.environ.get('DB_PORT')
    DB_USER: str = os.environ.get('DB_USER')
    DB_PASS: str = os.environ.get('DB_PASS')
    DB_NAME: str = os.environ.get('DB_NAME')

    DB_URL: str = (
        f'postgresql+asyncpg://{DB_USER}:{DB_PASS}@{DB_HOST}:{DB_PORT}/{DB_NAME}'
    )


class RedisSettings:
    REDIS_HOST: str = os.environ.get('REDIS_HOST')
    REDIS_PORT: str = os.environ.get('REDIS_PORT')

    REDIS_URL: str = f'redis://{REDIS_HOST}:{REDIS_PORT}'


class TestDatabaseSettings:
    load_dotenv(find_dotenv('.test.env'))
    DB_HOST_TEST: str = os.environ.get('DB_HOST_TEST')
    DB_PORT_TEST: str = os.environ.get('DB_PORT_TEST')
    DB_USER_TEST: str = os.environ.get('DB_USER_TEST')
    DB_PASS_TEST: str = os.environ.get('DB_PASS_TEST')
    DB_NAME_TEST: str = os.environ.get('DB_NAME_TEST')

    def test_db_url(self) -> str:
        return f'postgresql+asyncpg://{self.DB_USER_TEST}:{self.DB_PASS_TEST}@{self.DB_HOST_TEST}:{self.DB_PORT_TEST}/{self.DB_NAME_TEST}'


settings = Settings()
redis_config = RedisSettings()
test_db = TestDatabaseSettings()
