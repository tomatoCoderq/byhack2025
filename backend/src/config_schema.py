from enum import StrEnum
from pathlib import Path

import yaml
from pydantic import BaseModel, ConfigDict, Field, SecretStr


class Environment(StrEnum):
    DEVELOPMENT = "development"
    PRODUCTION = "production"


class SettingBaseModel(BaseModel):
    model_config = ConfigDict(use_attribute_docstrings=True, extra="forbid")

class Settings(SettingBaseModel):
    
    schema_: str | None = Field(None, alias="$schema")

    app_root_path: str = ""
    
    "PostgreSQL database settings"
    db_url: SecretStr = Field(
        examples=[
            "postgresql+asyncpg://postgres:postgres@localhost:5432/postgres",
            "postgresql+asyncpg://postgres:postgres@db:5432/postgres",
        ]
    )
    "Key to access the OpenAI API."
    openai_api_key: SecretStr = Field(
        examples=[
            "sk-XXXXXXXXXXXXXXXXXXXXXXXXXXXX",
        ]
    )
    "Allowed origins for CORS: from which domains requests to the API are allowed. Specify as a regex: `https://.*.innohassle.ru`"
    "InNoHassle Accounts integration settings"
    cors_allow_origin_regex: str = ".*"

    @classmethod
    def from_yaml(cls, path: Path) -> "Settings":
        with open(path) as f:
            yaml_config = yaml.safe_load(f)

        return cls.model_validate(yaml_config)

    @classmethod
    def save_schema(cls, path: Path) -> None:
        with open(path, "w") as f:
            schema = {"$schema": "https://json-schema.org/draft-07/schema", **cls.model_json_schema()}
            yaml.dump(schema, f, sort_keys=False)