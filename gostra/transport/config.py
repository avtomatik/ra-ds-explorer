from pathlib import Path

from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):

    model_config = SettingsConfigDict(env_prefix="GOSTRA_", env_file=".env")

    # =========================================================================
    # General
    # =========================================================================
    env: str

    # =========================================================================
    # Transport
    # =========================================================================
    curl_path: str
    cert_thumbprint: str
    timeout: int = 30
    verify_tls: bool = False

    # =========================================================================
    # API
    # =========================================================================
    api_base_url: str
    api_version: str = "1.0"

    # =========================================================================
    # Logging
    # =========================================================================
    log_level: str = "INFO"
    log_dir: Path = Path("./logs")
    http_log_dir: Path = Path("./logs/http")

    # =========================================================================
    # Development
    # =========================================================================
    debug_http: bool = False
    save_raw_responses: bool = False
