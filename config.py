import os
from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    PROJECT_NAME: str = "Vortexen + Plus UAE RevenueOS — AI Lead Generation & Outreach Module"
    VERSION: str = "1.0.0"
    API_V1_STR: str = "/api/v1"

    # Database Settings
    DATABASE_URL: str = os.getenv("DATABASE_URL", "postgresql://user:password@localhost:5432/revenue_os")

    # LLM Provider Keys
    OPENAI_API_KEY: str = os.getenv("OPENAI_API_KEY", "mock-openai-key")
    GEMINI_API_KEY: str = os.getenv("GEMINI_API_KEY", "mock-gemini-key")
    ANTHROPIC_API_KEY: str = os.getenv("ANTHROPIC_API_KEY", "mock-anthropic-key")
    DEFAULT_LLM_PROVIDER: str = "openai" # 'openai', 'gemini', 'anthropic'

    # Enrichment API Keys
    APOLLO_API_KEY: str = os.getenv("APOLLO_API_KEY", "mock-apollo-key")
    LUSHA_API_KEY: str = os.getenv("LUSHA_API_KEY", "mock-lusha-key")
    HUNTER_API_KEY: str = os.getenv("HUNTER_API_KEY", "mock-hunter-key")
    TAVILY_API_KEY: str = os.getenv("TAVILY_API_KEY", "mock-tavily-key")

    # Zoho CRM API Settings
    ZOHO_CRM_CLIENT_ID: str = os.getenv("ZOHO_CRM_CLIENT_ID", "mock-zoho-client-id")
    ZOHO_CRM_CLIENT_SECRET: str = os.getenv("ZOHO_CRM_CLIENT_SECRET", "mock-zoho-client-secret")
    ZOHO_CRM_REFRESH_TOKEN: str = os.getenv("ZOHO_CRM_REFRESH_TOKEN", "mock-zoho-refresh-token")
    ZOHO_CRM_API_DOMAIN: str = os.getenv("ZOHO_CRM_API_DOMAIN", "https://www.zohoapis.com/crm/v8")

    # Outreach & Voice Settings
    DEFAULT_SENDER_EMAIL: str = "outreach@plusuae.com"
    VAPI_API_KEY: str = os.getenv("VAPI_API_KEY", "mock-vapi-key")
    TWILIO_ACCOUNT_SID: str = os.getenv("TWILIO_ACCOUNT_SID", "mock-twilio-sid")
    TWILIO_AUTH_TOKEN: str = os.getenv("TWILIO_AUTH_TOKEN", "mock-twilio-token")

    # Compliance Thresholds
    MAX_SPAM_RATE_THRESHOLD: float = 0.001 # 0.1% max spam complaint rate
    MAX_BOUNCE_RATE_THRESHOLD: float = 0.02 # 2.0% max bounce rate
    UAE_CALLING_START_HOUR: int = 9 # 9:00 AM local time
    UAE_CALLING_END_HOUR: int = 18 # 6:00 PM local time

settings = Settings()
