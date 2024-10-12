from pydantic import (
    SecretStr,
    BaseModel,
)
from pydantic_settings import (
    BaseSettings,
    SettingsConfigDict,
)


class BotConfig(BaseModel):
    bot_token: SecretStr


class Settings(BaseSettings):
    model_config = SettingsConfigDict(
        env_file=(".env.template", ".env"),
        env_file_encoding="utf-8",
        env_nested_delimiter="__",
    )
    bot_config: BotConfig


settings = Settings()
