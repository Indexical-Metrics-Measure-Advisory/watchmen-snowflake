

from pydantic import BaseSettings


class Settings(BaseSettings):
    SNOWFLAKE_DATACENTER = 0
    SNOWFLAKE_WORKER = 0
    PROMETHEUS_ON = False
    PROJECT_NAME = "watchmen-snowflake"

    class Config:
        env_file = '.env'
        env_file_encoding = 'utf-8'
        case_sensitive = True


settings = Settings()
