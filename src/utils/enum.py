from enum import Enum


class LLMEnum(Enum):
    OPEN_AI = "OpenAI"
    ANTHROPIC = "Anthropic"

    def __str__(self):
        return self.value


class LLMModelEnum(Enum):
    OPEN_AI_3_5_TURBO = "gpt-3.5-turbo"
    OPEN_AI_4 = "gpt-4"
    OPEN_AI_4_TURBO = "gpt-4-turbo"
    OPEN_AI_4_OMNI = "gpt-4o"
    OPEN_AI_4_OMNI_MINI = "gpt-4o-mini"
    ANTHROPIC_3_OPUS = "claude-3-opus-20240229"
    ANTHROPIC_3_SONNET = "claude-3-sonnet-20240229"
    ANTHROPIC_3_HAIKU = "claude-3-haiku-20240307"

    def __str__(self):
        return self.value


class ProfileEnum(Enum):
    CREATIVE = "Creative"
    BALANCE = "Balance"
    PRECISE = "Precise"

    def __str__(self):
        return self.value
