from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    DB_HOST: str
    DB_PORT: str
    DB_USER: str
    DB_PASS: str
    DB_NAME: str

    API_KEY: str

    @property
    def DATABASE_URL(self) -> str:
        """
        Returns a string for bd connection
        """
        return f"postgresql+asyncpg://{self.DB_USER}:{self.DB_PASS}@{self.DB_HOST}:{self.DB_PORT}/{self.DB_NAME}"

    # "api/.env" when making migration and "/.env" when starting app 
    model_config = SettingsConfigDict(env_file=".env")


settings = Settings()
